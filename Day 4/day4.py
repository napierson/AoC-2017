with open('input.txt') as file_object:
	passphrases = file_object.readlines()

for i in range(0, len(passphrases)):
	passphrases[i] = passphrases[i].rstrip().split()

def is_valid(phrase):
	wordpile = []
	for word in phrase:
		if word in wordpile:
			return False
		else:
			wordpile.append(word)
	return True

valid_count = 0
for phrase in passphrases:
	if is_valid(phrase):
		valid_count += 1

print(valid_count)

test = 'ecdab'
print(list(test))
listtest = list(test)
listtest.sort()
print(''.join(listtest))

def is_extra_valid(phrase):
	wordpile = []
	for word in phrase:
		sortedword = list(word)
		sortedword.sort()
		sortedword = ''.join(sortedword)
		if sortedword in wordpile:
			return False
		else:
			wordpile.append(sortedword)
	return True

extra_valid_count = 0

for phrase in passphrases:
	if is_extra_valid(phrase):
		extra_valid_count += 1

print(extra_valid_count)