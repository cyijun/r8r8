import pvporcupine
import pyaudio
import struct
import wave
import numpy as np


def hotword_detect_loop(callback):
    porcupine = None
    pa = None
    audio_stream = None

    # AccessKey obtained from Picovoice Console (https://console.picovoice.ai/)
    access_key = "your_key"

    try:
        porcupine = pvporcupine.create(access_key=access_key, keyword_paths=[
            '/home/pi/Dev/voice_assist_main_prog/bin/Tree-New-Bee.ppn'])

        pa = pyaudio.PyAudio()
        audio_stream = pa.open(
            rate=16000,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=512)

        while True:
            pcm = audio_stream.read(512)
            pcm = struct.unpack_from("h" * 512, pcm)

            keyword_index = porcupine.process(pcm)
            if keyword_index >= 0:
                i = callback(audio_stream)

    finally:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if pa is not None:
            pa.terminate()


def recorder(least_time, cache_dir, pastream, level_threashold):
    frames = []
    for i in range(0, int(16000 / 512 * least_time)):
        audio_data = pastream.read(512)
        level_data = np.fromstring(audio_data, dtype=np.short)
        high_level_count_per_block = np.sum(level_data > level_threashold)
        
        frames.append(audio_data)

    wf = wave.open(cache_dir+'cache.wav', 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(16000)
    wf.writeframes(b''.join(frames))
    wf.close()
