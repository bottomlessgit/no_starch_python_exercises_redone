def count_words_in_file(word, filename):
    """Counts and returns number of instances of word in a text file
    NOTE: doesn't recognize instances of words not separated from punctuation
    by a space"""
    with open(filename) as file:
        return file.read().lower().count(word)


def announce_count_in_file(word, filename):
    """Prints count of given word in file and announces it
    Or catches the exception if file can't be found and announces failure"""
    try:
        # This function may throw an exception if file cannot be found
        instance_count = count_words_in_file(word, filename)
    except FileNotFoundError:
        print(filename + " cannot be found.")
    else:
        print(word + " is found in " + filename + " " + str(instance_count) 
              + " times.")
    

announce_count_in_file("the", "pride_and_prejudice.txt")
announce_count_in_file("the", "metamorphosis.txt")
announce_count_in_file("the", "the_souls_of_black_folk.txt")