from globals import DEBUG
from globals import DEBUG_COOR

def draw(height: int, coordinates, line: str = '.', border: bool = True, filler: str = ' '):

	# 입력좌표 1차 그래프 계산
	points = []
	line_type = []
	for s in coordinates:
		if (s[0][0] - s[1][0]):
			m = round(((s[0][1] - s[1][1]) / (s[0][0] - s[1][0])),2)
			c = round(s[0][1] - m * s[0][0])
			
			if (s[0][0] < s[1][0]):
				a = s[0][0]
				b = s[1][0]
			elif (s[0][0] > s[1][0]):
				a = s[1][0]
				b = s[0][0]

			if DEBUG_COOR: print(m, c)

			for i in range(a, b + 1):
				if DEBUG_COOR: print('x =', i, '\t', 'y =', round(m * i + c))
				points.append([i, round(m * i + c)])
				try:
					if s[0][2]:
						line_type.append(s[0][2])
				except:	
					line_type.append(line)

		else:
			if (s[0][1] < s[1][1]):
				a = s[0][1]
				b = s[1][1]
			elif (s[0][1] > s[1][1]):
				a = s[1][1]
				b = s[0][1]
			for i in range(a, b + 1):
				if DEBUG_COOR: print('x =', s[0][0], '\t', 'y =', i)
				points.append([s[0][0], i])
				try:
					if s[0][2]:
						line_type.append(s[0][2])
				except:	
					line_type.append(line)

	if DEBUG_COOR:
		print(points)
		print(line_type)

	# 프린팅
	print('=' * 100)
	for y in range(height):
		for x in range(100):
			if [x, y] in points:
				print(line_type[ points.index([x,y]) ], end = '')
			else:
				print(filler, end = '')
		print()
	print('=' * 100)