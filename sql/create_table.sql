CREATE TABLE coins_price (
    id SERIAL PRIMARY KEY,
    date TIMESTAMPTZ,
    price DOUBLE PRECISION,
    coin VARCHAR,
    source VARCHAR(25),
    UNIQUE (source, coin, date)
);