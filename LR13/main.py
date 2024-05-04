import csv
import json

def csv_to_json(csv_file, json_file):
    try:
        with open(csv_file, 'r') as file:
            csv_reader = csv.DictReader(file)
            data = list(csv_reader)

        with open(json_file, 'w') as file:
            json.dump(data, file, indent=4)

        print(f"Дані успішно конвертовано у файл {json_file}.")
    except FileNotFoundError:
        print(f"Помилка: файл {csv_file} не знайдено.")
    except Exception as e:
        print("Виникла помилка під час конвертації:", e)


# Приклад використання
csv_to_json("data.csv", "data.json")
