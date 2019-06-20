with open('input.txt') as file_object:
	dance_steps = file_object.read().rstrip()

dance_steps = dance_steps.split(',')
print(len(dance_steps))

programs = list('abcdefghijklmnop')

def spin(p, x):
	dist = len(p) - x
	return p[dist:] + p[:dist]

def exchange(p, a, b):
	temp = p[a]
	p[a] = p[b]
	p[b] = temp
	return p

def partner(p, a, b):
	a_ind = -1
	b_ind = -1
	for i in range(0, len(p)):
		if p[i] == a:
			a_ind = i
		if p[i] == b:
			b_ind = i

	p[a_ind] = b
	p[b_ind] = a

	return p
configs = [programs[:]]
for j in range(0, 1):
	for i in range(0, len(dance_steps)):
		if dance_steps[i][0] == 's':
			x = int(dance_steps[i][1:])
			programs = spin(programs, x)
		elif dance_steps[i][0] == 'x':
			params = dance_steps[i][1:].split('/')
			a = int(params[0])
			b = int(params[1])
			programs = exchange(programs, a, b)
		elif dance_steps[i][0] == 'p':
			params = dance_steps[i][1:].split('/')
			programs = partner(programs, params[0], params[1])
	
print(''.join(programs))