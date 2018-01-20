class Queue:
    def __init__(self):
        self.__list = []

    def __str__(self):
        result = "Here is a queue: "
        for item in list:
            result += str(item) + ", "
        return result

    def enqueue(self, item):
        self.__list.insert(0, item)

    def dequeue(self):
        self.__list.remove(self.__list[0])

    def clear(self):
        self.__list.clear()

queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

queue.dequeue()
queue.dequeue()

print(queue)
