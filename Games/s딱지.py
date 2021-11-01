#파이썬 내부, 외부 패키지
import keyboard_input

# 자체 패키지
import grfx
import globals as g
from globals import cls

# 게임 run 함수
def run():
	g.cls()

	# 설명 화면
	banner = open('./Assets/_딱지.txt', 'r')
	for line in banner:
		print(line, end = '')
	banner.close()

	input('딱지치기 게임\n뭐시기 뭐시기 이야기\n규칙\n엔터를 눌러 계속')

	# 3차원 리스트
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
	]

	# 메인 루프 함수사용 변수 정의, 초기화
	xpos = box_coordinates[0][0][0]
	right = True
	speed = 3
	
	# 첫 프레임 그리기
	grfx.draw(7, box_coordinates)

	# 메인 게임 루프
	while g.kbhit != "Key.space":
	
		if 0 < box_coordinates[0][0][0] and box_coordinates[0][0][0] < 99: 
			pass
		else: 
			right = not right

		temp_xpos = xpos
		if right:
			xpos += speed
		else:
			xpos -= speed

		cls()
		# 프레임의 위치가 다를때만 렌더링
		if round(xpos) != round(temp_xpos):
			print('스페이스를 눌러 박스안에 맞추기!!')
			box_coordinates[0][0][0], box_coordinates[0][1][0] = round(xpos), round(xpos)
			grfx.draw(7, box_coordinates)

	print(f'오차: {abs(50.5 - xpos)}')
	input('엔터를 눌러 계속...')
		