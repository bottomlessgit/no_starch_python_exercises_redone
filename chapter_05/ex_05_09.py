usernames = ["deerek", "horselina", "cowrlos", "gizelle", "admin", "rhyano"]
if usernames:
    for user in usernames:
        if user == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print("Welcome " + user.title() + "!")
else:
    print("We have to find some users!")