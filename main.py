###################
'''
슴우디(●'◡'●) 터미널 오징어겜

'오징어게임' 배너 잘 보일때까지 터미널 화면 끌어당기기
'''
####### DOCS #######
'''
적을꺼임
'''

import curses
import os
import time

import Games
import grfx
from debugger import init_debug

init_debug()

print('=' * 100 + '\n' + ' ' * 20 +
      "'=' 모양이 끝까지 보이도록 터미널의 크기를 맞추세요/당기세요" + '\n' + '=' * 100 + '\n')

print('\33[5m' + '완료되면 엔터를 누르세요...' + '\33[0m', end = '')
input()
os.system('clear')

banner = open('./Assets/1.txt', 'r')
for line in banner:
  print(line, end = '')
  time.sleep(.05)
banner.close()

print('\n\n' + '=' * 100)
print(' ' * 40 + 'presented by: 슴우디❤️')
print(' ' * 30 + '제작자: 지준원, 조영민, 조현준, 최이수')
print('=' * 100)

# 임시기능 - 사용 예시
input('(테스트) 딱지치기 게임 - 계속하려면 엔터를 누르시오')
os.system('clear')

box_coordinates = [
	[ [0, 1], [99, 1] ],
	[ [99, 1], [99, 5] ],
	[ [99, 5], [0, 5] ],
	[ [0, 5], [0, 1] ],

	[ [49, 2, '|'], [49, 4] ],
]

grfx.draw(7, box_coordinates)
right = True
while 1:
	if 0 < box_coordinates[4][0][0] and box_coordinates[4][0][0] < 99: pass
	else: right = not right
	if right:
		os.system('clear')
		box_coordinates[4][0][0] += 1
		box_coordinates[4][1][0] += 1
		grfx.draw(7, box_coordinates)
		time.sleep(.1)
	else:
		os.system('clear')
		box_coordinates[4][0][0] -= 1
		box_coordinates[4][1][0] -= 1
		grfx.draw(7, box_coordinates)
		time.sleep(.1)

'''
is_escape = 0;
while is_escape:
	pass
'''