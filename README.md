# Methods_Project

## Setting up the database
### Install PostgreSQL
View the following tutorial for help installing PostgreSQL:  
https://www.postgresqltutorial.com/install-postgresql/  

Visit this link to install PostgreSQL version 12.x:  
https://www.enterprisedb.com/software-downloads-postgres  

### Creating the database and tables in pgAdmin 4
1. Open pgAdmin 4
2. Enter the password created during PostgreSQL installation
3. Select and right click on Database in the left column
4. Click Create Database
5. In the General tab, enter in "methods_store" in the Database field to name the database
6. Click Save
7. Click on the arrow next to Database to expand the list of databases
8. Select and right click on the new methods_store database
9. Click Query Tool
10. Enter in SQL statements from the "sql statements" folder (must do store-schema.txt first)
11. Press F5 on keyboard or Execute/Refresh at the top toolbar of pgAdmin 4

## Setting up Python compatibility with the database
### Install psycopg2
1. Open a Command Prompt window
2. Verify that you have Python installed
`python --version`
3. If not, install Python (3.8.8 used in initial creation of this guide)
https://www.python.org/downloads/
4. Verify that you have PIP installed 
`pip --version`
5. If not, install Pip
https://www.makeuseof.com/tag/install-pip-for-python/
6. Install psycopg2 Python module
` pip install psycopg2-binary`
7. Verify that you have psycopg2 installed
`pip list`
