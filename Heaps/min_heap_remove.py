class MinHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def _heapify_up(self, index):
        while index > 0 and self.heap[index] < self.heap[self._parent(index)]:
            self._swap(index, self._parent(index))
            index = self._parent(index)

    def _heapify_down(self, index):
        smallest = index
        left = self._left_child(index)
        right = self._right_child(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self._swap(index, smallest)
            self._heapify_down(smallest)

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def remove(self):
        if len(self.heap) == 0:
            return None
        elif len(self.heap) == 1:
            return self.heap.pop()
        else:
            min_element = self.heap[0]
            self.heap[0] = self.heap.pop()
            self._heapify_down(0)
            return min_element

myheap = MinHeap()
myheap.insert(12)
myheap.insert(10)
myheap.insert(8)
myheap.insert(6)

print(myheap.heap)  # [6, 8, 10, 12]

myheap.insert(4)

print(myheap.heap)  # [4, 6, 10, 12, 8]

myheap.insert(2)

print(myheap.heap)  # [2, 6, 4, 12, 8, 10]