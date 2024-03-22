stack =[]
def push():
    element = input("Enter the element")
    stack.append(element)
    print(stack)
def pop():
    if not stack:
        print("stack is empty")
    else:
        e = stack.pop()
        print("removed element:",e)
        print(stack)
while True:
    print ("select the operation 1.push 2.pop 3.quit")
    chocie = int(input())
    if chocie==1:
        push()
    elif chocie == 2:
        pop()
    else:
        print("Enter the correct operation")