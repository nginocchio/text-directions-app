DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS address;

CREATE TABLE user (
    phone_number INTEGER PRIMARY KEY
);

CREATE TABLE address (
    user INTEGER NOT NULL,
    location_name TEXT NOT NULL,
    address TEXT NOT NULL,
    FOREIGN KEY (user) REFERENCES user (phone_number)
);
