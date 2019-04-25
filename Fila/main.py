from queue import Queue


q = Queue()

q.push(1)
q.push(2)
q.push(3)

q.pop()

print(q.front())