 Expense Tracker – “Khrcha Kam Kiya Karo”

A simple command-line based Expense Tracker written in Python.
This program helps you record daily expenses, view all expenses, and calculate your total khrcha. Perfect for beginners learning Python loops, lists, and dictionaries.

 Features

Add Expense
Enter date, category, description, and amount of your kharcha.

View All Expenses
Lists all recorded expenses in order.

View Total Khrcha
Automatically sums all expense amounts.

Exit the Program
Clean exit with a friendly message.

 How It Works

The program runs in a loop and displays a menu with four options:

Add Expense

Asks for date

Category (Food, Travel, Makeup, Books, etc.)

Description

Amount

Stores these details in a dictionary inside a list.

View All Expenses

Prints each stored expense with a serial number.

View Total Expense

Calculates total by summing the amnt from each stored expense.

Exit

Ends the program.

 Requirements

Python 3.x

No external libraries required.

How to Run

Save the file as expense_tracker.py

Open terminal or command prompt.

Run:

python expense_tracker.py


Follow the on-screen menu and enter your kharchas.

 Code Structure

expensesList → Stores all expenses as dictionaries

while True: loop → Keeps the menu running

if…elif blocks → Handle menu options

User input is taken via input()

Amount is stored as float

🔮 Example Output
Welcome to Expense Tracker Khrcha kam kiya karo
===MENU===
1. Add Expense
2. View all Expenses
3. View Total Khrcha
4. Exit
Enter your choice: 1
Kis date par khrcha kiya tha?: 12-11-2025
Kis type ka khrcha kiya? (Food, Travel, Makeup, Books): Food
Aur detail dedo: Pizza party
Enter the amount: 250
Done bro. Expense added successfully!

 Credits

Created for fun and learning — helping you track your daily khrcha in a simple way.

If you'd like, I can also format this as an actual README.md file or create a more advanced version of the script (with file storage, editing, deleting, categories, totals by type, etc.).

I prefer this response
