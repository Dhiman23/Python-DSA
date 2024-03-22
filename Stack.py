# Push

stack = []
stack.append(10)
stack.append(20)
print(stack)

#pop
stack.pop()
print(stack)

def check(stack):
  if len(stack) == 0 :
     print ("stack is empty")
     print(stack)
print("check") 
print(check(stack))
 
stack.append(10)
stack.append(20)
stack[-1]
print(stack)
 
