#Program to calculate customer due amount

bill_amount = float(input("Enter the total bill amount : "))
paid_amount = float(input("Enter the amount paid by customer : "))
due_amount = bill_amount - paid_amount

print("Customer Due Amount =", due_amount)