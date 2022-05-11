person = {
    "first_name" : "mary",
    "last_name" : "wollstonecraft",
    "country_of_origin" : "britain",
    "date_of_birth" : "04-27-1759",
}
for attribute in person:
    print(attribute.title(), "is", person[attribute].title())