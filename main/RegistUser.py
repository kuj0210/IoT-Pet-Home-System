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
        Description
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
                
    def closeDatabase(self):
        '''
        Description
            This function close to connect with database. 
            Usually, when database don't need to use, it use.
        '''
        self.conn.close()

    def updatePiSetting(self, PiKey, kakaoUserList, naverUserList, url):
        '''
        1. Arguement
            - PiKey : Device information that is registed in database.
            - kakaoUserList : Userlist, using kakao-talk platform, 
                              to recieve from device that request to update its information. 
            - naverUserList : Userlist, using naver-talk-talk platform, 
                              to recieve from device that request to update its information. 
            - url : Device's ip and port number for using port-forwarding.\

        2. Description
            This function updates information recieved from device(pi-server).
            Actually, when device(pi-server) turn on, this func is executed.
        '''
        try:
            with self.conn.cursor() as self.curs:
                query = "delete from homeSystem where PiKey=%s;" %(PiKey)
                self.curs.execute(query)
            self.conn.commit()

            with self.conn.cursor() as self.curs:
                for email in kakaoUserList:
                    query = "insert into homeSystem values (%s, %s, %s, %s);" %(PiKey, self.KAKAO_TALK, email, url)
                    self.curs.execute(query)
            self.conn.commit()

            with self.conn.cursor() as self.curs:
                for email in naverUserList:
                    query = "insert into homeSystem values (%s, %s, %s, %s);" %(PiKey, self.NAVER_TALK, email, url)
                    self.curs.execute(query)
            self.conn.commit()

        except:
            with self.conn.cursor() as self.curs:
                for email in naverUserList:
                    query = "insert into homeSystem values (%s, %s, %s, %s);" %(PiKey, self.KAKAO_TALK, email, url)
                    self.curs.execute(query)
            self.conn.commit()

            with self.conn.cursor() as self.curs:
                for email in naverUserList:
                    query = "insert into homeSystem values (%s, %s, %s, %s);"
                    self.curs.execute(query, (PiKey, self.NAVER_TALK, email, url))
            self.conn.commit()

    def insertUserData(self, platform, user_key, email, PiKey):
        '''
        1. Arguement
            - platfrom : "kakao-talk" | "naver-talk"
            - user_key : user_key recieved from platform's API server.
            - email : The information;email what that user input.
            - PiKey : The information;PiKey what that user input.

        2. Output
            Below data will be sent to ServerManager moudle. 
            - "등록된 유저" : If you registed in main-server 
                             and when main-server check that this user is a registed user. 
            - "등록되지 않은 키" :  If a PiKey wasn't registed in main-server
            - "등록 완료" : When registration step is completed

        3. Description
            This function is used to determine if the user is already registered to register information 
            with the main server and if the device key(PiKey) being registered with the server is correct.
            Also, if the checking step isn't the two types result(registed user, unregisted key),
            this func insert the information to database. Usually, this func use to recieved the request
            that a user send "[등록]/email/PiKey" message to main-server.
        '''
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

                        query = "insert into kakaoUser values (%s, %s, %s);" %(user_key, email, PiKey)
                        self.curs.execute(query)
                        self.conn.commit()
                    message = "등록 완료"
                    return message

                except:
                    message = "등록되지 않은 키"
                    return message
        else: # if platform == "naver-talk":
            with self.conn.cursor() as self.curs:
                query = "select * from naverUser where naverUser.email = %s;" %(email)
                self.curs.execute(query)
                rows = self.curs.fetchall()

                if len(rows) > 0:
                    message = "등록된 유저"
                    return message
                try:
                    with self.conn.cursor() as self.curs:
                        query = "select * from naverUser where naverUser.email=%s and naverUser.PiKey=%s;" %(email, PiKey)
                        self.curs.execute(query)

                        query = "insert into naverUser values (%s, %s, %s);" %(user_key, email, PiKey)
                        self.curs.execute(query)
                        self.conn.commit()
                    message = "등록 완료"
                    return message

                except:
                    message = "등록되지 않은 키"
                    return message


    def findURLandPiKey(self, platform, user_key):
        '''
        1. Arguement
            - platform : "naver-talk" | "kakao-talk"
            - user_key : To use the conditions of query sentence.

        2. Output
            URL, PiKey : To use many request to send correct url.

        3. Description
            This function refer a device's url and PiKey by using the platform and user_key.
            Pi-Server recognize correct url from a form;"<url>/<PiKey>/<operation>"
        '''
        if platform == "kakao-talk":
            with self.conn.cursor() as self.curs:
                query = "select url,kakaoUser.PiKey from kakaoUser join homeSystem on kakaoUser.Email=homeSystem.Email where kakaoUser.user_key=%s;" %(user_key)
                self.curs.execute(query)
        else:  # if platform == "naver-talk":
            with self.conn.cursor() as self.curs:
                query = "select url,naverUser.PiKey from naverUser join homeSystem on naverUser.Email=homeSystem.Email where naverUser.user_key=%s;" %(user_key)
                self.curs.execute(query)

        rows = self.curs.fetchall()
        url = rows[0][0]
        PiKey = rows[0][1]
        return url, PiKey

    def checkRegistedUser(self, platform, user_key):
        '''
        1. Arguement
            - platform : "naver-talk" | "kakao-talk"
            - user_key : To use the conditions of query sentence.

        2. Output
            True or False : Is this user the registed user? 

        3. Description
            This function use to check registed or unregisted user. 
            Usually, before message or data pasing step is executed, this func check them.
        '''
        if platform == "kakao-talk":
            with self.conn.cursor() as self.curs:
                query = "select email from kakaoUser where kakaoUser.user_key=%s;" %(user_key)
                self.curs.execute(query)
                rows = self.curs.fetchall()
                if len(rows) > 0: return True
                else : return False

        else: # if platform == "naver-talk":
            with self.conn.cursor() as self.curs:
                query = "select email from naverUser where naverUser.user_key=%s;" %(user_key)
                self.curs.execute(query)
                rows = self.curs.fetchall()
                if len(rows) > 0:
                    return True
                else:
                    return False

    def findUserEmail(self, platform, user_key):
        '''
        1. Arguement
            - platform : "naver-talk" | "kakao-talk"
            - user_key : To use the conditions of query sentence.

        2. Output
            An appropriate response to send user

        3. Description
            When a user request "[정보]" to this server(main-server), this function is executed.
            If the user is registed user, this func inform the user's email. If not, this requests regist to the user.
        '''
        if platform == "kakao-talk":
            with self.conn.cursor() as self.curs:
                query = "select email from kakaoUser where kakaoUser.user_key=%s;" %(user_key)
                self.curs.execute(query)
                rows = self.curs.fetchall()
                if len(rows) > 0:
                    message = "회원님의 E-mail은 아래와 같습니다\n %s" % (rows[0])
                    return message
                else:
                    return "등록되지 않은 유저입니다. 등록부터 진행해주세요."

        else: # if platform == "naver-talk":
            with self.conn.cursor() as self.curs:
                query = "select email from naverUser where naverUser.user_key=%s;" %(user_key)
                self.curs.execute(query)
                rows = self.curs.fetchall()
                if len(rows) > 0:
                    message = "회원님의 E-mail은 아래와 같습니다\n %s" % (rows[0])
                    return message
                else:
                    return "등록되지 않은 유저입니다. 등록부터 진행해주세요."

    def getUserlist(self, PiKey):
        '''
        1. Arguement
            - PiKey : To use the conditions of query sentence.

        2. Output
            The userlist included a PiKey's device.

        3. Description
            If this system want to inform push-alarm, this function is executed.
            Because this system must inform the correct users who is included their device data.

            +) Unfortunately, kakao platform don't support push service.
            Therefore naver-talk only support push service, and find users to use naver platform...
        '''
    
        with self.conn.cursor() as self.curs:
            query = "select naverUser.user_key from naverUser join homeSystem on naverUser.Email=homeSystem.Email where homeSystem.PiKey=%s;" %(PiKey)
            self.curs.execute(query)
            userlist = []
            rows = self.curs.fetchall()
            
            for row in rows:
                userlist.append(row)

            return userlist