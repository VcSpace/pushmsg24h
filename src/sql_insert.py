from src.config import config
import pymysql

class in_MySql(object):
    def __init__(self):
        host = config.get_server_host()
        self.localhost , self.sql_username, self.sql_password, self.sql_database, self.sql_table = config.get_sql_info()

    def connect(self):
        self.db = pymysql.connect(self.localhost, self.sql_username, self.sql_password, self.sql_database)

        # 使用cursor()方法获取操作游标
        self.cursor = self.db.cursor()
        #
        # sql = """INSERT INTO {0}(
        #          news_id, news_title, news_content, news_url, now())
        #          VALUES ('Mac', 'Mohan', 20, 'M', 2000)""".format(self.table)
        # try:
        #    # 执行sql语句
        #    self.cursor.execute(sql)
        #    # 提交到数据库执行
        #    self.db.commit()
        # except:
        #    # 如果发生错误则回滚
        #    self.db.rollback()

        # 关闭数据库连接
        self.db.close()


Sql = in_MySql()