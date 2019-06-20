key = 'hfdlxzhv'

#reverse takes as input a list k, a position pos, and a length
#it takes the substring starting at position pos of length length (wrapping around to the beginning of k)
#and reverses it in place
def reverse(k, pos, length):
	to_reverse = k[:]
	for i in range(0, length):
		k[(pos + i) % len(k)] = to_reverse[(pos + length - i - 1) % len(k)]

def format_input(s):
	len_tail = [17, 31, 73, 47, 23]
	lengths = []
	for i in range(0, len(s)):
		lengths.append(ord(s[i]))
	lengths.extend(len_tail)
	return lengths

def knot_hash(s):
	knot = [i for i in range(0, 256)]
	pos = 0
	skipcount = 0
	lengths = format_input(s)
	for i in range(0, 64):
		for j in range(0, len(lengths)):
			reverse(knot, pos, lengths[j])
			pos = (pos + lengths[j] + skipcount) % len(knot)
			skipcount += 1

	densehash = []
	for i in range(0, 16):
		xorpile = 0
		for j in range(0, 16):
			xorpile = xorpile ^ knot[16 * i + j]
		densehash.append(xorpile)

	knothash = []
	for i in range(0, len(densehash)):
		knothash.append(format(densehash[i], '02x'))
	knothash = ''.join(knothash)
	return knothash

defrag_grid = [[0 for i in range(0, 128)] for j in range(0, 128)]

def binary_from_hex(h):
	b = []
	ival = 0
	for i in range(0, len(h)):
		ival = int(h[i], 16)
		b.append(format(ival, '04b'))
	b = ''.join(b)
	return b

for row in range(0, 128):
	rowkey = key + '-{}'.format(row)
	hash_rowkey = binary_from_hex(knot_hash(rowkey))
	for col in range(0, 128):
		defrag_grid[row][col] = int(hash_rowkey[col])

used = 0
for row in range(0, 128):
	for col in range(0, 128):
		used += defrag_grid[row][col]

print(used)

regions = {}

def adjacent_points(point):
	adj = []
	x = point[0]
	y = point[1]
	if(x > 0):
		adj.append([x - 1, y])
	if(x < 127):
		adj.append([x + 1, y])
	if(y > 0):
		adj.append([x, y - 1])
	if(y < 127):
		adj.append([x, y + 1])
	return adj

def add_to_region(r, point):
	defrag_grid[point[0]][point[1]] = r
	for p in adjacent_points(point):
		if defrag_grid[p[0]][p[1]] == 1:
			add_to_region(r, p)

least_unused_region = 2
for row in range(0, 128):
	for col in range(0, 128):
		if defrag_grid[row][col] == 1:
			add_to_region(least_unused_region, [row, col])
			least_unused_region += 1

print(least_unused_region)
