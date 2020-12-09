from ultils import *
from my_utils import *
import networkx as nx
import copy
import random

dynamic_storage = {}

def dp_solve(G, S_max):
	"""
	Solve the problem by using DP.

	Input:
		G:     original graph
		S_max: maximum total stress

	Output:
		D:     dictionary map student to appropriate room
	"""
	n = G.number_of_nodes()

	result = dynamic_traverse(n, 0, G, S_max)

	D = {i: result[i] for i in range(result)}

	return D


def dynamic_traverse(n, k, G, S_max):
	"""
	Calculate by recursively call from vertex n toward vertex 0.

	Function:
	f(n, k, G, S_max) = max { [n] + f(n - 1, k, G, S_max), 
					f(n - 1, k + 1, G, S_max)    }

	Base case:
	f(0, k, G, S_max) = [[0]]
	"""

	if (n, k) in dynamic_storage.keys():
		value = copy.deepcopy(dynamic_storage[(n, k)])
		return value

	if n == 0:
		return [[n]]
	
	without_n = dynamic_traverse(n - 1, k + 1, G, S_max)
	without_n.append([n])
	
	with_n = dynamic_traverse(n - 1, k, G, S_max)
	max_group = max_happiness_subgraph(G, with_n, n, S_max / (k + len(with_n)))
	
	if not max_group:
		dynamic_storage[(n, k)] = without_n + [[n]]
		return dynamic_storage[(n, k)]

	max_group.append(n)

	dict_happiness_with_n = {i: with_n[i] for i in range(len(with_n))}
	dict_happiness_without_n = {i: without_n[i] for i in range(len(without_n))}

	happiness_with_n = calculate_happiness(dict_happiness_with_n, G)
	happiness_without_n = calculate_happiness(dict_happiness_without_n)

	if happiness_with_n > happiness_without_n:
		dynamic_storage[(n, k)] = with_n
	elif happiness_with_n < happiness_without_n:
		dynamic_storage[(n, k)] = without_n
	else:
		dynamic_storage[(n, k)] = random.choice([with_n, without_n])






















