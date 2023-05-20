import configparser
import os
class Config(object):
    def __init__(self):
        # 创建一个configparser对象
        self.config = configparser.ConfigParser()
        # 获取当前目录下的config.ini文件的绝对路径
        ini_path = os.path.join(os.getcwd(), 'config.ini')
        # 读取config.ini文件
        self.config.read(ini_path)

    def get_server_name(self):
        serv_name = self.config.get('DEFAULT', 'server_name')
        return serv_name

    def get_server_key(self):
        serv_key = self.config.get('DEFAULT', 'server_key')
        return serv_key

    def get_aes_key(self):
        key = self.config.get('DEFAULT', 'aes_key')
        return key

    def get_aes_iv(self):
        iv = self.config.get('DEFAULT', 'aes_iv')
        return iv

config = Config()
