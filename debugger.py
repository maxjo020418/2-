# 디버거
# globals.DEBUG 변수가 True일때 가동

from globals import DEBUG
from globals import COLOR_PALETTE
import os


def print_format_table():
    for style in range(8):
        for fg in range(30, 38):
            s1 = ''
            for bg in range(40, 48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')


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

        if COLOR_PALETTE: print_format_table()

        print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')
