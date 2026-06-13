"""
Модуль линейного поиска дня с максимальными расходами
"""


def find_max_expense_day(daily_totals):
    """
    Линейным поиском находит день с наибольшей суммой расходов

    Args:
        daily_totals: список дней
    Returns: 
        кортеж (день, сумма), если расходов нет (0, 0.0)
    """
    max_day = 0
    max_sum = 0.0

    for day in range(1, 32):
        day_sum = daily_totals[day]
        if day_sum > max_sum:
            max_sum = day_sum
            max_day = day

    return max_day, max_sum
