# 1. ლუწი რიცხვები

i = 1
while i <= 50:
    if i % 2 == 0:
        print(i)
    i += 1


# 2. ჯამი 1-დან N-მდე

n = int(input("Enter N: "))
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print("Sum:", total)


# 3. ფაქტორიალი

n = int(input("Enter n: "))
result = 1
i = 1
while i <= n:
    result *= i
    i += 1
print(f"{n}! = {result}")



# 4. საშუალო არითმეტიკული

count = 0
total = 0

num = float(input("Enter a number: "))
while num != 0:
    count += 1
    total += num
    num = float(input("Enter a number: "))

print("Count:", count)
print("Sum:", total)
if count > 0:
    print("Average:", total / count)
else:
    print("Average: no numbers were entered")


    # 5. გამოცნობის თამაში

secret = 7
attempts = 0
guessed = False

while attempts < 5 and not guessed:
    guess = int(input("Guess: "))
    attempts += 1
    if guess > secret:
        print("Too high")
    elif guess < secret:
        print("Too low")
    else:
        print("You win!")
        guessed = True

if not guessed:
    print("You lose! The number was", secret)