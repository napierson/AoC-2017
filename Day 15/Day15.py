akey = 591
bkey = 393

afactor = 16807
bfactor = 48271

avalue = akey
bvalue = bkey

def is_match(avalue, bvalue):
	abin = format(avalue, '032b')
	bbin = format(bvalue, '032b')
	return abin[16:] == bbin[16:]

#match_count = 0
#for i in range(0, 40000000):
#	avalue = (avalue * afactor) % 2147483647
#	bvalue = (bvalue * bfactor) % 2147483647
#	if is_match(avalue, bvalue):
#		match_count += 1

#print(match_count)

match_count = 0
to_compare = [[], []]

while(len(to_compare[0]) < 5000000):
	avalue = avalue * afactor % 2147483647
	if avalue % 4 == 0:
		to_compare[0].append(avalue)

while(len(to_compare[1]) < 5000000):
	bvalue = bvalue * bfactor % 2147483647
	if bvalue % 8 == 0:
		to_compare[1].append(bvalue)

pairs = len(to_compare[0])
if len(to_compare[1]) < pairs:
	pairs = len(to_compare[1])

for i in range(0, pairs):
	if is_match(to_compare[0][i], to_compare[1][i]):
		match_count += 1

print(match_count)