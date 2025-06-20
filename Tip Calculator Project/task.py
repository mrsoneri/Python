print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_percent = tip/100
tip_amt = bill * tip_percent
total_bill = bill + tip_amt
bill_per_person = total_bill / people
final_amt = round(bill_per_person,2)
print(f"Each Person should pay: ${final_amt}")