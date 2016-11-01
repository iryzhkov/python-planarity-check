class Node:
    def __init__(self, data):
        self.data = data
        data.linked_list_node = self 
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)

class LinkedList:
    # Class constructor
    def __init__(self):
        self.size = 0;
        self.head = None;
        self.tail = None;

    # len(linked_list) = linked_list.size
    def __len__(self):
        return self.size;

    # iterator over linked list
    def iter(self):
        if (not self.empty()):
            curr_node = self.head
            while (curr_node != self.tail):
                yield curr_node
                curr_node = curr_node.next
            yield curr_node    

    # A string representation of the list
    def __str__(self):
        result = "["
        for node in self.iter():
            result += str(node) + ", "
        result += "]"
        return result

    # initialize the list with one element
    def init(self, node):
        self.size = 1;
        self.head = node;
        self.tail = node;

        node.next = node;
        node.prev = node;

    # returns true if the list is empty, false otherwise
    def empty(self):
        return self.size == 0;

    # insert element to the back of the ilst
    def pushBack(self, node):
        if (self.empty()):
            self.init(node);
        else:
            self.tail.next = node
            node.prev = self.tail
            self.head.prev = node
            node.next = self.head
            self.tail = node
            self.size += 1

    # insert element at the position pos
    def insertAtPos(self, node, pos):
        pass

    # insert element after a specific element
    def insertAfterNode(self, new_node, old_node):
        pass

    # insert element before a specific element
    def insertBeforeNode(self, new_node, old_node):
        pass

    # deletes element at posisiton pos
    def deleteAtPos(self, pos):
        pass

    # delete element
    def delete(self, node):
        if (self.size == 1):
            self.clear();

    # delete all the elements from the list
    def clear(self):
        self.size = 0
        self.head = None
        self.tail = None
        pass
