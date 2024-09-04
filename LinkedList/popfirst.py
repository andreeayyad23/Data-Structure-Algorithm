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

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length +=1
    
    def preappend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        pre = self.head
        temp = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail.next = None
        self.tail = pre
        self.length -=1
        if self.length == 0:
            self.head = None
            self.head = None
        return temp.value
    
    def print_list(self):
        temp = self.head
        while temp:
            print (temp.value)
            temp = temp.next

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 0
        if self.length == 0:
            self.tail = 0
        return temp

    


# Example usage
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.print_list()
my_linked_list.preappend(3)

print("Popped value:", my_linked_list.pop())  

my_linked_list.print_list()

print("Head:", my_linked_list.head.value) 
print("Tail:", my_linked_list.tail.value)  
print("Length:", my_linked_list.length)    





# (2) Items - Returns 2 Node
print(my_linked_list.pop_first().value)
# (1) Item -  Returns 1 Node
print(my_linked_list.pop_first().value)
# (0) Items - Returns None
print(my_linked_list.pop_first())
my_linked_list.print_list()
