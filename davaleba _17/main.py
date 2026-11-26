
# ამოცანა 1.1 - ფუნქციების ლექსიკონი


def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b

operations = {
    "add": add,
    "sub": sub,
    "mul": mul,
    "div": div,
}

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operation (add, sub, mul, div): ").strip().lower()

if op in operations:
    func = operations[op]
    print("Result:", func(a, b))
else:
    print("Unknown operation")


# 2. დეკორატორები
# ამოცანა 2.1 - მისალმება


def greet(func):
    def wrapper(*args, **kwargs):
        print("Starting...")
        result = func(*args, **kwargs)
        print("Done!")
        return result
    return wrapper


@greet
def say_sum(x, y):
    return x + y

print(say_sum(3, 4))



# ამოცანა 2.2 - დროის გაზომვა


import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} executed in {end - start:.4f} seconds")
        return result
    return wrapper


@timer
def big_loop(n):
    total = 0
    for i in range(n):
        total += i
    return total

print(big_loop(10_000_000))



# 3. დეკორატორი პარამეტრით
# ამოცანა 3.1 - მინიმალური ასაკი


def min_age(limit):
    def decorator(func):
        @wraps(func)
        def wrapper(age, *args, **kwargs):
            if age < limit:
                print("Access denied")
                return None
            return func(age, *args, **kwargs)
        return wrapper
    return decorator


@min_age(18)
def enter_club(age):
    print("Welcome!")

enter_club(20)  # Welcome!
enter_club(15)  # Access denied



# ამოცანა 3.2 - ხელახლა ცდა


import random

def retry(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    pass
            print("All attempts failed")
        return wrapper
    return decorator


@retry(5)
def random_division():
    number = random.randint(0, 3)  # 25%-იანი შანსით მივიღებთ 0-ს
    print(f"Dividing 10 by {number}")
    result = 10 / number
    print(f"Result: {result}")

random_division()