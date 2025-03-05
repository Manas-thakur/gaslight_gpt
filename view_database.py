import sqlite3
from tabulate import tabulate

def view_database():
    try:
        # Connect to the database
        conn = sqlite3.connect('mydb2.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        # Get all tables in the database
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        for table in tables:
            table_name = table[0]
            print(f"\n=== Table: {table_name} ===")

            # Get column names
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = [column[1] for column in cursor.fetchall()]

            # Get table data
            cursor.execute(f"SELECT * FROM {table_name};")
            rows = cursor.fetchall()
            
            # Convert rows to list of dictionaries
            data = [dict(row) for row in rows]
            
            if data:
                # Print table in a formatted way
                print(tabulate(data, headers="keys", tablefmt="grid"))
            else:
                print("No data in table")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    view_database()