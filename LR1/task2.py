
﻿def знайти_суму_кратних_5(початок, кінець):

  if not isinstance(початок, int) or not isinstance(кінець, int):
    raise ValueError("початок і кінець повинні бути цілими числами")

  if початок > кінець:
    raise ValueError("початок повинен бути меншим або дорівнювати кінцю")

  сума = 0
  for число in range(початок, кінець + 1):
    if число % 5 == 0:
      сума += число

  return сума

# Введення даних користувачем
початок = int(input(500))
кінець = int(input(1000))

# Обчислення суми
сума = знайти_суму_кратних_5(початок, кінець)

# Виведення результату
print(f"Сума кратних 5 в діапазоні від {початок} до {кінець}: {сума}")