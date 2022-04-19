def make_tags(tag, word):
    """L"""
    return "<{0}>{1}</{0}>".format(tag, word)
print(make_tags('i', 'Yay'))
