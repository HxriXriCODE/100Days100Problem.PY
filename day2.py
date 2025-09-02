print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? RS "))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
TipMoney=(tip/bill)*100
TotalBill=(bill+TipMoney)/people
print(f"Per-person Bill Rs :{TotalBill}")




