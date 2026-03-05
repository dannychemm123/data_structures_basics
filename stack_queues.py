from collections import deque
from typing import Any

class Stack:
    """A data structure following the Last In First Out (LIFO) principle."""
    
    def __init__(self) -> None:
        self.stack: list = []

    def push(self, item: Any) -> None:
        """Add an item to the top of the stack."""
        self.stack.append(item)

    def pop(self) -> Any:
        """Remove and return the top item. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.stack.pop()
    
    def peek(self) -> Any:
        """Return the top item without removing it. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.stack[-1]
    
    def size(self) -> int:
        """Return the number of items in the stack."""
        return len(self.stack)
    
    def is_empty(self) -> bool:
        """Return True if the stack is empty."""
        return self.size() == 0
    
    def __str__(self) -> str:
        return str(self.stack)


class Queue:
    """A data structure following the First In First Out (FIFO) principle."""
    
    def __init__(self) -> None:
        self.queue: deque = deque()

    def enqueue(self, item: Any) -> None:
        """Add an item to the back of the queue."""
        self.queue.append(item)

    def dequeue(self) -> Any:
        """Remove and return the front item. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.queue.popleft()
    
    def peek(self) -> Any:
        """Return the front item without removing it. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.queue[0]
    
    def size(self) -> int:
        """Return the number of items in the queue."""
        return len(self.queue)
    
    def is_empty(self) -> bool:
        """Return True if the queue is empty."""
        return self.size() == 0
    
    def __str__(self) -> str:
        return str(list(self.queue))


if __name__ == "__main__":
    # Test Stack
    stk = Stack()
    stk.push(1)
    stk.push(2)
    stk.push(3)
    print(stk)
    stk.pop()
    print(stk)
    print(stk.peek())
    print(stk.size())
    print(stk.is_empty())   

    # Test Queue
    que = Queue()
    que.enqueue(1)
    que.enqueue(2)
    que.enqueue(3)
    print(que)
    que.dequeue()
    print(que)
    print(que.peek())
    print(que.size())
    print(que.is_empty())