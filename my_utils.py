from utils import *
import networkx as nx


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
    Return the valid group (pointer) with highest happiness if added with vertex.
    """
    max_group = []
    max_happiness = -1

    for room in rooms:
        sub_G = G.subgraph(room + [vertex])
        curr_happiness = max(sub_G.size("happiness"), 0)
        curr_stress = max(sub_G.size("stress"), 0)
        if curr_happiness > max_happiness and curr_stress < threshold:
            max_happiness = curr_happiness
            max_group = room

    return max_group

def room_to_student_to_student_to_room(S):
    """
    Args:
        S: map of room to students
    Return:
        D: map of student to room
    """
    D = {}

    for key in S.keys():
        for item in S[key]:
            D[item] = key

    return D