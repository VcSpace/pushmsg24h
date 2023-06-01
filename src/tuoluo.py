import requests
import time
import json

from src.push_msg import Pmsg

class TuoLuo(object):
    def __init__(self):
        self.topid = '0'
        self.date = ''

    def get_news(self):
        while True:
            m_json = ''
            url = 'https://api.tuoluo.cn/api/kuaixun/get_list?limit=20'
            headers = {
                'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
            }
            try:
                res = requests.get(url, headers=headers, timeout=30)
                if res.status_code == 200:
                    tl_json = json.loads(res.text)
                    m_json = tl_json['data']['list']
                    if self.topid == m_json[0]['s_id']:
                        print('tl_topid == json_topid' )
                        time.sleep(600)
                        continue

                    for n in range(len(m_json)):
                        content = m_json[n]['content'].replace("<p>", "").replace("</p>", "")
                        content_title = m_json[n]['title']
                        id = m_json[n]['s_id']
                        news_url = 'www.tuoluo.cn/kuaixun/detail-{0}.html'.format(id)
                        if self.topid == id:
                            print("tl_topid == json_id")
                            break
                        else:
                            Pmsg.sendmeg(news_url, content, content_title)
                            time.sleep(3)

                    self.topid = m_json[0]['s_id']
                    print("tl_发送成功 timesleep")
                time.sleep(600)
            except Exception as e:
                time.sleep(600)
                print(e)

Tl = TuoLuo()