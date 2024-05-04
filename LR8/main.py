def show_all_students():
  try:
      # Імпортуємо словник students_dict з файлу stud.py
      from stud import students_dict

      # Виводимо інформацію про всіх студентів
      print("Інформація про всіх студентів:")
      for student, info in students_dict.items():
          print(f"{student}: {info}")
  except ImportError:
      print("Помилка: файл stud.py не знайдено або він не містить словника students_dict.")

# Викликаємо функцію для відображення всіх студентів
show_all_students()

def add_student_info(students_dict):
  # Запитати користувача про дані нового студента
  group_number = input("Введіть номер групи: ")
  full_name = input("Введіть прізвище, ім'я та по батькові: ")
  course = int(input("Введіть курс: "))
  subjects = input("Введіть предмети через кому: ").split(',')
  grades = input("Введіть оцінки через кому: ").split(',')

  # Перевірка на коректність введених даних
  if len(subjects) != len(grades):
      print("Помилка: кількість предметів не відповідає кількості оцінок.")
      return

  # Додавання нового студента до словника
  students_dict[full_name] = {
      "group_number": group_number,
      "course": course,
      "subjects": subjects,
      "grades": grades
  }

  print("Інформація про студента успішно додана.")


def main():
  # Ініціалізація словника для зберігання інформації про студентів
  students_dict = {}

  # Додавання даних про студентів
  add_student_info(students_dict)

  # Виведення словника на екран для перевірки
  print("\nІнформація про студентів:")
  for student, info in students_dict.items():
      print(f"{student}: {info}")

  # Збереження даних у файлі stud.py
  with open("stud.py", "w") as file:
      file.write("students_dict = ")
      file.write(repr(students_dict))

if __name__ == "__main__":
  main()  
