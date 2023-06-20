use akonlineschooldb;
show tables;
create table Programs(
id int not null auto_increment,
program_name varchar(20) not null,
department varchar(50) not null,
prodescription varchar(300),
duration int not null,
primary key(id)
);
insert into Programs(program_name,department,prodescription,duration) values('Undergraduate','BSc in Computer Science','This is an undergraduate program in computer science field in which students will learn many contemporay courses that will enable them to become computer scientists. You can register for it.',4); 
insert into Programs(program_name,department,prodescription,duration) values('Undergraduate','BSc in Data Science','This is an undergraduate program in Data science field in which students will learn many contemporay courses that will enable them to become data scientists. You can register for it.',4); 
insert into Programs(program_name,department,prodescription,duration) values('Undergraduate','BSc in Artificial Intelligence','This is an undergraduate program in computer science field in which students will learn many contemporay courses that will enable them to become computer scientists. You can register for it.',4); 
insert into Programs(program_name,department,prodescription,duration) values('TVET','ICT LEVEL 4','This is an undergraduate program in computer science field in which students will learn many contemporay courses that will enable them to become computer scientists. You can register for it.',4); 
insert into Programs(program_name,department,prodescription,duration) values('Postgraduate','MSc in Artificial Intelligence','This is an undergraduate program in computer science field in which students will learn many contemporay courses that will enable them to become computer scientists. You can register for it.',4); 
select * from Programs;
create table Users(
id int not null auto_increment,
First_name varchar(20) not null,
Middle_name varchar(20) not null,
Last_name varchar(20) not null,
Email varchar(50) not null,
Passw varchar(300) not null,
primary key(id)
);
insert into Users(First_name, Middle_name, Last_name, Email, Passw) values('Amsalu','Dinote','Kuye','amsalu1981@gmail.com','123');
insert into Users(First_name, Middle_name, Last_name, Email, Passw) values('Kabina','Gamba','Karma','kabina@gmail.com','akpass');
insert into Users(First_name, Middle_name, Last_name, Email, Passw) values('Daniel','Tesfay','G/egziabher','danieltg@gmail.com','akpass');
insert into Users(First_name, Middle_name, Last_name, Email, Passw) values('Shanko','Sagoya','Kusse','shanko@gmail.com','akpass');
select * from Users;
update Users set Email='amsalu1981@gmail.com' where id=1;
drop table Users;
create table UserRole(
id int not null auto_increment,
Email varchar(50) not null,
Role_name varchar(15) not null,
primary key(id)
);
insert into UserRole(Email, Role_name) values('amsalu1981@gmail.com','admin');
insert into UserRole(Email, Role_name) values('dani@gmail.com','guest');
insert into UserRole(Email, Role_name) values('kiya@gmail.com','user');
select * from UserRole;