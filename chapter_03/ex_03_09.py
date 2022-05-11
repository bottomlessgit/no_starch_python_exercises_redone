# Taken from ex_03_04
guests = ["ada lovelace", "ada glovelace", "ada dovelace", "ada shovelace"]
message = "You are cordially invited to my fancy dinner,  "
print(message + guests[0].title())
print(message + guests[1].title())
print(message + guests[2].title())
print(message + guests[3].title())
# Message added using len()
print("We have invited " + str(len(guests)) + " guests.")