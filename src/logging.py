import os
import time
import logging
import logging.handlers
'''
日志模块
'''
class Writelog(object):
    def __init__(self):
        self.logger = logging.getLogger()
        self.path = "./logs/"
        self.LOG_FILENAME = self.path + "bark.log"

        self.set_log_filenme()
        self.set_logger()

    def set_log_filenme(self):
        isExists = os.path.exists(self.path)
        if not isExists:
            os.mkdir(self.path)
        log_time = time.strftime("%Y_%m_%d", time.localtime())  # 刷新
        self.LOG_FILENAME = self.path + "bark_" + log_time + ".log"
        if os.path.exists(self.LOG_FILENAME):
            log_time = time.strftime("%Y_%m_%d_%H", time.localtime())  # 另创建
            self.LOG_FILENAME = self.path + log_time + "时.log"

    def set_logger(self):
        formatter = logging.Formatter('%(asctime)s - %(process)d-%(threadName)s - '
                                  '%(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
        file_handler = logging.handlers.RotatingFileHandler(
            self.LOG_FILENAME, maxBytes=10485760, backupCount=5, encoding="utf-8")
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def log_info(self, context):

Log = Writelog()