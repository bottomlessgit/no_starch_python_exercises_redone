favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

poll_takers = ['jen', 'sarah', 'edward', 'phil', 'garth', 'matt', "flo", "dirk"]

for person in poll_takers:
    if person in favorite_languages:
        print("Thanks for taking the poll", person + "!")
    else:
        print('Please take the poll', person + ".")