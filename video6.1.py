import queue

q = queue.PriorityQueue()
numbers = [1,2,3,4,5,6,7]

q.put((2, "Hello World"))
q.put((11, 99))
q.put((5, 7.5))
q.put((1,True))
while not q.empty():
    print(q.get()[1])