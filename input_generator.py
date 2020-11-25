import networkx as nx
import random
import sys
from utils import *
from parse import *
from pathlib import Path

NUM_STUDENT = int(sys.argv[3])



def generate_input():
	"""
	Modified the graph such that it takes a desire output at a solution
	"""
	G = generate_random_input(NUM_STUDENT)
	
	# Modified graph with specific output in mind
	G[1][2]['stress'] = round(random.uniform(1500, 1600), 3)
	G[1][3]['stress'] = round(random.uniform(1500, 1600), 3)
	G[1][6]['stress'] = round(random.uniform(1500, 1600), 3)
	G[1][9]['stress'] = round(random.uniform(1500, 1600), 3)
	G[2][3]['stress'] = round(random.uniform(1500, 1600), 3)
	G[0][9]['stress'] = round(random.uniform(1500, 1600), 3)

	stress_budget = 1400

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
			G[r][c]['happiness'] = round(random.uniform(0, 100), 3)
			G[r][c]['stress'] = round(random.uniform(0, 50), 3)

	return G

def generate_input_from_output():
	n = NUM_STUDENT
	G = nx.complete_graph(NUM_STUDENT)
	for r in range(0, n - 1):
		for c in range(r + 1, n):
			G[r][c]['happiness'] = round(random.uniform(0, 5), 3)
			G[r][c]['stress'] = round(random.uniform(0, 0.5), 3)
	D = read_output_file(sys.argv[1], G, 60)

	stress_budget = 50

	for r in range(0, n - 1):
		for c in range(r + 1, n):
			if D[r] == D[c]:
				G[r][c]['happiness'] = round(random.uniform(70, 100), 3)
				G[r][c]['stress'] = round(random.uniform(0, 0.5), 3)
			else:
				if random.uniform(0, 10) > 5:
					G[r][c]['happiness'] = round(random.uniform(70, 100), 3)
					G[r][c]['stress'] = round(random.uniform(90, 99), 3)
				else:
					G[r][c]['happiness'] = round(random.uniform(0, 2), 3)
					G[r][c]['stress'] = round(random.uniform(27, 50), 3)

	write_input_file(G, stress_budget, sys.argv[2])

generate_input_from_output()