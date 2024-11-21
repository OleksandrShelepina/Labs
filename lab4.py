def remove_duplicates(input_list):
    # Зберігаємо порядок елементів, видаляючи дублікати
    seen = set()
    return [x for x in input_list if not (x in seen or seen.add(x))]

def sort_custom(input_list):
    # Розділяємо числа і рядки
    numbers = sorted([x for x in input_list if isinstance(x, (int, float))])
    strings = sorted([x for x in input_list if isinstance(x, str)])
    return numbers + strings

original_list = [3, 1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 6, 5, 4, 3, 4, 5, 4, 3, 'Привіт', 'анаконда']

unique_list = remove_duplicates(original_list)  # Видаляємо дублікати
sorted_list = sort_custom(unique_list)  # Сортуємо список

print("Список без повторень:", unique_list)
print("Відсортований список:", sorted_list)
