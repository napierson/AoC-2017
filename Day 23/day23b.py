def is_prime(b):
	for i in range(2, int(b**0.5) + 1):
		if b % i == 0:
			return False
	return True

for i in range(0, 10, 2):
	print(i)

composite_count = 0
for b in range(107900, 124917, 17):
	if not is_prime(b):
		composite_count += 1

print(composite_count)