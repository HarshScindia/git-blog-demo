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
    
    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in self.__graph_dict, a key  "vertex'
        with an empty list as a value is added to the dictionary. Otherwise nothing
        has to be done."""
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list; between two vertices 
        can be multiple edges! """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]


    def __generate_edges(self):
        """ A static method generating the edges of the graph "graph". 
        Edges are represented as sets with one (a loop back to the vertex) or two vertices"""
        edges = []
        for vertex in self.__graph_dict:
            for neigbour is self.__graph_dict[vertex]:
                if (neighbour, vertex)  not in edges:
                    edges.append({vertex, neighbour})
        return edges
