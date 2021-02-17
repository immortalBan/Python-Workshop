import random as rd

input_numbers = [int(input()) for _ in range(10)]

random_nambers = [random.randint(0, 20) for _ in range(10)]

if sum(input_numbers) => sum(random_nambers):
    print("Сумма случайных чисел не больше введённых")
else:
    print("Сумма случайных чисел боль введённых")
