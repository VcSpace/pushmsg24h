import requests
import time
import json

from src.push_msg import Pmsg

class Pannews(object):
    def __init__(self):
        self.topid = 0
        self.date = ''

    def get_news(self):
        while True:
            url = 'https://www.panewslab.com/webapi/flashnews?LId=1&LastTime=0&Rn=20&tw=0'
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Host': 'www.panewslab.com'
            }
            try:
                res = requests.get(url, headers=headers, timeout=30)
                if res.status_code == 200:
                    m_json = json.loads(res.text)
                    m_list = m_json['data']['flashNews']
                    m_id = m_list[0]['unix']
                    if self.topid >= m_id:
                        print('pan_topid == json_topid' )
                        time.sleep(300)
                        continue

                    m_lives = m_list[0]['list']
                    # print(m_lives)
                    for n in range(len(m_lives)):
                        try:
                            content = m_lives[n]['desc']
                            content_prefix = m_lives[n]['title']
                            id = m_lives[n]['id']
                            news_url = 'www.panewslab.com/zh/sqarticledetails/{0}.html'.format(id)
                            Pmsg.sendmeg(news_url, content.replace("\r\n", "\n"), content_prefix)
                            time.sleep(3)
                        except Exception as e:
                            print(e)

                    self.topid = m_id
                    print("pan_发送成功 timesleep")
                time.sleep(300)
            except Exception as e:
                print(e)
                time.sleep(600)

PAN = Pannews()