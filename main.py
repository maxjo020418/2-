'''
슴우디(●'◡'●) 터미널 오징어겜

'오징어게임' 배너 잘 보일때까지 터미널 화면 끌어당기기

조영민 왔다감
'''
import Games
from debugger import init_debug

init_debug()

banner = open('./Assets/1.txt', 'r')
print(banner.read())
banner.close()

print('\n\n' + '=' * 100 + '\n' + ' ' * 20 +
      "'=' 모양이 끝까지 모이도록 터미널의 크기를 맞추세요/당기세요" + '\n' + '=' * 100)

print(' ' * 30 + '제작자: 지준원, 조영민, 조현준, 최이수')

Games.test()