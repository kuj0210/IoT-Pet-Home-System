import pymysql
from .query import create, delete, insert, select, update, util
from ChattingBot.reply import reply
from ChattingBot.reply import exception

class Register:
	def __init__(self):
		# DB 계정정보 관리
		self.conn = None
		self.curs = None
		self.serial = None

		#로그 정보
		self.LOG = "DB_LOG"

	def connectDB(self):
		from . import dbcon
		self.conn = pymysql.connect(
			host=dbcon.host, user=dbcon.user, password=dbcon.pw, charset=dbcon.charset)
		self.curs = self.conn.cursor()
		try:
			self.curs.execute(util.USE_DB_QUERY)
		except:
			self.curs.execute(create.DB_QUERY)
			self.conn.commit()
			self.curs.execute(util.USE_DB_QUERY)

	def checkUserTable(self):
		self.curs = self.conn.cursor()
		try:
			self.curs.execute(select.USER_TABLE_QUERY)
		except:
			self.curs.execute(create.USER_TABLE_QUERY)
			self.conn.commit()

	def checkSystemTable(self):
		self.curs = self.conn.cursor()
		try:
			self.curs.execute(select.SERIAL_TABLE_QUERY)
		except:
			self.curs.execute(create.SERIAL_TABLE_QUERY)
			self.conn.commit()

	def checkRequestTable(self):
		self.curs = self.conn.cursor()
		try:
			self.curs.execute(select.REQUEST_TABLE_QUERY)
		except:
			self.curs.execute(create.REQUEST_TABLE_QUERY)
			self.conn.commit()

	def checkTempIdTable(self):
		self.curs = self.conn.cursor()
		try:
			self.curs.execute(select.TEMPID_TABLE_QUERY)
		except:
			self.curs.execute(create.TEMPID_TABLE_QUERY)
			self.conn.commit()

	def checkSavedImageTable(self):
		self.curs = self.conn.cursor()
		try:
			self.curs.execute(select.SAVED_IMAGE_TABLE_QUERY)
		except:
			self.curs.execute(create.SAVED_IMAGE_TABLE_QUERY)
			self.conn.commit()

	def openDB(self):
		self.connectDB()
		self.checkUserTable()
		self.checkSystemTable()
		self.checkRequestTable()
		self.checkTempIdTable()
		self.checkSavedImageTable()

	def closeDB(self):
		self.conn.close()

	def checkRegistedUserForOuter(self, user_key):
		self.openDB()
		self.curs = self.conn.cursor()
		try:
			self.curs.execute(select.userKeyByUserKey(user_key))
			rows = self.curs.fetchall()
			self.closeDB()

			if len(rows) > 0:
				return True
			else:
				return False
		except:
			self.closeDB()
			return False
			
	def checkRegistedUser(self, user_key):
		self.curs = self.conn.cursor()
		try:
			self.curs.execute(select.userKeyByUserKey(user_key))
			rows = self.curs.fetchall()

			if len(rows) > 0:
				return True
			else:
				return False

		except:
			return False
		
	def checkRegistedSerial(self, serial):
		self.curs = self.conn.cursor()
		try:
			print(serial)
			self.curs.execute(select.serialBySerial(serial))
			rows = self.curs.fetchall()
			print(rows)
			print(len(rows))
			if (len(rows)) > 0:
				return True
			else :
				return False
		except:
			return False

	def checkTempIDByTempID(self, tempID):
		self.curs = self.conn.cursor()
		try:
			self.curs.execute(select.tempinfoByTempId(tempID))
			if len(self.curs.fetchall()) > 0:
				return True
			else:
				return False
		except:
			return False

	def getPetName(self, user_key):
		self.openDB()
		self.curs = self.conn.cursor()
		
		try:
			self.curs.execute(select.petNameByUserKey(user_key))
			rows = self.curs.fetchone()
			self.closeDB()
			return " ".join(rows)
		except:
			self.closeDB()
			return exception.FAIL_TO_SELECT

	def insertUserData(self, user_key, serial, email, petname):
		self.openDB()
		self.curs = self.conn.cursor()

		if self.checkRegistedUser(user_key) == True:
			return exception.REGISTERD_USER

		try:
			if self.checkRegistedSerial(serial) == False:
				return exception.NO_REGISTERD_SERIAL

			self.curs.execute(insert.userTable(user_key,serial, email, petname))
			self.conn.commit()
			self.closeDB()
			return reply.SUCESS_IST_USER
		except:
			self.closeDB()
			return exception.DONT_REGIST
	
	def insertUserRequest(self, user_key, request):
		self.openDB()
		self.curs = self.conn.cursor()

		if self.checkRegistedUser(user_key) == False:
			return exception.NO_REGISTERD_USER
		serial = self.getSerialFromUser(user_key)
		try:
			self.curs.execute(insert.requestTable(user_key, serial, request))
			self.conn.commit()
			self.closeDB()
			return reply.SUCESS_RECEVIED_MSG
		except:
			self.closeDB()
			return exception.UNSUPPORTED_TYPE_COMMAND

	def fetchRequest(self, serial):
		self.openDB()
		self.curs = self.conn.cursor()

		if self.checkRegistedSerial(serial) == False:
			return exception.NO_REGISTERD_SERIAL

		try:
			self.curs.execute(select.requestBySerial(serial))
			rows=self.curs.fetchall()

			if len(rows)<=0:
				self.closeDB()
				return False

			self.curs.execute(delete.requestBySerial(serial))
			self.conn.commit()
			self.closeDB()
			return self.listToString(rows)
		except:
			self.closeDB()
			return

	def deleteUserData(self, user_key):
		self.openDB()
		self.curs = self.conn.cursor()

		if self.checkRegistedUser(user_key) == False:
			return reply.SUCESS_DEL_NO_REGISTERD_USER
		try:
			self.curs.execute(delete.userTableByUserKey(user_key))
			self.conn.commit()
			self.closeDB()
			return reply.SUCESS_DEL_REGISTERD_USER
		except:
			self.closeDB()
			return  exception.DEL_REGISTERD_USER

	def deleteTempID(self, tempID):
		self.openDB()
		self.curs = self.conn.cursor()

		if self.checkTempIDByTempID(tempID) == False:
			return False

		try:
			self.curs.execute(delete.tempinfoByID(tempID))
			self.conn.commit()
			self.closeDB()
			return True
		except:
			self.closeDB()
			return False

	def updatePetCount(self, user_key, petCount):
		self.openDB()
		self.curs = self.conn.cursor()

		try:
			self.curs.execute(select.userSerialByUserKey(user_key))
			rows = self.curs.fetchall()
			if len(rows) <= 0:
				return False

			serial = rows[0][0]
			if self.checkRegistedSerial(serial=serial) == False:
				return False

			print(update.petCountBySerial(petCount=int(petCount), serial=serial))
			self.curs.execute(update.petCountBySerial(petCount=int(petCount), serial=serial))
			self.conn.commit()
			self.closeDB()
			return True
		except:
			self.closeDB()
			return False

	def getSerialFromUser(self,user_key):
		self.curs = self.conn.cursor()
		if self.checkRegistedUser(user_key) == False:
			return exception.NO_REGISTERD_USER
		try:
			self.curs.execute(select.userSerialByUserKey(user_key))
			rows = self.curs.fetchall()
			
			if len(rows)<=0:
				return False
			return rows[0][0]
		except:
			return  exception.SELECT_FROM_CHECKING_SERIAL

	def getUserFromSerial(self, serial):
		self.openDB()
		self.curs = self.conn.cursor()

		if self.checkRegistedSerial(serial) == False:
			self.closeDB()
			return exception.NO_REGISTERD_SERIAL
		try:
			self.curs.execute(select.userKeyBySerial(serial))
			rows = self.curs.fetchall()
			self.closeDB()

			if len(rows)<=0:
				return False
				
			return self.listToString(rows)
		except:
			print("getUserFromSerial error")
			self.closeDB()
			return  exception.SELECT_FROM_CHECKING_USER

	def getPetCountFromSerial(self,serial):
		self.openDB()
		self.curs = self.conn.cursor()
		if self.checkRegistedSerial(serial) == False:
			self.closeDB()
			return exception.NO_REGISTERD_SERIAL
		try:
			petCNT =self.curs.execute(select.petCountBySerial(serial))
			self.closeDB()
			return petCNT
		except:
			self.closeDB()
			return  -1

	def insertTempID(self, user_key, id):
		self.openDB()
		self.curs = self.conn.cursor()

		if self.checkRegistedUser(user_key=user_key) == True:
			return False

		try:
			self.curs.execute(insert.tempIdTable(user_key, id))
			self.conn.commit()
		except:
			return exception.DONT_REGIST

	def getUserKeyByTempID(self, tempID):
		self.openDB()
		self.curs = self.conn.cursor()

		try:
			self.curs.execute(select.userKeyByTempID(tempID))
			user_key = self.curs.fetchall()[0][0]
			self.closeDB()
			return user_key
		except:
			self.closeDB()
			return None

	def listToString(self,list):
		str=""
		for item in list:
			for atom in item:
				str+=atom+" "
			str+="\n"
		print("list to string:::"+str)
		return str

if __name__=="__main__":
	user ="u9-NF6yuZ8H8TAgj1uzqnQ"
	Reg =Register()
	
	print(Reg.insertUserRequest(user,"TEST1 TEST2 TEST3"))
	print(Reg.insertUserRequest("testor","TEST4"))
