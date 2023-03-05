Create Database Restaurant;
use Restaurant;
show tables;


Create table swiggy(
Shop_Name Varchar(900),
Cuisine Varchar(900),
Location Varchar(900),
Rating Varchar(900),
Cost_for Varchar(900));

view table swiggy



load data infile "D:\Swiggy Bangalore Outlet Details.csv"
into table swiggy
fields terminated by ','
enclosed by '"'
lines terminated by '\n'
ignore 1 rows;