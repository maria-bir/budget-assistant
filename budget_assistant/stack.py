"""
Модуль стека для отмены последних добавленных расходов
"""


class UndoStack:
    """
    Стек состояний бюджета до каждого добавления расхода
    Можно отменить 5 добавлений
    """

    def __init__(self, max_size=5):
        """
        Создаёт пустой стек

        Args:
            max_size: количество последних состояний, которые сохраняются
        """
        self.items = []
        self.max_size = max_size

    def push(self, state):
        """
        Кладёт снимок состояния на вершину стека

        Args:
            state: данные для отмены (копия дерева и дневных сумм)
        """
        self.items.append(state)

        if len(self.items) > self.max_size:
            self.items.pop(0)

    def pop(self):
        """
        Снимает и возвращает последнее сохранённое состояние

        Return:
            состояние или None, если стек пуст
        """
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def is_empty(self):
        """
        Проверяет, пуст ли стек

        Return:
            True, если отменять нечего
        """
        return len(self.items) == 0
