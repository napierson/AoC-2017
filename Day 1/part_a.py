with open('input.txt') as file_object:
	captcha_code = file_object.read().rstrip()
sum = 0
captcha_length = len(captcha_code)

for i in range(len(captcha_code)):
	if captcha_code[i] == captcha_code[(i + 1) % len(captcha_code)]:
		sum += int(captcha_code[i])

print(sum)

test_code = '334566783'
test_sum = 0

for i in range(len(test_code)):
	if test_code[i] == test_code [(i + 1) % len(test_code)]:
		test_sum += int(test_code[i])

print(test_sum)

sum = 0

for i in range(captcha_length):
	sum += int(captcha_code[i]) * int(captcha_code[i] == captcha_code[(i + captcha_length // 2) % captcha_length])
	# if(captcha_code[i] == captcha_code[(i + captcha_length // 2) % captcha_length]):
	#	sum += int(captcha_code[i])

print(sum)
