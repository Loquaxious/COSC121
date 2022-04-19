def glue_small(sentence):
    """F"""
    string = ""
    slist = sentence.split()
    for word in slist:
        if len(word) < 4:
            string += word + " "
    return string.rstrip()

sentence = "One two buckle my shoe"
print(glue_small(sentence))

sentence = "I am the king"
glued = glue_small(sentence)
print("|{}|".format(glued))