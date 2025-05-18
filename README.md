# 🎯 Local Search Algorithms for Sphere Function Minimization

## 📘 Task Description

The goal is to minimize the **Sphere function**  
\[
f(x) = \sum\_{i=1}^{n} x_i^2
\]  
using three local optimization algorithms:

1. **Hill Climbing**
2. **Random Local Search**
3. **Simulated Annealing**

---

## ✅ Technical Conditions

- Search space: each coordinate \( x_i \in [-5, 5] \)
- Each algorithm must return:
  - Coordinates of the optimal solution
  - Function value at that point
- All functions must accept:
  - `iterations` (max number of steps)
  - `epsilon` (convergence threshold)
- Simulated Annealing also accepts:
  - `temp` (initial temperature)
  - `cooling_rate`

---

## ⚙️ Function Signature

```python
def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6): ...
def random_local_search(func, bounds, iterations=1000, epsilon=1e-6): ...
def simulated_annealing(func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6): ...
```

---

## 🧪 Example Output

```
Hill Climbing:
Розв'язок: [0.00053, 0.00078] Значення: 9.04e-07

Random Local Search:
Розв'язок: [0.0308, 0.1054] Значення: 0.0120

Simulated Annealing:
Розв'язок: [0.0245, -0.0048] Значення: 0.00062
```

---

## 🚀 Run the script

```bash
python local_search.py
```

---
