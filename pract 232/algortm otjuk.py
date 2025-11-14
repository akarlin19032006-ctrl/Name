import math
import random

def f(x):
    return (x - 7) ** 2 + 5

def simulated_annealing():
    # Ввод диапазона поиска
    a = float(input("Введите начало диапазона: "))
    b = float(input("Введите конец диапазона: "))
    
    # Параметры алгоритма
    start_temp = 1000
    min_temp = 1e-5
    alpha = 0.99
    max_iter = 100
    
    # Инициализация
    current = random.uniform(a, b)
    current_energy = f(current)
    temp = start_temp
    best_x, best_energy = current, current_energy
    
    while temp > min_temp:
        for _ in range(max_iter):
            # Генерация соседнего решения
            neighbor = current + random.uniform(-1, 1)
            # Проекция на диапазон [a, b]
            neighbor = max(a, min(b, neighbor))
            
            neighbor_energy = f(neighbor)
            delta_energy = neighbor_energy - current_energy
            
            # Принятие решения о переходе
            if delta_energy < 0 or random.random() < math.exp(-delta_energy / temp):
                current = neighbor
                current_energy = neighbor_energy
                
                if current_energy < best_energy:
                    best_x, best_energy = current, current_energy
                    
        temp *= alpha
    
    print(f"Найденный минимум: f({best_x:.5f}) = {best_energy:.5f}")

if __name__ == "__main__":
    simulated_annealing()
