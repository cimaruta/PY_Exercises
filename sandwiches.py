def sandwich(*toppings):
    #lists toppings on a sandich
    print('You have ordered the following toppings for your sandwich:')
    for topping in toppings:
        print(f' {topping.title()}')

sandwich('lettuce', 'tomato', 'bacon', 'avocado',)
sandwich('ham', 'cheese', 'onion', 'mustard',)
sandwich('turkey', 'spinach', 'pickles', 'mayo',)