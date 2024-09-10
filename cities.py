cities = {
    'las vegas': {
        'country': 'the united states',
        'population': '675,000',
        'fact': 'Home to more than half of the largest 20 hotels in the world by room count.',
        },
    'frankfurt': {
        'country': 'germany',
        'population':'764,000',
        'fact': 'One of the worlds leading financial centers and is home to the European Central Bank.',
        },
    'tokyo': {
        'country': 'japan',
        'population': '14,000,000',
        'fact': 'Home to the busiest train station in the world, Shinjuku Station.',},
    }
for city, info in cities.items():
    country = info['country']
    population = info['population']
    fact = info['fact']
    print(f'\n{city.title()} belongs to the country of {country.title()}.')
    print(f'{city.title()} has a population of {population}.')
    print(f'Here is an interesting fact about {city.title()}:')
    print(fact)