def count_vowels(text):
  # Ініціалізуємо множину голосних літер
  vowels = {'a', 'e', 'i', 'o', 'u', 'y'}

  # Ініціалізуємо лічильник голосних літер
  count = 0

  # Перевіряємо кожен символ у тексті
  for char in text:
      # Перевіряємо, чи є символ голосною літерою
      if char.lower() in vowels:
          count += 1

  return count

# Отримання тексту від користувача
text = input("Введіть текст: ")

# Визначення кількості голосних літер у тексті
vowel_count = count_vowels(text)

# Виведення результату
print("Кількість голосних літер у тексті:", vowel_count)
