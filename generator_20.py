import networkx as nx
import random
import sys
import statistics
from utils import *
from parse import *

NUM_STUDENT = 20
same_room = [[0, 1, 9, 17], [2, 7, 10, 14, 18], [3, 4, 13, 15, 16, 19], [5, 6], [8, 11, 12], [15]]



def generate_input():
	"""
	Modified the graph such that it takes a desire output at a solution
	"""
	G = generate_random_input(NUM_STUDENT)
	
	# Modified graph with specific output in mind
	stress_lst = []
	for room in same_room:
		k = len(room)
		stress = []
		
		for i in range(k - 1):
			for j in range(i + 1, k):
				G[room[i]][room[j]]['happiness'] = round(random.uniform(50, 100), 3)
				G[room[i]][room[j]]['stress'] = round(random.uniform(10, 70), 3)
				stress.append(G[room[i]][room[j]]['stress'])
		
		stress_lst.append(mean(stress))

	stress_budget = min(round(max(stress_lst), 0) + 5, 99)

	# Force 15 into a one-person room
	for i in range(15):
		G[room[i]][room[15]]['stress'] = stress_budget + 1

	for i in range(16, NUM_STUDENT):
		G[room[15]][room[i]]['stress'] = stress_budget + 1

	path = sys.argv[1]
	write_input_file(G, stress_budget, path)
	return None


def generate_random_input(n):
	"""
	Create a complete graph with n vertices and randomly generate the level of stress and happiness
	"""
	G = nx.complete_graph(n)

	for r in range(0, n - 1):
		for c in range(r + 1, n):
			G[r][c]['happiness'] = round(random.uniform(0, 90), 3)
			G[r][c]['stress'] = round(random.uniform(0, 100), 3)

	return G