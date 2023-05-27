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

    def get_server_host(self):
        serv_host = self.config.get('DEFAULT', 'server_host')
        return serv_host

    def get_server_key(self):
        serv_key = self.config.get('DEFAULT', 'server_key')
        return serv_key

    def get_aes_key(self):
        key = self.config.get('DEFAULT', 'aes_key')
        return key

    def get_aes_iv(self):
        iv = self.config.get('DEFAULT', 'aes_iv')
        return iv

    def get_sql_info(self):
        sql_host = self.config.get('MYSQL', 'sql_host')
        sql_username = self.config.get('MYSQL', 'sql_username')
        sql_password = self.config.get('MYSQL', 'sql_password')
        sql_database = self.config.get('MYSQL', 'sql_database')
        sql_table = self.config.get('MYSQL', 'sql_table')
        return sql_host, sql_username, sql_password, sql_database, sql_table

    def get_ti_key(self):
        ti_key = self.config.get('tkinsight', 'api_key')
        return ti_key

config = Config()
