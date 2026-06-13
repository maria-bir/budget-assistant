"""
Точка входа в программу «Бюджетный помощник»1
"""

from budget_assistant.budget_manager import BudgetManager


def print_menu():
    """Выводит главное меню программы"""
    print()
    print("=" * 45)
    print("       БЮДЖЕТНЫЙ ПОМОЩНИК")
    print("=" * 45)
    print("1. Добавить расход")
    print("2. Сумма расходов за период")
    print("3. День с максимальными расходами")
    print("4. Категории по сумме трат")
    print("5. Отменить последнее добавление")
    print("6. Показать расходы за день")
    print("7. Показать все расходы за месяц")
    print("0. Выход")
    print("=" * 45)


def read_int(prompt):
    """
    Считывает целое число с проверкой ввода

    Args:
        prompt: текст приглашения
    Return:
        введённое число или None при ошибке
    """
    text = input(prompt)
    try:
        return int(text)
    except ValueError:
        print("Ошибка: нужно ввести целое число")
        return None


def read_float(prompt):
    """
    Считывает число с плавающей точкой

    Args:
        prompt: текст приглашения
    Return:
        введённое число или None при ошибке
    """
    text = input(prompt)
    try:
        return float(text.replace(",", "."))
    except ValueError:
        print("Ошибка: нужно ввести число (например, 150.50)")
        return None


def handle_add_expense(budget):
    """Обрабатывает пункт меню «Добавить расход»"""
    day = read_int("Введите день (1-31): ")
    if day is None:
        return

    amount = read_float("Введите сумму (руб.): ")
    if amount is None:
        return

    if amount < 0:
        print("Ошибка: сумма не может быть отрицательной")
        return

    category = input("Введите категорию (например, еда): ").strip()
    if category == "":
        print("Ошибка: категория не может быть пустой")
        return

    if budget.add_expense(day, amount, category):
        print("Расход успешно добавлен")
    else:
        print("Ошибка: день должен быть от 1 до 31")


def handle_period_sum(budget):
    """Обрабатывает запрос суммы за период"""
    day_a = read_int("Введите начало периода (день A): ")
    if day_a is None:
        return

    day_b = read_int("Введите конец периода (день B): ")
    if day_b is None:
        return

    result = budget.get_period_sum(day_a, day_b)
    if result is None:
        print("Ошибка: проверьте дни (1-31) и что A <= B")
    else:
        print("Сумма за период с", day_a, "по", day_b, ":", round(result, 2), "руб.")


def handle_max_day(budget):
    """Показывает день с максимальными расходами"""
    max_day, max_sum = budget.get_max_expense_day()
    if max_day == 0:
        print("Расходов пока нет.")
    else:
        print("Максимальные расходы в день", max_day, ":", round(max_sum, 2), "руб.")


def handle_sorted_categories(budget):
    """
    Выводит результат сортировки вставками

    Сначала считаются суммы по категориям за все дни, затем список (категория, сумма) сортируется по убыванию
    """
    sorted_list = budget.get_sorted_categories()
    if len(sorted_list) == 0:
        print("Расходов пока нет.")
        return

    print("Категории по убыванию суммы трат:")
    for i in range(len(sorted_list)):
        category = sorted_list[i][0]
        total = sorted_list[i][1]
        print(" ", i + 1, ".", category, "—", round(total, 2), "руб.")


def handle_undo(budget):
    """Отменяет последнее добавление через стек"""
    if budget.undo_last_expense():
        print("Последнее добавление отменено")
    else:
        print("Нечего отменять.")


def handle_day_expenses(budget):
    """Показывает расходы за один день (поиск в дереве)"""
    day = read_int("Введите день (1-31): ")
    if day is None:
        return

    expenses = budget.get_expenses_by_day(day)
    if expenses is None:
        print("Ошибка: день должен быть от 1 до 31")
        return

    if len(expenses) == 0:
        print("В этот день расходов нет")
        return

    print("Расходы за день", day, ":")
    day_total = 0.0
    for i in range(len(expenses)):
        amount = expenses[i][0]
        category = expenses[i][1]
        day_total = day_total + amount
        print(" ", i + 1, ".", category, "—", round(amount, 2), "руб.")
    print("Итого за день:", round(day_total, 2), "руб.")


def handle_all_expenses(budget):
    """Показывает все расходы за месяц"""
    all_expenses = budget.get_all_expenses()
    if len(all_expenses) == 0:
        print("Расходов пока нет.")
        return

    print("Все расходы за месяц:")
    for i in range(len(all_expenses)):
        day = all_expenses[i][0]
        amount = all_expenses[i][1]
        category = all_expenses[i][2]
        print(" ", i + 1, ". День", day, "—", category, "—", round(amount, 2), "руб.")


def main():
    """Главный цикл программы с консольным меню"""
    budget = BudgetManager()
    print("Добро пожаловать в «Бюджетный помощник»!")

    while True:
        print_menu()
        choice = input("Выберите пункт меню: ").strip()

        if choice == "1":
            handle_add_expense(budget)
        elif choice == "2":
            handle_period_sum(budget)
        elif choice == "3":
            handle_max_day(budget)
        elif choice == "4":
            handle_sorted_categories(budget)
        elif choice == "5":
            handle_undo(budget)
        elif choice == "6":
            handle_day_expenses(budget)
        elif choice == "7":
            handle_all_expenses(budget)
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Неверный пункт меню. Попробуйте снова")


if __name__ == "__main__":
    main()
