def quick_sort(arr):
    """
    Быстрая сортировка (Quick Sort)
    """
    if len(arr) <= 1:
        return arr
    
    # Выбираем опорный элемент (pivot)
    pivot = arr[len(arr) // 2]
    
    # Разделяем массив на три части
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Рекурсивно сортируем левую и правую части
    return quick_sort(left) + middle + quick_sort(right)

# Версия с сортировкой на месте (in-place)
def quick_sort_inplace(arr, low=0, high=None):
    """
    Быстрая сортировка на месте (менее читаемая, но более эффективная)
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Получаем индекс опорного элемента
        pi = partition(arr, low, high)
        
        # Рекурсивно сортируем элементы до и после опорного
        quick_sort_inplace(arr, low, pi - 1)
        quick_sort_inplace(arr, pi + 1, high)

def partition(arr, low, high):
    """
    Функция разделения массива
    """
    # Выбираем последний элемент как опорный
    pivot = arr[high]
    
    # Индекс меньшего элемента (позиция опорного)
    i = low - 1
    
    for j in range(low, high):
        # Если текущий элемент меньше или равен опорному
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Помещаем опорный элемент на правильную позицию
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Демонстрация работы
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Исходный массив:", arr)
    
    # Простая версия
    sorted_arr = quick_sort(arr.copy())
    print("Отсортированный массив (простая версия):", sorted_arr)
    
    # In-place версия
    quick_sort_inplace(arr)
    print("Отсортированный массив (in-place версия):", arr)
