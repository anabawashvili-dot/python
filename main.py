# ა) კვადრატები 1-დან 10-მდე


for i in range(1, 11):
    print(f"{i} squared = {i ** 2}")

# ბ) უკუთვლა 10-დან 1-მდე


for i in range(10, 0, -1):
    print(i)
print("Go!")


# გ) ლუწი რიცხვების ჯამი 1-დან 100-მდე


total = 0
for i in range(2, 101, 2):
    total += i
print("Sum:", total)



# 2. ხმოვნების დათვლა

text = input("Enter text: ")
text = text.lower()

count = 0
for ch in text:
    if ch in "aeiou":
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
for row in range(1, n + 1):
    for _ in range(row):
        print("*", end=" ")
    print()

# შებრუნებული სამკუთხედი
for row in range(n, 0, -1):
    for _ in range(row):
        print("*", end=" ")
    print()