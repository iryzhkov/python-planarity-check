import linked_list

Node = linked_list.Node
LinkedList = linked_list.LinkedList

class Edge():
    # Create a new edge from start_vertex to end_vertex
    def __init__(self, start_vertex, end_vertex):
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex

        self.is_black = False

        self.linked_list_node = None

    # Is the edge blacken?
    def isBlack(self):
        return self.is_black

    # blacken the edge
    def blacken(self):
        self.is_black = True

    # whiten the edge
    def whiten(self):
        self.is_black = False 

class Vertex():
    def __init__(self):
        pass

    def addEdge(self):
        pass

class Graph():
    def __init__(self):
        pass

    def addVertex(self):
        pass

    def addEdge(self):
        pass
