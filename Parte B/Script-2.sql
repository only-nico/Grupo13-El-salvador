#1
SELECT c.city, c.customerName from customers c;
#2
select DISTINCT(c.city) from customers c;
#3
SELECT productName, quantityInStock from products order by quantityInStock asc;
#4
SELECT c.orderNumber, c.orderDate from orders c order by c.orderDate desc limit 3;
#5
select p.productName, p.productLine from products p where p.productLine like "%Cars%";
#6
SELECT p.productName, p.productLine from products p where p.productLine not like "%Planes%" and not like "%Motorcycles%";
#7
SELECT customerName ,productLine from customers c join orders o on c.customerNumber = o.customerNumber join orderdetails o2 on o2.orderNumber = o.orderNumber JOIN products p on p.productCode =o2.productCode where p.productLine="Planes";
#8
SELECT COUNT(p.productName), p.productLine  from products p group by p.productLine; 