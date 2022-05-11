guests = ["ada lovelace", "ada glovelace", "ada dovelace", "ada shovelace"]
message = "You are cordially invited to my fancy dinner,  "
print(message + guests[0].title())
print(message + guests[1].title())
print(message + guests[2].title())
print(message + guests[3].title())
print(guests[2].title() + " can't make it :(\nWe'll have to invite someone new")
guests[2] = "ada oflace"
print(message + guests[0].title())
print(message + guests[1].title())
print(message + guests[2].title())
print(message + guests[3].title())