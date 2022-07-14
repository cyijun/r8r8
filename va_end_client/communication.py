import requests
import base64
import wave


def encode_audio(filename):
    fin = open(filename, 'rb').read()
    return base64.b64encode(fin)


def decode_b64(b64str):
    try:
        return base64.b64decode(fin)
    except Exception:
        print(Exception)
        return False

#fo=open("result.txt", 'wb')
# fo.write(encode_audio("openac.wav"))


def post_request(url, cache_dir):
    myobj = {'wav': encode_audio(cache_dir+"cache.wav")}

    x = requests.post(url, json=myobj)

    print(x.text)
