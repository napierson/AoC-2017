with open('input.txt') as file_object:
	maze = file_object.readlines()

for i in range(0, len(maze)):
	maze[i] = int(maze[i].rstrip())

pos = 0
steps = 0

while (0 <= pos and
	pos < len(maze)):
	jumplength = maze[pos]
	if(jumplength >= 3):
		maze[pos] -= 1
	else:
		maze[pos] += 1
	pos += jumplength
	steps += 1

print(steps)