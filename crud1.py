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

def insert_data(conn):
    cursor = conn.cursor()
    level_category_name = input("Enter level category name: ")
    query = f"INSERT INTO level_category (level_category_name) VALUES ('{level_category_name}')"
    cursor.execute(query)
    conn.commit()
    print("Data inserted successfully.")

def update_data(conn):
    cursor = conn.cursor()
    facultyname = input("Enter the faculty name to update: ")
    new_facultyname = input("Enter the new faculty name: ")
    query = f"UPDATE faculty SET facultyname = '{new_facultyname}' WHERE facultyname = '{facultyname}'"
    cursor.execute(query)
    conn.commit()
    print("Data updated successfully.")

def delete_data(conn):
    cursor = conn.cursor()
    level_category_name = input("Enter the level category name to delete: ")
    query = f"DELETE FROM level_category WHERE level_category_name = '{level_category_name}'"
    cursor.execute(query)
    conn.commit()
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
            insert_data(conn)
        elif choice == '2':
            update_data(conn)
        elif choice == '3':
            delete_data(conn)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

    conn.close()

if __name__ == "__main__":
    main()
