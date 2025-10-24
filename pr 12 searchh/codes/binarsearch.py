def binary_search(arr, target):
    """
    Бинарный (двоичный) поиск
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2  # Находим середину
        
        # Если элемент в середине - это целевой элемент
        if arr[mid] == target:
            return mid
        
        # Если целевой элемент меньше, игнорируем правую половину
        elif arr[mid] > target:
            right = mid - 1
        
        # Если целевой элемент больше, игнорируем левую половину
        else:
            left = mid + 1
    
    # Если элемент не найден
    return -1

def binary_search_recursive(arr, target, left=0, right=None):
    """
    Рекурсивная версия бинарного поиска
    """
    if right is None:
        right = len(arr) - 1
    
    # Базовый случай - элемент не найден
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    # Базовый случай - элемент найден
    if arr[mid] == target:
        return mid
    
    # Рекурсивные случаи
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, right)

def binary_search_with_steps(arr, target):
    """
    Бинарный поиск с выводом шагов
    """
    left = 0
    right = len(arr) - 1
    steps = 0
    
    print(f"Поиск элемента {target} в отсортированном массиве: {arr}")
    
    while left <= right:
        steps += 1
        mid = (left + right) // 2
        print(f"Шаг {steps}: left={left}, right={right}, mid={mid}, arr[mid]={arr[mid]}")
        
        if arr[mid] == target:
            print(f"Элемент найден на позиции {mid} за {steps} шагов")
            return mid
        elif arr[mid] > target:
            print(f"  {arr[mid]} > {target} → ищем в левой половине")
            right = mid - 1
        else:
            print(f"  {arr[mid]} < {target} → ищем в правой половине")
            left = mid + 1
    
    print(f"Элемент не найден. Выполнено {steps} шагов")
    return -1

# Демонстрация работы
if __name__ == "__main__":
    # Важно: массив должен быть отсортирован!
    arr = [11, 12, 22, 25, 34, 64, 90]
    target = 22
    
    print("=== Итеративный бинарный поиск ===")
    result = binary_search(arr, target)
    print(f"Элемент {target} найден на позиции {result}" if result != -1 
          else f"Элемент {target} не найден")
    
    print("\n=== Рекурсивный бинарный поиск ===")
    result = binary_search_recursive(arr, target)
    print(f"Элемент {target} найден на позиции {result}" if result != -1 
          else f"Элемент {target} не найден")
    
    print("\n=== Поиск с выводом шагов ===")
    binary_search_with_steps(arr, target)
    
    print("\n=== Поиск отсутствующего элемента ===")
    binary_search_with_steps(arr, 99)
