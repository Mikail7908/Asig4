CREATE TABLE IF NOT EXISTS statements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)

INSERT INTO statements (name, age) 
VALUES 
("Alice", 30),
("Bob", 40),
("Charlie", 50)

 