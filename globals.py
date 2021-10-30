
# 여러 파일에서 공유할때 쓸 변수들
# import 해서 사용하소
# from globals import <변수명>
import os

WIN = False
DEBUG = True
DEBUG_COOR = False
COLOR_PALETTE = False
kbhit = 'none'

def cls():
	if WIN:
		os.system('cls')
	else:
		os.system('clear')