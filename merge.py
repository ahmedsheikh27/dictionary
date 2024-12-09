dict1 = {'a': 1, 'b': 2}  
# dict2 = {'a': 1, 'b': 3}  #printing false on change value to 3 
dict2 = {'a': 1, 'b': 2}   

# adding dict2 to dict1 

# dict1.update(dict2)
# print(f'{dict1}')

# next question

# checking 2 dict are equal 
onekey = dict1.items()
seckey = dict2.items()
if onekey == seckey:
    print('True')
else:
    print('False')
