class Node:
        """
        Each node of the linked list will have data and links to the 
        previous and next node. 
        """

        def __init__(self, data):
            """ 
            Initialize the node to the data provided.  Initially
            the links are unknown so they are set to None.
            """
            self.data = data
            self.next = None
            self.prev = None


# EXAMPLE 1 START
# Go through each node and manually link them together. The code directly below will help you test your code!
# If you get lost, look back on the trains and take a look at the sample output. 

A = Node("A") # This should be the head.
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F") # This should be the tail.

A.next = B
A.prev = None

B.next = C
B.prev = A

C.next = D
C.prev = B

D.next = E
D.prev = C

E.next = F
E.prev = D

F.next = None
F.prev = E


print()
# NOTE: This code here is *just* for showing the concept of a node.
# The example with linked lists will actually cover moving through a linked list.
node_list = [A,B,C,D,E,F]
for i in range(len(node_list)):

    # Gather the info for the current node. What's in front of it, what's behind it?
    node = node_list[i]
    next = node.next
    prev = node.prev

    # This code makes it so that it will print something out, even if your code doesn't work.
    node_out = node.data
    if next != None:
        next_out = next.data
    else:
        next_out = None
    if prev != None:
        prev_out = prev.data
    else:
        prev_out = None

    # What data is contained inside of the list?
    print(f"Node: {node_out} Next: {next_out} Prev: {prev_out}")
print()





class LinkedList:
    """
    Implement the LinkedList data structure.  The Node class below is an 
    inner class.  An inner class means that its real name is related to 
    the outer class.  To create a Node object, we will need to 
    specify LinkedList.Node
    """

    class Node:
        """
        Each node of the linked list will have data and links to the 
        previous and next node. 
        """

        def __init__(self, data):
            """ 
            Initialize the node to the data provided.  Initially
            the links are unknown so they are set to None.
            """
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None
        self.tail = None


    def insert_after(self, value, new_value):
        """
        Insert 'new_value' after the first occurance of 'value' in
        the linked list.
        """

        # EXAMPLE 2 START
        # Search for the node that matches 'value' by starting at the 
        # head of the list.
        curr = self.head
        new_node = LinkedList.Node(new_value)
        # Since the new node has already been created, we can use new_node when we add it.
        
        while curr is not None:

            if curr == self.tail: # Are we at the end of the list? If so, we can just add it after this node.
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
            
            elif curr.data == value: # otherwise, is this the first occurance of our value?
                new_node.prev = curr # Remember the diagram -- don't get too jumpy and cut the links between the nodes too early!
                new_node.next = curr.next

                curr.next = new_node
                curr.next.prev = new_node
                break # Don't forget to tell it to exit the loop when we're done!

            curr = curr.next # Go to the next node to search for 'value'

    def insert_head(self, value):
        """
        Insert a new node at the front (i.e. the head) of the
        linked list.
        """
        # Create the new node
        new_node = LinkedList.Node(value)  
        
        # If the list is empty, then point both head and tail
        # to the new node.
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # If the list is not empty, then only self.head will be
        # affected.
        else:
            new_node.next = self.head # Connect new node to the previous head
            self.head.prev = new_node # Connect the previous head to the new node
            self.head = new_node      # Update the head to point to the new node

    def remove_head(self):
        """ 
        Remove the first node (i.e. the head) of the linked list.
        """
        # If the list has only one item in it, then set head and tail 
        # to None resulting in an empty list.
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # If the list has more than one item in it, then only self.head
        # will be affected.
        elif self.head is not None:
            self.head.next.prev = None  # Disconnect the second node from the first node
            self.head = self.head.next  # Update the head to point to the second node

    def __iter__(self):
        """
        Iterate foward through the Linked List
        """
        curr = self.head  # Start at the begining since this is a forward iteration.
        while curr is not None:
            yield curr.data  # Provide (yield) each item to the user
            curr = curr.next # Go forwrd in the linked list

    def __str__(self):
        """
        Return a string representation of the linked list.
        """
        output = "linkedlist["
        first = True
        curr = self.head
        while curr is not None:
            if first:
                first = False
            else:
                output += ", "
            output += str(curr.data)
            curr = curr.next
        output += "]"
        return output

example_linked_list = LinkedList()

example_linked_list.insert_head(20)
example_linked_list.insert_head(50)
example_linked_list.insert_head(40)
example_linked_list.insert_head(30)
example_linked_list.insert_head(20)
example_linked_list.insert_head(10)

print("Contained in the linked list:")
for item in example_linked_list:
    print(item)
print()
print("After inserting a value:")
example_linked_list.insert_after(20, 25)
for item in example_linked_list:
    print(item)