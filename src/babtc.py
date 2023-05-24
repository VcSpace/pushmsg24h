import requests
import time
import json

from src.push_msg import Pmsg

class BABTC(object):
    def __init__(self):
        self.topid = '0'
        self.date = ''
        self.session = requests.Session()

    def get_news(self):
        while True:
            m_json = ''
            url = 'https://gate.8btc.cn:8443/one-graph-auth/graphql'
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
                # 'Referer': 'https://www.8btc.com/',
            }
            try:
                res = requests.get(url, headers=headers, timeout=30)
                if res.status_code == 200:
                    one_json = json.loads(res.text)
                    t_json = one_json['data']['articleGraph']
                    m_json = t_json['list']['edges']
                    print(m_json)
                    if self.topid == m_json[0]['id']:
                        print('topid == json_topid' )
                        time.sleep(300)
                        continue

                    for n in range(len(m_json)):
                        content = m_json[n]['description']
                        content_title = m_json[n]['title']
                        id = m_json[n]['id']
                        news_url = 'www.odaily.news/newsflash/{0}'.format(id)
                        if self.topid == id:
                            print("topid == json_topid")
                            break
                        else:
                            Pmsg.sendmeg(news_url, content, content_title)
                            time.sleep(3)

                self.topid = m_json[0]['id']
                time.sleep(300)
            except Exception as e:
                print(e)

babtc = BABTC()