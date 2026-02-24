### Integration Challenge 1


To run the program with ease please export
the current working directory to your python path
so you can run `lib/main.py` and pytest without 
changing import paths


```bash
chmod u+x add-to-path.sh
./add-to-path.sh
```


### Requirments
Make Sure that `psql` is installed on your local system, I use homebrew
for the installation because is more convinient for me.

```bash
brew install postgres@15 # stable version

brew start services postgress@15 # runs the psql server


psql -h localhost -U postgres # opens psql terminal session

CREATE TABLE music_library;

# you can type Ctrl+D and that wil close the termianl session
```


### Folder Structure
```
            lib
            ├── __init__.py
            ├── album.py
            ├── album_repository.py
            ├── artist.py
            ├── artist_repository.py
            ├── database_connection.py
            └── main.py # python3 lib/main.py 

```


You can confiure the sql queries in  `seeds/music_library.sql`
