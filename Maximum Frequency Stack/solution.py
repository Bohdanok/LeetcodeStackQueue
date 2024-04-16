
#  def pop(self):
#         if not self.head.next:
#             n = self.head.data
#             self.head = None
#             self.max_count -= 1
#             return n
#         if self.head.count == self.max_count:
#             n = self.head.data
#             self.head = self.head.next
#             self.max_count -= 1
#             return n
#         current_naode = self.head
#         while current_node:
#             if current_node.count == self.max_count:
#                 self.max_count -= 1
#                 break
#             prev = current_node
#             current_node = current_node.next
#         prev.next = current_node.next
#         n = current_node.data
#         current_node = None

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        self.count = 1
    def __repr__(self) -> str:
        return f"{self.data} -> {self.next}"

class MaxVal:
    def __init__(self) -> None:
        self.count = 1
    def __add__(self, other):
        return self.count + other

class FreqStack:

    def __init__(self):
        self.head = None
        self.max_count = 1

    def push(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
        else:
            current_node = self.head
            while current_node:
                if current_node.data == val:
                    self.head = Node(val, self.head)
                    num = current_node.count + self.head.count
                    self.head.count = num
                    if num > self.max_count:
                        self.max_count = num
                    return
                current_node = current_node.next
            self.head = Node(val, self.head)
    def pop(self):
        max_count = 0
        if not self.head.next:
            n = self.head.data
            self.head = None
            return n
        current_node = self.head
        while current_node:
            if current_node.count > max_count:
                max_count = current_node.count
            current_node = current_node.next
        if self.head.count == max_count:
            n = self.head.data
            self.head = self.head.next
            return n
        current_node = self.head
        while current_node:
            if current_node.count == max_count:
                break
            prev = current_node
            current_node = current_node.next
        prev.next = current_node.next
        n = current_node.data
        current_node = None

        return n
    def __repr__(self) -> str:
        return f"{self.head}::::{self.max_count}"

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

c = FreqStack()

c.push(1)

c.push(2)

c.push(1)

c.push(1)
c.push(2)
c.push(2)
c.push(2)
c.pop()
print(c)
c.pop()
print(c)
c.pop()
print(c)
c.pop()
print(c)
c.pop()
print(c)
c.pop()
print(c)
c.pop()
print(c)