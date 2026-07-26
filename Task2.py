import mysql.connector #Make sure to install the library
from mysql.connector import Error


DB_CONFIG = {
    "host": "localhost",
    "user": "root",       
    "password": "useradmin@100", #Kindly change the password as per your MySQL password
    "database": "ibm_z_summit"
}

def get_connection():
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except Error as err:
        print(f"Database Error: {err}")
        return None

def init_db():
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS attendees (
                id INT AUTO_INCREMENT PRIMARY KEY,
                full_name VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                college VARCHAR(100) NOT NULL,
                track VARCHAR(50) NOT NULL
            )
        """)
        conn.commit()
        cursor.close()
        conn.close()

def register_attendee():
    print("\n--- New Registration ---")
    name = input("Enter Full Name: ").strip()
    email = input("Enter Email: ").strip()
    college = input("Enter College Name: ").strip()
    track = input("Enter Track (e.g., Hackathon/Workshop): ").strip()

    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO attendees (full_name, email, college, track) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (name, email, college, track))
            conn.commit()
            print("Attendee registered successfully!")
        except Error as err:
            print(f"Failed to register: {err}")
        finally:
            cursor.close()
            conn.close()

def display_attendees():
    print("\n--- All Registered Attendees ---")
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, full_name, email, college, track FROM attendees")
        records = cursor.fetchall()
        
        if not records:
            print("No registrations found.")
        else:
            print(f"{'ID':<5} | {'Name':<20} | {'Email':<25} | {'College':<20} | {'Track':<15}")
            print("-" * 90)
            for row in records:
                print(f"{row[0]:<5} | {row[1]:<20} | {row[2]:<25} | {row[3]:<20} | {row[4]:<15}")
        
        cursor.close()
        conn.close()

def main():
    init_db()
    while True:
        print("\n==================================")
        print("  IBM Z Summit Registration System")
        print("==================================")
        print("1. Register New Attendee")
        print("2. View All Attendees")
        print("3. Exit")
        
        choice = input("Enter choice (1-3): ").strip()
        
        if choice == "1":
            register_attendee()
        elif choice == "2":
            display_attendees()
        elif choice == "3":
            print("\nExiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
