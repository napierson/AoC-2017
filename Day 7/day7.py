with open('input.txt') as file_object:
	programs_tower = file_object.readlines()

for i in range(0, len(programs_tower)):
	programs_tower[i] = programs_tower[i].rstrip().split(' -> ')
	program_id = programs_tower[i][0].split()
	program_id[1] = int(program_id[1][1:len(program_id[1]) - 1])
	if len(programs_tower[i]) > 1:
		successors = programs_tower[i][1].split(", ")
		program_id.extend(successors)
	programs_tower[i] = program_id

not_base = []
for program in programs_tower:
	if len(program) > 2:
		for i in range(2, len(program)):
			not_base.append(program[i])

for program in programs_tower:
	if program[0] not in not_base:
		print(program[0])

successors = {}
#keys: program names
#values: a list of successors

for program in programs_tower:
	if len(program) > 2:
		successors[program[0]] = program[2:]

weights = {}
#keys: program names
#values: the weight of the program. NOT including the disc the program is carrying above it

for program in programs_tower:
	weights[program[0]] = program[1]

#input: the name of a program
#output: the weight of the disc the program is carrying above it, including the weight of the program itself
def disc_weight(s):
	total_weight = weights[s]
	if(s in successors.keys()):
		for p in successors[s]:
			total_weight += disc_weight(p)
	return total_weight

total_weights = {}
for program in programs_tower:
	total_weights[program[0]] = disc_weight(program[0])

def is_balanced(s):
	if(s not in successors.keys()):
		return True
	else:
		balanced = True
		weight = total_weights[successors[s][0]]
		for i in range(1, len(successors[s])):
			balanced = (balanced and weight == total_weights[successors[s][i]])
		return balanced

for program in programs_tower:
	if not is_balanced(program[0]):
		print(program)
		for s in successors[program[0]]:
			print(total_weights[s])

print(total_weights['nzkxl'])
print(total_weights['mdbtyw'])
print(total_weights['dqwfuzn'])

print(total_weights['zqcrxm'])
print(total_weights['lfbocy'])
print(total_weights['uqrmg'])