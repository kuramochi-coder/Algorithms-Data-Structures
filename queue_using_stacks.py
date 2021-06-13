class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.size = 0
        

    def push(self, x):
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)
        self.size += 1
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.size > 0:
            self.size -= 1
            return self.stack.pop(0)
        

    def peek(self):
        """
        Get the front element.
        """
        if self.size > 0:
            return self.stack[0]
        

    def empty(self):
        """
        Returns whether the queue is empty.
        """
        if self.size > 0:
            return False
        else:
            return True

q = MyQueue()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
print(q.pop())
q.push(5)
q.push(6)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
# 1 2 3 4 5 6