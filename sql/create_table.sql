CREATE TABLE coins_price (
    id SERIAL PRIMARY KEY,
    date TIMESTAMP,
    price DOUBLE PRECISION,
    coin VARCHAR,
)