def make_album(name, album_name, count=None):
    album = {'singer_name': name, 'album_name': album_name}
    if count:
        album['count'] = count
    return album


print(make_album("jake", "test"))
print(make_album("jake", "test", 23))
