import requests
import threading
import base64

from Crypto.Cipher import AES
from src.config import config

mutex = threading.Lock() # 创建一个锁对象
class PushMsg(object):
    def __init__(self):
        self.serv_host = config.get_server_host()
        self.serv_key = config.get_server_key()
        self.aes_key = config.get_aes_key()
        self.aes_iv = config.get_aes_iv()

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
            'Host': '{0}:8080'.format(self.serv_host)
        }
    def deal_msg(self, news_url, news_content, news_title):
        try:
            mutex.acquire()  # 获取锁
            self.cipher = AES.new(self.aes_key.encode(), AES.MODE_CBC, self.aes_iv.encode())

            m_json = '{{"title": "{0}","body": "{1}", "url": "{2}", "sound": "healthnotification"}}'.format(
                news_title.replace("\"", "\\\""), news_content.replace("\n", "\\n").replace("\"", "\\\""), news_url)

            print(m_json)

            # 把字符串转换为字节
            message = m_json.encode()
            # 对字节进行填充，使其长度为16的倍数
            pad_length = 16 - len(message) % 16
            message += bytes([pad_length]) * pad_length
            # 加密字节
            token = self.cipher.encrypt(message)
            # 把加密后的字节转换为base64字符串
            token = base64.b64encode(token).decode()

            mutex.release()  # 释放锁
            return token
        except Exception as e:
            mutex.release()  # 释放锁
            print(e)


    def sendmeg(self, news_url, news_content, news_title):
        ciphertext = self.deal_msg(news_url, news_content, news_title)
        data = {
            "ciphertext": ciphertext,
            "iv": "{0}".format(self.aes_iv)
        }

        sendurl = 'http://{0}:8080/{1}'.format(self.serv_host, self.serv_key)
        try:
            for ll in range(3):
                res = requests.post(sendurl, headers=self.headers, data=data, timeout=30)
                if res.status_code == 200:
                    print('发送成功', res.text)
                    break
        except Exception as e:
            print(e)

Pmsg = PushMsg()

