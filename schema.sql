CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
); 

CREATE TABLE recipes (
    id INTEGER PRIMARY KEY,
    title TEXT,
    recipe TEXT,
    user_id INTEGER REFERENCES users
);

