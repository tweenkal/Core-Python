# 👉sql:-
# 👉primary key is the unique and not null means data is not blank or
# inside the data is unique not a duplicate.

import sqlite3

# 👉Create the database
db = sqlite3.connect("abc.db")
# if not exist means create the table , table is not exist means before the
# table is created then not give the error

# 👉create the table emp
db.execute("create table if not exists emp(id int primary key,name text,age int)")

# 👉create a second table student:-
db.execute("create table if not exists student(rollno int primary key,name text,mobile int)")
db.commit()

# 👉insert the values :- (3 types method to insert data)
# commit means the enter data into table is saved.
# db.execute("insert into emp values(1,'Twinkle',21)")
# db.execute("insert into emp(id,name) values(2,'Jurali')")
# db.commit()

# 👉insert data into student table
# db.execute("insert into student values(5,'YUI',4535647577)")
# db.commit()


# 👉User input data enter by the user

# id = int(input("Enter id="))
# name = input("Enter name=")
# age = int(input("Enter age="))
#
# db.execute("insert into emp values(?,?,?)", (id, name, age))
# db.commit()


# 👉delete the data into table
# 👉delete command is used to the delete the data inside the table
# db.execute("delete from emp")
# db.commit()

# 👉delete the data id 2 for specific data
# db.execute("delete from emp where id=2")
# db.commit()


# 👉How to define the DDL and DML command:-
# 👉with table keyword it is the DDL command
# 👉and not define the table keyword means it is the DML
# 👉DML :-
# 👉DML stand for Data manipulation language.
# 👉DML :- Manipulate the data for query update,delete,insert command
#👉inside the table data manipulation is called DML command

# 👉DDL:-
# 👉DDL stands for the data definition  language.
# 👉DDL :- Define the data for query create  command
# 👉change the table structure for example change the column data

# 👉drop table :- its delete a full table
# db.execute("drop table emp")
# db.commit()

# 👉Update query:-is update the data
# db.execute("Update emp set age=21 where id=1")
# db.commit()


# 👉Alter query:- change table structure,add specific column , delete
# specific column,change the column name

# 👉add the column mobile no
# db.execute("alter table emp add column mobile int")
# db.commit()

# 👉Update the colum name means rename the column name
# db.execute("alter table emp rename age to age1")
# db.commit()

# 👉delete column
# db.execute("alter table emp drop column mobile")
# db.commit()

# 👉get the store database data or retrive the data
# db.execute("select * from emp")
# db.commit()

# 👉fetchall :- all data return
# a = db.execute("select id,name from emp")
# data = sqlite3.Cursor.fetchall(a)
# db.commit()

# 👉data print line by line
# for i in data:
#     print(i)

# 👉print only name for emp line by line
# a = db.execute("select name from emp")
# data = sqlite3.Cursor.fetchall(a)
# db.commit()
#
# for i in data:
#     print(i)

# 👉print only emp name for xyz
# a = db.execute("select name from emp where id=2")
# print(sqlite3.Cursor.fetchall(a))
# db.commit()

# 👉print all data for id = 2
# a = db.execute("select * from emp where id = 3")
# print(sqlite3.Cursor.fetchall(a))
# db.commit()

# 👉Note:-In django get the data into database is give the output your
# give one row is output is tuple and give multiple row merge the list
# form.

# 👉fetchone :- only one data return
# a = db.execute("select id,name from emp")
# print(sqlite3.Cursor.fetchone(a))
# db.commit()


# 👉Inner Join:- it is return common data for two table

# a = db.execute("select * from emp inner join student on emp.id = student.rollno")
# data = sqlite3.Cursor.fetchall(a)
# for i in data:
#     print(i)


# 👉Outer join:- two types of outer join
# 👉left outer join :- give the all data for left side and right side
# give common data
# 👉right outer join :- give the all data for the right side and left
# side give common data

# 👉left join:-
# a = db.execute("select * from emp left join student on emp.id = student.rollno")
# data = sqlite3.Cursor.fetchall(a)
# for i in data:
#     print(i)

# 👉right join:-
a = db.execute("select * from emp right join student on emp.id = student.rollno")
data = sqlite3.Cursor.fetchall(a)
for i in data:
    print(i)