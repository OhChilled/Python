# Отримання розміру масиву від користувача
N = int(input("Введіть розмір масиву: "))

# Ініціалізація масиву
array = []

# Отримання елементів масиву від користувача
for i in range(N):
    element = float(input(f"Введіть {i+1}-й елемент масиву: "))
    array.append(element)

# Ініціалізуємо змінну для зберігання мінімального від'ємного елементу
min_negative_element = None

# Перевіряємо кожен елемент масиву
for element in array:
    if element < 0:  # Перевіряємо, чи елемент від'ємний
        if min_negative_element is None or element < min_negative_element:
            min_negative_element = element

# Виводимо результат
if min_negative_element is None:
    print("У введеному масиві немає від'ємних елементів.")
else:
    print("Мінімальний від'ємний елемент:", min_negative_element)
