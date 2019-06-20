with open('input.txt') as file_object:
	instructions = file_object.readlines()

for i in range(0, len(instructions)):
	instructions[i] = instructions[i].split()
	instructions[i][2] = int(instructions[i][2])
	instructions[i][-1] = int(instructions[i][-1])

#an instruction is a list of 7 elements
#important indices:
#0 - name of the register that instruction modifies
#1 - whether to increment or decrement the register
#2 - how much to increment or decrement by
#3 - the string 'if'
#4 - the register referred to in the condition
#5 - the comparison operator used in the condition
#6 - the value used in the condition

print(instructions[:10])

registers = {}
#keys: the names of registers
#values: the value that register currently has

highest_value = 0

def parse_instruction(inst):
	if inst[0] not in registers.keys():
		registers[inst[0]] = 0
	if inst[4] not in registers.keys():
		registers[inst[4]] = 0

	if ((inst[5] == '==' and registers[inst[4]] == inst[6]) or
		(inst[5] == '>' and registers[inst[4]] > inst[6]) or
		(inst[5] == '<' and registers[inst[4]] < inst[6]) or
		(inst[5] == '>=' and registers[inst[4]] >= inst[6]) or
		(inst[5] == '<=' and registers[inst[4]] <= inst[6]) or
		(inst[5] == '!=' and registers[inst[4]] != inst[6])):
		if(inst[1] == 'inc'):
			registers[inst[0]] += inst[2]
		elif(inst[1] == 'dec'):
			registers[inst[0]] -= inst[2]


for inst in instructions:
	parse_instruction(inst)
	if registers[inst[0]] > highest_value:
		highest_value = registers[inst[0]]

print(highest_value)

largest_value = 0
for key in registers.keys():
	if registers[key] > largest_value:
		largest_value = registers[key]

print(largest_value)