with open('input.txt') as file_object:
	grid = file_object.readlines()

for i in range(0, len(grid)):
	grid[i] = grid[i].rstrip()

dgrid = {}
for i in range(0, len(grid)):
	for j in range(0, len(grid[i])):
		dgrid['[{}, {}]'.format(i, j)] = grid[i][j]

pos = [12, 12]
facing = 'N'
infect_count = 0

def burst():
	global pos
	global infect_count
	global dgrid
	global facing
	if(str(pos) in dgrid.keys() and 
		dgrid[str(pos)] == '#'): #node is infected. clean it, turn right, move forward
		dgrid[str(pos)] = '.'
		if facing == 'N':
			facing = 'E'
			pos[1] = pos[1] + 1
		elif facing == 'E':
			facing = 'S'
			pos[0] = pos[0] + 1
		elif facing == 'S':
			facing = 'W'
			pos[1] = pos[1] - 1
		elif facing == 'W':
			facing = 'N'
			pos[0] = pos[0] - 1
	else: #node is either clean or undiscovered (hence clean). infect it, turn left, move forward
		dgrid[str(pos)] = '#'
		infect_count += 1 #this burst caused a clean node to become infected
		if facing == 'N':
			facing = 'W'
			pos[1] = pos[1] - 1
		elif facing == 'W':
			facing = 'S'
			pos[0] = pos[0] + 1
		elif facing == 'S':
			facing = 'E'
			pos[1] = pos[1] + 1
		elif facing == 'E':
			facing = 'N'
			pos[0] = pos[0] - 1

#for i in range(0, 10000):
#	burst()

def evo_burst():
	global pos
	global infect_count
	global dgrid
	global facing

	if(str(pos) in dgrid.keys() and 
		dgrid[str(pos)] == '#'): #flag the node, turn right
		dgrid[str(pos)] = 'F'
		if facing == 'N':
			facing = 'E'
		elif facing == 'E':
			facing = 'S'
		elif facing == 'S':
			facing = 'W'
		elif facing == 'W':
			facing = 'N'
	elif(str(pos) in dgrid.keys() and
		dgrid[str(pos)] == 'F'): #clean the node, reverse course
		dgrid[str(pos)] = '.'
		if facing == 'N':
			facing = 'S'
		elif facing == 'E':
			facing = 'W'
		elif facing == 'S':
			facing = 'N'
		elif facing == 'W':
			facing = 'E'
	elif(str(pos) in dgrid.keys() and
		dgrid[str(pos)] == 'W'): #infect the node, don't turn
		dgrid[str(pos)] = '#'
		infect_count += 1
	else: #weaken the node, turn left
		dgrid[str(pos)] = 'W'
		if facing == 'N':
			facing = 'W'
		elif facing == 'W':
			facing = 'S'
		elif facing == 'S':
			facing = 'E'
		elif facing == 'E':
			facing = 'N'

	if facing == 'N':
		pos[0] = pos[0] - 1
	elif facing == 'E':
		pos[1] = pos[1] + 1
	elif facing == 'S':
		pos[0] = pos[0] + 1
	elif facing == 'W':
		pos[1] = pos[1] - 1

for i in range(0, 10000000):
	evo_burst()

print(infect_count)