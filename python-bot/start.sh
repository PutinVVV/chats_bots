#!/bin/bash

# запуск бота из виртуального окружения
./.venv/bin/python -m bot

# дополнительные команды (можно запускать вручную при необходимости):
# ./venv/bin/python -m bot.recreate_database
# watch -n 1 'sqlite3 bot.sqlite -cmd ".mode box" "SELECT * FROM telegram_updates ORDER BY id DESC LIMIT 1"'
# watch -n 1 'sqlite3 bot.sqlite -cmd ".mode box" "SELECT * FROM users"'
# ./venv/bin/black .
# ./venv/bin/ruff check .
# PYTHONPATH=. ./venv/bin/pytest tests/ -v
# psql -U postgres -h localhost -p 5432
    