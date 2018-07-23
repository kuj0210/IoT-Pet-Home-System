from . import util

def userTable(user_key, serial, email, petname):
    return "insert into %s values (\"%s\", \"%s\", \"%s\", \"%s\");" % (
		util.USER_TABLE_NAME, user_key, serial, email, petname)

def tempIdTable(user_key, id):
    return "insert into %s values (\"%s\", \"%s\");" %(
        util.TEMPID_TABLE_NAME, user_key, id)

def oldimagelistTable(addr, serial):
    return "insert into %s values (\"%s\", \"%s\");" %(
        util.SAVED_IMAGE_TABLE_NAME, addr, serial)

def serialTable(serial, pet_cnt):
    return "insert into %s values (\"%s\", %d);" %(
        util.SERIAL_TABLE_NAME, serial, pet_cnt)

def requestTable(user_key, serial, request):
    return "insert into %s values (\"%s\", \"%s\",\"%s\");" % (
		util.REQUEST_NAME, serial, user_key, request)