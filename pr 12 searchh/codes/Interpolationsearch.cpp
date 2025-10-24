#include <iostream>
#include <vector>
using namespace std;

int interpolationSearch(vector<int>& arr, int target) {
    int low = 0;
    int high = arr.size() - 1;
    
    while (low <= high && target >= arr[low] && target <= arr[high]) {
        // Если границы совпадают
        if (low == high) {
            if (arr[low] == target) return low;
            return -1;
        }
        
        // Вычисляем позицию с помощью интерполяционной формулы
        int pos = low + ((double)(target - arr[low]) / (arr[high] - arr[low])) * (high - low);
        
        // Если элемент найден
        if (arr[pos] == target) {
            return pos;
        }
        
        // Если target меньше, ищем в левой части
        if (arr[pos] > target) {
            high = pos - 1;
        }
        // Если target больше, ищем в правой части
        else {
            low = pos + 1;
        }
    }
    
    return -1; // Элемент не найден
}

// Рекурсивная версия
int interpolationSearchRecursive(vector<int>& arr, int target, int low, int high) {
    if (low <= high && target >= arr[low] && target <= arr[high]) {
        if (low == high) {
            return (arr[low] == target) ? low : -1;
        }
        
        // Интерполяционная формула
        int pos = low + ((double)(target - arr[low]) / (arr[high] - arr[low])) * (high - low);
        
        if (arr[pos] == target) {
            return pos;
        }
        else if (arr[pos] > target) {
            return interpolationSearchRecursive(arr, target, low, pos - 1);
        }
        else {
            return interpolationSearchRecursive(arr, target, pos + 1, high);
        }
    }
    
    return -1;
}

int main() {
    vector<int> arr = {10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47};
    int target = 18;
    
    cout << "Массив: ";
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;
    
    // Итеративная версия
    int result = interpolationSearch(arr, target);
    if (result != -1) {
        cout << "Элемент " << target << " найден на позиции " << result << endl;
    } else {
        cout << "Элемент " << target << " не найден" << endl;
    }
    
    // Рекурсивная версия
    int result2 = interpolationSearchRecursive(arr, target, 0, arr.size() - 1);
    cout << "Рекурсивный поиск: элемент на позиции " << result2 << endl;
    
    return 0;
}
