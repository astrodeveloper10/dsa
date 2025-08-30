class QueueImpl:
    def __init__(self):
        self.data = []
        self.length = 0

    def enqueue(self, element):
        self.data.append(element)
        self.length += 1

    def dequeue(self):
        if self.length > 0:
            self.length -= 1
            return self.data.pop(0)
        return None

    def read(self):
        if self.length > 0:
            return self.data[0]
        return None


# q = QueueImpl()
# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)
#
# print(q.data)
# print(f'Length of queue is: {q.length}')
# print(q.read())
# q.dequeue()
# print(f'Length of queue is: {q.length}')
# print(q.data)