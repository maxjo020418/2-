import time
import os

import grfx
import keyboard_input as kb
import globals as g
from globals import cls

def run():
	box_coordinates = [
	[ [0, 1], [99, 1] ],
	[ [99, 1], [99, 5] ],
	[ [99, 5], [0, 5] ],
	[ [0, 5], [0, 1] ],

	[ [49, 2, '|'], [49, 4] ],
	]

	kb.listener.start() # keyboard_input에서 import

	'''
	while 1:
		print(g.kbhit)
		time.sleep(0.5)
	'''

	def loop():
		if g.kbhit != "'q'" and g.kbhit != 'Key.space':
			return True
		else:
			return False

	grfx.draw(7, box_coordinates)
	right = True
	while loop():
		if 0 < box_coordinates[4][0][0] and box_coordinates[4][0][0] < 99: pass
		else: right = not right
		if right:
			cls()
			box_coordinates[4][0][0] += 1
			box_coordinates[4][1][0] += 1
			grfx.draw(7, box_coordinates)
			print('스페이스 또는 q 눌러 정지')
			time.sleep(.1)
		else:
			cls()
			box_coordinates[4][0][0] -= 1
			box_coordinates[4][1][0] -= 1
			grfx.draw(7, box_coordinates)
			print('스페이스 또는 q 눌러 정지')
			time.sleep(.1)