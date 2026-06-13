"""
Модуль бинарного дерева поиска для хранения расходов по дням
Каждый узел хранит день месяца (ключ) и список расходов в этот день
"""


class TreeNode:
    """
    Узел бинарного дерева поиска

    Атрибуты:
        key (int): номер дня месяца (от 1 до 31).
        expenses (list): список расходов в формате (сумма, категория)
        left_child: левый потомок
        right_child: правый потомок
    """

    def __init__(self, key):
        """
        Создаёт новый узел дерева

        Args:
            key: номер дня месяца
        """
        self.key = key
        self.expenses = []
        self.left_child = None
        self.right_child = None


def insert_expense(tree, day, amount, category):
    """
    Вставляет расход в дерево поиска
    Если день уже есть в дереве, тогда расход добавляется в список узла, а если дня нет, то создаётся новый узел

    Args:
        tree: корень дерева
        day: номер дня
        amount: сумма расхода
        category: название категории
    Returns:
        корень дерева после вставки
    """
    if tree is None:
        new_node = TreeNode(day)
        new_node.expenses.append((amount, category))
        return new_node

    if day < tree.key:
        tree.left_child = insert_expense(
            tree.left_child, day, amount, category
        )
    elif day > tree.key:
        tree.right_child = insert_expense(
            tree.right_child, day, amount, category
        )
    else:
        tree.expenses.append((amount, category))

    return tree


def search_expenses(tree, day):
    """
    Ищет расходы за указанный день в дереве

    Args:
        tree: корень дерева
        day: номер дня
    Returns:
        список расходов (сумма, категория) или пустой список
    """
    if tree is None:
        return []

    if day < tree.key:
        return search_expenses(tree.left_child, day)
    if day > tree.key:
        return search_expenses(tree.right_child, day)

    return list(tree.expenses)


def inorder_collect(tree, result):
    """
    Обходит дерево в порядке inorder и собирает все расходы

    Args:
        tree: текущий узел
        result: список, куда добавляются пары (день, сумма, категория)
    """
    if tree:
        inorder_collect(tree.left_child, result)
        for amount, category in tree.expenses:
            result.append((tree.key, amount, category))
        inorder_collect(tree.right_child, result)


def copy_tree(tree):
    """
    Создаёт копию дерева

    Args:
        tree: корень исходного дерева
    Returns:
        корень копии или None
    """
    if tree is None:
        return None

    new_node = TreeNode(tree.key)
    new_node.expenses = list(tree.expenses)
    new_node.left_child = copy_tree(tree.left_child)
    new_node.right_child = copy_tree(tree.right_child)
    return new_node
