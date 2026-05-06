# Crypto-ETL-Pipeline

![Python](https://img.shields.io/badge/python-3.10+-blue.svg?style=for-the-badge&logo=python)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=power-bi&logoColor=black)

ETL-пайплайн для мониторинга цен криптовалютных токенов. Проект демонстрирует полный цикл работы с данными: от извлечения из API до облачного хранилища и автоматической визуализации.

---

## Архитектура решения (ETL)

![Архитектура ETL-пайплайна](img/crypto_etl_architecture.png)

Процесс обработки данных разделен на три логических этапа для обеспечения масштабируемости:

1.  **Extract (Извлечение)**: Сбор цен (BTC, ETH, SOL, TON) через **CoinGecko** и **Coinpaprika API**.
2.  **Transform (Трансформация)**: Обработка данных в `pandas`, приведение типов и временных меток.
3.  **Load (Загрузка)**: Сохранение в облачную СУБД **PostgreSQL (Neon)**.
4.  **Visualize (Визуализация)**: Подключение **Power BI** к БД Neon для построения графиков и анализа трендов.

---

## Автоматизация и Оркестрация

Пайплайн полностью автономен благодаря **GitHub Actions**:

1.  **Расписание (Cron)**: Скрипт запускается автоматически каждые 2 часа.
2.  **Безопасность**: API ключи и доступы к БД хранятся в **GitHub Secrets**.
3.  **Логирование**: Статус запусков можно отслеживать во вкладке *Actions*.

---

## Дашборд и Визуализация

Ниже представлен актуальный срез данных из Power BI. 

![Dashboard Preview](img/dashboard.png)

---

## Технологический стек

| Категория | Инструменты |
| :--- | :--- |
| **Язык** | Python 3.10+ |
| **Анализ данных** | Pandas |
| **База данных** | PostgreSQL (Neon.tech) |
| **Визуализация** | **Power BI Desktop / Service** |
| **Автоматизация** | GitHub Actions |

---
## Быстрый старт

### 1. Подготовка окружения
Создайте файл `.env` в корневой папке:
  ```env
    API_KEY=ваш_ключ_coingecko
    DB_PASS=ваш_пароль_от_neon_db
    URL_GECKO=https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&ids=bitcoin,ethereum,solana
    URL_PAPRIKA=https://api.coinpaprika.com/v1/tickers/ton-toncoin
  ```
### 2. Установите зависимости:

   ```bash
     pip install -r requirements.txt
   ```
### 3. Запустите:

   ```bash
     python src/main.py
   ```
