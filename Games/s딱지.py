#파이썬 내부, 외부 패키지
import time
import keyboard_input as kb

# 자체 패키지
import grfx
import globals as g
from globals import cls

# 게임 run 함수
def run():
	box_coordinates = [
			[[50, 2, '|'], [50, 4]],

			[[0, 1, '╔'], [0,1]],
			[[99, 1, '╗'], [99, 1]],
			[[99, 5, '╝'], [99, 5]],
			[[0, 5, '╚'], [0, 5]],

			[[0, 1, '═'], [99, 1]],
			[[99, 1, '║'], [99, 5]],
			[[99, 5, '═'], [0, 5]],
			[[0, 5, '║'], [0, 1]],

			[[50, 2, '▓'], [50, 4]],
			[[51, 2, '▓'], [51, 4]],

			[[49, 2, '▒'], [49, 4]],
			[[52, 2, '▒'], [52, 4]],
			[[48, 2, '▒'], [48, 4]],
			[[53, 2, '▒'], [53, 4]],

			[[47, 2, '░'], [47, 4]],
			[[54, 2, '░'], [54, 4]],
			[[46, 2, '░'], [46, 4]],
			[[55, 2, '░'], [55, 4]],
			[[45, 2, '░'], [45, 4]],
			[[56, 2, '░'], [56, 4]],
			[[44, 2, '░'], [44, 4]],
			[[57, 2, '░'], [57, 4]],
	] # 3차원 리스트

	kb.listener.start()  # keyboard_input에서 import - 키보드 리스너

	''''
	# async 키보드 리스너
	async def kb_hit():
		while 1:
			if g.kbhit == "'q'" or g.kbhit == "Key.space":
				return False
			else:
				return True
	'''

	#메인 루프 함수사용 변수 정의, 초기화
	xpos = box_coordinates[0][0][0]
	right = True
	speed = 3

	# 첫 프레임 그리기
	grfx.draw(7, box_coordinates)

	# 메인 게임 루프
	while g.kbhit != "Key.space":

		if 0 < box_coordinates[0][0][0] and box_coordinates[0][0][0] < 99: pass
		else: right = not right

		if right:
			temp_xpos = xpos
			xpos += speed
		else:
			temp_xpos = xpos
			xpos -= speed

		cls()
		# 프레임의 위치가 다를때만 렌더링
		if round(xpos) != round(temp_xpos):
			box_coordinates[0][0][0], box_coordinates[0][1][0] = round(xpos), round(xpos)
			grfx.draw(7, box_coordinates)
		