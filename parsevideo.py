import re

def parse_video(data):
    # information = dict()
    information = {}
    information['videoCodecType'] = re.findall(r'<videoCodecType>(.*?)<\/videoCodecType>', data)[0]
    videoResolutionWidth = re.findall(r'<videoResolutionWidth>(.*?)<\/videoResolutionWidth>', data)[0]
    videoResolutionHeight = re.findall(r'<videoResolutionHeight>(.*?)<\/videoResolutionHeight>', data)[0]
    information['Resolution'] = "{}*{}".format(videoResolutionWidth,videoResolutionHeight)
    information['constantBitRate'] = re.findall(r'<constantBitRate>(.*?)<\/constantBitRate>', data)[0]
    return information
