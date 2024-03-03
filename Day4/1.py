# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# print(fruits)
# fruits[-1] = "Melons"
# print(fruits)
# fruits.append("Lemons")
# print(fruits)
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dried = ["asd", "sdfg", "sdfsaa"]

dirty_dozen = [fruits, vegetables, dried]
print(dirty_dozen[0][1])
dirty_dozen[0][1] = 'hellow'
# dirty_dozen contain two lists , first [] choose which list 0=fruit 1=vegetables second [] is object inside the list
# print(dirty_dozen[0][0])
# Strawberries

print(dirty_dozen[0][1])
