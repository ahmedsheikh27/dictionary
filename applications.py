text = "hello world hello python world"

words = text.split()

words_count = {}
for word in words:
    words_count[word] = words_count.get(word, 0) +1


print(words_count)

# Write a Python program to find the key with the maximum value in the diction
# val = {'a': 10, 'b': 15, 'c': 7}


