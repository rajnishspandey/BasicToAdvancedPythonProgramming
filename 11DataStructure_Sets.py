#creating a set
set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
print(set1)

#convert list to set
album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19", \
              "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)
print(album_set)

#or

music_genres = set(["pop", "pop", "rock", "folk rock", "hard rock", "soul", \
                    "progressive rock", "soft rock", "R&B", "disco"])

print(music_genres)

#operations
A = set(["Thriller", "Back in Black", "AC/DC"])
print(A)

#add element to set

A.add("Testing add in set")
print(A)

#remove from set
A.remove("Testing add in set")
print(A)

#verification

print("Thriller" in A)

if "Thriller" in A:
    print("Found Thriller in set A")


#logic operations
album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])
print(album_set1)
print(album_set2)

#intersection (common in both)
c = album_set1&album_set2
print("this is intersection of the sets :",c)

#or
print("this is also a intersection of the sets : ",album_set1.intersection(album_set2))


#find the difference
D = album_set2.difference(album_set1)
print("differences : ", D)

D = album_set1.difference(album_set2)
print("differences : ", D)

#union

print("this is union : ",album_set1.union(album_set2))


# Check if superset

print(set(album_set1).issuperset(album_set2))
print(set(album_set2).issuperset(album_set1))

print(set(album_set1).issubset(album_set2))
print(set(album_set2).issubset(album_set1))

print(set({"Back in Black", "AC/DC"}).issubset(album_set1))
print(album_set2.issuperset({"The Dark Side of the Moon"}))


#sum

A = [1, 2, 2, 1]
B = set([1, 2, 2, 1])
print(B)

print(sum(A))
print(sum(B))
c = sum(A)+sum(B)
print(c)

#clear

B.clear()
print(B)

#copy
B=set(A)
print(B)

C = B.copy()
print(C)
C.add("Test")
print(C)

#empty set
print(set())

#discard
print(C)
C.discard("Test") #if element not found it will ignore #C.remove("10") - if element not found it will give error
print(C)

#pop
C.pop()
print(C)

#update
C.update(["Testing Update"], "Testing")
print(C)