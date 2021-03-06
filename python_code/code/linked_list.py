class Node:
    # Class constructor
    def __init__(self, data):
        self.data = data
        data.linked_list_node = self 
        self.next = None
        self.prev = None

    # A string representation of the node
    def __str__(self):
        return "(" + str(self.data) + ")"

class LinkedList:
    # Class constructor
    def __init__(self):
        self.size = 0;
        self.head = None;
        self.tail = None;

    # len(linked_list) = linked_list.size
    def __len__(self):
        return self.size;

    # 'in' operator. Compares item to the data in the node
    def __contains__(self, item):
        for node in self.iter():
            if (node.data == item):
                return True

        return False

    # iterator over linked list
    # used for the for loops (e.g. for node in nodes.iter())
    def iter(self):
        if (not self.empty()):
            curr_node = self.head
            while (curr_node != self.tail):
                yield curr_node
                curr_node = curr_node.next
            yield curr_node    

    # A string representation of the list
    def __str__(self):
        result = ""
        for node in self.iter():
            result += str(node) + ", "
        return "[" + result + "]"

    # returns true if the list is empty, false otherwise
    def empty(self):
        return self.size == 0;

    # initialize the list with one element
    def init(self, node):
        self.size = 1;
        self.head = node;
        self.tail = node;

        node.next = node;
        node.prev = node;

    # Return node at position pos
    def nodeAt(self, pos):
        if (self.empty()):
            return None

        if (pos >= self.size):
            return self.tail
        elif (pos <= 0):
            return self.head

        node = self.head    
        for i in range(pos):
            node = node.next

        return node

    # insert element to the back of the ilst
    def pushBack(self, node):
        if (self.empty()):
            self.init(node)
        else:
            self.insertAfterNode(node, self.tail) 

    # empalce element to the back of the list
    def emplaceBack(self, data):
        self.pushBack(Node(data))

    # insert element after a specific element
    def insertAfterNode(self, new_node, old_node):
        self.size += 1
        new_node.next = old_node.next
        old_node.next.prev = new_node

        new_node.prev = old_node
        old_node.next = new_node

        if (self.tail == old_node):
            self.tail = new_node

    # insert element before a specific element
    def insertBeforeNode(self, new_node, old_node):
        self.size += 1
        new_node.prev = old_node.prev
        old_node.prev.next = new_node

        new_node.next = old_node
        old_node.prev = new_node

        if (self.head == old_node):
            self.head = new_node

    # insert element at the position pos
    def insertAt(self, node, pos):
        if (self.empty()):
            self.init(node)
        else:
            if (pos <= 0):
                self.insertBeforeNode(node, self.head)
            else:
                self.insertAfterNode(node, self.nodeAt(pos-1))

    # deletes element at posisiton pos
    def deleteAt(self, pos):
        self.deleteNode(self.nodeAt(pos))

    # delete element
    def deleteNode(self, node):
        if (node is None):
            return

        node.prev.next = node.next
        node.next.prev = node.prev
        if (node == self.tail):
            self.tail = node.prev
        if (node == self.head):
            self.head = node.next

        node.prev = None
        node.next = None

        self.size -= 1

        if (self.size == 0):
            self.head = None
            self.tail = None

    # delete all the elements from the list
    def clear(self):
        for i in range(self.size):
            self.delete(self.head)

    # make a node new_head a new haed of the list.
    # new head has to be in the linked list
    def makeHead(self, new_head):
        if (self.size > 0):
            self.head = new_head
            self.tail = new_head.prev
