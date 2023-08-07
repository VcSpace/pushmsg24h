import requests
import time
import json

from src.push_msg import Pmsg

class CoinTime(object):
    def __init__(self):
        self.topid = '0'
        self.date = ''

    def get_news(self):
        while True:
            m_json = ''
            url = 'https://cn.cointime.com/api/column-items/more?column_id=111&datetime=2023&take=10&order=desc'
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
            }
            try:
                res = requests.get(url, headers=headers, timeout=30)
                if res.status_code == 200:
                    coin_json = json.loads(res.text)
                    m_json = coin_json['data']
                    if self.topid == m_json[0]['itemId']:
                        print('coin_time_topid == json_topid' )
                        time.sleep(600)
                        continue

                    for n in range(len(m_json)):
                        content = m_json[n]['description']
                        content_title = m_json[n]['title']
                        uri = m_json[n]['uri']
                        news_url = 'cn.cointime.com/flash-news{0}'.format(uri)
                        if self.topid == id:
                            print("od_topid == json_id")
                            break
                        else:
                            Pmsg.sendmeg(news_url, content, content_title)
                            time.sleep(3)

                    self.topid = m_json[0]['itemId']
                    print("cointime_发送成功 timesleep")
                time.sleep(1200)
            except Exception as e:
                time.sleep(600)
                print(e)

coin_time = CoinTime()
