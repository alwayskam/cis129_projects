# Kameron Craig
# CIS 129
# 9/26/24
# cis129_lab03_coffeeShop.py - create an interactive text based Coffee Shop simulator that calculates a receipt based on how many items the user wants to order.

"""If code gives error, re-run.
--Added while not statements that pull from list of ['yes','no'] to be- 
able to tell if the user says yes or no to wanting coffee/muffins,
prompting them to type a correct input."""

# Creating Function main()
def main():
     # Defining prices
    coffee_price = 5.000
    muffin_price = 4.000
    tax_rate = 0.06

    # Setting initial coffee/muffin amount
    num_coffees = 0
    num_muffins = 0

    # Ask if person wants coffee
    want_coffee = input('Do you want coffee? (yes/no)\n')
    while want_coffee not in ['yes', 'no']:
        print("Invalid input. Please enter 'yes' or 'no' in lowercase.")
        want_coffee = input('Do you want coffee? (yes/no)\n')
    if want_coffee == 'yes':
        num_coffees = int(input("How many coffee(s)?\n"))

    # Ask if person wants muffins
    want_muffin = input("Want muffins? (yes/no)\n")
    while want_muffin not in ['yes', 'no']:
        print("Invalid input. Please enter 'yes' or 'no' in lowercase.")
        want_muffin = input("Want muffins? (yes/no)\n")
    if want_muffin == 'yes':
        num_muffins = int(input("How many muffin(s)?\n"))
    else:
        print("Sorry those are the only options.")
    
    

    # Calculating the total cost (sub and total)
    coffee_total = num_coffees * coffee_price
    muffin_total = num_muffins * muffin_price
    subtotal = coffee_total + muffin_total
    tax = subtotal * tax_rate
    total = subtotal + tax

    # Printing the receipt
    print("\n***************************************")
    print("My Coffee and Muffin Shop")
    print(f"{num_coffees} Coffee(s) at ${coffee_price:.0f} each: $ {coffee_total:.2f}")
    print(f"{num_muffins} Muffin(s) at ${muffin_price:.0f} each: $ {muffin_total:.2f}")
    print(f"{tax_rate}% tax: $ {tax:.2f}")
    print("---------")
    print(f"Total: $ {total:.2f}")
    print("***************************************")

# Running the function
main()
