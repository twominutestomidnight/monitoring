from camera import Camera
import configparser
from DeviceInfo import deviceInfo
from read_xml import read_xml
if __name__ == '__main__':
    config_ini = configparser.ConfigParser()
    config_ini.read('config.ini')
    #print(config_ini['DEFAULT']['program_mode'])

    dict_list = read_xml(config_ini['DEFAULT']['read_file'])

    camerasArray = []

    for index in range(len(dict_list)):

        camerasArray.append(Camera(ip=dict_list[index]['ip'], port=int(dict_list[index]['port']),
                                   login=dict_list[index]['login'],password=dict_list[index]['password']))


    #result = open(config_ini['DEFAULT']['path_to_save_file'], "w", encoding='utf8')

    log = open(config_ini['DEFAULT']['log_file'], 'w')

    for camer in camerasArray:
        print(camer)

        status = deviceInfo(camer.ip,camer.port, camer.login, camer.password)



