def build_car(manufacturer, model, **car_info):
    car = {}
    # Set manufacturer and model
    car['manufacturer'] = manufacturer
    car['model'] = model
    # Go through keyword arguments and set values to keys in dictionary
    for attribute, info in car_info.items():
        car[attribute] = info
    # Return car dictionary object
    return car

# Call function to demonstrate use
new_car = build_car(
    'ford',
    'prefect',
    year=1938,
    transmission='manual',
    color='red'
    )

print(new_car)