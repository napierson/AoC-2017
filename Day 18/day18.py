with open('input.txt') as file_object:
	steps = file_object.readlines()

for i in range(0, len(steps)):
	steps[i] = steps[i].rstrip()
	steps[i] = steps[i].split()

regs = {'i':0, 'a':0, 'p':0, 'b':0, 'f':0, '1':1}

def set(r, x, y):
	if y in 'iapbf':
		r[x] = r[y]
	else:
		r[x] = int(y)

def add(r, x, y):
	if y in 'iabpf':
		r[x] = r[x] + r[y]
	else:
		r[x] = r[x] + int(y)

def mult(r, x, y):
	if y in 'iabpf':
		r[x] = r[x] * r[y]
	else:
		r[x] = r[x] * int(y)

def mod(r, x, y):
	if y in 'iabpf':
		r[x] = r[x] % r[y]
	else:
		r[x] = r[x] % int(y)

pos = 0
last_played = 0

for i in range(0, 100000):
	if steps[pos][0] == 'set':
		set(regs, steps[pos][1], steps[pos][2])
		pos += 1
	elif steps[pos][0] == 'add':
		add(regs, steps[pos][1], steps[pos][2])
		pos += 1
	elif steps[pos][0] == 'mul':
		mult(regs, steps[pos][1], steps[pos][2])
		pos += 1
	elif steps[pos][0] == 'mod':
		mod(regs, steps[pos][1], steps[pos][2])
		pos += 1
	elif steps[pos][0] == 'snd':
		last_played = regs[steps[pos][1]]
		pos += 1
	elif steps[pos][0] == 'rcv':
		if regs[steps[pos][1]] != 0:
			print(last_played)
		pos += 1
	elif steps[pos][0] == 'jgz':
		if regs[steps[pos][1]] > 0 and steps[pos][2] in 'iabpf':
			pos += regs[steps[pos][2]]
		elif regs[steps[pos][1]] > 0:
			pos += int(steps[pos][2])
		else:
			pos += 1
