people = []

person = {
    'first': 'aaron',
    'last': 'johnson',
    'age': 30,
    'city': 'vegas'
    }
people.append(person)

person = {
    'first': 'tam',
    'last': 'bui',
    'age': 29,
    'city': 'new york'
    }
people.append(person)

person = {
    'first': 'sam',
    'last': 'alberts',
    'age': 27,
    'city': 'vegas'
    }
people.append(person)

for person in people:
    name = f"{person['first']} {person['last']}"
    age = person['age']
    city = person['city']
    print(f'{name.title()} is {age} years old, and lives in {city}')