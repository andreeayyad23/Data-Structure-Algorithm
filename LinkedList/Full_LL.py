class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return self

    def pop(self):
        if self.head is None:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None

        if self.tail == self.head:  # If there was only one element
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        return self

    def pop_first(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        if self.head is None:  # If the list is now empty
            self.tail = None
        return temp
    
    def get(self, index):
        if index < 0:
            return None
        temp = self.head
        for _ in range(index):
            if temp is None:
                return None
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
        

    def insert(self, index, value):
        if index < 0:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.get_length():  # Use get_length() to check the end
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        if temp is None:
            return False
        new_node.next = temp.next
        temp.next = new_node
        return True

    def remove(self, index):
        if index < 0:
            return None
        if index == 0:
            return self.pop_first()
        pre = self.get(index - 1)
        if pre is None or pre.next is None:
            return None
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        if pre.next is None:  # If we removed the last element
            self.tail = pre
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        while temp is not None:
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return self

    def get_length(self):
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next
        return count

    def __str__(self):
        temp = self.head
        result = ""
        while temp is not None:
            result += str(temp.value) + " "
            temp = temp.next
        return result.strip()

# Example usage
my_linked_list = LinkedList(4)
my_linked_list.append(5)
my_linked_list.append(3)
my_linked_list.append(2)
my_linked_list.append(1)
my_linked_list.prepend(5)
my_linked_list.prepend(6)
my_linked_list.insert(2, 0)
my_linked_list.remove(2)
my_linked_list.reverse()

print(my_linked_list)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.get_length())