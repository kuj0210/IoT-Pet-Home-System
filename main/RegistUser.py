import pymysql, requests

class RegistUser:
    def __init__(self):
        self.conn = None
        self.curs = None
        self.PiKey = None

    def openDatabase(self):
        self.conn = pymysql.connect(host="localhost", user="root", password="apmsetup", charset="utf8")
        self.curs = self.conn.cursor()

        try:
            with self.conn.cursor() as self.curs:
                query = "use USERdata;"
                self.curs.execute(query)
        except:
            with self.conn.cursor() as self.curs:
                query = "create database USERdata DEFAULT CHARACTER SET utf8 collate utf8_general_ci;"
                self.curs.execute(query)
            self.conn.commit()

            with self.conn.cursor() as self.curs:
                query = "use USERdata;"
                self.curs.execute(query)

            #check table user
            try:
                with self.conn.cursor() as self.curs:
                    query = "select * from user;"
                    self.curs.execute(query)
            except:
                with self.conn.cursor() as self.curs:
                    query = """create table user(
                            user_key varchar(50),
                            Email varchar(50),
                            PiKey varchar(50),
                            primary key (Email)
                            ) ENGINE=InnoDB default character set utf8 collate utf8_general_ci;"""
                    self.curs.execute(query)
            self.conn.commit()

            # check table homeSystem
            try:
                with self.conn.cursor() as self.curs:
                    query = "select * from homeSystem;"
                    self.curs.execute(query)
            except:
                with self.conn.cursor() as self.curs:
                    query = """create table homeSystem(
                            PiKey varchar(50),
                            Email varchar(50),
                            url varchar(50)
                            ) ENGINE=InnoDB default character set utf8 collate utf8_general_ci;"""
                    self.curs.execute(query)
                self.conn.commit()

    def updatePiSetting(self, PiKey, userList, url):
        try:
            with self.conn.cursor() as self.curs:
                query = "delete from homeSystem where PiKey=%s;"
                self.curs.execute(query, PiKey)
            self.conn.commit()

            with self.conn.cursor() as self.curs:
                for i in userList:
                    query = "insert into homeSystem values (%s, %s, %s);"
                    self.curs.execute(query, (PiKey, userList[i], url))
            self.conn.commit()

        except:
            with self.conn.cursor() as self.curs:
                for email in userList:
                    query = "insert into homeSystem values (%s, %s, %s);"
                    self.curs.execute(query, (PiKey, email, url))
            self.conn.commit()

    def insertUserData(self, user_key, email, PiKey):
        with self.conn.cursor() as self.curs:
            query = "select * from user where user.email = %s;"
            self.curs.execute(query, email)
            rows = self.curs.fetchall()

            if len(rows) > 0 :
                message = "등록된 유저"
                return message
            try:
                with self.conn.cursor() as self.curs:
                    query = "select * from user where user.email=%s and user.PiKey=%s;"
                    self.curs.execute(query, (email,PiKey))

                    query = "insert into user values (%s, %s, %s);"
                    self.curs.execute(query, (user_key, email, PiKey))
                    self.conn.commit()
                message = "등록 완료"
                return message

            except:
                message = "등록되지 않은 키"
                return message

    def findURLandPiKey(self, user_key):
        with self.conn.cursor() as self.curs:
            query = "select url,user.PiKey from user join homeSystem on user.Email=homeSystem.Email where user.user_key=%s;"
            self.curs.execute(query, user_key)

        rows = self.curs.fetchall()
        url = rows[0][0]
        PiKey = rows[0][1]
        return url, PiKey

    def checkRegistedUser(self, user_key):
        with self.conn.cursor() as self.curs:
            query = "select email from user where user.user_key=%s;"
            self.curs.execute(query, user_key)

            rows = self.curs.fetchall()
            if len(rows) > 0: return True
            else : return False

    def findUserEmail(self, user_key):
        with self.conn.cursor() as self.curs:
            query = "select email from user where user.user_key=%s;"
            self.curs.execute(query,user_key)
            rows = self.curs.fetchall()

        if len(rows) > 0:
            message = "회원님의 E-mail은 아래와 같습니다\n %s" %(rows[0])
            return message
        else :
            return "등록되지 않은 유저입니다. 등록부터 진행해주세요."

    def closeDatabase(self):
        self.conn.close()
        
