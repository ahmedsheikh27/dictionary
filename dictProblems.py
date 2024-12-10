# Given two dictionaries , write a Python program to add the values of matching keys and print the result.
# def addDict(dictionary, key):
#     return dictionary.add(key)

# dict1 = {'a': 5, 'b': 10}
# dict2 = {'a': 3, 'b': 7}
# result = {key:dict1[key] + dict2.get(key,0) for key in dict1}
# print(result)


# 27Write a Python program to create a dictionary where the keys are the first n positive integers, and the values are their cubes. Take n as user input.
# n = int(input("Enter a positive num: "))
# if n > 0:
#     cube = {i: i**3 for i in range(1, n + 1)}

#     print(cube)
# else:
#     print("Please enter positive num")

# Flatten the following nested dictionary into a single-level dictionary:
nested_dict = {'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': 4}} 

flattenDic = {}

for key, val in nested_dict.items():
    for fkey, value in val.items():
        flattenDic[f'{key}.{fkey}'] = value



print(flattenDic)

