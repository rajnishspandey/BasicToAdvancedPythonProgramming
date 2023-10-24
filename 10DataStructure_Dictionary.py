Dict = {1: 1,
        "key2": "2",
        "key3": [3, 3, 3],
        "key4": (4, 4, 4),
        ('key5'): 5,
        (0, 1): 6}  #Keys can only be strings, numbers, or tuples, but values can be any data type.
print(Dict)

#Access to the value by Key
print(Dict["key2"])

print(Dict[(0,1)])

#create a dictionary

release_year_dict = {"Thriller": "1982", "Back in Black": "1980", \
                    "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", \
                    "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", \
                    "Saturday Night Fever": "1977", "Rumours": "1977"}
print(release_year_dict)


print(release_year_dict[("Thriller")])

#get all the keys in dictionary

print(release_year_dict.keys())

#get all the values in the dictionary

print(release_year_dict.values())

#append a value with the key in dictionary

release_year_dict["Test Key"] ="Test Value"
print(release_year_dict)

#delete a entry from dictionary by key

del(release_year_dict["Test Key"])
print(release_year_dict)

#verify if the key is there in the Dictionary or not

print("Thriller" in release_year_dict)



