import networkx as nx
import random
from utils import *
from parse import *

NUM_STUDENT = 20



def generate_input():
	"""
	Modified the graph such that it takes a desire output at a solution
	"""
	G = generate_random_input(NUM_STUDENT)
	
	# Modified graph with specific output in mind
	G[1][2]['stress'] = round(random.uniform(50, 100), 3)
	G[1][3]['stress'] = round(random.uniform(50, 100), 3)
	G[1][6]['stress'] = round(random.uniform(50, 100), 3)
	G[1][9]['stress'] = round(random.uniform(50, 100), 3)
	G[2][3]['stress'] = round(random.uniform(50, 100), 3)
	G[0][9]['stress'] = round(random.uniform(50, 100), 3)

	stress_budget = 50

	path = '/samples'#sys.argv[1]

	write_input_file(G, stress_budget, path)
	return None


def generate_random_input(n):
	"""
	Create a complete graph with n vertices and randomly generate the level of stress and happiness
	"""
	G = nx.complete_graph(n)

	for r in range(0, n - 1):
		for c in range(r + 1, n):
			G[r][c]['happiness'] = round(random.uniform(0, 100), 3)
			G[r][c]['stress'] = round(random.uniform(0, 50), 3)

	return G



