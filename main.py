from collections import deque
deq: deque[int] =deque()
#deq=deque()
#冒号是类型注解,实际上不使用类型注解一样能够输出正确结果，但是看起来不是很好，并且没有带类型检查
deq.append(1)
deq.append(2)
deq.append(3)
deq.appendleft(5)
deq.appendleft(6)
print(deq)
front:int =deq[0]
rear:int =deq[-1]
pop_front:int=deq.popleft()
print("pop front is",pop_front)

