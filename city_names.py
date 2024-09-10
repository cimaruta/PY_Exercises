def city_country(city, country):
    """Gets the names of a city and its country"""
    city_and_country = f"{city}, {country}"
    print(city_and_country)
    return city_and_country.title()

city_country('las vegas', 'united states')
city_country('frankfurt', 'germany')
city_country('tokyo', 'japan')