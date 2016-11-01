import unittest

from ..code import linked_list

Node = linked_list.Node
LinkedList = linked_list.LinkedList


class DummyClass():
    def __init__(self, data):
        self.linked_list_node = None
        self.data = data

    def __str__(self):
        return str(self.data)


class TestingLinkedListNode(unittest.TestCase):
    # Testing the state of linked list node after initialization
    def test_init(self):
        node = Node(DummyClass(25))
        self.assertEquals(node.data.data, 25, "node.data is different from initialization value")
        self.assertEquals(node.data.linked_list_node, node, "node didn't update the node attribute of the data")

        node = Node(DummyClass("String"))
        self.assertEquals(node.data.data, "String", "node.data is different from initialization value")
        self.assertEquals(node.data.linked_list_node, node, "node didn't update the node attribute of the data")


class TestingLinkedList(unittest.TestCase):
    # Testing the state of linked list after initialization
    def test_init(self):
        linked_list = LinkedList()

        self.assertTrue(linked_list.empty(), "Initialized linked list is not empty")
        self.assertEquals(len(linked_list), 0, "Initialized linked list has size != 0")

    # Testing what happens to the linked list during pushBack
    def test_pushBack(self):
        linked_list = LinkedList()

        node = Node(DummyClass(25));
        linked_list.pushBack(node);

        self.assertFalse(linked_list.empty(), "Linked list with 1 element is empty")
        self.assertEquals(linked_list.head, node, "The only node is not the head")
        self.assertEquals(linked_list.tail, node, "The only node is not the tail")
        self.assertEquals(len(linked_list), 1, "Linked list with 1 element has size " + str(len(linked_list)))

        node = Node(DummyClass(26));
        linked_list.pushBack(node);

        self.assertFalse(linked_list.empty(), "Linked list with 2 element is empty")
        self.assertNotEquals(linked_list.head, node, "The second node is the head")
        self.assertEquals(linked_list.tail, node, "The last node is not the tail")
        self.assertEquals(len(linked_list), 2, "Linked list with 2 element has size " + str(len(linked_list)))
    
    # Testing how the iter and nodeAT functions behave
    def test_iter_nodeAt(self):
        linked_list = LinkedList()

        nodes = [Node(DummyClass(i)) for i in range(25)];
        for node in nodes:
            linked_list.pushBack(node);

        index = 0 
        for node in linked_list.iter():
            self.assertEquals(node, nodes[index], "The iter gives wrong order. Expected " + str(nodes[index]) + ", got " + str(node))
            self.assertEquals(linked_list.nodeAt(index), nodes[index], "The node at gives wrong order")
            index += 1

        self.assertEquals(index, 25, "The iter only returned " + str(index) + "values, while the list has 25.")
        self.assertEquals(linked_list.head, nodes[0], "The first node is not the head of the list")
        self.assertEquals(linked_list.tail, nodes[-1], "The last node is not the tail of the list")

    def test_inserts(self):
        linked_list = LinkedList()

        nodes = [Node(DummyClass(i)) for i in range(25)];
        for node in nodes:
            linked_list.pushBack(node);

        node = Node(DummyClass(123))
        linked_list.insertAfterNode(node, linked_list.head)

        self.assertNotEquals(linked_list.head, node, "The second element became the head")
        self.assertNotEquals(linked_list.tail, node, "The second element became the tail")
        self.assertEquals(linked_list.nodeAt(1), node, "The inserting element after head did not make it second")

        node = Node(DummyClass(321))
        linked_list.insertBeforeNode(node, linked_list.head)

        self.assertEquals(linked_list.head, node, "The first element did not become the head")
        self.assertNotEquals(linked_list.tail, node, "The second element became the tail")
        self.assertEquals(linked_list.nodeAt(0), node, "The inserting element before head did not make it first")

        node = Node(DummyClass(1234))
        linked_list.insertAfterNode(node, linked_list.tail)

        self.assertNotEquals(linked_list.head, node, "The last element became the head")
        self.assertEquals(linked_list.tail, node, "The last element did not become the tail")
        self.assertEquals(linked_list.nodeAt(27), node, "The inserting element after tail did not make it last")

        node = Node(DummyClass(4321))
        linked_list.insertBeforeNode(node, linked_list.tail)

        self.assertNotEquals(linked_list.head, node, "The almost last element became the head")
        self.assertNotEquals(linked_list.tail, node, "The almost last element became the tail")
        self.assertEquals(linked_list.nodeAt(27), node, "The inserting element before tail did not make it second to last")

        nodes = [Node(DummyClass(23*i)) for i in range(23)]
        for i in range(len(nodes)):
            linked_list.insertAt(nodes[i], 3+i)
            self.assertEquals(nodes[i], linked_list.nodeAt(3+i), "The insertAt doesn't allign with nodeAt")

    def test_deletes(self):
        linked_list = LinkedList()


if __name__ == "__main__":
    unittest.main()
