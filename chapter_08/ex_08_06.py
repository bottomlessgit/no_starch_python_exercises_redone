def city_names(city, country):
    """
    Takes name of city and country and returns string of them combined and
    formatted. E.G: city_names('caracas', 'venezuela') => 'Caracas, Venezuela'
    """
    formatted_location =  city.title() + ", " + country.title()
    return formatted_location
# Calls and prints result function to test it
print(city_names("santiago","chile"))
print(city_names("london","england"))
print(city_names("cape town","south africa"))
