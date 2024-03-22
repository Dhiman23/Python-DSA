list = [1,2,3,4]  #list are mutable 
list.append(4)
print(list)

#tuple 
tuple = (1,2,3,4)
print (tuple)
tuple = (1,2,3,4,4)

tuple.append(10) # this will not work because this is immutable 
print(tuple)
