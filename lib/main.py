import traceback
from artist_repository import ArtistRepository
from artist import Artist
from album_repository import AlbumRepository
from database_connection import DatabaseConnection

SEED_PATH = "seeds/music_library.sql"

def main():
    try:
        conn = DatabaseConnection()
        conn.connect()
        conn.seed(SEED_PATH)

        artist_repo = ArtistRepository(conn)
        artists = artist_repo.all()
        print("\n    ALL ARTISTS    \n")
        print(f"  {'ID':<5} {'NAME':<15} {'GENRE':<15}")
        for artist in artists:
            print(f"  {artist.artist_id:<5} {artist.name:<15}  {artist.genre:<15}")
            # print(artist.artist_id, artist.name, artist.genre)


        album_repo = AlbumRepository(conn)
        all_albums = album_repo.all()
        print("\n      ALL ALBUMS   \n")
        print(f"  {'ID':<5} {'TITLE':<25} {'RELEASE-YEAR':<15}")
        for album in all_albums:
            print(f"  {album.album_id:<5} {album.title:<25} {album.release_year}" )

    except Exception as e:
        print(" [main] database error frmo pyscopg")
        traceback.print_exc()

if __name__ == "__main__":
    main()
