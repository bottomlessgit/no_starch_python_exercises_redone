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

# Now calling function and printing result to demonstrate functionality
print(make_album('kate bush', 'the kick inside'))
print(make_album('the jimi hendrix experience', 'are you experienced'))
print(make_album('miles davis', 'kind of blue'))

# Now calling with num_tracks value present
print(make_album('ann peebles', "i can't stand the rain", 10))
print(make_album('kendrick lamar', 'untitled unmastered', 8))
print(make_album('amy winehouse', 'back to black', 11))