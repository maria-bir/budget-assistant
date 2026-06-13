"""
Модуль префиксных сумм для быстрых запросов за период
"""


def build_prefix_sum(daily_totals):
    """
    Строит массив префиксных сумм по дневным итогам
     
    Args:
        daily_totals: список длиной 32, daily_totals[d] — сумма за день d
    Returns:
        список prefix_sum длиной 
    """
    prefix_sum = [0] * 32
    for day in range(1, 32):
        prefix_sum[day] = prefix_sum[day - 1] + daily_totals[day]
    return prefix_sum


def sum_period(prefix_sum, day_a, day_b):
    """
    Возвращает сумму расходов за период с дня A по день B 

    Args:
        prefix_sum: массив префиксных сумм
        day_a: начало периода
        day_b: конец периода
    Returns:
        сумма расходов за период
    """
    return prefix_sum[day_b] - prefix_sum[day_a - 1]
