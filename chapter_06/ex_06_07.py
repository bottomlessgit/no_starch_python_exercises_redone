m_wollstonecraft = {
    "first_name" : "mary",
    "last_name" : "wollstonecraft",
    "country_of_birth" : "britain",
    "date_of_birth" : "04-27-1759",
}

a_einstein = {
    "first_name" : "albert",
    "last_name" : "einstein",
    "country_of_birth" : "germany",
    "date_of_birth" : "03-14-1879",
}

n_mandela = {
    "first_name" : "nelson",
    "last_name" : "mandela",
    "country_of_birth" : "south africa",
    "date_of_birth" : "07-18-1918",
}

people = [m_wollstonecraft, a_einstein, n_mandela]

for person in people:
    for attribute_name, attribute in person.items():
        print(attribute_name.title(), "is", attribute.title())
    print()
