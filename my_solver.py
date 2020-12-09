from ultils import *
import networkx as nx

def heuristic(G, s):
















def max_happiness_edge(G, students, threshold):
	"""
	Args:
		G:            original graph
		students:     list of avalable students to pair
		threshold:    threshold of stress
	Return the valid edge with highest happiness.
	"""
	sub_G = G.subgraph(students)
	valid_pair = dict(filter(lambda x: x[1]['stress'] < threshold, dict(sub_G.edges()).items()))
	return max(valid_pair.items(), key=lambda x: x[1]['happiness'])


def max_happiness_subgraph(G, rooms, vertex, threshold):
	"""
	Args:
		G:            original graph
		rooms:        list of list of vertices in the groups
		vertex:       vertex to add to any group
		threshold:    threshold of stress
	Return the valid group with highest happiness if added with vertex.
	"""
	max_happiness = 0
	max_group = []

	for room in rooms:
		sub_G = G.subgraph(group + [vertex])
		curr_happiness = sub_G.size("happiness")
		if curr_happiness > max_happiness and sub_G.size("stress") < threshold:
			max_happiness = curr_happiness
			max_group = room

	return max_group