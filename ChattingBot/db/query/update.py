from . import util

def petCountBySerial(petCount, serial):
    return "UPDATE %s SET %s.petCount=%d WHERE %s.serial = \'%s\';" %(
    util.SERIAL_TABLE_NAME, util.SERIAL_TABLE_NAME, petCount, util.SERIAL_TABLE_NAME, serial)