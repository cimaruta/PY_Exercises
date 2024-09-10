favorite_places = {
    'aaron': ['ca', 'maui', 'nevada',],
    'mari': ['korea', 'seattle', 'japan',],
    'tam': ['nyc', 'germany', 'france',],
    }
for names, places in favorite_places.items():
    print(f"\n{names.title()}'s favorite places are:")
    for place in places:
        print(f'- {place.title()}')