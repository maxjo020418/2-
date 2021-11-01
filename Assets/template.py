# Games 기본 템플릿 v1
# 11/1 제작

#파이썬 내부, 외부 패키지
import keyboard_input as kb

# 자체 패키지
import grfx
import globals as g
from globals import cls

# 게임 run 함수
def run():
	g.cls()
	# 3차원 리스트
	# 아래 링크에서 아스키코드 쓰는것을 추천 (이쁜 상자 같은거 만들고 싶으면)
	# https://www.meridianoutpost.com/resources/articles/ASCII-Extended-Code-reference-chart.php
	box_coordinates = [
		[[], []]
	]

	# 메인 루프 함수사용 변수 정의, 초기화 - 원하면 추가, 삭제 가능
	xpos_1 = 10 # 움직일 부분의 초기 x좌표점
	ypos_1 = 10 # 움직일 부분의 초기 y좌표점
	# xpos_2 = 10 # 원하면 추가 가능 _2, _3 이런 식으로
	# ypos_2 = 10 # 추가하려면 추가적인 절차 필요 - 이야기하소
	speed = 3 # 프레임 이동 속도 (선택사항)

	# 첫 프레임 그리기
	grfx.draw(7, box_coordinates)

	# 메인 게임 루프
	while g.kbhit != "Key.space": # "Key.space"를 다른 키로 변경 가능 - 바꾸고 싶으면 이야기하셈
		temp_xpos_1 = xpos_1
		temp_ypos_1 = ypos_1

		##### 여기 채워넣기 #####
		'''
		1. 게임 데이터 계산
		2. 게임 데이터 계산에 따른(xpos, ypos)) 화면의 도트 움직임 또는 speed 변수에 따른 움직임 (아래 예시 참고)
		3. grfx.draw 함수로 화면에 도트 그리기 - 이미 되어있으나 필요하면 고쳐야할수도 있으므로
		'''

		#########################

		'''
		box coordiante 변경하는 코드 (예시)
		box_coordinates[0][0][0] += speed (리스트상의 위치(인덱스)는 알아서 찾을 수 있지?)
		'''

		# 스크린 초기화
		cls()
		# 프레임의 위치가 다를때만 렌더링
		if round(xpos_1) != round(temp_xpos_1) or round(ypos_1) != round(temp_ypos_1):
			box_coordinates[0][0][0], box_coordinates[0][1][0] = round(xpos_1), round(xpos_1)
			grfx.draw(7, box_coordinates)