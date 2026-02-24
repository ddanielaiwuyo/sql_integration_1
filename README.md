### Integration Challenge 1




### Requirments
Make sure that `psql`, `git` and `python` are installed on your local system, I use homebrew
for most of my installations because is more convinient for me. Feel free to skip if you 
already have them configured

```bash
brew install postgres@15 # stable version

brew start services postgress@15 # runs the psql server


psql -h localhost -U postgres # opens psql terminal session

CREATE TABLE music_library;

# you can type Ctrl+D and that wil close the terminal session
```

### Clone Repository
```bash
git clone https://github.com/ddanielaiwuyo/sql_integration_1.git
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
            └── main.py      # python3 lib/main.py 

```


You can configure the sql queries in  `seeds/music_library.sql`


### Run Program


To run the program with ease please export
the current working directory to your python path
so you can run `lib/main.py` and pytest without 
changing import paths
Or simply reference this [stackoverflow safe solution](https://stackoverflow.com/questions/3402168/permanently-add-a-directory-to-pythonpath) 
that I use in most of my python projects.
```bash
chmod u+x add-to-path.sh
./add-to-path.sh
```


```bash
# creates a virtual environment and activates it
python3 -m env env && source env/bin/activate


# install packages and dependencies
pip install -r requirements.txt  

# run main program
python3 lib/main.py

# for tests
pytest
```
