"""Demo of keyword arguments. """

def describe(name='Unknown', species='unkown creature', age='unkown'):
    """L"""
    template = '{} is a {}, age: {}.'
    print(template.format(name, species, age))


def main():
    """Test the describe function """
    describe(name='Angus', species='chipmunk')
    print(30 * '=')
    describe(species='human', name='Marina')
    print(30 * '=')
    describe(age='17')
    print(30 * '=')
    describe('Peter', 'penguin', 10)

main()