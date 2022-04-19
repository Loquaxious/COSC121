def char_freqs(input_str):
    """L"""
    
    freq = {}
    for char in list(input_str):
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1
    return freq
            
count_dict = char_freqs("aaAA BbBb cC Dd ee f")
for char, count in sorted(count_dict.items()):
    print(repr(char),'->', count)