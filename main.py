####### DOCS #######
'''

'''


'''
슴우디(●'◡'●) 터미널 오징어겜

'오징어게임' 배너 잘 보일때까지 터미널 화면 끌어당기기

조영민 왔다감
지준원 왔구먼
'''
import Games
import grfx
from debugger import init_debug

import time

init_debug()

print('=' * 100 + '\n' + ' ' * 20 +
      "'=' 모양이 끝까지 보이도록 터미널의 크기를 맞추세요/당기세요" + '\n' + '=' * 100 + '\n')

print('\33[5m' + '완료되면 엔터를 누르세요...' + '\33[0m', end = '')
input()
print()

banner = open('./Assets/1.txt', 'r')
for line in banner:
  print(line, end = '')
  time.sleep(.05)
banner.close()

print('\n\n' + '=' * 100)
print(' ' * 40 + 'presented by: 슴우디❤️')
print(' ' * 30 + '제작자: 지준원, 조영민, 조현준, 최이수')
print('=' * 100)


coordinates = [
	[ [0, 0], [10, 10] ],
	[ [34, 5], [13, 66] ],
	[ [54, 2], [3, 56] ],
]
grfx.draw(100, )