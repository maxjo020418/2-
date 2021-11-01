
# 여러 파일에서 공유할때 쓸 변수들
# import 해서 사용하소
# from globals import <변수명>
import os

WIN = False # 윈도, 리눅스 기반 시스템 판별 - Flase는 리눅스
DEBUG = True # 시작 debug
DEBUG_COOR = False # grfx 좌표 debug
COLOR_PALETTE = True # 색갈 코드, 팔레트 출력

kbhit = 'none' # 키보드 키 저장 - 초기화 none

def cls(): # clear terminal 커맨드
	if WIN:
		os.system('cls')
	else:
		os.system('clear')