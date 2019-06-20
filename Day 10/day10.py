with open('input.txt') as file_object:
	lengths = file_object.read().rstrip()
	lengths2 = str(lengths)


lengths = lengths.split(',')
for i in range(0, len(lengths)):
	lengths[i] = int(lengths[i])

knot = [i for i in range(0, 256)]
skipcount = 0
pos = 0

#reverse takes as input a list k, a position pos, and a length
#it takes the substring starting at position pos of length length (wrapping around to the beginning of k)
#and reverses it in place
def reverse(k, pos, length):
	to_reverse = k[:]
	for i in range(0, length):
		k[(pos + i) % len(k)] = to_reverse[(pos + length - i - 1) % len(k)]


for i in range(0, len(lengths)):
	reverse(knot, pos, lengths[i])
	pos = (pos + lengths[i] + skipcount) % len(knot)
	skipcount += 1

#print(knot)
#print(knot[0] * knot[1])

len_tail = [17, 31, 73, 47, 23]

lengths3 = []

for i in range(0, len(lengths2)):
	lengths3.append(ord(lengths2[i]))

lengths3.extend(len_tail)

#print(lengths3)

pos = 0
skipcount = 0
knot = [i for i in range(0, 256)]

for i in range(0, 64):
	for j in range(0, len(lengths3)):
		reverse(knot, pos, lengths3[j])
		pos = (pos + lengths3[j] + skipcount) % len(knot)
		skipcount += 1

#print(knot)

densehash = []
for i in range(0, 16):
	xorpile = 0
	for j in range(0, 16):
		xorpile = xorpile ^ knot[16 * i + j]
	densehash.append(xorpile)
print(densehash)

a = 15
#print(format(a, '02x'))

knothash = []
for i in range(0, len(densehash)):
	knothash.append(format(densehash[i], '02x'))
knothash = ''.join(knothash)
print(knothash)