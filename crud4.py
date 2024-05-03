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
            levelid INT AUTO_INCREMENT PRIMARY KEY,
            levelname VARCHAR(255) NOT NULL,
            description TEXT
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS levelcategory (
            categoryid INT AUTO_INCREMENT PRIMARY KEY,
            categoryname VARCHAR(255) NOT NULL,
            description TEXT
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS faculty (
            facultyid INT AUTO_INCREMENT PRIMARY KEY,
            facultyname VARCHAR(255) NOT NULL,
            levelid INT,
            FOREIGN KEY (levelid) REFERENCES level (levelid)
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS class (
            classid INT AUTO_INCREMENT PRIMARY KEY,
            classname VARCHAR(255) NOT NULL,
            levelid INT,
            facultyid INT,
            FOREIGN KEY (levelid) REFERENCES level (levelid),
            FOREIGN KEY (facultyid) REFERENCES faculty (facultyid)
        )
        """)
        print("Tables created successfully.")
    except mysql.connector.Error as e:
        print(e)

# Function to insert data into level table
def insert_level(conn, levelname, description=None):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO level (levelname, description) VALUES (%s, %s)", (levelname, description))
        conn.commit()
        print("Level inserted successfully.")
    except mysql.connector.Error as e:
        print(e)

# Function to insert data into levelcategory table
def insert_level_category(conn, categoryname, description=None):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO levelcategory (categoryname, description) VALUES (%s, %s)", (categoryname, description))
        conn.commit()
        print("Level category inserted successfully.")
    except mysql.connector.Error as e:
        print(e)

# Function to insert data into faculty table
def insert_faculty(conn, facultyname, levelid):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO faculty (facultyname, levelid) VALUES (%s, %s)", (facultyname, levelid))
        conn.commit()
        print("Faculty inserted successfully.")
    except mysql.connector.Error as e:
        print(e)

# Function to insert data into class table
def insert_class(conn, classname, levelid, facultyid):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO class (classname, levelid, facultyid) VALUES (%s, %s, %s)", (classname, levelid, facultyid))
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
def delete_class(conn, classid):
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM class WHERE classid=%s", (classid,))
        conn.commit()
        print("Class deleted successfully.")
    except mysql.connector.Error as e:
        print(e)

# Function to update a class name
def update_class_name(conn, classid, new_name):
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE class SET classname=%s WHERE classid=%s", (new_name, classid))
        conn.commit()
        print("Class name updated successfully.")
    except mysql.connector.Error as e:
        print(e)

# Function to update a class's level
def update_class_level(conn, classid, new_levelid):
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE class SET levelid=%s WHERE classid=%s", (new_levelid, classid))
        conn.commit()
        print("Class level updated successfully.")
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
            print("8. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                levelname = input("Enter level name: ")
                description = input("Enter level description: ")
                insert_level(conn, levelname, description)
            elif choice == "2":
                categoryname = input("Enter level category name: ")
                description = input("Enter level category description: ")
                insert_level_category(conn, categoryname, description)
            elif choice == "3":
                facultyname = input("Enter faculty name: ")
                levelid = int(input("Enter level ID: "))
                insert_faculty(conn, facultyname, levelid)
            elif choice == "4":
                classname = input("Enter class name: ")
                levelid = int(input("Enter level ID: "))
                facultyid = int(input("Enter faculty ID: "))
                insert_class(conn, classname, levelid, facultyid)
            elif choice == "5":
                classid = int(input("Enter class ID to delete: "))
                delete_class(conn, classid)
            elif choice == "6":
                classid = int(input("Enter class ID to update name: "))
                new_name = input("Enter new name: ")
                update_class_name(conn, classid, new_name)
            elif choice == "7":
                classid = int(input("Enter class"))






