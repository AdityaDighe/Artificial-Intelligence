# Get the code checked once

import random

def objective_function(x):
    return x ** 2

def hill_climbing(max_iterations, step_size, initial_solution):
    current_solution = initial_solution
    current_value = objective_function(current_solution)

    for _ in range(max_iterations):
        neighbor = current_solution + random.uniform(-step_size, step_size)
        neighbor_value = objective_function(neighbor)

        if neighbor_value > current_value:
            current_solution = neighbor
            current_value = neighbor_value

    return current_solution, current_value

max_iterations = 100
step_size = 0.1
initial_solution = random.uniform(-10, 10)

best_solution, best_value = hill_climbing(max_iterations, step_size, initial_solution)

print(f"Best solution found: x = {best_solution}")
print(f"Objective function value at the best solution: {best_value}")
