print("Tip Calculator - Calculate Your Share Precisely")

bill_amount = float(input("Please enter the total bill amount:\n$:"))
tip_percentage = int(input("Enter the tip percentage you'd like to add:\n%:"))
num_people = int(input("Specify the number of people sharing the bill:\n:"))

total_per_person = "{:.2f}".format((bill_amount * (tip_percentage / 100) + bill_amount) / num_people)

print(f"Each individual is responsible for: ${total_per_person}")