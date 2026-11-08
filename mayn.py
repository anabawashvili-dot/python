# 1
word = 'programming'

print(word[0])        
print(word[-1])       
print(word[-3])       
print(word[:4])       
print(word[-4:])      
print(word[::2])      
print(word[::-1])    


# 2
email = input("Enter email: ")

at_pos = email.index("@")
username = email[:at_pos]
domain = email[at_pos + 1:]

dot_pos = domain.index(".")
first_part = domain[:dot_pos]

print("Username:", username)
print("Domain:", domain)
print("First part of domain:", first_part)


# 3

phone = input("Enter phone: ")

cleaned = phone.replace(" ", "").replace("-", "")
print(cleaned)

# 4

title = input("Enter title: ")

slug = "-".join(title.lower().split())
print(slug)

# 5

name = input("Enter name: ")
age = input("Enter age: ")
city = input("Enter city: ")
language = input("Enter favorite programming language: ")

print("=" * 25)
print(f"Name: {name.title()}")
print(f"Age: {age}")
print(f"City: {city.title()}")
print(f"Favorite language: {language.upper()}")
print("=" * 25)