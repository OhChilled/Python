def split_list(input_list):
  # Ініціалізуємо два окремих списки для цифр і літер
  digits = []
  letters = []

  # Розділяємо елементи списку на цифри і літери
  for item in input_list:
      if str(item).isdigit():
          digits.append(item)
      elif str(item).isalpha():
          letters.append(item)

  return digits, letters

# Отримання списку від користувача
def get_user_list():
  user_input = input("Введіть елементи списку через пробіл: ")
  user_list = user_input.split()
  return user_list

# Отримання списку від користувача
user_list = get_user_list()

# Розділення списку на цифри і літери
digits, letters = split_list(user_list)

# Вивід результату
print("Список цифр:", digits)
print("Список літер:", letters)
