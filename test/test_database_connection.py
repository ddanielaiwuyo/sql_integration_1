from lib.database_connection import DatabaseConnection


"""
Tests the database successfully 
exceutes the seed into the database
"""
def test_db_connection():
    conn = DatabaseConnection()
    conn.connect()
    conn.seed("seeds/test_seed.sql")

    response = conn.execute("SELECT * FROM users")
    expected_result = [
            {"user_id": 1, "name": "Tony Maguire"},
            {"user_id": 2, "name": "Eren Yeager"},
    ]


    assert response == expected_result

