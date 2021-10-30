import grfx

def run():
	box_coordinates = [

		[[0, 1, '╔'], [0,1]],
		[[99, 1, '╗'], [99, 1]],
		[[99, 5, '╝'], [99, 5]],
		[[0, 5, '╚'], [0, 5]],

	] # 3차원 리스트'

	grfx.draw(7, box_coordinates)

