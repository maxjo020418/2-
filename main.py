'''
슴우디(●'◡'●) 터미널 오징어겜

'오징어게임' 배너 잘 보일때까지 터미널 화면 끌어당기기

조영민 왔다감
'''
import os
import Games
from globals import DEBUG
#from .Games import _1무궁화꽃, _2뽑기, _3줄다리기, _4구슬치기, _5징검다리, _6오징어, s노숙자, s딱지

if DEBUG:
    print('== DEBUG MODE ==')
    print(os.path)
    for module in os.listdir(os.path.dirname('./')):
        print(module, end='')
        if module == 'Assets':
            print(' -', os.listdir('./Assets'))
        elif module == 'Games':
            print(' -', os.listdir('./Games'))
        else:
            print()

banner = open('./Assets/1.txt', 'r')
print(banner.read())
banner.close()

print('\n\n' + '=' * 100 + '\n' + ' ' * 20 +
      "'=' 모양이 끝까지 모이도록 터미널의 크기를 맞추세요/당기세요" + '\n' + '=' * 100)

print(' ' * 30 + '제작자: 지준원, 조영민, 조현준, 최이수')

Games.test()