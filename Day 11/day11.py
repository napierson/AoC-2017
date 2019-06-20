with open('input.txt') as file_object:
	directions = file_object.read().rstrip()

directions = directions.split(',')
print(directions)

def distance_from_center(coords):
	return (abs(coords[0]) + abs(coords[1]) + abs(coords[2])) // 2

def least(a, b, c):
	least = a
	if b < a:
		least = b
	if c < least:
		least = c
	return least

def greatest(a, b, c):
	greatest = a
	if b > a:
		greatest = b
	if c > greatest:
		greatest = c
	return greatest

pos = [0, 0, 0]
#first coordinate is how many steps NE you are from the origin
#second coordinate is how many steps NW you are from the SW-NE axis
maxdistance = 0

for i in range(0, len(directions)):
	if(directions[i] == 'n'):
		pos[0] += 1
		pos[1] -= 1
	elif(directions[i] == 'ne'):
		pos[0] += 1
		pos[2] -= 1
	elif(directions[i] == 'se'):
		pos[1] += 1
		pos[2] -= 1
	elif(directions[i] == 's'):
		pos[0] -= 1
		pos[1] += 1
	elif(directions[i] == 'sw'):
		pos[0] -= 1
		pos[2] += 1
	elif(directions[i] == 'nw'):
		pos[1] -= 1
		pos[2] += 1
	if(distance_from_center(pos)) > maxdistance:
		maxdistance = distance_from_center(pos)

print(pos)
print(distance_from_center(pos))
print(maxdistance)

