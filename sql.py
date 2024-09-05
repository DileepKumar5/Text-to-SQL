import sqlite3

# Connect to the database (or create it if it doesn't exist)
connection = sqlite3.connect("employee.db")

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# SQL command to create the EMPLOYEE table with updated locations
table_info = """
Create table EMPLOYEE (
    Name VARCHAR(50), 
    Location VARCHAR(50), 
    Position VARCHAR(50), 
    Salary INT
);
"""

# Execute the command to create the table
cursor.execute(table_info)

# Insert records into the EMPLOYEE table with updated locations
cursor.execute("Insert Into EMPLOYEE (Name, Location, Position, Salary) values ('Dileep', 'Karachi, Pakistan', 'Software Engineer', 70000)")
cursor.execute("Insert Into EMPLOYEE (Name, Location, Position, Salary) values ('Karan', 'Berlin, Germany', 'DevOps Engineer', 65000)")
cursor.execute("Insert Into EMPLOYEE (Name, Location, Position, Salary) values ('Simran', 'Munich, Germany', 'Data Scientist', 80000)")
cursor.execute("Insert Into EMPLOYEE (Name, Location, Position, Salary) values ('Aliza', 'Dubai, UAE', 'SQA Engineer', 60000)")
cursor.execute("Insert Into EMPLOYEE (Name, Location, Position, Salary) values ('Hasaan', 'Lahore, Pakistan', 'Software Engineer', 72000)")

# Display the inserted records
print("The inserted records are:")

# Select all records from the EMPLOYEE table
data = cursor.execute("Select * From EMPLOYEE")

# Print each record
for row in data:
    print(row)

# Commit the changes and close the connection
connection.commit()
connection.close()
