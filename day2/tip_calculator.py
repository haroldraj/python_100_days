print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? ")) / 100
people = int(input("How many people to split the bill?"))

tip *= total
total += tip
person = total / people

print(f"Each person should pay: ${person:.2f}")
