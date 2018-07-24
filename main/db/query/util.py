# DB 정보관리 , 테이블 명칭 변경 시 모든 쿼리에 적용
DB_NAME = "SystemData"
USER_TABLE_NAME = "naverUser"
SERIAL_TABLE_NAME = "homeSystem"
REQUEST_NAME = "request"
TEMPID_TABLE_NAME = "TempID"
SAVED_IMAGE_TABLE_NAME = "OldImageList"
# 쿼리문 관리

##DB사용 쿼리문
USE_DB_QUERY = "use %s;" % (DB_NAME)

# 전달문자관리
SUCESS_TO_REGIST = "등록 완료"
SUCESS_DEL_NO_REGISTERD_USER = "미등록 유저입니다. 모든 정보들이 삭제되었습니다"
SUCESS_DEL_REGISTERD_USER = "등록 시 넣은 정보들이 정상 삭제 되었습니다."
# 성공

FAIL_TO_REGIST_USER = "사용자 등록에 실패하셨습니다. 이미 등록된 유저이거나 잘못된 시리얼 넘버입니다."