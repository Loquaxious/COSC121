word_freq = {"this": 4, "is": 2, "a": 3, "question": 1}

# Indexs the 1 on list then 1 in tuple
print(list(word_freq.items())[1][1]) 
# Indexs "question": 1 then adds 1 to the value which is 1 therefore 2
print(sorted(word_freq.items())[2][1] + 1)  
# gets all the values and indexs "a"s value therefore 3
print(sorted(word_freq.values())[2])
# value of a - value of question therefore 2
print(word_freq["a"] - word_freq["question"])
