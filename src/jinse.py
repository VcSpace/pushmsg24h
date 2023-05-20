import requests
import time
import json

from src.push_msg import Pmsg

class Jinse(object):
    def __init__(self):
        self.topid = '0'
        self.date = ''

    def get_news(self):
        while True:
            url = 'https://api.jinse.cn/noah/v2/lives?limit=20&reading=false&source=web'
            headers = {
                'Origin': 'https://www.jinse.com',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
                'Referer': 'https://www.jinse.com/',
                'Host': 'api.jinse.cn'
            }
            try:
                res = requests.get(url, headers=headers, timeout=20)
                if res.status_code == 200:
                    m_json = json.loads(res.text)
                    if self.topid == m_json['top_id']:
                        print('topid == json_topid' )
                        time.sleep(300)
                        continue

                    m_list = m_json['list']
                    m_lives = m_list[0]['lives']
                    for n in range(10):
                        content = m_lives[n]['content']
                        content_prefix = m_lives[n]['content_prefix']
                        id = m_lives[n]['id']
                        news_url = 'https://www.jinse.cn/lives/{0}.html'.format(id)
                        if self.topid == id:
                            print("topid == json_topid")
                            break
                        else:
                            Pmsg.sendmeg(news_url, content, content_prefix)
                            time.sleep(3)

                    if self.date != m_list[0]['date'] and self.date != '':
                        for n in range(5):
                            try:
                                m_lives = m_list[1]['lives']
                                content = m_lives[n]['content']
                                content_prefix = m_lives[n]['content_prefix']
                                id = m_lives[n]['id']
                                news_url = 'https://www.jinse.cn/lives/{0}.html'.format(id)
                                if self.topid == id:
                                    print("topid == json_topid")
                                    break
                                else:
                                    Pmsg.sendmeg(news_url, content, content_prefix)
                                    time.sleep(5)
                            except Exception as e:
                                print(e)
                self.date = m_list[0]['date']
                self.topid = m_json['top_id']
                time.sleep(300)
            except Exception as e:
                print(e)

Js = Jinse()