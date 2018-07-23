from . import util

def userTableByUserKey(user_key):
    return "delete from %s where %s.user_key =\"%s\";" % (
		util.USER_TABLE_NAME, util.USER_TABLE_NAME, user_key)

def requestBySerial(serial):
    return "delete from %s where %s.serial = \"%s\";" % (
		util.REQUEST_NAME, util.REQUEST_NAME, serial)

def tempinfoByID(id):
    return "delete from %s where ID=\"%s\";" %(
        util.TEMPID_TABLE_NAME, id)

def imageBySerial(serial):
    return "delete from %s where serial=\"%s\";" %(
        util.SERIAL_TABLE_NAME, serial)