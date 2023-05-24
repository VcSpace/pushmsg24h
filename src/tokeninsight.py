import requests
import time
import json

from src.push_msg import Pmsg

class TOKEN_IN(object):
    def __init__(self):
        self.topid = '0'
        self.date = ''

    def get_news(self):
        while True:
            session = requests.Session()
            session.get('https://cn.tokeninsight.com/zh/news')
            m_json = ''
            url = 'https://tokeninsight.com/apiv2/research/newsList'
            headers = {
                'Accept': 'application/json, text/plain, */*',
                'referer': 'https://tokeninsight.com/zh/news',
                'Host': 'cn.tokeninsight.com',
                'Content-Type':'application/json',
                'cookie': 'language_=zh; language=cn; _ga=GA1.1.1942975179.1684938824; _ga_3F9MFYLVT6=GS1.1.1684938824.1.1.1684939141.60.0.0; __cf_bm=gSjkNX.lfGox_nyh4aU01V.9ePt3GhDFI0lFz6YaTpQ-1684939151-0-AWerUzhwL71tAEiglNbAAU2JRxXBZG7Gtb2nJOh+hNpWbwoUf8YLw7r1hHtvx1eQuzbQ4ON1Zr+NsT1X8d7Arvc=; cookieShow=true',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15'
            }
            data = '{{\"current\":1,\"language\":\"cn\",\"pageSize\":10,\"tagId\":\"\",\"startDate\":\"\",\"endDate\":\"\"}}'
            data2 = {
                "current":1,
                "language":"cn",
                "pageSize":10,
                "tagId":"",
                "startDate":"",
                "endDate":""
            }

            try:
                res = session.post(url, headers=headers, data=data, timeout=60)
                if res.status_code == 200:
                    one_json = json.loads(res.text)
                    m_json = one_json['data']['list']
                    print(m_json)
                    if self.topid == m_json[0]['tagId']:
                        print('topid == json_topid' )
                        time.sleep(300)
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
                            Pmsg.sendmeg(news_url, content, content_title)
                            time.sleep(3)

                self.topid = m_json[0]['tagId']
                time.sleep(300)
            except Exception as e:
                print(e)

tkin = TOKEN_IN()