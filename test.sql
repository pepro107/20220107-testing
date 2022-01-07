/*
Question1
*/
select p.firstName,p.lastName,a.city,a.state from person p
left join Address a 
on a.personId = p.personId


/*
Question2
*/

SELECT c.name FROM Customers c
left join Orders o
on c.id = o.customersId
where o.id == null
/*
Question3
*/

select Email from Person
GROUP BY Email
HAVING COUNT(Email)>1