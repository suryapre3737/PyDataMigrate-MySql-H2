from MySqlDatabase import MySqlDatabase
from H2Database import H2Database



class Test:
    def __init__(self):
        self.mysqlDb_instance = MySqlDatabase()
        self.h2Db_instance = H2Database()

    def queryMySqlDB(self):
        self.mysqlDb_instance.connect()
        rows = self.mysqlDb_instance.query("SELECT * FROM TEST.EMPLOYEE")
        self.mysqlDb_instance.close()
        return rows

    def queryH2DB(self):
        self.h2Db_instance.connect()
        rows = self.h2Db_instance.query("SELECT * FROM EMPLOYEE")
        if rows:
            for row in rows:
                print(row)
        self.h2Db_instance.close()
    
    def queryH2DB(self):
        self.h2Db_instance.connect()
        rows = self.h2Db_instance.query("select * from EMPLOYEE")
        if rows:
            for row in rows:
                print(row)
        self.h2Db_instance.close()

    def insertIntoH2DB(self, mySqlDBResult):
        # self.h2Db_instance.query("INSERT INTO EMPLOYEE (ID, NAME) VALUES (12000, 'John12')")
        self.h2Db_instance.connect()
        if mySqlDBResult:
            for row in mySqlDBResult:
                self.h2Db_instance.query("INSERT INTO EMPLOYEE (ID, NAME) VALUES ({0}, '{1}')".format(int(row[0]), str(row[1])))
        self.h2Db_instance.close()


# Usage
obj = Test()
# mySqlDBResult = obj.queryMySqlDB()
# if mySqlDBResult:
#             for row in mySqlDBResult:
#                 print(row)
# obj.queryH2DB()
obj.insertIntoH2DB(obj.queryMySqlDB())
