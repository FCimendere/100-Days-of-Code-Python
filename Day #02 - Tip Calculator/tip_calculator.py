"""If the bill was $150.00, split between 5 people, with 12% tip. 
E.g. Each person should pay (150.00 / 5) * 1.12 = 33.6
Format the result to 2 decimal places = 33.60
"""


print("Welcome to the tip calculator.")

# collect the user's infos
bill = float(input("What was the total bill? €"))
tip = int(input("What percentage tip would you like to give? 10, 12, 15 "))
# calculation of the percentage
tip_as_num = 1 + tip/100
# collect the people numbers who will share the payment.
people = int(input("How many people split the bill? "))

# payment calculation.
calc_payment = (bill / people) * tip_as_num
# optional 2 decimal showing ways.
# print("%.2f" % calc_payment)
# print(format(calc_payment, '.2f'))
final_amount = "{:.2f}".format(calc_payment)
print(f"Each person should pay €{final_amount}" )