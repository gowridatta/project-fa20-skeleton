import networkx as nx
from parse import read_input_file, write_output_file, read_output_file
from utils import is_valid_solution, calculate_happiness, calculate_stress_for_room, calculate_happiness_for_room
import sys
from os.path import basename, normpath
import glob


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
    D = {}
    rooms = {}
    k = G.number_of_nodes()
    for i in range(G.number_of_nodes()):
        D[i] = i
        rooms[i] = [i]
    changed = []
    for i in range(G.number_of_nodes()-2):
        for j in range(G.number_of_nodes()):
            if j in list(rooms):
                max_happy = 0
                min_stress = s / (len(rooms) - 1)
                curr_min_stress = min_stress
                reee = 0
                for asdf in list(G[j]):
                    if calculate_stress_for_room(rooms[D[j]] + [asdf], G) < min_stress and (calculate_stress_for_room(rooms[D[j]] + [asdf], G) < curr_min_stress or calculate_happiness_for_room(rooms[D[j]] + [asdf], G) > max_happy):
                        max_happy = calculate_happiness_for_room(rooms[D[j]] + [asdf], G)
                        curr_min_stress = calculate_stress_for_room(rooms[D[j]] + [asdf], G)
                        reee = asdf
                if reee and reee not in changed:
                    changed.append(reee)
                    D[reee] = j
                    rooms[j].append(reee)
                    del rooms[reee]
    return D, len(rooms)







# Here's an example of how to run your solver.

# Usage: python3 solver.py test.in

# if __name__ == '__main__':
#     assert len(sys.argv) == 2
#     path = sys.argv[1]
#     G, s = read_input_file(path)
#     D, k = solve(G, s)
#     assert is_valid_solution(D, G, s, k)
#     print("Total Happiness: {}".format(calculate_happiness(D, G)))
#     # print("???: {}".format(calculate_happiness(read_output_file(sys.argv[2], G, s), G)))
#     # write_output_file(D, 'out/test.out')


# For testing a folder of inputs to create a folder of outputs, you can use glob (need to import it)
if __name__ == '__main__':
    inputs = glob.glob('inputs/*')
    for input_path in inputs:
        output_path = 'outputs/' + basename(normpath(input_path))[:-3] + '.out'
        G, s = read_input_file(input_path)
        D, k = solve(G, s)
        assert is_valid_solution(D, G, s, k)
        happiness = calculate_happiness(D, G)
        write_output_file(D, output_path)
        print("{} done".format(basename(normpath(input_path))[:-3]))
