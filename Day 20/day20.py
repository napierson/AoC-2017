with open('input.txt') as file_object:
	particles = file_object.readlines()

for i in range(0, len(particles)):
	particles[i] = particles[i].split(', ')

	lpos = particles[i][0][3:-1].split(',')
	pos = {}
	pos['x'] = int(lpos[0])
	pos['y'] = int(lpos[1])
	pos['z'] = int(lpos[2])

	lvel = particles[i][1][3:-1].split(',')
	vel = {}
	vel['x'] = int(lvel[0])
	vel['y'] = int(lvel[1])
	vel['z'] = int(lvel[2])

	lacc = particles[i][2][3:-2].split(',')
	acc = {}
	acc['x'] = int(lacc[0])
	acc['y'] = int(lacc[1])
	acc['z'] = int(lacc[2])

	particles[i] = {'pos':pos, 'vel':vel, 'acc':acc, 'coll':False}

print(len(particles))

#particles is a whole *thing* it's a list of dictionaries of dictionaries
#particles[i]['pos'] is a position vector
#particles[i]['pos']['x'] is the x coordinate of the position
#particles[i]['vel'] is a velocity vector
#particles[i]['acc'] is an acceleration vector

def distance(i):
	return abs(particles[i]['pos']['x']) + abs(particles[i]['pos']['y']) + abs(particles[i]['pos']['z'])

def closest():
	closest = 0
	for i in range(1, len(particles)):
		if distance(i) < distance(closest):
			closest = i
	return closest

def advance():
	for i in range(0, len(particles)):
		if(not particles[i]['coll']):
			for k in 'xyz':
				particles[i]['vel'][k] += particles[i]['acc'][k]
				particles[i]['pos'][k] += particles[i]['vel'][k]

for i in range(0, 40):
	for j in range(0, len(particles)):
		to_remove = particles[j]['coll']
		for k in range(j + 1, len(particles)):
			if(not particles[j]['coll'] and 
				not particles[k]['coll'] and 
				particles[j]['pos'] == particles[k]['pos']):
				to_remove = True
				particles[k]['coll'] = True
		particles[j]['coll'] = to_remove
	advance()

count = 0
for i in range(0, len(particles)):
	if not particles[i]['coll']:
		count += 1

print(count)