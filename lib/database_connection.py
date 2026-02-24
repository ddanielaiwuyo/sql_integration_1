import traceback
import psycopg
import os
from lib.artist import Artist
from psycopg.rows import dict_row

class DatabaseConnection:
    database = "music_library"
    conn_string = f"postgresql://localhost/{database}"
    def connect(self):
        self.connection = psycopg.connect(self.conn_string, row_factory=dict_row)

    def seed(self, path):
        if not os.path.exists(path):
            raise Exception("Could not find file ", path)
        seed = ""
        with open(path, "r") as f:
            seed = f.read()

        self._check_connection()
        with self.connection.cursor() as cursor:
            cursor.execute(seed)
            self.connection.commit()


    def execute(self, query, params=None):
        if params is None:
            params = []

        self._check_connection()
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            if cursor.description is not None:

                result = cursor.fetchall()
            else:
                result = None

            print(cursor.statusmessage)
            self.connection.commit()
            return result

    def _check_connection(self):
        if self.connection is None:
            raise Exception("Connection to db is null or closed")



def test_run():
    try:
        conn = DatabaseConnection()
        conn.connect()
        conn.seed("seeds/music_library.sql")
        res = conn.execute("""select * from artists;""")
        if res is None:
            return
        
        artists = []
        for row in res:
            artist = Artist(row["artist_id"], row["name"], row["genre"])
            artists.append(artist)

        print("\n ====== TEST-ARTISTS ======= ")
        for artist in artists:
            print(artist.artist_id, artist.name, artist.genre)

    except psycopg.OperationalError as e:
        print(" [main] operational err on db")
        traceback.print_exc()

    except Exception as e:
        print(" [main] unexpected error occured")
        traceback.print_exc()

if __name__ == "__main__":
    test_run()
