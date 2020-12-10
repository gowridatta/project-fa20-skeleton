import networkx as nx
from parse import read_input_file, write_output_file
from utils import is_valid_solution, calculate_happiness
from os.path import basename, normpath
import glob
import sys
from DP_solver import *
from greedy_solver import *
from collections import OrderedDict


def solve(G, s):
    """
    Args:
        G: networkx.Graph
        s: stress_budget
    Returns:
        D: Dictionary mapping for student to breakout room r e.g. {0:2, 1:0, 2:1, 3:2}
        k: Number of breakout rooms
    """

    # TODO: your code here!
    D_dp, k_dp = dp_solve(G, s)
    D_dp = dict(OrderedDict(sorted(D_dp.items())))
    print(D_dp)
    return D_dp, k_dp, True

    D_gr, k_gr = greedy_solve(G, s)
    D_gr = dict(OrderedDict(sorted(D_gr.items())))

    if not is_valid_solution(D_dp, G, s, k_dp):
        return D_gr, k_gr, False

    if calculate_happiness(D_dp, G) >= calculate_happiness(D_gr, G):
        return D_dp, k_dp, True
    else:
        return D_gr, k_gr, False


# Here's an example of how to run your solver.

# Usage: python3 solver.py test.in

if __name__ == '__main__':
    assert len(sys.argv) == 2
    path = sys.argv[1]
    G, s = read_input_file(path)
    D, k, dp = solve(G, s)
    assert is_valid_solution(D, G, s, k)
    print("Total Happiness: {}".format(calculate_happiness(D, G)))
    write_output_file(D, 'out/test.out')


# For testing a folder of inputs to create a folder of outputs, you can use glob (need to import it)
# if __name__ == '__main__':
#     inputs = glob.glob('inputs/*')
#     for input_path in inputs:
#         output_path = 'outputs/' + basename(normpath(input_path))[:-3] + '.out'
#         G, s = read_input_file(input_path)
#         D, k, dp = solve(G, s)
#         assert is_valid_solution(D, G, s, k)
#         happiness = calculate_happiness(D, G)
#         write_output_file(D, output_path)
#         print("{} done".format(basename(normpath(input_path))[:-3]), end="")
#         if not dp:
#             print("\t\t\t\tUse greedy")
#         else:
#             print("")
