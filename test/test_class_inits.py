from lib.artist import Artist
from lib.album import Album

def test_artist_init():
    artist = Artist(1, "Bill Evans", "Jazz",)
    assert artist.artist_id == 1
    assert artist.name == "Bill Evans"
    assert artist.genre == "Jazz"

def test_album_init():
    album = Album(1, "Metaphorical Soul", "2001-02-11", 2)
    assert album.album_id == 1
    assert album.title == "Metaphorical Soul"
    assert album.artist_id == 2
