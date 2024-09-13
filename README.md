## Используемые инструменты
* **Python** (3.12);
* **Django** (5.0.4);
* **djangorestframework** (3.15.1);
* **Docker** and **Docker Compose** (containerization);
* **gunicorn** (23.0.0);
* **pillow** (10.3.0);
* **Nginx** (server for linking frontend and backend).

## Сборка и запуск приложения
1. Собираем и запускаем контейнеры с приложением. В терминале в общей директории (с файлом "docker-compose.yml") 
вводим команду:
    ```
    docker-compose up -d
    ```
В демонстрационных данных в базу данных уже добавлены некоторые продукты и пользователи с заказами.
