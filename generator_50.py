import networkx as nx
import random
import sys
from utils import *
from parse import *

NUM_STUDENT = 50
same_room = [[0, 6, 12, 23, 26, 33], [1, 2, 27, 38, 39, 42, 46], [3, 8, 16, 21], [4, 7, 11, 37, 48], [5, 18, 31, 34, 47],
			 [9, 13, 22, 32, 43], [10, 19, 29, 41], [14, 15, 17, 44], [20, 24, 36, 49], [25, 28, 30], [35, 40, 45]]



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
		
		stress_lst.append(sum(stress) / len(stress))

	stress_budget = min(round(max(stress_lst), 0) + 5, 99)

	path = sys.argv[1]
	write_input_file(G, stress_budget, path)
	d = [[0, 6, 12, 23, 26, 33], [1, 2, 27, 38, 39, 42, 46], [3, 8, 16, 21], [4, 7, 11, 37, 48], [5, 18, 31, 34, 47],
			 [9, 13, 22, 32, 43], [10, 19, 29, 41], [14, 15, 17, 44], [20, 24, 36, 49], [25, 28, 30], [35, 40, 45]]
	D = {}
	for i in range(len(d)):
		for j in range(len(d[i])):
			D[d[i][j]] = i
	print(D)
	write_output_file(D, sys.argv[2])

	read_output_file(sys.argv[2], G, stress_budget)

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

generate_input()