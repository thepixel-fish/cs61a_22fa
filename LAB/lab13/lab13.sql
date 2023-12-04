.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet FROM students WHERE color = 'blue' and pet = 'dog';

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song FROM students WHERE color = 'blue' and pet = 'dog';


CREATE TABLE smallest_int_having AS
  SELECT time, smallest FROM students GROUP BY smallest HAVING count(*) = 1;


CREATE TABLE matchmaker AS
  SELECT a.pet, a.song, a.color, b.color FROM students AS a, students AS b 
    WHERE a.pet = b.pet and a.song = b.song and a.time < b.time;


CREATE TABLE sevens AS
  SELECT stu.seven FROM students AS stu, numbers AS nums 
    WHERE stu.time = nums.time and stu.number = 7 and nums.'7' = 'True';


CREATE TABLE average_prices AS
  SELECT category, avg(MSRP) AS average_price FROM products GROUP BY category;


CREATE TABLE lowest_prices AS
  SELECT store, item, min(price) AS lowest_price FROM inventory GROUP BY item;


CREATE TABLE shopping_list AS
  SELECT item, store FROM lowest_prices AS low, products 
      WHERE item = name GROUP BY category HAVING min(MSRP / rating);


CREATE TABLE total_bandwidth AS
  SELECT SUM(Mbs) FROM shopping_list AS l, stores AS s WHERE l.store = s.store;

