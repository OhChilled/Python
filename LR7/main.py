def main():
  # Введення даних про багаж для кожного пасажира
  baggage_data = []
  for i in range(1, 11):
      print(f"Дані для пасажира {i}:")
      num_items = int(input("Кількість речей у багажі: "))
      total_weight = float(input("Загальна вага багажу (кг): "))
      baggage_data.append((num_items, total_weight))

  # a) Кількість пасажирів, які мають більше двох речей
  passengers_more_than_two_items = sum(1 for num_items, _ in baggage_data if num_items > 2)
  print("a) Кількість пасажирів, які мають більше двох речей:", passengers_more_than_two_items)

  # b) Чи є хоч один пасажир, багаж якого складається з однієї речі вагою менше 25 кг
  has_passenger_under_25kg = any(total_weight < 25 for _, total_weight in baggage_data)
  print("б) Чи є хоч один пасажир, багаж якого складається з однієї речі вагою менше 25 кг:", has_passenger_under_25kg)

  # в) Номери багажів, в яких вага однієї речі відрізняється від середньої ваги на не більше 0,5 кг
  average_weight = sum(total_weight / num_items for num_items, total_weight in baggage_data) / len(baggage_data)
  close_to_average = [i + 1 for i, (num_items, total_weight) in enumerate(baggage_data) if abs(total_weight / num_items - average_weight) <= 0.5]
  print("в) Номери багажів, в яких вага однієї речі відрізняється від середньої ваги на не більше 0,5 кг:", close_to_average)

if __name__ == "__main__":
  main()
