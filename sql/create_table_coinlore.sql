CREATE SCHEMA IF NOT EXISTS raw;

CREATE TABLE IF NOT EXISTS raw.coin_lore (
    id SERIAL PRIMARY KEY,
    date TIMESTAMPTZ NOT NULL,
    nameid VARCHAR NOT NULL,
    price DOUBLE PRECISION,
    percent_change_24h DOUBLE PRECISION,
    percent_change_7d DOUBLE PRECISION,
    market_cap_usd DOUBLE PRECISION,
    source VARCHAR(50),
    UNIQUE (nameid, date, source)
);