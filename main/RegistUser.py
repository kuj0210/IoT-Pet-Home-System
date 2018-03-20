'''
Copyright (c) IoT-Pet-Home-system team : Woo-jin Kim, Keon-hee Lee, Dae-seok Ko
LICENSE : GPL v3 LICENSE

- Description : https://github.com/kuj0210/IoT-Pet-Home-System
- If you want to contact us, please send mail "beta1360@naver.com"
'''
import pymysql

class RegistUser:
'''
This class is related database(MySQL) and use many MySQL query sentence.
Addiontionally, this class is included in ServerUtility module.
'''
    def __init__(self):
        self.conn = None
        self.curs = None
        self.PiKey = None
        self.KAKAO_TALK = "kakao-talk"
        self.NAVER_TALK = "naver-talk"

    def openDatabase(self):
    '''
    Description:
        This function approach in and set available database.
        If database don't have database and tables, this func create new database and tables.
        (This func also check them.)
    '''
        self.conn = pymysql.connect(host="localhost", user="root", password="root", charset="utf8")
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
                    query = "select * from kakaoUser;"
                    self.curs.execute(query)
            except:
                with self.conn.cursor() as self.curs:
                    query = """create table kakaoUser(
                            user_key varchar(50),
                            Email varchar(50),
                            PiKey varchar(50),
                            primary key (Email)
                            ) ENGINE=InnoDB default character set utf8 collate utf8_general_ci;"""
                    self.curs.execute(query)
            self.conn.commit()

            try:
                with self.conn.cursor() as self.curs:
                    query = "select * from naverUser;"
                    self.curs.execute(query)
            except:
                with self.conn.cursor() as self.curs:
                    query = """create table naverUser(
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
                            Platform varchar(30),
                            Email varchar(50),
                            url varchar(50)
                            ) ENGINE=InnoDB default character set utf8 collate utf8_general_ci;"""
                    self.curs.execute(query)
                self.conn.commit()

    def updatePiSetting(self, PiKey, kakaoUserList, naverUserList, url):
        try:
            with self.conn.cursor() as self.curs:
                query = "delete from homeSystem where PiKey=%s;"
                self.curs.execute(query, PiKey)
            self.conn.commit()

            with self.conn.cursor() as self.curs:
                for email in kakaoUserList:
                    query = "insert into homeSystem values (%s, %s, %s, %s);"
                    self.curs.execute(query, (PiKey, self.KAKAO_TALK, email, url))
            self.conn.commit()

            with self.conn.cursor() as self.curs:
                for email in naverUserList:
                    query = "insert into homeSystem values (%s, %s, %s, %s);"
                    self.curs.execute(query, (PiKey, self.NAVER_TALK, email, url))
            self.conn.commit()

        except:
            with self.conn.cursor() as self.curs:
                for email in naverUserList:
                    query = "insert into homeSystem values (%s, %s, %s, %s);"
                    self.curs.execute(query, (PiKey, self.KAKAO_TALK, email, url))
            self.conn.commit()

            with self.conn.cursor() as self.curs:
                for email in naverUserList:
                    query = "insert into homeSystem values (%s, %s, %s, %s);"
                    self.curs.execute(query, (PiKey, self.NAVER_TALK, email, url))
            self.conn.commit()

    def insertUserData(self, platform, user_key, email, PiKey):
        if platform == "kakao-talk":
            with self.conn.cursor() as self.curs:
                query = "select * from kakaoUser where kakaoUser.email = %s;"
                self.curs.execute(query, email)
                rows = self.curs.fetchall()

                if len(rows) > 0 :
                    message = "등록된 유저"
                    return message
                try:
                    with self.conn.cursor() as self.curs:
                        query = "select * from kakaoUser where kakaoUser.email=%s and kakaoUser.PiKey=%s;"
                        self.curs.execute(query, (email,PiKey))

                        query = "insert into kakaoUser values (%s, %s, %s);"
                        self.curs.execute(query, (user_key, email, PiKey))
                        self.conn.commit()
                    message = "등록 완료"
                    return message

                except:
                    message = "등록되지 않은 키"
                    return message
        else: # if platform == "naver-talk":
            with self.conn.cursor() as self.curs:
                query = "select * from naverUser where naverUser.email = %s;"
                self.curs.execute(query, email)
                rows = self.curs.fetchall()

                if len(rows) > 0:
                    message = "등록된 유저"
                    return message
                try:
                    with self.conn.cursor() as self.curs:
                        query = "select * from naverUser where naverUser.email=%s and naverUser.PiKey=%s;"
                        self.curs.execute(query, (email, PiKey))

                        query = "insert into naverUser values (%s, %s, %s);"
                        self.curs.execute(query, (user_key, email, PiKey))
                        self.conn.commit()
                    message = "등록 완료"
                    return message

                except:
                    message = "등록되지 않은 키"
                    return message


    def findURLandPiKey(self, platform, user_key):
        if platform == "kakao-talk":
            with self.conn.cursor() as self.curs:
                query = "select url,kakaoUser.PiKey from kakaoUser join homeSystem on kakaoUser.Email=homeSystem.Email where kakaoUser.user_key=%s;"
                self.curs.execute(query, user_key)
        else:  # if platform == "naver-talk":
            with self.conn.cursor() as self.curs:
                query = "select url,naverUser.PiKey from naverUser join homeSystem on naverUser.Email=homeSystem.Email where naverUser.user_key=%s;"
                self.curs.execute(query, user_key)

        rows = self.curs.fetchall()
        url = rows[0][0]
        PiKey = rows[0][1]
        return url, PiKey

    def checkRegistedUser(self, platform, user_key):
        if platform == "kakao-talk":
            with self.conn.cursor() as self.curs:
                query = "select email from kakaoUser where kakaoUser.user_key=%s;"
                self.curs.execute(query, user_key)
                rows = self.curs.fetchall()
                if len(rows) > 0: return True
                else : return False

        else: # if platform == "naver-talk":
            with self.conn.cursor() as self.curs:
                query = "select email from naverUser where naverUser.user_key=%s;"
                self.curs.execute(query, user_key)
                rows = self.curs.fetchall()
                if len(rows) > 0:
                    return True
                else:
                    return False

    def findUserEmail(self, platform, user_key):
        if platform == "kakao-talk":
            with self.conn.cursor() as self.curs:
                query = "select email from kakaoUser where kakaoUser.user_key=%s;"
                self.curs.execute(query,user_key)
                rows = self.curs.fetchall()
                if len(rows) > 0:
                    message = "회원님의 E-mail은 아래와 같습니다\n %s" % (rows[0])
                    return message
                else:
                    return "등록되지 않은 유저입니다. 등록부터 진행해주세요."

        else: # if platform == "naver-talk":
            with self.conn.cursor() as self.curs:
                query = "select email from naverUser where naverUser.user_key=%s;"
                self.curs.execute(query,user_key)
                rows = self.curs.fetchall()
                if len(rows) > 0:
                    message = "회원님의 E-mail은 아래와 같습니다\n %s" % (rows[0])
                    return message
                else:
                    return "등록되지 않은 유저입니다. 등록부터 진행해주세요."

    def getUserlist(self, PiKey):
        """
        Unfortunately, kakao platform don't support push service.
        Therefore naver-talk only support push service, and find users to use naver platform...
        """
        with self.conn.cursor() as self.curs:
            query = "select naverUser.user_key from naverUser join homeSystem " \
                    "on naverUser.Email=homeSystem.Email where homeSystem.PiKey=%s;"
            self.curs.execute(query, PiKey)
            userlist = []
            rows = self.curs.fetchall()
            
            for row in rows:
                userlist.append(row)

            return userlist

    def closeDatabase(self):
        self.conn.close()
        
