import requests
import time
import json
import distutils

from requests.cookies import RequestsCookieJar
from src.push_msg import Pmsg

class TOKEN_IN(object):
    def __init__(self):
        self.topid = '0'
        self.date = ''

    def get_news(self):
        while True:
            session = requests.Session()
            # cookie_jar = session.get('https://cn.tokeninsight.com/zh/news').cookies
            # cookie_t = requests.utils.dict_from_cookiejar(cookie_jar)
            m_json = ''
            url = 'https://tokeninsight.com/apiv2/research/newsList'
            url = 'https://back.tokeninsight.com/app/news/list?date=&page=1&size=30'
            headers2 = {
                'Accept': 'application/json, text/plain, */*',
                'referer': 'https://tokeninsight.com/zh/news',
                'Content-Type':'application/json',
                'Cookie': 'language_=zh; language=cn; cf_bm=18BF4wWkNwA9vouobb_pe3ZNfmODPDeekfZIVIP88Is-1684942722-0-AVpxJJgapGxbRLA0SOFl0v6XV3b7AQA/6/GqM3My8AIUaVe4pINfeyTais+qRRbr3XJzVY1jPJv0DeVchdvzKT0=; SERVERID=efe99b30cbeeac07a0a49ddc4c447aee|1684943591|1684942722; SERVERCORSID=efe99b30cbeeac07a0a49ddc4c447aee|1684943591|1684942722',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15'
            }

            headers = {
                'Host': 'back.tokeninsight.com',
                'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'Accept': '*/*',
                'lan': 'cn',
                'platform': 'iOS',
                'User-Agent': 'TokenInsight_iOS/1.3.4 (iPhone; iOS 16.1.1; Scale/3.00)',
                'Connection': 'keep-alive'
            }
            data = '{{\"current\":1,\"language\":\"cn\",\"pageSize\":10,\"tagId\":\"\",\"startDate\":\"\",\"endDate\":\"\"}}'
            data = {
                "current":1,
                "language":"cn",
                "pageSize":10,
                "tagId":"",
                "startDate":"",
                "endDate":""
            }

            try:
                res = session.get(url, headers=headers, timeout=60)
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