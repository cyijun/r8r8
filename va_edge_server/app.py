from flask import Flask
from flask import request
import base64
import wave
import numpy as np

#import deepspeech
#from deepspeech import Model, version
#import numpy as np
#import itertools
#import argparse
#DeepSpeech = Model("deepspeech-0.9.3-models.tflite")
#DeepSpeech.enableExternalScorer("deepspeech-0.9.3-models.scorer")

from hwc_cn_asr import huaweicloud_asr

from my_nlu import dealWithCommand

cache_dir='/tmp/myapi/'

app = Flask(__name__)

def decode_b64(b64str):
    try:
        return base64.b64decode(b64str)
    except Exception:
        print('cannot decode')
        return False

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/voice_assistant", methods=['GET', 'POST'])
def va_stt():
    if request.method == 'POST':
        received=request.json
        
        #fout=open(cache_dir+'cache.wav','wb+')
        #fout.write(decode_b64(received['wav']))
        #fout.close()
        #
        #wav=wave.open(cache_dir+'cache.wav','rb')
        #audio = np.frombuffer(wav.readframes(wav.getnframes()), np.int16)
        #wav.close()
        
        #wav=wave(decode_b64(received['wav']))
        #return "<p>"+DeepSpeech.stt(audio)+"</p>"
        
        resp=huaweicloud_asr(received['wav']).to_dict()
        dealWithCommand(resp["result"]["text"])
        return str(resp)
    return "<p>error</p>"

@app.route("/face_identification", methods=['GET', 'POST'])
def verify_face():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(host="0.0.0.0")