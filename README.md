# Быстрый старт

## Устанавливаем Ollama:

Windows:

```
irm https://ollama.com/install.ps1 | iex
```

Linux / MacOS:

```
curl -fsSL https://ollama.com/install.sh | sh
```

## Создаем виртуальное окружение

Переходим в папку с программой и вводим в терминал:

Windows:

```
python -m venv .venv
./.venv/Scripts/activate
```

Linux / MacOS:

```
python3 -m venv .venv
source .venv/bin/activate
```

## Запускаем

```
python main.py
```
