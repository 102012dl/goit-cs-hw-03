from pymongo import MongoClient
from bson.objectid import ObjectId


# Підключення до MongoDB
client = MongoClient("your_mongodb_connection_string")
db = client["cats_db"]
collection = db["cats"]


def create_cat(name, age, features):
    """Створення нового кота"""
    cat = {
        "name": name,
        "age": age,
        "features": features
    }
    result = collection.insert_one(cat)
    print(f"Cat created with id: {result.inserted_id}")


def read_all_cats():
    """Виведення всіх котів"""
    cats = collection.find()
    for cat in cats:
        print(cat)


def read_cat_by_name(name):
    """Виведення кота за ім'ям"""
    cat = collection.find_one({"name": name})
    if cat:
        print(cat)
    else:
        print(f"No cat found with name: {name}")


def update_cat_age(name, new_age):
    """Оновлення віку кота"""
    result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
    if result.matched_count > 0:
        print(f"Updated age of cat {name} to {new_age}")
    else:
        print(f"No cat found with name: {name}")


def add_feature_to_cat(name, feature):
    """Додавання нової характеристики до кота"""
    result = collection.update_one({"name": name}, {"$push": {"features": feature}})
    if result.matched_count > 0:
        print(f"Added feature '{feature}' to cat {name}")
    else:
        print(f"No cat found with name: {name}")


def delete_cat_by_name(name):
    """Видалення кота за ім'ям"""
    result = collection.delete_one({"name": name})
    if result.deleted_count > 0:
        print(f"Deleted cat with name: {name}")
    else:
        print(f"No cat found with name: {name}")


def delete_all_cats():
    """Видалення всіх котів"""
    result = collection.delete_many({})
    print(f"Deleted {result.deleted_count} cats")


# Основна функція для тестування CRUD операцій
if __name__ == "__main__":
    # Створення нового кота
    create_cat("barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])

    # Читання всіх записів
    print("All cats:")
    read_all_cats()

    # Читання кота за іменем
    print("\nRead cat by name 'barsik':")
    read_cat_by_name("barsik")

    # Оновлення віку кота
    print("\nUpdate cat age:")
    update_cat_age("barsik", 5)
    read_cat_by_name("barsik")

    # Додавання нової характеристики коту
    print("\nAdd feature to cat:")
    add_feature_to_cat("barsik", "любий до дітей")
    read_cat_by_name("barsik")

    # Видалення кота за ім'ям
    print("\nDelete cat by name:")
    delete_cat_by_name("barsik")
    read_all_cats()

    # Видалення всіх котів
    print("\nDelete all cats:")
    delete_all_cats()
    read_all_cats()
