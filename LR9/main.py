def create_file(filename):
  try:
      # Створення текстового файлу з рядками латинських букв різної довжини
      with open(filename, 'w') as file:
          lines = ["aBc", "dEfG", "hIjKL", "mnOPqr", "stUVWxy", "Z"]
          for line in lines:
              file.write(line + '\n')
      print(f"Файл {filename} успішно створено.")
  except IOError:
      print(f"Помилка: не вдалося створити файл {filename}.")

def modify_file(input_filename, output_filename):
  try:
      # Читання вмісту з файлу TF26_1 і заміна великих літер на малі
      with open(input_filename, 'r') as input_file:
          content = input_file.read()
          modified_content = content.lower()

      # Запис зміненого вмісту у файл TF26_2
      with open(output_filename, 'w') as output_file:
          output_file.write(modified_content)
      print(f"Змінений вміст успішно записано у файл {output_filename}.")
  except IOError:
      print(f"Помилка: не вдалося змінити або записати вміст у файл {output_filename}.")

def print_file_content(filename):
  try:
      # Читання вмісту з файлу і його виведення по рядках
      with open(filename, 'r') as file:
          print(f"Вміст файлу {filename}:")
          for line in file:
              print(line.strip())
  except IOError:
      print(f"Помилка: не вдалося прочитати файл {filename}.")

def main():
  # Назви файлів
  input_file = "TF26_1.txt"
  output_file = "TF26_2.txt"

  # Створення текстового файлу з рядками латинських букв
  create_file(input_file)

  # Модифікація файлу: заміна великих літер на малі
  modify_file(input_file, output_file)

  # Друкування вмісту файлу з малими літерами
  print_file_content(output_file)

if __name__ == "__main__":
  main()
