def linear_search(arr, target):
    """
    Последовательный (линейный) поиск
    """
    # Проходим по всем элементам массива
    for i in range(len(arr)):
        # Если нашли целевой элемент, возвращаем его индекс
        if arr[i] == target:
            return i
    
    # Если элемент не найден, возвращаем -1
    return -1

def linear_search_with_steps(arr, target):
    """
    Последовательный поиск с выводом шагов
    """
    print(f"Поиск элемента {target} в массиве: {arr}")
    steps = 0
    
    for i in range(len(arr)):
        steps += 1
        print(f"Шаг {steps}: сравниваем arr[{i}] = {arr[i]} с {target}")
        
        if arr[i] == target:
            print(f"Элемент найден на позиции {i} за {steps} шагов")
            return i
    
    print(f"Элемент не найден. Выполнено {steps} шагов")
    return -1

# Демонстрация работы
if __name__ == "__main__":
    # Пример 1: Простой поиск
    arr = [64, 34, 25, 12, 22, 11, 90]
    target = 22
    
    print("=== Простой линейный поиск ===")
    result = linear_search(arr, target)
    if result != -1:
        print(f"Элемент {target} найден на позиции {result}")
    else:
        print(f"Элемент {target} не найден")
    
    print("\n=== Поиск с выводом шагов ===")
    # Пример 2: Поиск с выводом процесса
    linear_search_with_steps(arr, target)
    
    print("\n=== Поиск отсутствующего элемента ===")
    # Пример 3: Поиск отсутствующего элемента
    linear_search_with_steps(arr, 99)
