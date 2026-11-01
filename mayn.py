# ამოცანა 1
# მონაცემთა ტიპები და type()
age = 25
height = 1.78
name = "John Doe"
is_student = True


print("Age:", age, "Type:", type(age))
print("Height:", height, "Type:", type(height))
print("Name:", name, "Type:", type(name))
print("Is Student:", is_student, "Type:", type(is_student))


# ამოცანა 2
# მათემატიკური ოპერაციები
a = float(input("შეიყვანეთ პირველი რიცხვი: "))
b = float(input("შეიყვანეთ მეორე რიცხვი: "))

print("ჯამი:", a + b)
print("სხვაობა:", a - b)
print("ნამრავლი:", a * b)
print("გაყოფა:", a / b)
print("მთელი გაყოფა:", a // b)
print("ნაშთი:", a % b)
print("ხარისხი:", a ** b)

# ამოცანა 3
# სტრიქონების მანიპულაცია
first_name = input("შეიყვანეთ სახელი: ")
last_name = input("შეიყვანეთ გვარი: ")

full_name = first_name + " " + last_name
print("სრული სახელი:", full_name)
print("დიდი ასოებით:", full_name.upper())
print("პატარა ასოებით:", full_name.lower())
print("პირველი ასო დიდი:", full_name.capitalize())


 

 # ამოცანა 4
# print()-ის პარამეტრები: sep და end
print("ვაშლი", "მსხალი", "ატამი", sep="-")
print("ერთი", "ორი", "სამი", sep="***")
print("a", "b", "c", sep="\t")
 
print("პირველი", end=" | ")
print("მეორე", end=" ... ")
print("მესამე", end="!\n")
print(1, 2, 3, sep=", ", end=" <- რიცხვები\n")
 


 # ამოცანა 5
# შედარების და ლოგიკური ოპერატორები
age = 20
height = 1.75
is_student = True
 
print(age, '> 18 =', age > 18)
print(age, '== 18 =', age == 18)
print(age, '!= 18 =', age != 18)
print(age, '< 18 =', age < 18)
print(age, '>= 20 =', age >= 20)
print(age, '<= 20 =', age <= 20)
 
print("ასაკი > 18 and სტუდენტია:", age > 18 and is_student)
print("სიმაღლე > 1.80 or სტუდენტია:", height > 1.80 or is_student)
print("not სტუდენტი:", not is_student)
print("სიმაღლე > 1.70 and სტუდენტია:", height > 1.70 and is_student)


 # ამოცანა 5
# შედარების და ლოგიკური ოპერატორები
age = 20
height = 1.75
is_student = True
 
print(age, '> 18 =', age > 18)
print(age, '== 18 =', age == 18)
print(age, '!= 18 =', age != 18)
print(age, '< 18 =', age < 18)
print(age, '>= 20 =', age >= 20)
print(age, '<= 20 =', age <= 20)
 
print("ასაკი > 18 and სტუდენტია:", age > 18 and is_student)
print("სიმაღლე > 1.80 or სტუდენტია:", height > 1.80 or is_student)
print("not სტუდენტი:", not is_student)
print("სიმაღლე > 1.70 and სტუდენტია:", height > 1.70 and is_student)


     # ამოცანა 6
# input() და ტიპის სწორად გარდაქმნა
user_name = input("შეიყვანეთ სახელი: ")
user_age = int(input("შეიყვანეთ ასაკი: "))
user_height = float(input("შეიყვანეთ სიმაღლე (მეტრებში): "))
 
print("გამარჯობა,", user_name + "!")
print("შენი ასაკია", user_age, "წელი და სიმაღლე", user_height, "მ.")
 