#1
age = int(input("Enter age: "))
money = int(input("Enter money: "))

if age >= 12 and money >= 15:
    print("Enjoy the movie")
else:
    print("Access denied")

# 2

year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")


# 3
correct_pin = 1234
balance = 500

pin = int(input("Enter PIN: "))
amount = int(input("Enter amount: "))

if pin != correct_pin:
    print("Wrong PIN")
else:
    if amount <= 0:
        print("Invalid amount")
    elif amount > balance:
        print("Not enough money")
    else:
        balance -= amount
        print(f"Take your money: {amount}")
        print(f"New balance: {balance}")

        # 4
try:
    name = input('Enter name: ')
    age = int(input('Enter age: '))
    number = int(input('Enter a number to divide 100 by: '))

    print('100 /', number, '=', 100 / number)
    print(f'Hello, {name}! Next year you will be {age + 1} years old.')

except ValueError:
    print('Invalid input')
except ZeroDivisionError:
    print('Cannot divide by zero')
except TypeError:
    print('Cannot join text and number')
except Exception as e:
    print(e)


    