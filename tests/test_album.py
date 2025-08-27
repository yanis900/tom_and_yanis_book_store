from lib.album import Album

def test_album_constructs():
    album = Album(1, 'Test Song', 2025, 2)
    assert album.id == 1
    assert album.title == 'Test Song'
    assert album.release_year == 2025
    assert album.artist_id == 2
    
def test_albums_format_nicely():
    album = Album(1, 'Test Song', 2025, 2)
    assert str(album) == "Album(1, Test Song, 2025, 2)"

def test_albums_are_equal():
    album1 = Album(1, 'Test Song', 2025, 2)
    album2 = Album(1, 'Test Song', 2025, 2)
    assert album1 == album2
    