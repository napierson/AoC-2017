with open('input.txt') as file_object:
	steps = file_object.readlines()

for i in range(0, len(steps)):
	steps[i] = steps[i].rstrip()
	steps[i] = steps[i].split()

regs = {x:0 for x in 'abcdefgh'}
regs['a'] = 1
mul_count = 0
pos = 0

def set(x, y):
	global regs
	global pos
	if y in regs.keys():
		regs[x] = regs[y]
	else:
		regs[x] = int(y)
	pos += 1

def sub(x, y):
	global regs
	global pos
	if y in regs.keys():
		regs[x] = regs[x] - regs[y]
	else:
		regs[x] = regs[x] - int(y)
	pos += 1

def mul(x, y):
	global regs
	global mul_count
	global pos
	mul_count += 1
	if y in regs.keys():
		regs[x] = regs[x] * regs[y]
	else:
		regs[x] = regs[x] * int(y)
	pos += 1

def jnz(x, y):
	global regs
	global pos
	if((x in regs.keys() and regs[x] != 0) or
		(x not in regs.keys() and int(x) != 0)):
		pos += int(y)
	else:
		pos += 1

step_count = 0
hvals = []
pos = 0
while(0 <= pos and pos < len(steps)):
	todo = steps[pos][0]
	x = steps[pos][1]
	y = steps[pos][2]
	if todo == 'set':
		set(x, y)
	elif todo == 'sub':
		sub(x, y)
	elif todo == 'mul':
		mul(x, y)
	elif todo == 'jnz':
		jnz(x, y)

	step_count += 1
	if step_count % 100000 == 0:
		posstring = "pos: {}".format(pos)
		print(posstring + str(regs))