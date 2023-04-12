def make_album(name, album_name, count=None):
    album = {'singer_name': name, 'album_name': album_name}
    if count:
        album['count'] = count
    return album


while True:
    print("\nPlease tell me singer name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("singer name:")
    if f_name == 'q':
        break
    l_name = input("album_name:")
    if l_name == 'q':
        break

    print(make_album(f_name, l_name))
