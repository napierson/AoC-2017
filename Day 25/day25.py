state = 'A'
pos = 0
tape = {0:0}
steps = 0
max_steps = 12656374

def step():
	global state
	global pos
	global tape
	global steps
	if state == 'A':
		if (pos not in tape.keys() or tape[pos] == 0):
			tape[pos] = 1
			pos += 1
			state = 'B'
		else:
			tape[pos] = 0
			pos -= 1
			state = 'C'
	elif state == 'B':
		if (pos not in tape.keys() or tape[pos] == 0):
			tape[pos] = 1
			pos -= 1
			state = 'A'
		else:
			tape[pos] = 1
			pos -= 1
			state = 'D'
	elif state == 'C':
		if (pos not in tape.keys() or tape[pos] == 0):
			tape[pos] = 1
			pos += 1
			state = 'D'
		else:
			tape[pos] = 0
			pos += 1
			state = 'C'
	elif state == 'D':
		if (pos not in tape.keys() or tape[pos] == 0):
			tape[pos] = 0
			pos -= 1
			state = 'B'
		else:
			tape[pos] = 0
			pos += 1
			state = 'E'
	elif state == 'E':
		if (pos not in tape.keys() or tape[pos] == 0):
			tape[pos] = 1
			pos += 1
			state = 'C'
		else:
			tape[pos] = 1
			pos -= 1
			state = 'F'
	elif state == 'F':
		if (pos not in tape.keys() or tape[pos] == 0):
			tape[pos] = 1
			pos -= 1
			state = 'E'
		else:
			tape[pos] = 1
			pos += 1
			state = 'A'
	steps += 1

def checksum():
	global tape
	total = 0
	for pos in tape.keys():
		total += tape[pos]
	return total

for i in range(0, max_steps):
	step()

print(checksum())