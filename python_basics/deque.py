import collections
from collections import deque

de = deque(['name', 'age', 'DOB'])
print(de)

dq = deque([10,20,30])
dq.append(40) # deque([10, 20, 30, 40])
print(dq)
dq.append(50) # deque([10, 20, 30, 40, 50])
print(dq)
dq.appendleft(60)  # deque([60, 10, 20, 30, 40, 50])
print(dq)
dq.extendleft([70,80]) # deque([80, 70, 60, 10, 20, 30, 40, 50])
print(dq)
dq.extendleft([90,100]) # deque([100, 90, 80, 70, 60, 10, 20, 30, 40, 50])
print(dq)
dq.pop() # deque([100, 90, 80, 70, 60, 10, 20, 30, 40])
print(dq)
dq.popleft() # deque([90, 80, 70, 60, 10, 20, 30, 40])
print(dq)
dq.clear()
print(dq)

dq = collections.deque([10,20,30])
print(dq[0])
print(dq[-1])
print(len(dq))