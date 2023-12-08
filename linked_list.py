class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        """
        Add a new Node to the end of the Linked List

        Complexity: O(1)
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

        return True
    
    def pop(self):
        """
        Removes and returns the last Node in the Linked List

        Complexity: O(n)
        """
        if self.length == 0:
            return None
        
        temp = self.head
        prev = self.head
        
        while temp.next is not None:
            prev = temp
            temp = temp.next

        self.tail = prev
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        
        return temp
    
    def prepend(self, value):
        """
        Add a new Node to the start of the Linked List

        Complexity: O(1)
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1

        return True

    def pop_first(self):
        """
        Removes and returns the first Node of the Linked List

        Complexity: O(1)
        """
        if self.length == 0:
            return None
        
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None

        return temp
    
    def get(self, index):
        """
        Retrieve a Node from a specified index from the Linked List

        Complexity: O(n)
        """
        if index < 0 or index >= self.length:
            return None
        
        temp = self.head
        for _ in range(index):
            temp = temp.next
        
        return temp
    
    def set_value(self, index, value):
        """
        Change the value of a Node at a specfied index in the Linked List

        Complexity: O(n)
        """
        temp = self.get(index)
        
        if temp:
            temp.value = value
            return True
        
        return False
    
    def insert(self, index, value):
        """
        Create a new Node and add to a specified index in the Linked List

        Complexity: O(n)
        """
        if index < 0 or index > self.length:
            return False
        
        if index == 0:
            return self.prepend(value)
        
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node

        self.length += 1

        return True
    
    def remove(self, index):
        """
        Removes and returns a Node from the Linked List based on a given index

        Complexity: O(n)
        """
        if index < 0 or index >= self.length:
            return None
        
        if index == 0:
            return self.pop_first()
        
        if index == self.length-1:
            return self.pop()
        
        prev = self.get(index - 1)
        temp = prev.next      # this method is O(1), instead of using self.get(index), which is O(n)
        prev.next = temp.next
        temp.next = None
        self.length -= 1

        return temp
    
    def reverse(self):
        """
        Reverse the order of the Nodes in the Linked List.

        Complexity: O(n)
        """
        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

my_linked_list.reverse()

my_linked_list.print_list()