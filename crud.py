import mysql.connector

def connect_to_mysql():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="SMS"
    )

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
    while True:
        print("1. Insert data\n2. Update data\n3. Delete data\n4. Exit")
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
