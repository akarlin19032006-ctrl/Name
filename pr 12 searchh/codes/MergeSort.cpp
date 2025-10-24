#include <iostream>
#include <vector>
using namespace std;

// Функция слияния двух отсортированных массивов
void merge(vector<int>& arr, int left, int mid, int right) {
    int n1 = mid - left + 1;  // размер левого подмассива
    int n2 = right - mid;     // размер правого подмассива
    
    // Создаем временные массивы
    vector<int> leftArr(n1);
    vector<int> rightArr(n2);
    
    // Копируем данные во временные массивы
    for (int i = 0; i < n1; i++)
        leftArr[i] = arr[left + i];
    for (int j = 0; j < n2; j++)
        rightArr[j] = arr[mid + 1 + j];
    
    // Слияние временных массивов обратно в arr
    int i = 0, j = 0, k = left;
    
    while (i < n1 && j < n2) {
        if (leftArr[i] <= rightArr[j]) {
            arr[k] = leftArr[i];
            i++;
        } else {
            arr[k] = rightArr[j];
            j++;
        }
        k++;
    }
    
    // Копируем оставшиеся элементы leftArr
    while (i < n1) {
        arr[k] = leftArr[i];
        i++;
        k++;
    }
    
    // Копируем оставшиеся элементы rightArr
    while (j < n2) {
        arr[k] = rightArr[j];
        j++;
        k++;
    }
}

// Рекурсивная функция сортировки слиянием
void mergeSort(vector<int>& arr, int left, int right) {
    if (left >= right) return;  // базовый случай
    
    int mid = left + (right - left) / 2;
    
    // Рекурсивно сортируем две половины
    mergeSort(arr, left, mid);
    mergeSort(arr, mid + 1, right);
    
    // Сливаем отсортированные половины
    merge(arr, left, mid, right);
}

// Вспомогательная функция для вывода массива
void printArray(const vector<int>& arr) {
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;
}

int main() {
    vector<int> arr = {12, 11, 13, 5, 6, 7};
    
    cout << "Исходный массив: ";
    printArray(arr);
    
    mergeSort(arr, 0, arr.size() - 1);
    
    cout << "Отсортированный массив: ";
    printArray(arr);
    
    return 0;
}
