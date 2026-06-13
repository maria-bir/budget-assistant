"""
Модуль сортировки вставками для категорий расходов
"""

def insertion_sort_categories(category_list):
    """
    Сортирует список пар (категория, сумма) методом вставок по убыванию суммы

    Args:
        category_list: список вида [[категория, сумма], ...].
    Returns:
        отсортированный список
    """
    for i in range(1, len(category_list)):
        value = category_list[i]
        j = i
       
        while j > 0 and category_list[j - 1][1] < value[1]:
            category_list[j] = category_list[j - 1]
            j = j - 1
        category_list[j] = value

    return category_list
