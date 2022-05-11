# Function to be tested using the unittest module

def get_location_name(city, country, population = ""):
    """Generates a conventionally formatted city name"""
    full_location_name = city + ", " + country
    if population:
        full_location_name += " - " + str(population)
    return full_location_name.title()
