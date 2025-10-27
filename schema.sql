CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
); 

CREATE TABLE recipes (
    id INTEGER PRIMARY KEY,
    title TEXT,
    ingredients TEXT,
    user_id INTEGER REFERENCES users
);

CREATE TABLE comments (
    id INTEGER PRIMARY KEY,
    recipe_id INTEGER REFERENCES recipes,
    user_id INTEGER REFERENCES users,
    comment TEXT
);

CREATE TABLE classes (
    id INTEGER PRIMARY KEY,
    title TEXT,
    value TEXT
);

CREATE TABLE recipe_classes (
    id INTEGER PRIMARY KEY, 
    recipe_id INTEGER REFERENCES recipes, 
    title TEXT, 
    value TEXT
);

CREATE TABLE images (
    id INTEGER PRIMARY KEY,
    recipe_id INTEGER REFERENCES recipes,
    image BLOB
);