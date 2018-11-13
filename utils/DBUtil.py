# coding:utf-8
from django.db import connections, transaction


class DBUtil(object):
    def __init__(self, db_name="default"):
        self.db_name = db_name

    def get_cursor(self):
        return connections[self.db_name]

    def query_sql(self, sql, params=None):
        """
        查询数据
        :param sql:
        :param params:
        :return:
        """
        cursor = connections[self.db_name].cursor()
        cursor.execute(sql, params)
        result = cursor.fetchall()
        list = []
        try:
            for row in result:
                r = dict(zip([x[0] for x in cursor.description], row))
                list.append(r)
            return list
        except Exception as e:
            print(e.message)
            return None
        finally:
            if cursor is not None:
                cursor.close()

    def update_sql(self, sql, params=None, rowid=False):
        """
        插入/更新数据
        :param sql:
        :param params:
        :return:
        """
        cursor = connections[self.db_name].cursor()
        try:
            cursor.execute(sql, params)
            count = cursor.rowcount
            if rowid is True:
                count = cursor.lastrowid
            return count
        except Exception as e:
            print(e.message)
            return 0
        finally:
            if cursor is not None:
                cursor.close()

    def update_multi(self, sql, paramsList=None):
        """
        批量操作
        :param sql:
        :param paramsList:[(tuple)]
        :return:
        """
        cursor = connections[self.db_name].cursor()
        try:
            cursor.executemany(sql, paramsList)
            rowcount = cursor.rowcount
            return rowcount
        except Exception as e:
            print(e.message)
            return 0
        finally:
            if cursor is not None:
                cursor.close()

    def update_multi_with_transaction(self, sqlList):
        """
        带事物的批量操作
        :param sqlList:
        :param paramsList:
        :return:
        """
        cursor = connections[self.db_name].cursor()
        transaction.set_autocommit(False)
        success = 0
        try:
            for sql in sqlList:
                cursor.execute(sql)
                success = success + 1
            transaction.commit()
            return cursor.rowcount
        except Exception as e:
            print(e.message)
            success = 0
            transaction.rollback()
        finally:
            if cursor is not None:
                cursor.close()
        return success
