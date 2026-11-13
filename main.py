# 1. საყიდლების სია

shopping = ['milk', 'bread', 'eggs']

shopping.append('cheese')
print(shopping)       

shopping.insert(0, 'apples')
print(shopping)      
shopping[-1] = 'butter'
print(shopping)        

shopping.extend(['tea', 'coffee'])
print(shopping)        

shopping.remove('bread')
print(shopping)        
removed = shopping.pop(1)
print(shopping)       
print("Removed:", removed)   


#2. გამოცდის ქულები

scores = [85, 92, 78, 92, 65, 88, 92]

asc_scores = sorted(scores)                

print("Count of 92:", scores.count(92))
print("Index of 78:", scores.index(78))
print("Ascending:", asc_scores)
print("Descending:", desc_scores)
print(f"Highest: {asc_scores[-1]}, Lowest: {asc_scores[0]}")
print("Original:", scores)

#3. მატრიცა

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("Rows:", len(matrix))                
print("Last row:", matrix[-1])              
print("6 (positive):", matrix[1][2])        
print("6 (negative):", matrix[-2][-1])      
print("7:", matrix[-1][-3])                 

matrix[1][1] = 50
print(matrix)                            


# 4. სიის შევსება while-ით

numbers = []

while True:
    value = input("Enter a number: ")
    if value == "stop":
        break
    try:
        numbers.append(int(value))
    except ValueError:
        print("Please enter a valid number or 'stop'.")

print("List:", numbers)
print("Count:", len(numbers))
if numbers:
    print(f"First: {numbers[0]}, Last: {numbers[-1]}")
    print("Descending:", sorted(numbers, reverse=True))