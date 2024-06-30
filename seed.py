import psycopg2
from psycopg2 import Error
from faker import Faker
fake = Faker()
try:
    # Підключення до бази даних
    connection = psycopg2.connect(
        user="your_username",
        password="your_password",
        host="your_host",
        port="your_port",
        database="your_database"
    )
    cursor = connection.cursor()
    # Додавання статусів
    statuses = [('new',), ('in progress',), ('completed',)]
    cursor.executemany("INSERT INTO status (name) VALUES (%s) ON CONFLICT (name) DO NOTHING", statuses)
    # Додавання користувачів
    for _ in range(10):
        fullname = fake.name()
        email = fake.email()
        cursor.execute("INSERT INTO users (fullname, email) VALUES (%s, %s) RETURNING id", (fullname, email))
        user_id = cursor.fetchone()[0]
        # Додавання завдань для кожного користувача
        for _ in range(fake.random_int(min=1, max=5)):
            title = fake.sentence()
            description = fake.text()
            status_id = fake.random_int(min=1, max=3)
            cursor.execute(
                "INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
                (title, description, status_id, user_id)
            )
    # Підтвердження змін
    connection.commit()
    print("Дані успішно додано до таблиць")
except (Exception, Error) as error:
    print("Помилка при роботі з PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("З'єднання з PostgreSQL закрито")
