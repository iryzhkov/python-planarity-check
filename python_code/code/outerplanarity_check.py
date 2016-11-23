from graph import *
from linked_list import *

# is the graph outerplannar
def isOuterplannar(graph):
    # find all vertices with degree less than or equal to two.
    vs_with_deg_le_two = filter(lambda x: len(graph.vertices[x].edges) <= 2, graph.vertices) 

    # Call a recursive helper function to figure out the result
    return isOuterplannarAux(graph, vs_with_deg_le_two)

# recursive helper function that figures out the solution
def isOuterplannarAux(graph, vs_with_deg_le_two):
    # First base case: the graph is empty, nothing to do
    if len(graph.vertices) == 0:
        return True

    # Second base case: no more vertices with degree less than or equal to two 
    if len(vs_with_deg_le_two) == 0:
        return False

    # pick the last element, remove it from the list
    curr_vertex = vs_with_deg_le_two.pop() 

    # Clean the dirty edges, if the vertex has more than two after cleaning, go to the
    # next in the list. Repeat until find good vertex, or the list is empty
    while (not cleanDirtyEdgesForVertex(graph, curr_vertex)) and len(vs_with_deg_le_two) > 0:
        curr_vertex = vs_with_deg_le_two.pop() 

    # Third base case: no more vertices with degree less than or equal to two after cleaning 
    if len(graph.vertices[curr_vertex].edges) > 2 and len(vs_with_deg_le_two) == 0:
        return False

    # Perform a two reduction, and remember data needed for restoration.
    restore_data = twoReduction(graph, curr_vertex, vs_with_deg_le_two)

    print "Performed two reduction on the vertex " + str(curr_vertex)

    # Recurse on the subproblem
    # If something went wrong in the subproblem, return False to signal that the graph is not outerplannar
    if not isOuterplannarAux(graph, vs_with_deg_le_two):
        return False

    # In case of success, perform graph restoration, to printout the cyclic order
    success = twoReductionRestoration(graph, restore_data, curr_vertex)
    return success 

# Perform a two reduction
def twoReduction(graph, v, vs_with_deg_le_two):
    if len(graph.vertices[v].edges) < 2:
        return twoReductionDegreeLessThanTwo(graph, v, vs_with_deg_le_two)
    else:
        return twoReductionDegreeEqualTwo(graph, v, vs_with_deg_le_two)

# Perform a two reduction for vertex with degree < 2
# Returns two edges for the reconstruction
def twoReductionDegreeLessThanTwo(graph, v, vs_with_deg_le_two):
    vertex = graph.vertices[v] 
    edge = None
    inverse_edge = None

    # If there is an edge, then delete the edge and the vertex from the graph,
    # otherwise remove only the vertex
    if len(vertex.edges) > 0:
        edge = vertex.edges.nodeAt(0).data
        inverse_edge = edge.inverse_edge

        end_vertex = graph.vertices[edge.end_vertex]
        end_vertex.edges.deleteNode(inverse_edge.linked_list_node)

        # Add vertex to the list if new degree becomes 2
        if (len(end_vertex.edges) == 2):
            vs_with_deg_le_two.append(end_vertex.identification)

        vertex.edges.deleteNode(edge.linked_list_node)

    del graph.vertices[v]

    return [True, edge, inverse_edge]

# Perform a two reduction for vertex with degree 2
# Returns 2 edges for the reconstruction
def twoReductionDegreeEqualTwo(graph, v, vs_with_deg_le_two):
    vertex = graph.vertices[v] 

    # Work on the first edge and the vertex that it leads to
    edge_1 = vertex.edges.nodeAt(0).data
    inverse_edge_1 = edge_1.inverse_edge
    end_vertex_1 = graph.vertices[edge_1.end_vertex]
    end_vertex_1.edges.deleteNode(inverse_edge_1.linked_list_node)

    # Add vertex to the list if new degree becomes 2
    if (len(end_vertex_1.edges) == 2):
        vs_with_deg_le_two.append(end_vertex_1.identification)

    # Work on the second edge and the vertex that it leads to
    edge_2 = vertex.edges.nodeAt(1).data
    inverse_edge_2 = edge_2.inverse_edge
    end_vertex_2 = graph.vertices[edge_2.end_vertex]
    end_vertex_2.edges.deleteNode(inverse_edge_2.linked_list_node)

    # Add vertex to the list if new degree becomes 2
    if (len(end_vertex_2.edges) == 2):
        vs_with_deg_le_two.append(end_vertex_2.identification)

    # Delete vertex from the graph
    vertex.edges.deleteNode(edge_1.linked_list_node)
    vertex.edges.deleteNode(edge_2.linked_list_node)
    del graph.vertices[v]

    # Add dirty edge to the neighbours
    dirty_edge_1 = Edge(end_vertex_1.identification, end_vertex_2.identification, True)
    dirty_edge_2 = Edge(end_vertex_2.identification, end_vertex_1.identification, True)
    dirty_edge_1.couple(dirty_edge_2)

    end_vertex_1.addEdge(dirty_edge_1)
    end_vertex_2.addEdge(dirty_edge_2)

    return [False, edge_1, inverse_edge_1, edge_2, inverse_edge_2]

