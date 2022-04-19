def make_out_word(out, word):
    """L"""
    n = len(out) / 2
    
    return out[:int(n)] + word + out[int(n):]

print(make_out_word('<<>>', 'Yay'))
