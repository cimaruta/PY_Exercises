def describe_city(city, country="the united states"):
    """Describes a city"""
    print(f'{city.title()} is in {country.title()}')
describe_city('las vegas')
describe_city('los angeles')
describe_city('frankfurt', country='germany')