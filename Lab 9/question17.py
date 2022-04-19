def produce_index(words_on_page):
    """Takes a dictionary mapping from page number to a list of the unique words
    on that page and returns a dictionary that maps from a word to an ordered 
    list of pages on which that word appears"""
    
    inverted = {}
    pages = []
    for page, words in words_on_page.items():
        for word in words:
            if word in inverted:
                inverted[word].append(page)
            else:
                inverted[word] = list()
                inverted[word].append(page)
    return inverted

    
input_dict = {
   1: ['hi', 'there', 'fred'], 
   2: ['there', 'we', 'go'],
   3: ['fred', 'was', 'there']}
output_dict = produce_index(input_dict)
for word in sorted(output_dict.keys()):
    print(word + ': ' + str(output_dict[word]))