spinbuffer = [0]
pos = 0
stepsize = 344

justadded = 0
pos = 0
for i in range(1, 50000001):
	pos = (pos + stepsize) % i
	if pos == 0:
		justadded = i
	pos = (pos + 1) % (i + 1)

print(justadded)