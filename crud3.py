import mysql.connector

# Function to create a connection to the MySQL database
def create_connection(host, user, password, database):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="",
            database="school_management"
        )
        print("Connected to MySQL database successfully.")
        return conn
    except mysql.connector.Error as e:
        print(e)
        return None

# Function to create tables if they don't exist
def create_tables(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS level (
            levelID INT AUTO_INCREMENT PRIMARY KEY,
            levelname VARCHAR(255) NOT NULL,
            FOREIGN KEY (level_categoryID) REFERENCES level_category(level_categoryID)

            description TEXT
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS level_category (
            level_categoryID INT AUTO_INCREMENT PRIMARY KEY,
            level_category_name VARCHAR(255) NOT NULL,
            description TEXT
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS faculty (
            facultyID INT AUTO_INCREMENT PRIMARY KEY,
            facultyname VARCHAR(255) NOT NULL,
            FOREIGN KEY (levelID) REFERENCES level(levelID)
            description TEXT
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS class (
        classID INT AUTO_INCREMENT PRIMARY KEY,
        classname VARCHAR(255),
        facultyID INT,
        FOREIGN KEY (facultyID) REFERENCES faculty(facultyID)
        )
        """)
        print("Tables created successfully.")
    except mysql.connector.Error as e:
        print(e)

# Function to insert data into level table
def insert_level(conn, name, description=None):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO level (levelID,level_name,level_categoryID ) VALUES (%s, %s,%s )", (id,name,lid))
        conn.commit()
        print("Level inserted successfully.")
    except mysql.connector.Error as e:
        print(e)

# Function to insert data into levelcategory table
def insert_level_category(conn, name, description=None):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO levelcategory (level_CategoryID, level_category_name) VALUES (%s, %s)", (name, description))
        conn.commit()
        print("Level category inserted successfully.")
    except mysql.connector.Error as e:
        print(e)

# Function to insert data into faculty table
def insert_faculty(conn, name, description=None):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO faculty (facultyID,facultyname,levelID ) VALUES (%s,%s, %s)", (id,name, level_id))
        conn.commit()
        print("Faculty inserted successfully.")
    except mysql.connector.Error as e:
        print(e)

# Function to insert data into class table
def insert_class(conn, name, level_id, category_id, faculty_id):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO class (name, level_id, category_id, faculty_id) VALUES (%s, %s, %s, %s)", (name, level_id, category_id, faculty_id))
        conn.commit()
        print("Class inserted successfully.")
    except mysql.connector.Error as e:
        print(e)

# Function to fetch all levels
def get_all_levels(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM level")
        rows = cursor.fetchall()
        return rows
    except mysql.connector.Error as e:
        print(e)

# Function to fetch all level categories
def get_all_level_categories(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM levelcategory")
        rows = cursor.fetchall()
        return rows
    except mysql.connector.Error as e:
        print(e)

# Function to fetch all faculties
def get_all_faculties(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM faculty")
        rows = cursor.fetchall()
        return rows
    except mysql.connector.Error as e:
        print(e)

# Function to fetch all classes
def get_all_classes(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM class")
        rows = cursor.fetchall()
        return rows
    except mysql.connector.Error as e:
        print(e)

# Function to delete a class by id
def delete_class(conn, classID):
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM class WHERE id=%s", (classID,))
        conn.commit()
        print("Class deleted successfully.")
    except mysql.connector.Error as e:
        print(e)

# Function to update a class name
def update_class_name(conn, classID, new_name):
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE class SET name=%s WHERE id=%s", (new_name, classID))
        conn.commit()
        print("Class name updated successfully.")
    except mysql.connector.Error as e:
        print(e)

# Function to update a class's level
def update_class_level(conn, classID, new_level_id):
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE class SET level_id=%s WHERE levelID=%s", (new_level_id, classID))
        conn.commit()
        print("Class level updated successfully.")
    except mysql.connector.Error as e:
        print(e)

# Function to update a class's category
def update_class_category(conn, classID, new_category_id):
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE class SET category_id=%s WHERE id=%s", (new_category_id, classID))
        conn.commit()
        print("Class category updated successfully.")
    except mysql.connector.Error as e:
        print(e)

# Function to update a class's faculty
def update_class_faculty(conn, class_id, new_faculty_id):
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE class SET faculty_id=%s WHERE id=%s", (new_faculty_id, class_id))
        conn.commit()
        print("Class faculty updated successfully.")
    except mysql.connector.Error as e:
        print(e)

# Main function
def main():
    host = 'localhost'
    user = 'your_username'
    password = 'your_password'
    database = 'your_database_name'
    
    conn = create_connection(host, user, password, database)

    if conn is not None:
        create_tables(conn)

        while True:
            print("\nChoose an operation:")
            print("1. Insert level")
            print("2. Insert level category")
            print("3. Insert faculty")
            print("4. Insert class")
            print("5. Delete class")
            print("6. Update class name")
            print("7. Update class level")
            print("8. Update class category")
            print("9. Update class faculty")
            print("10. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter level name: ")
                description = input("Enter level description: ")
                insert_level(conn, name, description)
            elif choice == "2":
                name = input("Enter level category name: ")
                description = input("Enter level category description: ")
                insert_level_category
