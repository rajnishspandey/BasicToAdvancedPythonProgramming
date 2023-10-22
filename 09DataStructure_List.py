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

extended = List.extend([1])
print(extended)

