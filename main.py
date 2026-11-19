# ამოცანა 1. დუბლიკატების მოშორება

numbers = [4, 8, 15, 8, 16, 23, 4, 42, 15, 8]

unique = list(set(numbers))
print(unique)                 
print(len(unique))            
print(23 in set(numbers))     



# ამოცანა 2. სეტების ოპერაციები

ana = {'python', 'java', 'c', 'sql'}
nika = {'python', 'javascript', 'sql', 'go'}

# ოპერატორებით
print(ana | nika)   # ყველა ენა, რომელიც ერთმა მაინც იცის
print(ana & nika)   # {'python', 'sql'}
print(ana - nika)   # {'java', 'c'}

# მეთოდებით
print(ana.union(nika))
print(ana.intersection(nika))
print(ana.difference(nika))

# დამატებით: სიმეტრიული სხვაობა (მხოლოდ ერთმა იცის)
print(ana ^ nika)
print(ana.symmetric_difference(nika))
# ამოცანა 3. კენჭისყრა

votes = ['Ana', 'Nika', 'Ana', 'Mari', 'Nika', 'Ana', 'Mari', 'Ana']

counts = {}
for name in votes:
    if name in counts:
        counts[name] += 1
    else:
        counts[name] = 1

for name, count in counts.items():
    print(f"{name}: {count}")



# ამოცანა 4. მაღაზიის მარაგი

inventory = {
    'laptop': {'price': 2500, 'quantity': 5},
    'mouse': {'price': 40, 'quantity': 0},
    'keyboard': {'price': 120, 'quantity': 12},
    'monitor': {'price': 800, 'quantity': 0},
}

# 1. მარაგის საერთო ღირებულება
total = 0
for item in inventory.values():
    total += item['price'] * item['quantity']
print("საერთო ღირებულება:", total)   # 13940

# 2. ამოწურული პროდუქტები
print("ამოწურულია:")
for name, item in inventory.items():
    if item['quantity'] == 0:
        print(name)

# 3. შეძენა
name = input("პროდუქტის სახელი: ")
qty = int(input("რაოდენობა: "))

if name not in inventory:
    print("პროდუქტი ვერ მოიძებნა")
elif inventory[name]['quantity'] < qty:
    print("მარაგი არასაკმარისია")
else:
    inventory[name]['quantity'] -= qty
    cost = inventory[name]['price'] * qty
    print(f"შეძენის ღირებულება: {cost}")

# ამოცანა 5. Comprehension-ები

words = ['python', 'java', 'ai', 'sql', 'go', 'python']

squares = [x ** 2 for x in range(1, 11)]
lengths = {w: len(w) for w in words}
first_letters = {w[0] for w in words}

print(squares)        
print(lengths)        
print(first_letters)  