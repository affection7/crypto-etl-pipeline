# Crypto-ETL-pipeline

Минималистичный ETL-пайплайн для мониторинга цены Bitcoin.

## Как это работает:
1. **Extract**: Получает данные из **CoinGecko API** (`requests`).
2. **Transform**: Формирует структуру данных с меткой времени (`pandas`).
3. **Load**: Сохраняет результат в локальный **CSV** и облачный **PostgreSQL (Neon)**.

## Стек:
Python, Pandas, Psycopg2, PostgreSQL (Neon).

## Быстрый старт:
1. Настройте ключи в `.env`:
   ```env
   API_KEY=your_coingecko_key
   DB_PASS=your_neon_password
