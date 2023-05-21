import threading

from src.jinse import Js
from src.odaily import oda
from src.sql_insert import Sql

def run():
    t1 = threading.Thread(target=Js.get_news, args=())
    t2 = threading.Thread(target=oda.get_news, args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()
if __name__ == '__main__':
    # run()
    # Js.get_news()
    oda.get_news()

    # print('')