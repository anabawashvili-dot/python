# ამოცანა 1. ბილეთების ბეჭდვა
def print_ticket(passenger, destination, travel_class):
    print('--- TICKET ---')
    print(f'Passenger: {passenger}')
    print(f'Destination: {destination}')
    print(f'Class: {travel_class}')


# მხოლოდ პოზიციური არგუმენტები
print_ticket('Nika', 'Batumi', 'Economy')

# მხოლოდ keyword არგუმენტები
print_ticket(passenger='Mari', destination='Kutaisi', travel_class='Business')

# პოზიციური + keyword (მხოლოდ კლასი არის keyword)
print_ticket('Luka', 'Batumi', travel_class='Economy')
# ამოცანა 2. ტემპერატურა

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def is_warm(celsius, limit=20):
    return celsius > limit


f0 = celsius_to_fahrenheit(0)
f37 = celsius_to_fahrenheit(37)
f100 = celsius_to_fahrenheit(100)

print(f'0C = {f0:.1f}F')
print(f'37C = {f37:.1f}F')
print(f'100C = {f100:.1f}F')

print(is_warm(25))                     
print(is_warm(25, 30))                  
print(is_warm(limit=10, celsius=15))    
# ამოცანა 3. რიცხვების ანალიზი

def analyze_numbers(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)


data = [12, 7, 25, 3, 18]

smallest, largest, average = analyze_numbers(data)
print(f'Min: {smallest}, Max: {largest}, Average: {average}')
# Min: 3, Max: 25, Average: 13.0

result = analyze_numbers(data)
print(result)
# (3, 25, 13.0)



# ამოცანა 4. ჯგუფის სია




def add_student(name, group=None):
    if group is None:
        group = []
    if name not in group:
        group.append(name)
    return group


group_a = add_student('Ana')
group_b = add_student('Nika')
group_a = add_student('Mari', group_a)
group_a = add_student('Ana', group_a)

print(group_a)  # ['Ana', 'Mari']
print(group_b)  # ['Nika']
# ამოცანა 5. პაროლის სიძლიერე

def check_password(password):
    if len(password) < 6:
        return 'Too short'
    if password.isdigit():
        return 'Weak'
    has_digit = any(ch.isdigit() for ch in password)
    has_letter = any(ch.isalpha() for ch in password)
    if not has_digit or not has_letter:
        return 'Medium'
    return 'Strong'


passwords = ['abc', '1234567', 'qwerty', 'python3', 'Tbilisi2024']

for password in passwords:
    print(f'{password} -> {check_password(password)}')

