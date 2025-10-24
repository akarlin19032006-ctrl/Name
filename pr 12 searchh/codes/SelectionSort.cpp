#include <iostream>
#include <vector>

void selectionSort(std::vector<int>& arr) {
    int n = arr.size();
    
    // Проходим по всем элементам массива
    for (int i = 0; i < n - 1; i++) {
        // Находим индекс минимального элемента в неотсортированной части
        int minIndex = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        
        // Меняем местами найденный минимальный элемент с первым неотсортированным
        if (minIndex != i) {
            std::swap(arr[i], arr[minIndex]);
        }
    }
}

// Вспомогательная функция для вывода массива
void printArray(const std::vector<int>& arr) {
    for (int num : arr) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
}

int main() {
    std::vector<int> arr = {64, 25, 12, 22, 11};
    
    std::cout << "Исходный массив: ";
    printArray(arr);
    
    selectionSort(arr);
    
    std::cout << "Отсортированный массив: ";
    printArray(arr);
    
    return 0;
}
