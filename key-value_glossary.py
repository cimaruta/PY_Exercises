glossary = {
    'variable': 'A name that holds a value',
    'function': 'A block of resusable code that performs a Task',
    'loop': 'A way to repeat a block of code multiple times',
    'list': 'A collection of items that are ordered and changeable',
    'string': 'A sequence of characters enclosed in quotes',
}
glossary['boolean expression'] = 'An expression used in programming languages that produces a true or false value'
for word, definition in glossary.items():
    print(f'\nThe definition of {word.title()} is:\n{definition}.')
print('\nHere are some other words and their definitions')