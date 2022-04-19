def word_zapper(words, allowed_chars, start_index=0):
    
    for i in range(start_index, len(words)):
        if words[i] is in allowed_chars:
            words