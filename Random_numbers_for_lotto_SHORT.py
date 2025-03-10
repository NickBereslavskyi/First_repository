import random

def get_numbers_ticket(min_value: int, max_value: int, quantity: int) -> list:
    """
    Генерує унікальний набір випадкових чисел у заданому діапазоні та повертає відсортований список.
    
    :param min_value: Мінімальне можливе число у наборі (не менше 1).
    :param max_value: Максимальне можливе число у наборі (не більше 1000).
    :param quantity: Кількість чисел, які потрібно вибрати.
    :return: Відсортований список унікальних випадкових чисел або пустий список при некоректних параметрах.
    """
    if not (1 <= min_value <= max_value <= 1000) or not (min_value <= quantity <= max_value):
        return []
    
    return sorted(random.sample(range(min_value, max_value + 1), quantity))

# Приклад використання
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)