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

        self.inverse_edge = None

    # The string of the edge is (A -> B)
    def __str__(self):
        return str(self.start_vertex) + " -> " + str(self.end_vertex)

    # couple two inverse edges (e.g. a -> b and b -> a)
    def couple(self, other_edge):
        self.inverse_edge = other_edge
        other_edge.inverse_edge = self

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
    # Initialization of the vertex
    def __init__(self, identification):
        self.identification = identification

        self.edges = LinkedList()
        self.dirty_edges = LinkedList()

        self.dfs_discovery_time = -1
        self.dfs_finishing_time = -1

    # Compare to the other vertex
    def __eq__(self, other_vertex):
        return other_vertex.identificaiton == self.identification

    # Make a string out of vertex
    def __str__(self):
        return "V[" + str(self.identification) + "] edges: " + \
               str(self.edges) + ", dirty edges: " + str(self.dirtyEdges)   

    # The size of the vertex is the number of edges
    def __len__(self):
        return len(self.edges) + len(self.dirty_edges) 

    # Gives a list of neighbours: for v in vertex.neighbours()
    def neighbours(self):
        for node in self.edges.iter():
            yield node.data.end_vertex 

    # Gives a list of edges
    def edges(self):
        for node in self.edges.iter():
            yield node.data
        
    # Checks if the other vertex is neighbour of this vertex 
    def isNeighbour(self, other_vertex):
        for vertex_id in self.neighbours():
            if (vertex_id == other_vertex.identification):
                return True
        return False

    # Add edge to the vertex
    def addEdge(self, edge):
        if (edge.isBlack()):
            self.dirty_edges.emplaceBack(edge)
        else:
            self.edges.emplaceBack(edge)

    
class Graph():
    # Init graph with 0 vertices
    def __init__(self):
        self.vertices = {}
        self.edge_count = 0

    # Add vertex to the graph if its id is not taken 
    def addVertex(self, vertex_id):
        if (vertex_id not in self.vertices):
            self.vertices[vertex_id] = Vertex(vertex_id)
    
    # Add the edge between two vertices. Add vertices to the graph, if they are not there
    def addEdgeBetween(self, vertex_id_a, vertex_id_b):
        edge_1 = Edge(vertex_id_a, vertex_id_b)
        edge_2 = Edge(vertex_id_b, vertex_id_a)
        edge_1.couple(edge_2)

        # make sure that both vertices are in the graph
        self.addVertex(vertex_id_a)
        self.addVertex(vertex_id_b)

        self.vertices[vertex_id_a].addEdge(edge_1)
        self.vertices[vertex_id_b].addEdge(edge_2)
        self.edge_count += 1
