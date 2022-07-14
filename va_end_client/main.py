from usb_pixel_ring_v2 import PixelRing, findPixelRing
from audio_tools import hotword_detect_loop, recorder
import time
from communication import post_request

LEVEL_THREASHOLD = 200
SILENT_COUNT = 20000
LEAST_TIME = 4

cache_dir = '/mnt/ramdisk/'
asr_url = 'http://your_asr_server_addr:5000/voice_assistant'

f=open(cache_dir+'cache.wav','w+')
f.write('x')
f.close()

def hotword_callback(pastream):
    try:
        # record
        pixel_ring.listen()
        recorder(LEAST_TIME, cache_dir, pastream, LEVEL_THREASHOLD)

        # request
        pixel_ring.think()
        post_request(asr_url, cache_dir)
        time.sleep(1)
        
        # session over
        pixel_ring.off()
    except Exception:
        return


if __name__ == '__main__':
    pixel_ring = findPixelRing()
    try:
        hotword_detect_loop(hotword_callback)
    finally:
        pixel_ring.off()
