
CREATE TABLE counter(
    id SERIAL PRIMARY KEY,
    value INT NOT NULL
);

INSERT INTO counter (value) VALUES (0);