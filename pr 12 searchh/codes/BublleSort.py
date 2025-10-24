def bubble_sort(arr):
    """
    Сортировка пузырьком (обменом)
    """
    n = len(arr)
    
    # Проходим по всем элементам массива
    for i in range(n):
        # Флаг для оптимизации - если не было обменов, массив отсортирован
        swapped = False
        
        # Последние i элементов уже на своих местах
        for j in range(0, n - i - 1):
            # Сравниваем соседние элементы
            if arr[j] > arr[j + 1]:
                # Меняем местами, если они в неправильном порядке
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # Если не было обменов, массив уже отсортирован
        if not swapped:
            break
    
    return arr

def bubble_sort_simple(arr):
    """
    Простая версия без оптимизации (для демонстрации сложности)
    """
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr

# Демонстрация работы
if __name__ == "__main__":
    # Тестовые данные
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    arr2 = [5, 1, 4, 2, 8]
    
    print("Исходный массив 1:", arr1)
    sorted_arr1 = bubble_sort(arr1.copy())
    print("Отсортированный массив 1:", sorted_arr1)
    
    print("\nИсходный массив 2:", arr2)
    sorted_arr2 = bubble_sort(arr2.copy())
    print("Отсортированный массив 2:", sorted_arr2)
    
    # Демонстрация пошагового выполнения
    print("\n--- Пошаговое выполнение ---")
    test_arr = [5, 1, 4, 2, 8]
    print("Начальный массив:", test_arr)
    
    n = len(test_arr)
    for i in range(n):
        swapped = False
        print(f"\nПроход {i + 1}:")
        
        for j in range(0, n - i - 1):
            comparison = f"{test_arr[j]} > {test_arr[j + 1]}"
            if test_arr[j] > test_arr[j + 1]:
                test_arr[j], test_arr[j + 1] = test_arr[j + 1], test_arr[j]
                swapped = True
                print(f"  Сравнение {comparison} - ДА, меняем: {test_arr}")
            else:
                print(f"  Сравнение {comparison} - нет")
        
        if not swapped:
            print("  Обменов не было, завершаем раньше")
            break
    
    print("Финальный массив:", test_arr)
