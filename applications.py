# text = "hello world hello python world"

# words = text.split()

# words_count = {}
# for word in words:
#     words_count[word] = words_count.get(word, 0) +1


# print(words_count)

# Write a Python program to find the key with the maximum value in the diction
# val = {'a': 10, 'b': 15, 'c': 7}
# max_val = max(val, key=val.get)
# print(max_val)


# Maping square
# sq = { x:x**2 
#       for x in range(1,6)
# }
# print(sq)



# Write a Python program to remove duplicate values from the dictionary 
# duplicate = {'a': 10, 'b': 15, 'c': 10, 'd': 15}
# new_dict = {}
# new_val =set()

# for key, value in duplicate.items():
#     if value not in new_val:
#         new_dict[key] = value
#         new_val.add(value)

# print('old doubled values dic: ',duplicate)
# print('new single value dic: ',new_dict)

#25 Write a Python function that accepts a dictionary and a key, and returns the value associated with the key. If the key doesn’t exist, return "Key not found".
def keyValue(dictionary, key):
    return dictionary.get(key, 'key not found')
person = {
    "Name": "John",
    "Age": 30,
    "Address": {
        "Street": "123 Elm St",
        "City": "Boston",
        "Phone":"123-456-7890"
    }
}

key = input('Enter a key: ')

value = keyValue(person,key)
print(value)