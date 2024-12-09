dict1 = {'a': 1, 'b': 2}  
dict2 = {'a': 1, 'b': 9}   

# dict1.update(dict2)
# print(f'{dict1}')

# next question
onekey = dict1.items()
seckey = dict2.items()
if onekey == seckey:
    print('True')
else:
    print('False')
