def make_album(artist, title, num_tracks = ''):
    """Creates and returns a dictionary object with artist name, album title
    and optionally the number of tracks on the album"""
    # Create initial album
    album = {'artist': artist, 'title': title}
    # If num_tracks value present, add num_tracks to album
    if num_tracks:
        album['num_tracks'] = num_tracks
    # Return result
    return album

# Creating while loop to repeatedly Query user for album artist and title
# Explain program to user
explanation = (
    "We're gathering information on albums. We will continue to query you "
    "until you enter 'q' (case sensitie) in response to a request for "
    "information. To enter information type it on the keyboard and press"
    " enter. We will print the resulting dictionary object representing your"
    "album after every input of the album title"
    )
print(explanation)

# Now run while loop to query user for info
while True:
    # Query user for artist name
    artist = input("\nPlease input album artist (or 'q' to exit) ")
    # Check exit condition
    if artist == 'q':
        break
    # Query user for album title
    title = input("\nPlease input album title (or 'q' to exit) ")
    # Check exit condition
    if title == 'q':
        break
    # Creat and print album dict
    album = {'artist' : artist, 'title' : title}
    print("\nYour album is:")
    print(album)
# Print exit statement
print("\nFarewell!\n")