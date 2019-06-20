with open('input.txt') as file_object:
	mem_banks = file_object.read()

mem_banks = mem_banks.split("\t")
mem_banks[-1].rstrip()
for i in range(0, len(mem_banks)):
	mem_banks[i] = int(mem_banks[i])

#input: a list of banks m
#output: an index pos identifying the bank with the greatest number of blocks in it
#ties broken by lowest index
def most_blocks(m):
	pos = 0
	for i in range(0, len(m)):
		if m[i] > m[pos]:
			pos = i
	return pos

#input: a list of banks m
#output: rebalances the blocks contained in the banks, doesn't return anything
def rebalance(m):
	pos = most_blocks(m)
	block_count = m[pos]
	m[pos] = 0

	for i in range(0, block_count):
		pos = (pos + 1) % len(m)
		m[pos] += 1

rebalance_count = 0
visited_states = []

while str(mem_banks) not in visited_states:
	visited_states.append(str(mem_banks))
	rebalance_count += 1
	rebalance(mem_banks)

print(rebalance_count)

visited_states = {}
#visited_states is a dictionary
#the key is a str copy of a memory bank configuration that has been reached
#the value is the first time that configuration was achieved
steps = 0
while str(mem_banks) not in visited_states.keys():
	visited_states[str(mem_banks)] = steps
	steps += 1
	rebalance(mem_banks)

print(steps - visited_states[str(mem_banks)])
print(mem_banks)