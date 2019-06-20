with open('input.txt') as file_object:
	pipes = file_object.readlines()

for i in range(0, len(pipes)):
	pipes[i] = pipes[i].rstrip()
	pipes[i] = pipes[i].split(' <-> ')
	pipes[i][1] = pipes[i][1].split(', ')

graph = {}
#graph is a dictionary
#the keys are nodes on the graph
#the values are lists of nodes adjacent to the key node
#e.g. since 0 is adjacent to 480 and 1750
#graphs['0'] = ['480', '1750']

for pipe in pipes:
	graph[pipe[0]] = pipe[1]

#starting at node, build the connected component node is in, starting with the component you're already aware of
#returns a list of nodes
def update_component(node, component):
	if len(component) == 0:
		component = [node]
	elif node not in component:
		component.append(node)

	for i in range(0, len(graph[node])):
		if graph[node][i] not in component:
			update_component(graph[node][i], component)

	return component

zero_component = ['0']
zero_component = update_component('0', zero_component)
print(sorted(zero_component))
print(len(zero_component))

components = [zero_component]
in_a_component = zero_component[:]

for node in graph.keys():
	if node not in in_a_component:
		new_component = [node]
		new_component = update_component(node, new_component)
		components.append(new_component)
		in_a_component.extend(new_component)

print(len(components))

compsizes = []
for comp in components:
	compsizes.append(len(comp))
print(sorted(compsizes, reverse=True))