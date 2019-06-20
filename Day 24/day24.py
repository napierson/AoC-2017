with open('input.txt') as file_object:
	components = file_object.readlines()

for i in range(0, len(components)):
	components[i] = components[i].rstrip()
	components[i] = components[i].split('/')

graph = {comp[i]:[] for comp in components for i in range(0, 2)}
for comp in components:
	if comp[1] not in graph[comp[0]]:
		graph[comp[0]].append(comp[1])
	if comp[0] not in graph[comp[1]]:
		graph[comp[1]].append(comp[0])

def best_bridge(x, used_edges):
	global graph
	best_so_far = int(x)
	for y in graph[x]:
		if('[{}, {}]'.format(x, y) not in used_edges and 
			'[{}, {}]'.format(y, x) not in used_edges):
			yedges = used_edges[:]
			yedges.append('[{}, {}]'.format(x, y))
			ybridge = int(x) + int(x) +  best_bridge(y, yedges)
			if ybridge > best_so_far:
				best_so_far = ybridge
	return best_so_far

print(best_bridge('0', []))

def longest_bridge(x, used_edges, l):
	global graph
	best_so_far = int(x)
	longest_so_far = l
	for y in graph[x]:
		if('[{}, {}]'.format(x, y) not in used_edges and
			'[{}, {}]'.format(y, x) not in used_edges):
			yedges = used_edges[:]
			yedges.append('[{}, {}]'.format(x, y))
			yresult = longest_bridge(y, yedges, 0)
			ybridge = int(x) + int(x) + yresult[0]
			ylen = l + 1 + yresult[1]
			if (ylen > longest_so_far) or (ylen == longest_so_far and ybridge > best_so_far):
				best_so_far = ybridge
				longest_so_far = ylen
	return [best_so_far, longest_so_far]

print(longest_bridge('0', [], 0))