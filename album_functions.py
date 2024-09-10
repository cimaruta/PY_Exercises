def make_album(artist, album):
    """Formats user input"""
    fav_albums = {
        'artist': artist,
        'album': album,
        }
    return fav_albums

while True:
    print("Please tell me your favorite artist, followed by your favorite album from that artist")
    print("Type 'q' at any time to exit the program")

    user_artist = input("Artist: ")
    if user_artist == 'q':
        break

    user_album = input("Album: ")
    if user_album == 'q':
        break
    user_fav = make_album(user_artist, user_album)
    print(user_fav)