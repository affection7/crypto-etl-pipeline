# Crypto-ETL-pipeline

Минималистичный ETL-пайплайн для мониторинга цен токенов.

## ETL:
1. **Extract**: Получает данные из **CoinGecko API и Coinpaprika API** (`requests`).
2. **Transform**: Формирует структуру данных с меткой времени (`pandas`).
3. **Load**: Сохраняет результат в облачный **PostgreSQL (Neon)**.

## Оркестрация и Автоматизация:
Пайплайн полностью автоматизирован с помощью **GitHub Actions**.

- **Расписание**: Скрипт запускается автоматически каждые 10 минут (факт. 2 часа)

## Стек:
Python, Pandas, Psycopg2, PostgreSQL (Neon).

## Быстрый старт:
1. Настройте ключи в `.env`:
  ```env
   API_KEY=YOUR_COINGECKO_API_KEY_HERE
   DB_PASS=your_secure_password
   URL_GECKO=https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&ids=bitcoin,ethereum,solana
   URL_PAPRIKA=https://api.coinpaprika.com/v1/tickers/ton-toncoin
  ```
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   
3. Запустите:
   ```bash
   py src/main.py

## Схема таблицы:
   coins_price (id SERIAL PRIMARY KEY, date TIMESTAMP, price FLOAT, coin VARCHAR(10))

## Визуализация данных
Дашборд в Power BI отображает динамику курсов криптовалют.

![Dashboard Preview](img/powerBI_ETL_bitcoin-04.05.2026.png)

