"""
1- tupple  ()  -- immutable
2 - List   [] -- mutable
3 - Dictionary  {} -- mutable
"""

#create a tuple

Tuple = (1,2,3,4)
print(Tuple)

#Find the first two elements of tuple
chr = Tuple[0:2]
print(chr)
print(type(chr))

print(Tuple[-1])

print(type(Tuple))

#concatination using tuple

Tuple2 = Tuple + ("Testing String",5,6,)
print(Tuple2)

#slicing

print(Tuple2[2:5])
print(Tuple2[2:5:2])

print(len(Tuple2))

#sorting

numbers = (1,3,4,5,6,3,2,1,0,10,12,4,15,34,20)
print(numbers)

print(sorted(numbers)) #output will be in the form of list

#nested Tuple

Tuple3 = (Tuple, Tuple2,(4,5,6,7,(1,2,3)))
print(Tuple3)


#indexing on Nested Tuple

print('Element 0 of Tuple :',Tuple3[0])
print('Element 2 of Tuple :',Tuple3[2])
print('Element 0, 0 of Tuple :',Tuple3[0][2])
print('Element 2, 2 of Tuple :',Tuple3[2][2])
print('Element 2, 4,1 of Tuple :',Tuple3[2][4][1])

#find the index of element
element = ("Hello","It's me","can you hear me")
print("Index of element :",element.index("It's me"))

