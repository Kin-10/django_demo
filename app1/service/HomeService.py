from utils.DBUtil import DBUtil as Dao

dao = Dao("db_81_e_fr")


class HomeService(object):
    def get_list(self):
        """
        :return:
        """
        sql = """
        select * from REPORT_DJANGO_SMS_LOG t where SMS_TO = %s
        """
        params = ['17777780817']
        res = dao.query_sql(sql, params)
        return res
