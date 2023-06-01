import threading

from src.jinse import Js
from src.odaily import oda
from src.babtc import babtc
from src.tokeninsight import ti
from src.sql_insert import Sql
from src.tuoluo import Tl

def run():
    t1 = threading.Thread(target=Js.get_news, args=())
    t2 = threading.Thread(target=oda.get_news, args=())
    t3 = threading.Thread(target=Tl.get_news, args=())
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
if __name__ == '__main__':
    run()
    # Js.get_news()
    # oda.get_news()
    # ti.get_news()
    # Tl.get_news()
