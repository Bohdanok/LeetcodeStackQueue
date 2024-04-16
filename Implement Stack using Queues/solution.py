class Node:
    def __init__(self, data, next = None) -> None:
        self.data = data
        self.next = next
    def __repr__(self) -> str:
        return f"{self.data} -> {self.next}"

class Queue:
    def __init__(self) -> None:
        self.head = None

    def push(self, node):
        if not self.head:
            self.head = node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = node

    def pop(self):
        if not self.head:
            return
        output_node = Node(self.head.data)
        self.head = self.head.next
        return output_node

    def __repr__(self) -> str:
        return repr(self.head)


class MyStack:

    def __init__(self):
        self.head = None

    def push(self, x: int) -> None:
        current_queue = Queue()
        current_queue.push(self.head)
        current_queue.push(Node(x))
        self.head = current_queue.head

    def pop(self) -> int:
        if not self.head:
            return
        reverse_queue = Queue()
        reverse_queue.push(self.head)
        output_queue = Queue()
        current_node = reverse_queue.head
        while current_node.next:
            output_queue.push(reverse_queue.pop())
            current_node = current_node.next
        self.head = output_queue.head
        return current_node.data



    def top(self) -> int:
        if not self.head:
            return
        reverse_queue = Queue()
        reverse_queue.push(self.head)
        n = reverse_queue.pop()
        while True:
            m = n
            n = reverse_queue.pop()
            if n is None:
                return m.data
            # n = reverse_queue.pop()

    def empty(self) -> bool:
        reverse_queue = Queue()
        reverse_queue.push(self.head)
        n = reverse_queue.pop()
        return n is None

    def __repr__(self) -> str:
        return repr(self.head)


my_queue = Queue()
my_queue.push(Node(1))
my_queue.push(Node(2))
print(my_queue)

my_stack = MyStack()
my_stack.push(1)
print(my_stack)
my_stack.push(2)
print(my_stack)

print(my_stack.top())
