# 디버거
# globals.DEBUG 변수가 True일때 가동

from globals import DEBUG
import os

def init_debug():
  if DEBUG:
      print('== DEBUG MODE ==')
      print('PATH:', os.path)
      print('DIR:')
      for module in os.listdir(os.path.dirname('./')):
          print(module, end='')
          if module == 'Assets':
              print(' -', os.listdir('./Assets'))
          elif module == 'Games':
              print(' -', os.listdir('./Games'))
          else:
              print()
      print()