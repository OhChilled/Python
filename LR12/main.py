import json

def load_data(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")
        return None

def save_data(data, filename):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Дані успішно збережено у файлі {filename}.")
    except IOError:
        print(f"Помилка: не вдалося зберегти дані у файл {filename}.")

def display_json_content(filename):
    data = load_data(filename)
    if data:
        print("Вміст JSON файлу:")
        print(json.dumps(data, indent=4))

def add_record(filename, record):
    data = load_data(filename)
    if data:
        data.append(record)
        save_data(data, filename)

def delete_record(filename, index):
    data = load_data(filename)
    if data:
        try:
            del data[index]
            save_data(data, filename)
        except IndexError:
            print("Помилка: вказаний індекс не існує.")

def search_data_by_field(filename, field, value):
    data = load_data(filename)
    if data:
        found_records = [record for record in data if record.get(field) == value]
        if found_records:
            print(f"Знайдені записи за полем '{field}' зі значенням '{value}':")
            print(json.dumps(found_records, indent=4))
        else:
            print("Записи не знайдено.")

def main():
    # Відкриємо JSON файл
    filename = "passengers.json"

    while True:
        print("\nМеню:")
        print("1. Вивести вміст JSON файлу")
        print("2. Додати новий запис")
        print("3. Видалити запис за індексом")
        print("4. Пошук записів за полем")
        print("5. Виконати завдання")
        print("6. Вийти")
        choice = input("Оберіть опцію: ")

        if choice == "1":
            display_json_content(filename)
        elif choice == "2":
            record = json.loads(input("Введіть новий запис у форматі JSON: "))
            add_record(filename, record)
        elif choice == "3":
            index = int(input("Введіть індекс запису, який потрібно видалити: "))
            delete_record(filename, index)
        elif choice == "4":
            field = input("Введіть поле для пошуку: ")
            value = input("Введіть значення поля: ")
            search_data_by_field(filename, field, value)
        elif choice == "5":
            # Виконання завдань за варіантом
            data = load_data(filename)
            if data:
                # а) прізвища пасажирів, які мають більше двох речей
                surnames_more_than_two_items = [record["surname"] for record in data if record.get("num_items") > 2]
                print("Прізвища пасажирів, які мають більше двох речей:", surnames_more_than_two_items)

                # б) кількість пасажирів, у яких вага багажу менше 5 кг, від 5 до 25 кг, перевищує 25 кг
                count_less_than_5kg = sum(1 for record in data if record.get("total_weight") < 5)
                count_between_5_and_25kg = sum(1 for record in data if 5 <= record.get("total_weight") <= 25)
                count_over_25kg = sum(1 for record in data if record.get("total_weight") > 25)
                print("Кількість пасажирів, у яких вага багажу:")
                print(f"- менше 5 кг: {count_less_than_5kg}")
                print(f"- від 5 до 25 кг: {count_between_5_and_25kg}")
                print(f"- більше 25 кг: {count_over_25kg}")
        elif choice == "6":
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()  
