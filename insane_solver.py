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
    setting, k = brute_force(G, s)

    setting = dict(OrderedDict(sorted(setting.items())))

    D_dp, k_dp = dp_solve(G, s)
    D_dp = dict(OrderedDict(sorted(D_dp.items())))

    print(setting)

    return setting, k, D_dp, k_dp    


def brute_force(G, S_max):

    n = G.number_of_nodes()

    print(n)

    assert n == 10

    lst = set_partition(n)
    max_happiness = -1
    max_setting = {}
    max_room = -1
    
    for setting in lst:
        S = {i: setting[i] for i in range(len(setting))}
        D = room_to_student_to_student_to_room(S)
        room = len(S)

        curr_happiness = max(calculate_happiness(D, G), 0)

        if curr_happiness > max_happiness and is_valid_solution(D, G, S_max, room):
            max_happiness = curr_happiness
            max_setting = D
            max_room = room

    return max_setting, max_room


def partition(collection):
    if len(collection) == 1:
        yield [ collection ]
        return

    first = collection[0]
    for smaller in partition(collection[1:]):
        # insert `first` in each of the subpartition's subsets
        for n, subset in enumerate(smaller):
            yield smaller[:n] + [[ first ] + subset]  + smaller[n+1:]
        # put `first` in its own subset 
        yield [ [ first ] ] + smaller


def set_partition(n):
    lst = []
    something = list(range(n))

    for n, p in enumerate(partition(something), 1):
        #print(n, sorted(p))
        lst.append(sorted(p))
    
    return lst

# Here's an example of how to run your solver.

# Usage: python3 solver.py test.in

# if __name__ == '__main__':
#     assert len(sys.argv) == 2
#     path = sys.argv[1]
#     G, s = read_input_file(path)
#     D, k = solve(G, s)
#     assert is_valid_solution(D, G, s, k)
#     print(D)
#     print("Total Happiness: {}".format(calculate_happiness(D, G)))
#     write_output_file(D, 'out/test.out')


# For testing a folder of inputs to create a folder of outputs, you can use glob (need to import it)
if __name__ == '__main__':
    inputs = glob.glob('insane_inputs_nonlocal/*')
    for input_path in inputs:
        output_path = 'insane_outputs_nonlocal/' + basename(normpath(input_path))[:-3] + '.out'
        G, s = read_input_file(input_path)
        D, k, D_dp, k_dp = solve(G, s)
        assert is_valid_solution(D, G, s, k)
        happiness = calculate_happiness(D, G)
        happiness_dp = calculate_happiness(D_dp, G)
        print("Happiness: " + str(happiness) + "\t" + str(happiness_dp))
        write_output_file(D, output_path)
        print("{} done".format(basename(normpath(input_path))[:-3]), end="")

# if __name__ == '__main__':
#     assert len(sys.argv) == 2
#     n = sys.argv[1]
#     print("hi")
#     brute_force(int(n))
