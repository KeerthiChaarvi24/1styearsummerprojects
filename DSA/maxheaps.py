class MaxHeap:

    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def insert(self, value):

        self.heap.append(value)

        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:

            self.heap[current], self.heap[self._parent(current)] = \
                self.heap[self._parent(current)], self.heap[current]

            current = self._parent(current)

    def _sink_down(self, index):

        max_index = index

        while True:

            left = self._left_child(index)
            right = self._right_child(index)

            if left < len(self.heap) and self.heap[left] > self.heap[max_index]:
                max_index = left

            if right < len(self.heap) and self.heap[right] > self.heap[max_index]:
                max_index = right

            if max_index != index:
                self.heap[index], self.heap[max_index] = \
                    self.heap[max_index], self.heap[index]

                index = max_index

            else:
                return

    def remove(self):

        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]

        self.heap[0] = self.heap.pop()

        self._sink_down(0)

        return max_value