# Undo the twoReduction operation
def twoReductionRestoration(graph, restore_data, restore_vertex):
    if restore_data[0]:
        return twoReductionRestorationDegreeLessThenTwo(graph, restore_data, restore_vertex)
    else:
        return twoReductionRestorationDegreeEqualTwo(graph, restore_data, restore_vertex)

# Undo twoReduction for vertex with degree < 2
def twoReductionRestorationDegreeLessThenTwo(graph, restore_data, restore_vertex):
    graph.addVertex(restore_vertex)

    # Read in the restoration information
    edge_from_vertex = restore_data[1]
    edge_to_vertex = restore_data[2]

    # If there were edges, insert them. Make the edge that went into the restored vertex 
    # To become head, and be placed before the current head of the other vertex
    if not edge_from_vertex is None:
        graph.vertices[restore_vertex].addEdge(edge_from_vertex)
        graph.vertices[edge_from_vertex.end_vertex].edges.insertAt(Node(edge_to_vertex), 0)

    return True

# Undo twoReduction for vertex with degree = 2
def twoReductionRestorationDegreeEqualTwo(graph, restore_data, restore_vertex):
    graph.addVertex(restore_vertex)
    vertex = graph.vertices[restore_vertex]

    # Read in the restoration information
    edge_1_from_vertex = restore_data[1]
    edge_1_to_vertex = restore_data[2]
    edge_2_from_vertex = restore_data[3]
    edge_2_to_vertex = restore_data[4]

    # Get the neighbouring vertices 
    neighbour_1 = graph.vertices[edge_1_from_vertex.end_vertex]
    neighbour_2 = graph.vertices[edge_2_from_vertex.end_vertex]

    # Make sure that neighbour 1 is to the left of neighbour 2 from restored vertex perspective
    # Swap them if they are mixed
    if neighbour_2.edges.head.data.end_vertex == neighbour_1.identification:
        t = edge_1_from_vertex
        edge_1_from_vertex = edge_2_from_vertex
        edge_2_from_vertex = t

        t = edge_1_to_vertex
        edge_1_to_vertex = edge_2_to_vertex
        edge_2_to_vertex = t

        t = neighbour_1
        neighbour_1 = neighbour_2
        neighbour_2 = t

    # If Swapping cannot help, then we are in situation, where restoration is impossible
    elif not neighbour_1.edges.head.data.end_vertex == neighbour_2.identification:  
        return False

    # put the edges in the right order
    node = Node(edge_1_to_vertex)
    neighbour_1.edges.insertAt(node, 1)
    neighbour_1.edges.makeHead(node)

    node = Node(edge_2_to_vertex)
    neighbour_2.edges.insertAt(node, 1)

    # if the edge between neighbour 1 and 2 is originally dirty, we need to remove it
    if (neighbour_1.edges.tail.data.originally_black):
        edge_1 = neighbour_1.edges.tail.data
        edge_2 = edge_1.inverse_edge
        neighbour_1.edges.deleteNode(edge_1.linked_list_node)
        neighbour_2.edges.deleteNode(edge_2.linked_list_node)

    vertex.edges.emplaceBack(edge_2_from_vertex)
    vertex.edges.emplaceBack(edge_1_from_vertex)
    return True
        

# Go though dirty edges of vertex, add the ones which are not present yet.
# Return True if the resulting vertex has a degree less than or equal to two
# Return False otherwise
def cleanDirtyEdgesForVertex(graph, v):
    vertex = graph.vertices[v]

    # Insert dirty edges that are not there until no more dirty edges are left
    # or the number of clean edges exceeds 2
    while len(vertex.dirty_edges) > 0 and len(vertex.edges) <= 2:
        # Get the first dirty edge
        dirty_edge_node = vertex.dirty_edges.nodeAt(0)
        dirty_edge = dirty_edge_node.data
        vertex.dirty_edges.deleteNode(dirty_edge_node) 

        # Get the inverse of it
        other_dirty_edge = dirty_edge.inverse_edge
        other_vertex = graph.vertices[dirty_edge.end_vertex]
        other_vertex.dirty_edges.deleteNode(other_dirty_edge.linked_list_node)

        # See if this edge is already in the vertex
        if not dirty_edge in vertex.edges:
            # If it is, add it 
            dirty_edge.whiten()
            vertex.addEdge(dirty_edge)

            # Add the inverse edge as well
            other_dirty_edge.whiten()
            other_vertex.addEdge(other_dirty_edge)

    return len(vertex.edges) <= 2 

g = Graph()
g.addVertex(0)
g.addVertex(1)
g.addVertex(2)
g.addVertex(3)

g.addEdgeBetween(0,1)
g.addEdgeBetween(0,2)
g.addEdgeBetween(1,2)
g.addEdgeBetween(0,3)
g.addEdgeBetween(3,2)
g.addEdgeBetween(3,1)

print isOuterplannar(g)
print str(g)
