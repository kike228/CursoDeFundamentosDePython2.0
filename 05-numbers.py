""" lives = 3
print(type(lives))
age = 12
budget = 100

temperature = 12.12
print(type(temperature))

lives = 2
print(lives)
lives = 1
print(lives)

lives = 12 + 15
print(lives)

lives = lives - 1
print(lives)

lives -= 1
print(lives)

lives -= 5
print(lives)

lives += 5
print(lives)

number = 4500000000000000000.1
print(number)

number_b = 0.0000000000000001
print(number_b) """


budget_january = input("¿Cuál es tu presupuesto para enero? ")
budger_february = input("¿Cuál es tu presupuesto para febrero? ")
budger_march = input("¿Cuál es tu presupuesto para marzo? ")

budget_january = int(budget_january)
budger_february = int(budger_february)
budger_march = int(budger_march)

budget_total = budget_january + budger_february + budger_march
print(f"La suma total del presupuesto es {budget_total}")

budget_total = int(budget_total)

promedio = budget_total / 3
print(f"El promedio del presupuesto es {promedio}")