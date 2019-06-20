with open('input.txt') as file_object:
	spreadsheet = file_object.readlines()

checksum = 0
for row in spreadsheet:
	splitrow = row.split("\t")
	for i in range(0, len(splitrow)):
		m = int(splitrow[i])
		for j in range(i + 1, len(splitrow)):
			n = int(splitrow[j])
			if(m % n == 0):
				checksum += m // n
			if(n % m == 0):
				checksum += n // m

print(checksum)
