# Import Libraries
import csv
import sqlite3
from sys import argv, exit

# UI Menu
print("\n\n--| DB TO CSV FILE GENERATOR |--")
print("--------------------------------\n")
print("Do you want to generate .csv file?\n")

# Connection to sqlite3 database file
connection = sqlite3.connect("DATABASE/students.db")

# Cursor to connect to database
cursor = connection.cursor()

# Select all data from database file
database = cursor.execute("SELECT * from students")

# Keep prompting till valid input
while (True):

    # Prompt for option
    ask = input("Type YES or NO: ")

    # If no, exit program
    if ask.lower() == "no" or ask.lower() == "n":
        print("\nOperation Cancelled by the user\n\n")
        exit(1)
    
    # If yes, execute below code, generate .csv file in current directory
    if ask.lower() == "yes" or ask.lower() == "y":

        # Print New-line
        print()

        # Fetch all data as nested Lists
        students_data = database.fetchall()

        # Create fieldnames for CSV file
        fieldnames = ["ID", "First", "Middle", "Last", "Age", "Class", "Father's Name", "Phone Number"]

        # Declare filename for CSV file
        filename = "records.csv"

        # Open CSV file as Write mode
        with open(filename, "w") as csvfile:

            # CSV writer object
            csv_writer = csv.writer(csvfile)

            # Write fieldnames to CSV file
            csv_writer.writerow(fieldnames)

            # Write each row in CSV file
            csv_writer.writerows(students_data)

            print("All records exported Successfully!")
            print("Check your directory for the generated .csv file\n")
            print("Developed By Syed Shehroz Ali\n\n")

        # Close CSV file, Exit program Successfully
        csvfile.close()
        exit(0)

    # Else
    print("Type Correct Option!\n")

