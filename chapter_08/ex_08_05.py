def describe_city(city, country = "morocco"):
    """
    Prints a message stating which country a city is in 
    with Morrocco as a default value for country
    """
    print(city.title() + " is in " + country.title() + ".")

# Call function with and without default value
describe_city("casablanca")
describe_city("nador")
describe_city("daegu", "south korea")


