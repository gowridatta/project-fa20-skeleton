from ultils import *
from my_utils import *
import networkx as nx
import copy
import random

dynamic_storage = {}

def greedy_solve(G, S_max):
	"""
	Solve the problem by using DP.

	Input:
		G:     original graph
		S_max: maximum total stress

	Output:
		D:     dictionary map student to appropriate room
	"""
	n = G.number_of_nodes()

	result = dynamic_traverse(n, 1, G, S_max)

	D = {i: result[i] for i in range(result)}

	return D


def graph_traverse(n, k, G, S_max):
	"""
	Calculate by recursively call from vertex n toward vertex 0.

	Function:
	f(n, k, G, S_max) = max { [n] + f(n - 1, k, G, S_max), 
					f(n - 1, k + 1, G, S_max)    }

	Base case:
	f(0, k, G, S_max) = [[0]]
	"""
	return None





















