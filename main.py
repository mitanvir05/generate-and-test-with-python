import random

def find_solution(func, target, inputs, max_iter=1000):
    for i in range(max_iter):
        x = random.choice(inputs)
        y = func(x)
        if y == target:
            return x, y

    return None

def example_function(x):
    return x**2 - 5*x + 6

inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9]


x, y = find_solution(example_function, 0, inputs)

print(f"x = {x}, y = {y}.")