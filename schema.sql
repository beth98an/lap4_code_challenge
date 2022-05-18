DROP TABLE IF EXISTS shorten_url;

CREATE TABLE shorten_url (
    id INTEGER PRIMARY KEY,
    url VARCHAR(2000),
    short_url VARCHAR(20)
);
