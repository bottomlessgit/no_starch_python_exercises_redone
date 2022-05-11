current_users = ["deerek", "horselina", "cowrlos", "gizelle", "admin", "rhyano"]
new_users = ["dolphineas", "whaleand", "horselina", "deerek", "cattleina"]
for new_user in new_users:
    if new_user.lower() in current_users:
        print("Username", new_user, 
             " is not available. Please choose a new username.")
    else:
        print("Username", new_user, "is available.")