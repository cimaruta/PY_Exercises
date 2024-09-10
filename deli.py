sandwich_orders = ['blt', 'grilled_cheese', 'club', 'reuben', 'italian']
finished_sandwiches = []
while sandwich_orders:
    order = sandwich_orders.pop()
    print(f'\nYour {order.title()}, is ready.')

    finished_sandwiches.append(order)

print('\nThe current sandwich orders have been filled.')
for sandwich in finished_sandwiches:
    print(f'- {sandwich.title()}')