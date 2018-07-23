from . import util

##테이블 선택 쿼리문
USER_TABLE_QUERY = "select * from %s;" % (util.USER_TABLE_NAME)
SERIAL_TABLE_QUERY = "select * from %s;" % (util.SERIAL_TABLE_NAME)
REQUEST_TABLE_QUERY = "select * from %s;" % (util.REQUEST_NAME)
TEMPID_TABLE_QUERY = "select * from %s;" %(util.TEMPID_TABLE_NAME)
SAVED_IMAGE_TABLE_QUERY = "select * from %s;" %(util.SAVED_IMAGE_TABLE_NAME)

def userKeyByUserKey(user_key):
    return "select user_key from %s where %s.user_key = \"%s\";" % (
		util.USER_TABLE_NAME, util.USER_TABLE_NAME, user_key)

def userKeyByUserKey(user_key):
    return "select user_key from %s where %s.user_key = \"%s\";" % (
		util.USER_TABLE_NAME, util.USER_TABLE_NAME, user_key)

def userKeyBySerial(serial):
    return "select user_key from %s where %s.serial = \"%s\";" % (
		util.USER_TABLE_NAME, util.USER_TABLE_NAME, serial)

def userKeyByPetname(pet_name):
    return "select user_key from %s where %s.petName = \"%s\";" %(
        util.USER_TABLE_NAME, util.USER_TABLE_NAME, pet_name)

def userKeyByEmail(email):
    return "select user_key from %s where %s.Email = \"%s\";" %(
        util.USER_TABLE_NAME, util.USER_TABLE_NAME, email)

def userKeyByTempID(tempID):
    return "select user_key from %s where %s.ID = \"%s\";" %(
        util.TEMPID_TABLE_NAME, util.TEMPID_TABLE_NAME, tempID)

def petNameByUserKey(user_key):
    return "select petName from %s where %s.user_key = \"%s\";" %(
        util.USER_TABLE_NAME, util.USER_TABLE_NAME, user_key)

def petNameBySerial(serial):
    return "select petName from %s where %s.serial = \"%s\";" %(
        util.USER_TABLE_NAME, util.USER_TABLE_NAME, serial)

def emailByUserKey(email):
    return "select Email from %s where %s.user_key = \"%s\";" %(
        util.USER_TABLE_NAME, util.USER_TABLE_NAME, email)

def emailBySerial(serial):
    return "select Email from %s where %s.serial = \"%s\";" %(
        util.USER_TABLE_NAME, util.USER_TABLE_NAME, serial)

def userByUserKeyAndSerial(user_key, serial):
    return "select * from %s where %s.user_key=\"%s\" and user_key.serial=\"%s\";" % (
		util.USER_TABLE_NAME , user_key, util.USER_TABLE_NAME, serial)

def tempinfoByTempId(temp_id):
    return "select * from %s where ID = \"%s\";" %(
        util.TEMPID_TABLE_NAME, temp_id)

def tempidByUserKey(user_key):
    return "select ID from %s where user_key = \"%s\";" %(
        util.TEMPID_TABLE_NAME, user_key)

def pathBySerial(serial):
    return "select addr from %s where serial = \"%s\";" %(
        util.SAVED_IMAGE_TABLE_NAME, serial)

def serialBySerial(serial):
    return "select * from %s where %s.serial = \"%s\";" % (
		util.SERIAL_TABLE_NAME, util.SERIAL_TABLE_NAME, serial)

def petCountBySerial(serial):
    return "select petCount from %s where %s.serial = \"%s\";" %(
        util.SERIAL_TABLE_NAME, util.SERIAL_TABLE_NAME, serial)

def userSerialByUserKey(user_key):
    return "select %s.serial from %s where %s.user_key = \"%s\";" % (
		util.USER_TABLE_NAME, util.USER_TABLE_NAME, util.USER_TABLE_NAME, user_key)

def requestBySerial(serial):
    return "select * from %s where %s.serial = \"%s\";" % (
		util.REQUEST_NAME, util.REQUEST_NAME, serial)

def requesterBySerial(serial):
    return "select requestor from %s where %s.serial = \"%s\";" % (
		util.REQUEST_NAME, util.REQUEST_NAME, serial)

def requestsBySerial(serial):
    return "select request from %s where %s.serial = \"%s\";" % (
		util.REQUEST_NAME, util.REQUEST_NAME, serial)