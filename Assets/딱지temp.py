#파이썬 내부, 외부 패키지
import time
import keyboard_input as kb

# 자체 패키지
import grfx
import globals as g
from globals import cls

# 메인 게임 함수
def run():
	box_coordinates = [
			[[0, 1], [99, 1]],
			[[99, 1], [99, 5]],
			[[99, 5], [0, 5]],
			[[0, 5], [0, 1]],
			[[49, 2, '|'], [49, 4]],
	] # 3차원 리스트

	kb.listener.start()  # keyboard_input에서 import - 키보드 리스너

	# 키보드상태 회수 루프
	def loop():
			if g.kbhit != "'q'" and g.kbhit != 'Key.space':
					return True
			else:
					return False

	#메인 루프 함수사용 변수 정의, 초기화
	xpos = box_coordinates[4][0][0]
	grfx.draw(7, box_coordinates)
	right = True

	# 메인 게임 루프
	while loop():

		if 0 < box_coordinates[4][0][0] and box_coordinates[4][0][0] < 99: pass
		else: right = not right

		if right:
			xpos += 1
			cls()
			box_coordinates[4][0][0], box_coordinates[4][1][0] = round(xpos), round(xpos)
			grfx.draw(7, box_coordinates)
			print('스페이스 또는 q 눌러 정지')
			time.sleep(.1)
		else:
			cls()
			box_coordinates[4][0][0] -= 1
			box_coordinates[4][1][0] -= 1
			grfx.draw(7, box_coordinates)
			print('스페이스 또는 q 눌러 정지')
			time.sleep(.1)

	accuracy = 10
	print(f'정확도: {accuracy} ()')
