# Kameron Craig
# CIS 129
# 9/26/24
# cis129_lab03_coffeeShop.py - creates an interactive text based Coffee Shop simulator that calculates a receipt based on how many items the user wants to order.

"""If code gives error, re-run.
--Added while not statements that pull from list of ['yes','no'] to be able to tell 
if the user says yes or no to wanting coffee/muffins, prompting them to type a correct input.--"""

# Creating Function main()
def main():
     # Defining prices
    coffee_price = 5.000
    muffin_price = 4.000
    cookie_price = 2.000
    tea_price = 6.000
    tax_rate = 0.06

    # Setting initial coffee/muffin amount
    num_coffees = 0
    num_muffins = 0
    num_cookies = 0
    num_tea = 0

    # Shows user list of items + prices
    print(f"Coffee: ${coffee_price:.2f}\nMuffin: ${muffin_price:.2f}\nCookie: ${cookie_price:.2f}\nTea: ${tea_price:.2f}\n")

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

    # Ask if person wants cookies
    want_cookie = input("Want cookies? (yes/no)\n")
    while want_cookie not in ['yes', 'no']:
        print("Invalid input. Please enter 'yes' or 'no' in lowercase.")
        want_cookie = input("Want cookies? (yes/no)\n")
    if want_cookie == 'yes':
        num_cookies = int(input("How many cookie(s)?\n"))

    # Ask if person wants tea
    want_tea = input("Want tea? (yes/no)\n")
    while want_tea not in ['yes', 'no']:
        print("Invalid input. Please enter 'yes' or 'no' in lowercase.")
        want_tea = input("Want tea? (yes/no)\n")
    if want_tea == 'yes':
        num_tea = int(input("How many tea(s):\n"))
    

    # Calculating the total cost (sub and total)
    coffee_total = num_coffees * coffee_price
    muffin_total = num_muffins * muffin_price
    cookie_total = num_cookies * cookie_price
    tea_total = num_tea * tea_price
    subtotal = coffee_total + muffin_total + cookie_total + tea_total
    tax = subtotal * tax_rate
    total = subtotal + tax

    # Printing the receipt
    print("\n***************************************")
    print("Kam's Cafe")
    print(f"{num_coffees} Coffee(s) at ${coffee_price:.0f} each: $ {coffee_total:.2f}")
    print(f"{num_muffins} Muffin(s) at ${muffin_price:.0f} each: $ {muffin_total:.2f}")
    print(f"{num_cookies} Cookie(s) at ${cookie_price:.0f} each: $ {cookie_total:.2f}")
    print(f"{num_tea} Tea(s) at ${tea_price:.0f} each: $ {tea_total:.2f}")
    print(f"6% tax: $ {tax:.2f}")
    print("---------")
    print(f"Total: $ {total:.2f}")
    print("***************************************")
    print("Thank you, We hope you are satisfied!")

# Running the function
main()
