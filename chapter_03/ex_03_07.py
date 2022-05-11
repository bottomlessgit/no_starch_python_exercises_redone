guests = ["ada lovelace", "ada glovelace", "ada dovelace", "ada shovelace"]
message = "You are cordially invited to my fancy dinner,  "
print(message + guests[0].title())
print(message + guests[1].title())
print(message + guests[2].title())
print(message + guests[3].title())
print("Oh wait, we got a bigger table, now we can invite the rejects.")
guests.insert(0, "blayda bloodlace")
guests.insert(len(guests) // 2 , "raida roadrace")
guests.append("shayda mudshapes")
print(message + guests[0].title())
print(message + guests[1].title())
print(message + guests[2].title())
print(message + guests[3].title())
print(message + guests[4].title())
print(message + guests[5].title())
print(message + guests[6].title())
# Exercise 03_07 addition
print("Oh wait, the table broke, now we only have room for 2 guests.")
print(guests.pop().title() + ", you're uninvited, sorry.")
print(guests.pop().title() + ", you're uninvited, sorry.")
print(guests.pop().title() + ", you're uninvited, sorry.")
print(guests.pop().title() + ", you're uninvited, sorry.")
print(guests.pop().title() + ", you're uninvited, sorry.")
print(guests[0].title() + ", you're still invited.")
print(guests[1].title() + ", you're still invited.")
del guests[1]
del guests[0]
print(guests)