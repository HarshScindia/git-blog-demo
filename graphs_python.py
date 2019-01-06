# graphs code from python-course.eu
graph = {"a": ["c"],
         "b": ["c", "e"],
         "c": ["a","b","d","e"],
         "d": ["c"],
         "e": ["c","b"],
         "f": []
         }
# Function to generate the list of all edges
def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))
    return edges

print(generate_edges(graph))

# function to find isolated nodes
def find_isolated_nodes(graph):
    """ returns a list of isolated nodes. """
    isolated = []
    for node in graph:
        if not graph[node]:
            isolated += node
    return isolated

# Graphs as a python class
""" A Python Class a simple python graph class, demonstrating the essential
facts and functionalities of graphs."""

class Graph(object):
    def __init__(self, graph_dict=None):
        """ Initializes a graph object if no dictionary or None is given, an
        empty dictionary will be used"""
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph.dict

