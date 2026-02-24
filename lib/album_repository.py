from lib.album import Album

class AlbumRepository:
    def __init__(self, conn):
        self._conn = conn

    def all(self):
        query = "select * from albums"
        response = self._conn.execute(query)
        if response is None:
            return response

        albums = []
        for row in response:
            album = Album(row["album_id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(album)

        return albums

