with open('input.txt') as file_object:
	stream = file_object.read()

in_garbage = False
depth = 1
score = 0

def stream_score(s):
	in_garbage = False
	depth = 1
	score = 0
	for i in range(0, len(s)):
		if not in_garbage:
			if s[i] == '{':
				score += depth
				depth += 1
			elif s[i] == '}':
				depth -= 1
			elif s[i] == '<':
				in_garbage = True
		else:
			if (s[i] == '>'):
				is_canceled = False
				j = i - 1
				while s[j] == '!':
					is_canceled = not is_canceled
					j -= 1
				if not is_canceled:
					in_garbage = False
	return score

test1 = '{}'
test2 = '{{{}}}'
test3 = '{{{},{},{{}}}}'
test4 = '{{<!!>},{<!!>},{<!!>},{<!!>}}'
test5 = '{{<a!>},{<a!>},{<a!>},{<ab>}}'

print(stream_score(test1))
print(stream_score(test2))
print(stream_score(test3))
print(stream_score(test4))
print(stream_score(test5))

print(stream_score(stream))

def garbage_count(s):
	in_garbage = False
	is_canceled = False
	garbage_letters = 0
	for i in range(0, len(s)):
		if (not in_garbage and s[i] == '<'):
			in_garbage = True
		else:
			if is_canceled:
				is_canceled = False
			elif s[i] == '!':
				is_canceled = True
			elif s[i] == '>':
				in_garbage = False
			elif in_garbage:
				garbage_letters += 1
	return garbage_letters

test1 = '<>'
test2 = '<random characters>'
test3 = '<<<<>'
test4 = '<!!!>>'
test5 = '{<{o"i!a,<{i<a>}'

print(garbage_count(test1))
print(garbage_count(test2))
print(garbage_count(test3))
print(garbage_count(test4))
print(garbage_count(test5))

print(garbage_count(stream))

