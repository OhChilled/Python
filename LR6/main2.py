def replace_negatives_with_zeroes(input_list):
  # Проходимося по кожному елементу списку
  for i in range(len(input_list)):
      # Перевіряємо, чи є елемент від'ємним
      if input_list[i] < 0:
          # Якщо так, замінюємо його на 0
          input_list[i] = 0

# Функція для отримання списку від користувача
def get_user_list():
  user_input = input("Введіть елементи списку через пробіл: ")
  user_list = list(map(int, user_input.split()))
  return user_list

# Отримання списку від користувача
user_list = get_user_list()

# Заміна всіх від'ємних елементів на 0
replace_negatives_with_zeroes(user_list)

# Вивід результату
print("Список після заміни від'ємних елементів на 0:", user_list)
