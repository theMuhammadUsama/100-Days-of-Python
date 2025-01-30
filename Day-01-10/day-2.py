print("Welocme to the tip calculator! \n")
bill = float(input("What was the total bill? $ \n"))
tip = int(input("What percentage tip would you give? 10, 12, 15 \n"))
people = int(input("How many people you want to split the bill? \n"))
tip_percent = tip /100
total_tip_final = tip_percent * bill
bill_final = bill + total_tip_final
final_amount = round(bill_final/people, 3)
print(f"Each person should pay {round(final_amount, 3)} dollars")