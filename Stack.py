class Stack:
    def __init__(self):
        self.__list = []

    def __str__(self):
        result = "Here is a stack: "
        for item in self.__list:
            result += str(item) + ", "
        return result

    def push(self, item):
        self.__list.append(item)

    def pop(self):
        self.__list.pop()

    def get_num_of_elements(self):
        return len(self.__list)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

stack.pop()
stack.pop()

print(stack)
