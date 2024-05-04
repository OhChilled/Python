def count_letters_in_words(sentence):
  words = sentence.split()
  letter_counts = {}

  for word in words:
      letter_counts[word] = len(word)

  return letter_counts

# Задане речення
sentence = "Вчення в щасті украшає, а в нещасті утішає."

# Виклик функції для підрахунку кількості літер у кожному слові
result = count_letters_in_words(sentence)

# Виводимо результат
for word, count in result.items():
  print(f"Кількість літер у слові '{word}': {count}")
