def fibonacci_search(arr, target):
    """
    Поиск Фибоначчи в отсортированном массиве
    """
    n = len(arr)
    
    # Инициализируем числа Фибоначчи
    fib_m2 = 0  # F(m-2)
    fib_m1 = 1  # F(m-1)
    fib_m = fib_m2 + fib_m1  # F(m)
    
    # Находим наименьшее число Фибоначчи, большее или равное n
    while fib_m < n:
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m2 + fib_m1
    
    # Инициализируем переменные для поиска
    offset = -1
    comparisons = 0
    
    while fib_m > 1:
        comparisons += 1
        # Проверяем валидность индекса
        i = min(offset + fib_m2, n - 1)
        
        print(f"Сравнение {comparisons}: индекс={i}, значение={arr[i]}, ищем={target}")
        
        # Если target больше, сдвигаемся вправо
        if arr[i] < target:
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = i
        # Если target меньше, сдвигаемся влево
        elif arr[i] > target:
            fib_m = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib_m - fib_m1
        # Если нашли элемент
        else:
            print(f"Элемент найден за {comparisons} сравнений")
            return i
    
    # Проверяем последний элемент
    if fib_m1 and offset + 1 < n and arr[offset + 1] == target:
        print(f"Элемент найден за {comparisons + 1} сравнений")
        return offset + 1
    
    print(f"Элемент не найден. Выполнено {comparisons} сравнений")
    return -1

def generate_fibonacci_sequence(n):
    """
    Генерирует последовательность Фибоначчи до числа >= n
    """
    fib = [0, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    return fib

# Демонстрация работы
if __name__ == "__main__":
    # Отсортированный массив
    arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
    target = 85
    
    print("Массив:", arr)
    print("Ищем элемент:", target)
    print("Последовательность Фибоначчи:", generate_fibonacci_sequence(len(arr)))
    print()
    
    result = fibonacci_search(arr, target)
    
    if result != -1:
        print(f"Элемент {target} найден на позиции {result}")
    else:
        print(f"Элемент {target} не найден")
