#makes dequeue time complexity as O(1) instead of O(n)
from collections import deque

queue = deque()

queue.append(10)
queue.append(20)

print(queue)

queue.popleft()

print(queue)

queue.appendleft(30)
print(queue)
