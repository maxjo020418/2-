###################
'''
슴우디(●'◡'●) 터미널 오징어겜

'오징어게임' 배너 잘 보일때까지 터미널 화면 끌어당기기

여기서 키보드 리스너 인풋은 위의 하얀 화면 클릭해서 포커스 맞추고 키보드 사용해야함!!!
'''
####### DOCS #######
'''
적을꺼임
'''
import Games
from debugger import init_debug
from globals import WIN, cls

if WIN:
	from msvcrt import getch
else:
	from easy_getch import getch
import os
import time

init_debug()

print('=' * 100 + '\n' + ' ' * 20 +
      "'=' 모양이 끝까지 보이도록 터미널의 크기를 맞추세요/당기세요" + '\n' + '=' * 100 + '\n')

print('\33[5m' + '완료되면 아무키나 누르세요...' + '\33[0m')
getch()
cls()

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
print('(테스트) 딱지치기 게임 - 계속하려면 아무키나 누르시오')
getch()
cls()

Games.s딱지.run()
