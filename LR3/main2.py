def sort_letters(word):
    vowels = "аеіоуАЕІОУ"
    consonants = ""

    # Розділення літер слова на голосні та приголосні
    for letter in word:
      if letter in vowels:
          print(letter)
      else:
          consonants += letter

    # Виведення приголосних літер
    print(consonants)

    # Задане слово
word = input("Введіть слово: ")

    # Виклик функції для сортування літер
sort_letters(word)

