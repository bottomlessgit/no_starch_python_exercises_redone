opening_messsage = ("We're taking a poll on where in the world people "
                    "want to go, for which people will input their name, "
                    "and where they'd like to go.\n")
print(opening_messsage)

poll = {}
poll_active = True
while poll_active:
    name = input("\n\nWhat is your name? ")
    place = input("\nWhat one place in the world would you like to visit? ")
    poll[name] = place
    new_user_check = input("\nAre there any more people who want to take the" 
                           "poll? Input 'yes' and press enter to continue, or " 
                           "anything else to exit. ")
    if new_user_check != "yes":
        poll_active = False

print("\n\nThe results of our poll are:")
for name, place in poll.items():
    print("\t" + name.title() + " wants to go to " + place.title())


