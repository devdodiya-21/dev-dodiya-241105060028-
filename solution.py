print("Water Bill")
units = float(input("Enter units: "))
if units <= 50:
 bill = units * 2
elif units <= 100:
 bill = units * 5
else:
 bill = units * 8
tax = bill * 0.05
total = bill + tax
print("Total:", total)
for i in range(3):
    print("Generated")
print("End")