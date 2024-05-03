import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="SMS"
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Define INSERT queries
insert_queries = [
    """
    INSERT INTO level_category (level_category_name) VALUES ('Primary'),
                                                         ('Secondary'),
                                                         ('Higher-Secondary')
    """,
    """
    INSERT INTO level (levelname, level_categoryID) VALUES ('Level 1', 1),
                                                          ('Level 2', 2),
                                                          ('Level 3', 3)
    """,
    """
    INSERT INTO faculty (facultyname, levelID) VALUES ('Teacher', 1),
                                                    ('Principal', 2),
                                                    ('HOD', 3)
    """,
    """
    INSERT INTO Class (classname, facultyID) VALUES ('Math', 1),
                                                 ('Physics', 2),
                                                 ('Biology', 3)
    """
]

# Execute each INSERT query
for query in insert_queries:
    cursor.execute(query)

# Commit changes and close connection
conn.commit()
conn.close()
