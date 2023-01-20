# Department-library-management-system
Department library management system using python, Tkinter and Mysql

create datadase with two tables books and books_issued.

#Create Database
CREATE DATABASE db;

#Create Table books
CREATE TABLE books (
    bid int not null auto_increment primary key,
    title varchar(255),
    author varchar(255),
    status varchar(255),
    publication varchar(255),
    vol int(20),
    pub_year(year)
);

#create Table books_issued
CEART TABLE books_issued (
      bid int not null FOREIGN KEY REFERENCES books(bid),
      issuedto varchar(255),
      issued_date timestamp not null default current_timestamp on update current_timestamp,
      return_date timestamp not null default current_timestamp on update current_timestamp
);

#create main.py design the main page of the project

#addbook.py contains adding new book columns, such as (book id, book title, publication author, volume, publication year).

#deletebook.py for deleting the book by using the book id.

#viewbook.py; this page contains all the information about the book, which is already given to the add book page.

#issuebook.py this page contains the bid and issue to (whos going to take the book and their information; if it is a student, give the student register number and if it is a staff give their name along with their department name)

#returnbook.py this page contains only the book.

Here the issued date and the return date are updated automatically based on the Mysql query.
