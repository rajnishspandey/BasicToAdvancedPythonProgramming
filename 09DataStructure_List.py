List = ['a','b','c']
print(List)

#Find the first two elements of the list 
print(List[0:2])
#Change the first element of the list to an uppercase 
print(List[0].upper())


#slicing

print(List[1])

List2 = ["Jordan","Java","Python","C++"]
List3 = ["Aadm", "Gilchrist","Mathew", "Haden",List]
List4 = [List,List2,List3,]
print(List4)
print(List4[1][2])


#extend

List4.extend(["Pop",10]) #extend adds new item in the list element
print(List4)

#append
List4.append(["Append Pop",10])  #append adds new element as a new nested list
print(List4)

#change the elemenet based on the index
List4[0] = 'Changed the element'
print(List4)

#delete the element based on the index
del(List4[0])
print(List4)

#split
print("Hello World".split()) #be default it splits by SPace

print(("Hello, How are you?").split(","))


#copy and reference

NewList = [1,2,3,4,5,6,7,]
NewList2 = NewList
print(NewList)
print(NewList2)

#insert
NewList2.insert(1,"Inerted New Element")
print(NewList2)

#reverse
NewList2.reverse()
print(NewList)

#sort
a = [2,3,4,5,6,7]
a.sort()
print(a)

a.sort(reverse=True)
print(a)
