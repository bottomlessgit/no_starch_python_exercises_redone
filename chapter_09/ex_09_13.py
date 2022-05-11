# This code puts the defintions from ex_06_04 in an OrderedDict object
from collections import OrderedDict

definitions = OrderedDict()

definitions["if-statement"] = ("A statement that evaluates a boolean condition"
                               "and only runs that statement if the boolean "
                               "condition evaluates to true.")

definitions["else-statement"] = ("A companion statement to the if statement "
                                 "that only runs if the previous if-statement "
                                 "did not.")

definitions["for-loop"] = ("A looping command that performs a set of "
                           "instructions for every member of a container "
                           "object.")

definitions["list"] = ("An ordered data structure that keeps the order of it's "
                       "elements, allows indexed access to them, and is "
                       "mutable, i.e. elements can be added and reassigned "
                       "values.")

definitions["dictionary"] = ("An unordered and mutable data structure that "
                             "holds key-value pairs and allows acces to the "
                             "values using the keys as indices.")

definitions["variable"] = ("Holds a value and associates it with an identifier "
                           "that can be used as a reference to that value in "
                           "your code, and can be reassigned to "
                           "different values.")

definitions["string"] = ("An immutable data type that holds a string of "
                         "characters.")

definitions["integer"] = ("A mutable data type that holds a single integer "
                          "value, i.e. a whole negative or positive number.")

definitions["float"] = ("A mutable data type that holds a single decimal "
                        "number value.")

definitions["tuple"] = ("An immutable list, i.e. an ordered sequence of fixed "
                        "length, and whose elements that cannot be reassigned.")

# Now loop through keys and values and print them
print("Here are the definitions of some terms relevant to python:\n")
for word, definition in definitions.items():
    print(word  + ":\n" + definition + "\n")