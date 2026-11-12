# 1. for და range()

# 1) კვადრატები 1-დან 10-მდე
for i in range(1, 11):
    print(f"{i} squared = {i ** 2}")


    # 2) უკუთვლა 10-დან 1-მდე
for i in range(10, 0, -1):
    print(i)
print("Go!")


# 3) 1-დან 100-მდე ლუწების ჯამი
total = 0
for i in range(2, 101, 2):
    total += i
print(total)  


# 2. ხმოვნების დათვლა

text = input("Enter text: ").lower()
count = 0
for char in text:
    if char in "aeiou":
        count += 1
print("Vowels:", count)



# 3. რიცხვების ჯამი (continue)

total = 0
count = 0

while True:
    value = input("Enter a number: ")
    if value == "stop":
        break
    number = int(value)
    if number < 0:
        print("Negative numbers are not allowed")
        continue
    total += number
    count += 1

print("Sum:", total)
print("Count:", count)


# 4. სამკუთხედი (ჩადგმული ციკლები)

n = int(input("Enter n: "))

# ჩვეულებრივი სამკუთხედი
for i in range(1, n + 1):
    for j in range(i):
        print('*', end=' ')
    print()

# შებრუნებული სამკუთხედი
for i in range(n, 0, -1):
    for j in range(i):
        print('*', end=' ')
    print()