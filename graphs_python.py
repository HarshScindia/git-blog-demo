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
        self.__graph_dict = graph_dict
    
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
            for neighbour in self.__graph_dict[vertex]:
                if (neighbour, vertex)  not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

    def find_path(self, start_vertex, end_vertex, path=None):
        """ find a path from star_vertex to end_vertex in graph """
        if path == None:
            path = []
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in  graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex, end_vertex, path)
                if extended_path:
                    return extended_path
        return None

    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        """ find all paths from start vertex to end_vertex in graph """
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        path = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex, end_vertex, path)
                for p in extended_paths:
                    paths.append(p)
        return paths
    
    def vertex_degree(self, vertex):
        """ The degree of a vertex is the number of edges connecting it, i,e,
        the number of adjacent vertices. loops are counted double, i.e every occurence
        of vertex in the list"""
        adj_vertices = self.__graph_dict[vertex]
        degree = len(adj_vertices) + adj_vertices.count(vertex)
        return degree

    def find_isolated_vertices(self):
        """ return a list of isolated vertices. """
        graph = self.__graph_dict
        isolated = []
        for vertex in graph:
            print(isolated, vertex)
            if not graph[vertex]:
                isolated += [vertex]
        return isolated

if __name__ == "__main__":

    g = { "a" : ["d"],
          "b" : ["c"],
          "c" : ["b", "c", "d", "e"],
          "e" : ["c"],
          "f" : []
        }
    graph = Graph(g)

    print("Vertices of graph:")
    print(graph.vertices())
    
    print("Edges of graph:")
    print(graph.edges())

    print("Add vertex:")
    graph.add_vertex("z")

    print("Vertices of graph")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())

    print('Adding an edge {"x", "y"} with new vertices:')
    graph.add_edge({"x", "y"})
    print("Vertices of graph:")
    print(graph.vertices())
    print("Edges of graph:")
    print(graph.edges())
