rivers = {
    'nile': 'egypt',
    'mississippi': 'the united States',
    'yangtze': 'china',
}
for river, place in rivers.items():
    print(f'\nThe {river.title()} river runs through {place.title()}.')

print('\nHere are the rivers in this data set:')
for river in rivers.keys():
    print(f'\n-{river.title()}')

print('\nHere are the places in this data set:')
for place in rivers.values():
    print(f'\n-{place.title()}')