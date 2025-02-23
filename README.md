# Expense-Tracker
An expense tracker program built using Python and SQLite

**Overview**
As a software engineer, my goal with this project is to deepen my understanding of how to integrate applications with relational databases and to refine my skills in building real-world software. This program is an Expense Tracker designed to help individuals manage their finances by storing and retrieving expenses through a SQL Relational Database.

The application allows users to:

Add new expenses
View existing expenses
Update expense details
Delete expenses
Filter expenses by category and date
Summarize the total amount spent in each category
It uses SQLite as the relational database, allowing the program to store and query data efficiently. The database interacts with the program through SQL commands that allow the user to insert, modify, retrieve, and delete records.

https://youtu.be/G1bKnxJHffc

Relational Database
This application uses SQLite, a lightweight relational database, which is built directly into Python using the sqlite3 library. SQLite is chosen for its simplicity and portability, making it ideal for this project.

The database contains the following table:

expenses: Stores individual expenses with fields for id, category, description, amount, and date.
Structure of the expenses table:

id: INTEGER (Primary Key) – Unique identifier for each expense.
category: TEXT – The category of the expense (e.g., "Food", "Utilities").
description: TEXT – A short description of the expense.
amount: REAL – The amount spent.
date: TEXT – The date the expense was recorded.
Development Environment
For the development of this application, the following tools and technologies were used:

Python: The programming language for writing the software.
SQLite: A relational database embedded in the application, used to store the expenses.
VS Code: The Integrated Development Environment (IDE) used for coding.
sqlite3 library: Built into Python to manage SQLite databases.
This project is a simple command-line application that demonstrates how to interact with a relational database using Python.

Useful Websites
Here are some resources I found particularly helpful while working on this project:

SQLite Tutorial
Python sqlite3 Documentation
W3Schools SQL Tutorial
SQLite and Python
Future Work
There are several areas I plan to improve and expand on in the future:

Add more features for data visualization, such as charts for tracking spending trends.
Implement authentication and user accounts for multiple users.
Add the ability to export and import data from external sources like CSV files.
Improve the user interface (e.g., create a graphical user interface with Tkinter or another framework).
Integrate automatic expense categorization based on merchant names or descriptions.
