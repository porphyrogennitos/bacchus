-- CREATE TABLE users (id INTEGER, email TEXT NOT NULL, hash TEXT NOT NULL, PRIMARY KEY(id));
-- DROP TABLE users;
-- DELETE FROM users WHERE email="poutsa@gmail.com";

-- CREATE TABLE festivals (user_id INTEGER, name TEXT NOT NULL, location TEXT NOT NULL, date DATE NOT NULL, FOREIGN KEY(user_id) REFERENCES users(id));
-- DROP TABLE festivals;
-- INSERT INTO festivals (name, location, date) VALUES ("Το σπάσιμο της στάμνας", "Κεφαλονιά", "Μεγάλο Σάββατο")
-- DELETE FROM festivals WHERE id=1;


