import requests
from requests.auth import HTTPDigestAuth
from parsedeviceInfo import parse_deviceInfo

def deviceInfo(ip,port,login,password):
    url = 'http://{}:{}/ISAPI/System/deviceinfo'.format(ip, port)
    print(url)
    try:
        r = requests.get(url, auth=HTTPDigestAuth(login, password))
        #print(r.text)
        w = parse_deviceInfo(r.text)
        print(w)
    except:
        return "False, error with data "
