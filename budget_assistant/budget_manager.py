"""
Класс, который связывает дерево, префиксные суммы, стек отмены и остальные алгоритмы
"""

from budget_assistant.tree import (
    insert_expense,
    search_expenses,
    inorder_collect,
    copy_tree,
)
from budget_assistant.prefix_sum import build_prefix_sum, sum_period
from budget_assistant.linear_search import find_max_expense_day
from budget_assistant.insertion_sort import insertion_sort_categories
from budget_assistant.stack import UndoStack


class BudgetManager:
    """
    Хранит расходы за месяц и выполняет все операции из задания
    """

    def __init__(self):
        """Создаёт пустой бюджет на 31 день"""
        self.tree = None
        self.daily_totals = [0.0] * 32
        self.prefix_sum = build_prefix_sum(self.daily_totals)
        self.undo_stack = UndoStack(max_size=5)

    def _save_state_for_undo(self):
        """Сохраняет текущее состояние в стек перед добавлением расхода"""
        state = {
            "tree": copy_tree(self.tree),
            "daily_totals": list(self.daily_totals),
        }
        self.undo_stack.push(state)

    def _rebuild_prefix_sum(self):
        """Пересчитывает массив префиксных сумм после изменения данных"""
        self.prefix_sum = build_prefix_sum(self.daily_totals)

    def add_expense(self, day, amount, category):
        """
        Добавляет расход и обновляет структуры данных

        Args:
            day: день месяца (1–31)
            amount: сумма расхода
            category: категория (строка)
        Return: 
            True, если все верно, False если день неверный
        """
        if day < 1 or day > 31:
            return False

        self._save_state_for_undo()
        self.tree = insert_expense(self.tree, day, amount, category)
        self.daily_totals[day] = self.daily_totals[day] + amount
        self._rebuild_prefix_sum()
        return True

    def get_period_sum(self, day_a, day_b):
        """
        Возвращает сумму расходов за период A-B

        Return: сумма или None, если дни указаны неверно
        """
        if day_a < 1 or day_b > 31 or day_a > day_b:
            return None
        return sum_period(self.prefix_sum, day_a, day_b)

    def get_max_expense_day(self):
        """
        Находит день с максимальными расходами (линейный поиск)

        Return:
            кортеж (день, сумма)
        """
        return find_max_expense_day(self.daily_totals)

    def get_sorted_categories(self):
        """
        Считает суммы по категориям и сортирует вставками по убыванию

        Return:
            отсортированный список [категория, сумма]
        """
        all_expenses = []
        inorder_collect(self.tree, all_expenses)

        category_totals = {}
        for day, amount, category in all_expenses:
            if category in category_totals:
                category_totals[category] = category_totals[category] + amount
            else:
                category_totals[category] = amount

        category_list = []
        for category in category_totals:
            category_list.append([category, category_totals[category]])

        return insertion_sort_categories(category_list)

    def undo_last_expense(self):
        """
        Отменяет последнее добавление расхода через стек

        Return:
            True, если отмена прошла успешно
        """
        state = self.undo_stack.pop()
        if state is None:
            return False

        self.tree = state["tree"]
        self.daily_totals = list(state["daily_totals"])
        self._rebuild_prefix_sum()
        return True

    def get_expenses_by_day(self, day):
        """
        Возвращает список расходов за один день (поиск в дереве)

        Args:
            day: номер дня (1–31)
        Return:
            список пар (сумма, категория) или None
        """
        if day < 1 or day > 31:
            return None
        return search_expenses(self.tree, day)

    def get_all_expenses(self):
        """
        Возвращает все расходы за месяц в порядке возрастания дня

        Return:
            список кортежей (день, сумма, категория)
        """
        result = []
        inorder_collect(self.tree, result)
        return result
