import queue

stack = queue.LifoQueue()

# it's a push operation
stack.put(10)
stack.put(20)
stack.put(30)

print(stack)

# it's a pop operation

stack.get()

print(stack)

#time out
stack = queue.LifoQueue(3)
stack.put(10)
stack.put(20)
stack.put(30)

stack.put(40,timeout=1)
#same we can use for get/pop


