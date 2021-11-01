###################
'''
슴우디(●'◡'●) 터미널 오징어겜

'오징어게임' 배너 잘 보일때까지 터미널 화면 끌어당기기

여기서 키보드 리스너 인풋은 위의 하얀 화면 클릭해서 포커스 맞추고 키보드 사용해야함!!!
'''
####### DOCS #######
'''
적을꺼임 (안함)
'''
import Games
import keyboard_input
from debugger import init_debug
#from globals import WIN, cls, kbhit
import globals as g

if g.WIN:
	from msvcrt import getch
else:
	from easy_getch import getch
import time

init_debug()

print('═' * 100 + '\n' + ' ' * 20 +
      "'═' 모양이 끝까지 보이도록 터미널의 크기를 맞추세요/당기세요" + '\n' + '═' * 100 + '\n')

print('\33[5m' + '완료되면 아무키나 누르세요...' + '\33[0m')
getch()
g.cls()

keyboard_input.listener.start() # keyboard_input에서 import - 키보드 리스너
while 1:
	g.cls()
	# 메뉴화면
	menu_list = [
		'1. 무궁화꽃이 피었습니다',
		'2. 뽑기',
		'3. 줄다리기',
		'4. 구슬치기',
		'5. 징검다리',
		'6. 오징어게임',
		'스페셜: 딱지치기',
		'종료'
	]
		# 첫 프레임
	banner = open('./Assets/1.txt', 'r')
	for line in banner:
		print(line, end = '')
	print('\n\n' + '═' * 100)
	print(' ' * 40 + 'presented by: 슴우디❤️')
	print(' ' * 30 + '제작자: 조영민, 지준원, 조현준, 최이수')
	print('═' * 100)
	print('\x1b[6;30;42m'+'위, 아래 방향키를 눌러 이동 | 엔터를 눌러 선택'+'\x1b[0m\n')
	for game in range(len(menu_list)):
		if game == 0:
			print('\x1b[1;30;47m' + menu_list[game] + '\x1b[0m')
		else:
			print(menu_list[game])

		# 이후 프레임
	def update(selection):
		g.cls()
		for line in banner:
			print(line, end = '')
		print('\n\n' + '═' * 100)
		print(' ' * 40 + 'presented by: 슴우디❤️')
		print(' ' * 30 + '제작자: 조영민, 지준원, 조현준, 최이수')
		print('═' * 100)

		print('\x1b[6;30;42m'+'위, 아래 방향키를 눌러 이동 | 엔터를 눌러 선택'+'\x1b[0m\n')

		for game in range(len(menu_list)):
			if game == selection:
				print('\x1b[1;30;47m' + menu_list[game] + '\x1b[0m')
			else:
				print(menu_list[game])

	selection = 0
	while g.kbhit != 'Key.enter':
		if g.kbhit == 'Key.up' and selection != 0:
			selection -= 1
			update(selection)
			time.sleep(.25)
		elif g.kbhit == 'Key.down' and selection != 7:
			selection += 1
			update(selection)
			time.sleep(.25)

	banner.close()

# 선택 게임 실행

	if selection == 0:
		Games._1무궁화꽃.run()
	elif selection == 1:
		Games._2뽑기.run()
	elif selection == 2:
		Games._3줄다리기.run()
	elif selection == 3:
		Games._4구슬치기.run()
	elif selection == 4:
		Games._5징검다리.run()
	elif selection == 5:
		Games._6오징어.run()
	elif selection == 6:
		Games.s딱지.run()
	elif selection == 7:
		break

# 임시기능
'''
print('(그림 테스트) 노숙자 게임 - 계속하려면 아무키나 누르시오')
getch()
cls()
Games.s노숙자.run()

print('(테스트) 딱지치기 게임 - 계속하려면 아무키나 누르시오')
getch()
cls()
Games.s딱지.run()
'''
