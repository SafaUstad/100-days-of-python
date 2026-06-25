print("Welcome to the tip calculator!")

# The input is in string hence needs to be converted in the suitable data type
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

# Covert tip from percent
total_tip = bill * (tip / 100)

# Add tip and bill 
total_bill = total_tip + bill

# Divide the bill in number of people
bill_per_person = total_bill / people

# Round off that bill to get only 2 digits after the decimal
final = round(bill_per_person, 2)

# Display final bill for each person
print(f"Bill per person is: ${final}")
