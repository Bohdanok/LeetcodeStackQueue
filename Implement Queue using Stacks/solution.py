class Node:
    def __init__(self, data, next = None) -> None:
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        return f"{self.data} -> {self.next}"

class Stack:
    def __init__(self):
        self.head = None
    def push(self, node):
        if not self.head:
            self.head = node
        else:
            current_node = self.head
            while current_node. next:
                current_node = current_node.next
            current_node.next = node

    def pop(self):
        if not self.head:
            return
        else:
            cur = self.head
            if not cur.next:
                n = cur.data
                self.head = None
            else:
                while cur.next.next:
                    cur = cur.next
                n = cur.next.data
                cur.next = cur.next.next

                
            return n

    def empty(self):
        return self.head is None

    def top(self):
        if not self.head:
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        return current_node.data

    def __repr__(self) -> str:
        return repr(self.head)

class MyQueue:
    def __init__(self):
        self.stackhead = Stack()
        self.stacktail = Stack()

    def push(self, x: int) -> None:
        self.stackhead.push(Node(x))
        self.stacktail.push(Node(x))

    def pop(self) -> int:
        if not self.stackhead.head:
            return
        self.stacktail = Stack()
        # n = self.stackhead.pop()
        # self.stacktail.push(Node(n))
        while not self.stackhead.empty():
            n = self.stackhead.pop()
            if not self.stackhead.empty():
                self.stacktail.push(Node(n))
            else: break
        t = self.stacktail.head.data if self.stacktail.head else None
        while not self.stacktail.empty():
            self.stackhead.push(Node(self.stacktail.pop()))
        self.stacktail = Stack()
        if t:
            self.stacktail.push(Node(t))
        return n

        
    def __repr__(self) -> str:
        return repr(self.stackhead.head)

    def peek(self) -> int:
        return self.stackhead.head.data if self.stackhead.head else None

    def empty(self) -> bool:
        return self.stackhead.empty()
        


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
# print(obj)
obj.push(2)

print(obj)

obj.pop()

print(obj)

# obj.push(3)

# print(obj)

# obj.push(3)

# obj.push(4)

# obj.pop()

# print(obj.peek())


# print(obj.pop())
# print(obj.peek())

# obj.pop()

# print(obj)

print(obj.empty())

# print(obj.peek())

# print(obj)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()