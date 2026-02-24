class Album:
    def __init__(
        self,
        album_id, title,
        release_year, artist_id
            ):
        self.album_id = album_id
        self.title = title
        self.release_year = release_year
        self.artist_id = artist_id

    def __eq__(self, other):
        if not isinstance(other, Album):
            return False

        return (self.album_id == other.album_id  and 
                self.title == other.title and 
                self.artist_id == other.artist_id and 
                self.release_year == other.release_year)

    def __repr__(self):
        return f"""
        {self.album_id} {self.title} {self.release_year} {self.artist_id}
        """



