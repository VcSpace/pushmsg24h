import requests
import time
import json
import distutils

from requests.cookies import RequestsCookieJar
from src.config import config
from src.push_msg import Pmsg

class TOKEN_IN(object):
    def __init__(self):
        self.topid = '0'
        self.date = ''
        self.ti_api_key = config.get_ti_key()

    def get_news(self):
        while True:
            # cookie_jar = session.get('https://cn.tokeninsight.com/zh/news').cookies
            # cookie_t = requests.utils.dict_from_cookiejar(cookie_jar)
            m_json = ''
            # url = "https://api.tokeninsight.com/api/v1/news/list"
            url = 'https://tokeninsight.com/apiv2/research/newsList'

            headers = {
                "accept": "application/json",
                "TI_API_KEY": "{0}".format(self.ti_api_key)
            }

            data = {"current": 1, "language": "cn", "pageSize": 10, "tagId": "", "startDate": "", "endDate": ""}

            try:
                res = requests.post(url, headers=headers, data=data, timeout=65)
                if res.status_code == 200:
                    one_json = json.loads(res.text)
                    m_json = one_json['data']['list']
                    print(m_json)
                    if self.topid == m_json[0]['id']:
                        print('topid == json_topid' )
                        time.sleep(6000)
                        continue

                    for n in range(len(m_json)):
                        content = m_json[n]['html']
                        content_title = m_json[n]['title']
                        id = m_json[n]['tagId']
                        article_link = m_json[n]['articleLink']
                        news_url = 'tokeninsight.com/zh/news/{0}'.format(article_link)
                        if self.topid == id:
                            print("topid == json_topid")
                            break
                        else:
                            Pmsg.sendmeg(news_url, content, content_title, 'ti')
                            time.sleep(3)

                    self.topid = m_json[0]['tagId']
                    print("发送成功 timesleep")
                time.sleep(6000)
            except Exception as e:
                time.sleep(6000)
                print(e)

ti = TOKEN_IN()