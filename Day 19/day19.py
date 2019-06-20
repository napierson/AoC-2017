with open('input.txt') as file_object:
	maze = file_object.readlines()

for i in range(0, len(maze)):
	maze[i] = list(maze[i])

pos = {'row':0, 'col':0}
facing = 'S'
abcs = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters = []
steps = 0

for i in range(0, len(maze[0])):
	if maze[0][i] == '|':
		pos['col'] = i
print(pos)

while 'T' not in letters:
	steps += 1
	row = pos['row']
	col = pos['col']
	cell = maze[row][col]
	if facing == 'S': #row -> row + 1
		if cell in abcs :
			letters.append(cell)
			pos['row'] = pos['row'] + 1
		elif cell == '+':
			if(col < len(maze[row]) - 1 and maze[row][col + 1] == '-'):
				facing = 'E'
				pos['col'] = pos['col'] + 1
			else:
				facing = 'W'
				pos['col'] = pos['col'] - 1
		else:
			pos['row'] = pos['row'] + 1
	elif facing == 'N': #row -> row - 1
		if cell in abcs:
			letters.append(cell)
			pos['row'] = pos['row'] - 1
		elif cell == '+':
			if(col < len(maze[row]) - 1 and maze[row][col + 1] == '-'):
				facing = 'E'
				pos['col'] = pos['col'] + 1
			else:
				facing = 'W'
				pos['col'] = pos['col'] - 1
		else:
			pos['row'] = pos['row'] - 1
	elif facing == 'E': #col -> col + 1
		if cell in abcs:
			letters.append(cell)
			pos['col'] = pos['col'] + 1
		elif cell == '+':
			if (row < len(maze) - 1 and maze[row + 1][col] == '|'):
				facing = 'S'
				pos['row'] = pos['row'] + 1
			else:
				facing = 'N'
				pos['row'] = pos['row'] - 1
		else:
			pos['col'] = pos['col'] + 1
	elif facing == 'W': #col -> col - 1
		if cell in abcs:
			letters.append(cell)
			pos['col'] = pos['col'] - 1
		elif cell == '+':
			if(row < len(maze) - 1 and maze[row + 1][col] == '|'):
				facing = 'S'
				pos['row'] = pos['row'] + 1
			else:
				facing = 'N'
				pos['row'] = pos['row'] - 1
		else:
			pos['col'] = pos['col'] - 1

print(''.join(letters))
print(steps)