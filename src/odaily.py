import requests
import time
import json

from src.push_msg import Pmsg

class oDaily(object):
    def __init__(self):
        self.topid = '0'
        self.date = ''

    def get_news(self):
        while True:
            m_json = ''
            url = 'https://www.odaily.news/api/pp/api/info-flow/newsflash_columns/newsflashes?b_id=&per_page=10'
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
                'Referer': 'https://www.odaily.news/newsflash',
                'Host': 'www.odaily.news'
            }
            try:
                res = requests.get(url, headers=headers, timeout=30)
                if res.status_code == 200:
                    od_json = json.loads(res.text)
                    m_json = od_json['data']['items']
                    if self.topid == m_json[0]['id']:
                        print('od_topid == json_topid' )
                        time.sleep(600)
                        continue

                    for n in range(len(m_json)):
                        content = m_json[n]['description']
                        content_title = m_json[n]['title']
                        id = m_json[n]['id']
                        news_url = 'www.odaily.news/newsflash/{0}'.format(id)
                        if self.topid == id:
                            print("od_topid == json_id")
                            break
                        else:
                            Pmsg.sendmeg(news_url, content, content_title)
                            time.sleep(3)

                    self.topid = m_json[0]['id']
                    print("od_发送成功 timesleep")
                time.sleep(600)
            except Exception as e:
                time.sleep(600)
                print(e)

oda = oDaily()