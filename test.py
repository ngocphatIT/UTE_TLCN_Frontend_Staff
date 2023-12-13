import sqlite3

# Connect to the database
connection = sqlite3.connect("session.db")

# Create a cursor object
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  email TEXT UNIQUE
);
""")
cursor.execute("""
INSERT INTO users (name, email)
VALUES ("John Doe", "johndoe@example.com");
""")

# Commit the changes to the database
connection.commit()
# Select all users from the table
cursor.execute("SELECT * FROM users")

# Fetch all rows as a list of tuples
users = cursor.fetchall()

# Print the first user's name
print(users[0][1])
cursor.execute("""
UPDATE users SET email = "john.doe@example.com" WHERE id = 1;
""")

# Commit the changes
connection.commit()