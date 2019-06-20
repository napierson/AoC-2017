init = '.#./..#/###'

def line_from_square(s):
	line = []
	for i in range(0, len(s)):
		line.extend(s[i])
		line.extend('/')
	line = ''.join(line[:-1])
	return line

def square_from_line(l):
	square = l.split('/')
	return square

def rotate_cw(s):
	newsquare = []
	for i in range(0, len(s)):
		newrow = []
		for j in range(0, len(s)):
			newrow.append(s[len(s) - j - 1][i])
		newrow = ''.join(newrow)
		newsquare.append(newrow)
	return newsquare

def vert_flip(s):
	newsquare = []
	for i in range(0, len(s)):
		newrow = []
		for j in range(0, len(s)):
			newrow.append(s[i][len(s) - j - 1])
		newrow = ''.join(newrow)
		newsquare.append(newrow)
	return newsquare

with open('input.txt') as file_object:
	lrules = file_object.readlines()

rules = {}
for i in range(0, len(lrules)):
	lrules[i] = lrules[i].rstrip()
	lrules[i] = lrules[i].split(' => ')
	rules[lrules[i][0]] = lrules[i][1]

#print(rules)
#s must be 2x2 or 3x3
def apply_rule(s):
	for i in range(0, 4):
		l = line_from_square(s)
		if l in rules.keys():
			l = rules[l]
			return square_from_line(l)
		s = rotate_cw(s)

	s = vert_flip(s)
	for i in range(0, 4):
		l = line_from_square(s)
		if l in rules.keys():
			l = rules[l]
			return square_from_line(l)
		s = rotate_cw(s)
	return ['ERR']

def split_square(s):
	squares = []
	if len(s) % 2 == 0:
		#break s into 2x2 squares
		for i in range(0, len(s) // 2):
			squares.append([])
			for j in range(0, len(s) // 2):
				row1 = s[2 * i][2*j: 2*j + 2]
				row2 = s[2 * i + 1][2*j: 2*j + 2]
				squares[i].append([row1, row2])
	elif len(s) % 3 == 0:
		for i in range(0, len(s) // 3):
			squares.append([])
			for j in range(0, len(s) // 3):
				row1 = s[3 * i][3*j: 3*j + 3]
				row2 = s[3 * i + 1][3*j: 3*j + 3]
				row3 = s[3 * i + 2][3*j: 3*j + 3]
				squares[i].append([row1, row2, row3])
	return squares

#s is a list of lists of squares
def join_square(s):
	n = len(s) * len(s[0][0])
	rows = []
	for i in range(0, n):
		newrow = []
		for j in range(0, len(s)):
			newrow.append(s[i // len(s[0][0])][j][i % len(s[0][0])])
		newrow = ''.join(newrow)
		rows.append(newrow[:])
	return rows

def enhance(s):
	squares = split_square(s)
	for i in range(0, len(squares)):
		for j in range(0, len(squares[i])):
			squares[i][j] = apply_rule(squares[i][j])
	return join_square(squares)

s = square_from_line(init)
for i in range(0, 18):
	s = enhance(s)

pixels = 0
l = line_from_square(s)
for i in range(0, len(l)):
	if l[i] == '#':
		pixels += 1

print(pixels)