import time
import random
import sys
from functools import wraps



#  ნაწილი I - ფუნქციები და დეკორატორები


# 1. ფუნქცია როგორც ობიექტი
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


#  ნაწილი II - გენერატორები


#
# ამოცანა 1 - ლუწი რიცხვები


def evens(n):
    for i in range(0, n + 1, 2):
        yield i


for num in evens(10):
    print(num)
# 0 2 4 6 8 10 (თითო ხაზზე)



# ამოცანა 2 - კენტი რიცხვების კვადრატები

total = sum(x ** 2 for x in range(1, 11) if x % 2 == 1)
print(total)  # 165



# ამოცანა 3 - გაერთიანება yield from-ით


def my_chain(*iterables):
    for it in iterables:
        yield from it


print(list(my_chain([1, 2], (3, 4), "ab")))
# [1, 2, 3, 4, 'a', 'b']



# ამოცანა 4 - მეხსიერების შედარება

squares_list = [x ** 2 for x in range(1, 100_001)]
squares_gen = (x ** 2 for x in range(1, 100_001))

print("List:     ", sys.getsizeof(squares_list), "bytes")
print("Generator:", sys.getsizeof(squares_gen), "bytes")

