# coding: utf-8

from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdksis.v1.region.sis_region import SisRegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdksis.v1 import *

def huaweicloud_asr(b64wav):
    ak = "your_ak"
    sk = "your_sk"

    credentials = BasicCredentials(ak, sk) \

    client = SisClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(SisRegion.value_of("cn-north-4")) \
        .build()

    try:
        request = RecognizeShortAudioRequest()
        configConfig = Config(
            audio_format="wav",
            _property="chinese_16k_common"
        )
        request.body = PostShortAudioReq(
            data=b64wav,
            config=configConfig
        )
        response = client.recognize_short_audio(request)
        print(response)
        return(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)