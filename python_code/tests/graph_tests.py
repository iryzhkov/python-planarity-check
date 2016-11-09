import unittest

from ..code import linked_list 
from ..code import graph 

Node = linked_list.Node
LinkedList = linked_list.LinkedList

Edge = graph.Edge
Vertex = graph.Vertex
Graph = graph.Graph

class TestingEdge(unittest.TestCase):
    # Test init and coupling with inverse vertex 
    def test_init_and_couple(self):
        edge_a = Edge(1,2)
        edge_b = Edge(2,1)

        self.assertEquals(edge_a.start_vertex, 1)
        self.assertEquals(edge_a.end_vertex, 2)
        self.assertIsNone(edge_a.inverse_edge)
        
        self.assertEquals(edge_b.start_vertex, 2)
        self.assertEquals(edge_b.end_vertex, 1)
        self.assertIsNone(edge_b.inverse_edge)

        edge_a.couple(edge_b)
        self.assertEquals(edge_a.inverse_edge, edge_b)
        self.assertEquals(edge_b.inverse_edge, edge_a)

    # Test how blacken, whiten and isBlack behave
    def test_white_and_black(self):
        edge = Edge(1,2)
        self.assertFalse(edge.isBlack())
        edge.blacken()
        self.assertTrue(edge.isBlack())
        edge.whiten()
        self.assertFalse(edge.isBlack())


class TestingVertex(unittest.TestCase):
    # Test whether the new vertex has all the right properties
    def test_init(self):
        vertex = Vertex(1)
        self.assertEquals(len(vertex), 0)

    # Test how adding edges affect the vertex
    def test_edges(self):
        vertex = Vertex(1)

        edge_a = Edge(1,2)
        vertex.addEdge(edge_a)
        self.assertEquals(len(vertex), 1)

        edge_b = Edge(1,3)
        vertex.addEdge(edge_b)
        self.assertEquals(len(vertex), 2)

    # Test how vertecies which are neighbours behave
    def test_neighbours(self):
        pass


class TestingGraph(unittest.TestCase):
    def test_init(self):
        pass

    def test_adding_verticies(self):
        pass


if __name__ == "__main__":
    unittest.main()
