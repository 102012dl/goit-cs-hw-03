import psycopg2
from psycopg2 import Error
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
    # Створення таблиці users
    create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        fullname VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL
    )
    """
    # Створення таблиці status
    create_status_table = """
    CREATE TABLE IF NOT EXISTS status (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) UNIQUE NOT NULL
    )
    """
    # Створення таблиці tasks
    create_tasks_table = """
    CREATE TABLE IF NOT EXISTS tasks (
        id SERIAL PRIMARY KEY,
        title VARCHAR(100) NOT NULL,
        description TEXT,
        status_id INTEGER REFERENCES status(id),
        user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
    )
    """
    # Виконання SQL-запитів для створення таблиць
    cursor.execute(create_users_table)
    cursor.execute(create_status_table)
    cursor.execute(create_tasks_table)
    # Підтвердження змін
    connection.commit()
    print("Таблиці успішно створено")
except (Exception, Error) as error:
    print("Помилка при роботі з PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("З'єднання з PostgreSQL закрито")
