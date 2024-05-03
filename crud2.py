import mysql.connector

def connect_to_mysql():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="SMS"
    )

def execute_queries(conn, queries):
    cursor = conn.cursor()
    for query in queries:
        cursor.execute(query)
    conn.commit()
    cursor.close()

def insert_queries(conn):
    insert_queries = [
        """
        INSERT INTO level_category (level_category_name) VALUES ('Beginner'),
                                                             ('Intermediate'),
                                                             ('Advanced')
        """,
        """
        INSERT INTO level (levelname, level_categoryID) VALUES ('Level 1', 1),
                                                              ('Level 2', 2),
                                                              ('Level 3', 3)
        """,
        """
        INSERT INTO faculty (facultyname, levelID) VALUES ('John Doe', 1),
                                                        ('Jane Smith', 2),
                                                        ('David Johnson', 3)
        """,
        """
        INSERT INTO Class (classname, facultyID) VALUES ('Math', 1),
                                                       ('Physics', 2),
                                                       ('Biology', 3)
        """
    ]
    execute_queries(conn, insert_queries)
    print("Data inserted successfully.")

def update_queries(conn):
    update_queries = [
        """
        UPDATE level_category
        SET level_category_name = 'Novice'
        WHERE level_category_name = 'Beginner'
        """,
        """
        UPDATE faculty
        SET facultyname = 'Ram Bahadur'
        WHERE facultyname = 'John Doe'
        """
    ]
    execute_queries(conn, update_queries)
    print("Data updated successfully.")

def delete_queries(conn):
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
    execute_queries(conn, delete_queries)
    print("Data deleted successfully.")

def main():
    conn = connect_to_mysql()

    create_table_queries = [
        """
        CREATE TABLE IF NOT EXISTS level_category (
            level_categoryID INT AUTO_INCREMENT PRIMARY KEY,
            level_category_name VARCHAR(255)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS level (
            levelID INT AUTO_INCREMENT PRIMARY KEY,
            levelname VARCHAR(255),
            level_categoryID INT,
            FOREIGN KEY (level_categoryID) REFERENCES level_category(level_categoryID)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS faculty (
            facultyID INT AUTO_INCREMENT PRIMARY KEY,
            facultyname VARCHAR(255),
            levelID INT,
            FOREIGN KEY (levelID) REFERENCES level(levelID)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS Class (
            classID INT AUTO_INCREMENT PRIMARY KEY,
            classname VARCHAR(255),
            facultyID INT,
            FOREIGN KEY (facultyID) REFERENCES faculty(facultyID)
        )
        """
    ]

    execute_queries(conn, create_table_queries)

    while True:
        print("\n1. Insert data\n2. Update data\n3. Delete data\n4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            insert_queries(conn)
        elif choice == '2':
            update_queries(conn)
        elif choice == '3':
            delete_queries(conn)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

    conn.close()

if __name__ == "__main__":
    main()
