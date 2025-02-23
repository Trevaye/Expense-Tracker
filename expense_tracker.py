import sqlite3
from datetime import datetime

# Connect to the database
def connect_db():
    print("Connecting to the database...")
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    print("Connected to the database successfully.")
    return conn, cursor

# Create the expenses table
def create_table(cursor):
    print("Creating the expenses table if it doesn't exist...")
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
                        id INTEGER PRIMARY KEY,
                        date TEXT,
                        category TEXT,
                        amount REAL,
                        description TEXT)''')
    print("Table created or already exists.")

# Add an expense to the database
def add_expense(conn, cursor):
    print("Adding an expense...")
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    cursor.execute("INSERT INTO expenses (date, category, amount, description) VALUES (?, ?, ?, ?)",
                   (date, category, amount, description))
    conn.commit()
    print(f"✅ Expense added: {date}, {category}, {amount}, {description}")

# View all expenses
def view_expenses(cursor):
    print("Viewing all expenses...")
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    if rows:
        print("📌 My Expense Records:")
        for row in rows:
            print(f"ID: {row[0]}, Date: {row[1]}, Category: {row[2]}, Amount: ${row[3]}, Description: {row[4]}")
    else:
        print("No expenses found.")

# Delete an expense by ID
def delete_expense(conn, cursor):
    print("Deleting an expense...")
    expense_id = int(input("Enter the expense ID to delete: "))
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    print(f"✅ Expense with ID {expense_id} deleted.")

# Update an expense
def update_expense(conn, cursor):
    print("Updating an expense...")
    expense_id = int(input("Enter the expense ID to update: "))
    new_category = input("Enter new category: ")
    new_amount = float(input("Enter new amount: "))
    new_description = input("Enter new description: ")

    cursor.execute("UPDATE expenses SET category = ?, amount = ?, description = ? WHERE id = ?",
                   (new_category, new_amount, new_description, expense_id))
    conn.commit()
    print(f"✅ Expense with ID {expense_id} updated.")

# Filter expenses by date
def filter_expenses_by_date(cursor):
    print("Filtering expenses by date...")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    cursor.execute("SELECT * FROM expenses WHERE date BETWEEN ? AND ?", (start_date, end_date))
    rows = cursor.fetchall()
    if rows:
        print(f"📌 Expenses from {start_date} to {end_date}:")
        for row in rows:
            print(f"ID: {row[0]}, Date: {row[1]}, Category: {row[2]}, Amount: ${row[3]}, Description: {row[4]}")
    else:
        print("No expenses found in this date range.")

# Summarize spending by category
def summarize_spending(cursor):
    print("Summarizing spending by category...")
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    rows = cursor.fetchall()
    if rows:
        print("📊 Spending by Category:")
        for row in rows:
            print(f"Category: {row[0]}, Total Amount: ${row[1]}")
    else:
        print("No spending data found.")

# Main menu
def main():
    print("Starting Expense Tracker Program...")
    conn, cursor = connect_db()
    create_table(cursor)

    while True:
        print("\n📊 Expense Tracker Menu")
        print("1. Add an Expense")
        print("2. View All Expenses")
        print("3. Delete an Expense")
        print("4. Update an Expense")
        print("5. Filter Expenses by Date")
        print("6. View Spending Summary")
        print("7. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense(conn, cursor)
        elif choice == '2':
            view_expenses(cursor)
        elif choice == '3':
            delete_expense(conn, cursor)
        elif choice == '4':
            update_expense(conn, cursor)
        elif choice == '5':
            filter_expenses_by_date(cursor)
        elif choice == '6':
            summarize_spending(cursor)
        elif choice == '7':
            print("👋 Exiting... Have a great day!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

    conn.close()

# Run the program
if __name__ == "__main__":
    main()
