import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="school_management_system"
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Define DELETE queries
delete_queries = [
    """
    DELETE FROM level_category
    WHERE level_category_name = 'Beginner'
    """,
    """
    DELETE FROM faculty
    WHERE facultyname = 'John Doe'
    """
]

# Execute each DELETE query
for query in delete_queries:
    cursor.execute(query)

# Commit changes and close connection
conn.commit()
conn.close()
