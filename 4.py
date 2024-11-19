def remove_duplicates(input_list):
    """
    Видаляє повторення зі списку.
    """
    return list(set(input_list))

def sort_custom(input_list):
    """
    Сортує список: числа за зростанням, рядки в алфавітному порядку.
    """
    numbers = sorted([item for item in input_list if isinstance(item, (int, float))])
    strings = sorted([item for item in input_list if isinstance(item, str)])
    return numbers + strings


original_list = [3, 1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 6, 5, 4, 3, 4, 5, 4, 3, 'Привіт', 'анаконда']


unique_list = remove_duplicates(original_list)
sorted_list = sort_custom(unique_list)

print("Список без повторень:", unique_list)
print("Відсортований список:", sorted_list)


