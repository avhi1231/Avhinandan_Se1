import sqlite3

def create_connection(db_name):
    """Create a connection to the SQLite3 database."""
    conn = sqlite3.connect(db_name)
    return conn

def create_table(conn):
    """Create a table if it does not exist."""
    query = '''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL
              );'''
    conn.execute(query)
    conn.commit()

def insert_data(conn, name, age):
    """Insert data into the table."""
    query = '''INSERT INTO users (name, age) VALUES (?, ?)'''
    conn.execute(query, (name, age))
    conn.commit()

def fetch_data(conn):
    """Fetch all data from the table."""
    query = '''SELECT * FROM users'''
    cursor = conn.execute(query)
    for row in cursor:
        print(row)

def main():
    db_name = "example.db"
    conn = create_connection(db_name)
    create_table(conn)
    
    # Insert some sample data
    insert_data(conn, "Abhinandan", 24)
    insert_data(conn, "Rahul", 30)
    insert_data(conn, "Sonu", 22)
    
    print("Data in the users table:")
    fetch_data(conn)
    
    conn.close()

if __name__ == "__main__":
    main()