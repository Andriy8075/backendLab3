# Інструкція для запуску проєкту

1. Склонувати репозиторій
2. Перейти в папку з потрібний файлом docker-compose (backendLab2/docker/dev бо backendLab2/docker/production)
3. білдити проєкт через docker-compose up
4. відкрити проєкт в браузері

#### Для швидкого запуску можна скопіювати і запустити в терміналі команди

```bash
    git clone https://github.com/Andriy8075/backendLab2
    cd backendLab2/docker/dev
    docker compose up
```
Після цього сайт буде працювати на порті 8080:
http://127.0.0.1:8080

Ці команди запустять сайт в режимі розробки (development build)

Команди для запуску в production:

```bash
    git clone https://github.com/Andriy8075/backendLab2
    cd backendLab2/docker/production
    docker compose up
```
Після цього сайт буде працювати на порті 80 (стандартному для http):
http://127.0.0.1

# Посилання на працюючий сайт:

https://backendLab2-1.onrender.com/

Під час деплою було використано production build (з папки docker/production)

# Postman

Postman колекція знаходиться в файлі postman_collection.json

Посилання на Postman flow:
https://andriiashomka.postman.co/workspace/My-Workspace~7862311b-2d89-4ce6-862a-9d07de91b827/flow/68fa6edc08102d0014d69bf0

# Обчислення варіанту:

Група ІМ-34. 34 % 3 = 1. Тому в цій (третій) лабораторній роботі додано 
валюти для записів та валюти за замовчуванням у користувачів

