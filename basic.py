# 프로그램 운영시 중요한 부분을 로그로 남기는것
# 단순한 에러인지, 출력인지등을 관리하는 모듈
import logging
# print(logging.DEBUG)     # 필요한 정보를 기록
# # logging.setLevel(logging.INFO)      # 정보알림
# print(logging.WARNING)   #작동은 하지만 예상치 못한일이 발생할것으로 예측
# logger.setLevel(logging.ERROR)     #에러
# logger.setLevel(logging.CRITICAL)  # 심각한 오류

# 1.로거 생성
logger=logging.getLogger('테스트')
logger.setLevel(logging.DEBUG) #1-2 레벨설정 #레벨설정안하면 warning부터
# 2. 파일핸들러 생성
f1=logging.FileHandler('.\\data\\default.log',encoding='utf-8')
f2=logging.FileHandler('.\\data\\secret.log',encoding='utf-8')
#2-2 레벨설정
f1.setLevel(logging.WARNING)

logger.addHandler(f1) #로거와 핸들러연결
logger.addHandler(f2)
# 3. 포매터 생성
fomatter=logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')
f1.setFormatter(fomatter)
f2.setFormatter(fomatter)
# print(3)
# logger.debug('프로그램 디버그')
# logger.info('프로그램 인포')
# logger.warning('프로그램 워닝')
# logger.error('에러가 발생했어요')
# logger.critical('심각한오류')






