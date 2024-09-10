def car_info(manufacturer, model, **info):
    info['manufacturer'] = manufacturer
    info['model'] = model
    return info



car = car_info('toyota', 'prius',
               color='black',
               mileage='150,000')

print(car)