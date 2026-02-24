from artist import Artist

class ArtistRepository:
    def __init__(self, conn):
        self._conn = conn

    def all(self):
        query = "select * from artists"
        response = self._conn.execute(query)
        if response is None:
            return response

        artists = []
        for row in response:
            artist = Artist(row["artist_id"], row["name"], row["genre"])
            artists.append(artist)

        return artists
