# Function to be tested using the unittest module

def get_location_name(city, country):
    """Generates a conventionally formatted city name"""
    full_location_name = city + ", " + country
    return full_location_name.title()
