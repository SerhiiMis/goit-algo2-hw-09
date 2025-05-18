import random
import math

# 🎯 Sphere function
def sphere_function(x):
    return sum(xi ** 2 for xi in x)

# 🚀 Hill Climbing algorithm
def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    # Стартова точка
    current = [random.uniform(low, high) for (low, high) in bounds]
    current_value = func(current)

    for _ in range(iterations):
        # Генерація сусідньої точки з малим зсувом
        neighbor = [xi + random.uniform(-0.1, 0.1) for xi in current]
        # Обмеження в межах bounds
        neighbor = [max(min(xi, high), low) for xi, (low, high) in zip(neighbor, bounds)]
        neighbor_value = func(neighbor)

        # Якщо покращення достатнє — приймаємо точку
        if current_value - neighbor_value > epsilon:
            current = neighbor
            current_value = neighbor_value
        else:
            break  # Зупинити, якщо немає покращення

    return current, current_value

# 🧪 Порожні заглушки для інших методів (реалізуємо після)
def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    pass

def simulated_annealing(func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6):
    pass

# ▶️ Виконання
if __name__ == "__main__":
    bounds = [(-5, 5), (-5, 5)]

    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Розв'язок:", hc_solution, "Значення:", hc_value)

    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("Розв'язок:", rls_solution, "Значення:", rls_value)

    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("Розв'язок:", sa_solution, "Значення:", sa_value)
