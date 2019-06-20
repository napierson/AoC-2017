with open('input.txt') as file_object:
	steps = file_object.readlines()

for i in range(0, len(steps)):
	steps[i] = steps[i].rstrip()
	steps[i] = steps[i].split()

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

regs0 = {'i':0, 'a':0, 'p':0, 'b':0, 'f':0, '1':1}
regs1 = {'i':0, 'a':0, 'p':1, 'b':0, 'f':0, '1':1}

queue0 = []
queue1 = []

sendcount = 0
pos0 = 0
pos1 = 0

locked0 = False
locked1 = False
to_continue = True

while (not locked0 or not locked1):
	#act on 0:
	step0 = steps[pos0]
	inst0 = step0[0]
	x0 = step0[1]
	if(len(step0) > 2):
		y0 = step0[2]
	if inst0 == 'set':
		set(regs0, x0, y0)
		pos0 += 1
	elif inst0 == 'add':
		add(regs0, x0, y0)
		pos0 += 1
	elif inst0 == 'mul':
		mult(regs0, x0, y0)
		pos0 += 1
	elif inst0 == 'mod':
		mod(regs0, x0, y0)
		pos0 += 1
	elif inst0 == 'snd':
		queue1.append(regs0[x0])
		locked1 = False
		pos0 += 1
	elif inst0 == 'rcv':
		if len(queue0) == 0:
			locked0 = True
		else:
			regs0[x0] = queue0.pop(0)
			pos0 += 1
	elif inst0 == 'jgz':
		if (regs0[x0] > 0 and y0 in 'iapbf'):
			pos0 += regs0[y0]
		elif regs0[x0] > 0:
			pos0 += int(y0)
		else:
			pos0 += 1

	#act on 1:
	step1 = steps[pos1]
	inst1 = step1[0]
	x1 = step1[1]
	if(len(step1) > 2):
		y1 = step1[2]
	if inst1 == 'set':
		set(regs1, x1, y1)
		pos1 += 1
	elif inst1 == 'add':
		add(regs1, x1, y1)
		pos1 += 1
	elif inst1 == 'mul':
		mult(regs1, x1, y1)
		pos1 += 1
	elif inst1 == 'mod':
		mod(regs1, x1, y1)
		pos1 += 1
	elif inst1 == 'snd':
		queue0.append(regs1[x1])
		locked0 = False
		sendcount += 1
		pos1 += 1
	elif inst1 == 'rcv':
		if len(queue1) == 0:
			locked1 = True
		else:
			regs1[x1] = queue1.pop(0)
			pos1 += 1
	elif inst1 == 'jgz':
		if (regs1[x1] > 0 and y1 in 'iapbf'):
			pos1 += regs1[y1]
		elif regs1[x1] > 0:
			pos1 += int(y1)
		else:
			pos1 += 1

print(sendcount)