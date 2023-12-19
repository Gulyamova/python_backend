# FastAPI "Hello World" Приложение

Это простое приложение "Hello World", созданное с использованием FastAPI

### Использование

1. Запустите FastAPI приложение с помощью Uvicorn:

    ```bash
    uvicorn main:app --reload
    ```

   Приложение будет доступно по адресу `http://localhost:8000`.

2. Доступные эндпоинты:

   - `/hello/{name}`: Приветствие человека с указанным именем в пути.
   - `/greet?name={name}`: Приветствие человека с указанным именем, используя параметр запроса.
   - `/greeting`: Создание пользовательского приветствия для человека с использованием тела запроса.

### Форматирование и Линтинг кода

- Форматирование кода с помощью Black:

    ```bash
    black .
    ```

- Линтинг кода с Flake8:
  Создайте файл .flake8:
  ````
  [flake8]
  max-line-length = 88
  exclude = .git,__pycache__,.mypy_cache,env,venv
  ignore = E203, E266, E501, W503, F403
  
Запуск линтинга:

    ```bash
    flake8
    ```