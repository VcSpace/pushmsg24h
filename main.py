import threading

from src.jinse import Js
from src.odaily import oda
from src.babtc import babtc
from src.tuoluo import Tl
from src.CoinTime import coin_time

def run():
    t1 = threading.Thread(target=Js.get_news, args=(), daemon=True)
    t2 = threading.Thread(target=oda.get_news, args=(), daemon=True)
    t3 = threading.Thread(target=Tl.get_news, args=(), daemon=True)
    t4 = threading.Thread(target=coin_time.get_news, args=(), daemon=True)
    t1.start()
    t2.start()
    t3.start()
    t4.start()


if __name__ == '__main__':
    # run()
    # Js.get_news()
    # oda.get_news()
    # ti.get_news()
    # Tl.get_news()
    coin_time.get_news()
