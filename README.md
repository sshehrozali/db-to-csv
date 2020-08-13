<h1>.DB file to .CSV file (Python)</h1>

<h3>What is .DB file?</h3>
    <p>DB file stands for database file.A database file is a file which contains all data relevant to your program stored in a form of table containing rows and
    columns just like MS Excel spreadsheets or Google Sheets.Generally database files are used to store data to keep quering and using data for different tasks
     and purposes.Mostly Database files are written in SQL (Structured Query Language). This program works only with sqlite3 .db file</p>
     
<h3>What is .CSV file?</h3>     
  <p>CSV file stands for comma-separated values which is a method used to separate one field with another with the help of comma(,).This file is also used to store
      data but in a different format just same as MS Excel file.In .CSV file every field is separated with a comma(,) within a row and with columns of 
      required fields.CSV files can directly be open with any spreadsheet or CSV editor for e.g MS Excel or Google Sheets.</p>
      
<h2>How My program works?</h2>
<p>This script is written especially for my students database management system in python.Here is the <a href="https://github.com/ShahrozAliPK/students-management-system"
    alt="students-database-management">link.</a></p>But you can always change fieldnames for your own .db file.The script opens .db file in <i>DATABASE</i> folder
    inside <i>DB-to-CSV</i> folder and reads sqlite3 database and stores inside a memory at a particular address.Now another variable is used to fetch all data
    inside database and stores in the form of nested list.Now another CSV file is opened as <i>csvfile</i> and <i><csv_writer</i> object is created to write rows
    inside .CSV file and fieldnames.
    <br>
    After writing all rows successfully the program prints a success message on the terminal window.
