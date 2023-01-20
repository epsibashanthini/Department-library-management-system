# Department-library-management-system
Department library management system using python, Tkinter and Mysql

create datadase with two tables books and books_issued.

## Create Database
```sql
CREATE DATABASE db;
```

## Create Table books
```sql
CREATE TABLE books (
    bid int not null auto_increment primary key,
    title varchar(255),
    author varchar(255),
    status varchar(255),
    publication varchar(255),
    vol int(20),
    pub_year(year)
);
```

## create Table books_issued
```sql 
CREATE TABLE books_issued (
      bid int not null FOREIGN KEY REFERENCES books(bid),
      issuedto varchar(255),
      issued_date timestamp not null default current_timestamp on update current_timestamp,
      return_date timestamp not null default current_timestamp on update current_timestamp
);
```
## Creating Python Files 
1. create `main.py` design the main page of the project

2. `addbook.py` contains adding new book columns, such as (book id, book title, publication author, volume, publication year).

3. `deletebook.py` for deleting the book by using the book id.

4. `viewbook.py` this page contains all the information about the book, which is already given to the add book page.

5. `issuebook.py` this page contains the bid and issue to (whos going to take the book and their information; if it is a student, give the student register number and if it is a staff give their name along with their department name)

6. `returnbook.py` this page contains only the book.

Here the issued date and the return date are updated automatically based on the Mysql query.
