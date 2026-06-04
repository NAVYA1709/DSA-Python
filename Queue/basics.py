#QUEUE (FIFO)
queue = []
print(queue)
#enqueue
queue.append(10)
queue.append(20)
queue.append(30)
# queue.insert(0,5)
print(queue)
#dequeue
removed = queue.pop(0)
print(removed)
print(queue)

# Front Element
print(queue[0])
# Rear Element
print(queue[-1])

#empty queue check 
if len(queue) == 0:
    print("Empty")
else:
    print("Not Empty")
