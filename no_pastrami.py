sandwich_orders = ['blt', 'pastrami', 'grilled_cheese', 'club', 'pastrami', 'reuben', 'italian', 'pastrami',]
finished_sandwiches = []
print('Sorry, we have run out of pastrami')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    order = sandwich_orders.pop()
    print(f'\nYour {order.title()}, is ready.')

    finished_sandwiches.append(order)

print('\nThe current sandwich orders have been filled.')
for sandwich in finished_sandwiches:
    print(f'- {sandwich.title()}')