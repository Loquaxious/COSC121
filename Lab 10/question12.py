class Thing:
    """Defines the Thing class
       Data Attributes: name of class str
                        height of class float
                        words of class list
    """
    
    def __init__(self, name, height, words):
        """Creates a new Thing object with the specified name, height and words"""
        self.name = name
        self.height = height
        self.words = words
    
    def taller_by(self, number=0):
        """Returns the increases height by a given value"""
        self.height += number

    def learn(self, word):
        """Adds a word to the words list"""
        self.words += word
        
    def __str__(self):
        """Returns a formatted string representation of the Thing 
        object"""
        template = "Hi. I'm {0}. I'm {1} cm tall.\nWords I know: {2}"
        name = self.name
        height = self.height
        words = self.words
        words_str = ''
        i = 0
        for word in words:
            if i < len(words) - 1:
                words_str += word + ', '
                i += 1
            else:
                words_str += word
        if words_str != '':
            return template.format(name, height, words_str + '.')
        else:
            return template.format(name, height, words_str)
            
    
        
                

thing = Thing("Pedro", 177, ["fiddle", "faddle", "foodle"])
print(thing)
thing.taller_by(23)
thing.learn(['grunt'])
print(thing)

another = Thing("Donald", 40, ["quack", "quack"])
print(another)
another.taller_by(1)
another.learn(['quack'])
print(another)

him = Thing("Bubba", 70, [])
print(him)
him.learn(['Mama'])
print(him)