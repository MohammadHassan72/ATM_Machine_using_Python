import os, sys, time, logging
from datetime import datetime

# Clear screen
os.system('cls' if os.name == 'nt' else 'clear')

# Initialize logging
logging.basicConfig(filename='reference.log', level=logging.DEBUG, format='%(asctime)s - %(message)s')

# Current day and time
DT = datetime.now()
print(DT)
time.sleep(0.6)
print('Please Slot in Your Card...')
time.sleep(2)
print('Loading Card...')
time.sleep(1)
print("""
============================================
======= Welcome to ATM Center ============
======= Author : Mohammad Hassan ==========
======= Version : 1.0 =====================
============================================
""")
time.sleep(2)

# Global balance
balance = 10000

def check_balance():
    global balance
    print(f"Your Balance is: {balance}")

def withdraw():
    global balance
    try:
        amount = int(input("Enter the amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print("Transaction processing...")
            time.sleep(1)
            print(f"Withdrawing {amount}.")
            print("Done! Please take your cash.")
    except ValueError:
        print("Invalid amount. Please enter a number.")

def transfer():
    global balance
    try:
        receiver = input("Enter the account number: ")
        if len(receiver) != 10 or not receiver.isdigit():
            print("Invalid account number.")
            return
        amount = int(input("Enter the amount to transfer: "))
        if amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print(f"You transferred {amount} to {receiver}.")
            print("Transfer successful.")
    except ValueError:
        print("Invalid amount. Please enter a number.")

def transactions():
    while True:
        print("""
What would you like to perform?
1. Check Balance
2. Withdraw
3. Transfer
4. Exit
""")
        try:
            choice = int(input("Choose 1/2/3/4: "))
            logging.debug(f"Transaction choice: {choice}")
            if choice == 1:
                check_balance()
            elif choice == 2:
                withdraw()
            elif choice == 3:
                transfer()
            elif choice == 4:
                print("Goodbye!")
                sys.exit()
            else:
                print("Invalid choice. Please select from the menu.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        
        again = input("Do you want to perform another transaction? (yes/no): ").lower()
        if again != 'yes':
            print("Goodbye!")
            break

def get_pin():
    pins = [1234, 1122, 1133, 1803, 1672, 1110, 1111]
    for attempt in range(3):
        try:
            pin = int(input("Enter your PIN: "))
            if pin in pins:
                print("Welcome to your account!")
                time.sleep(1)
                transactions()
                break
            else:
                print("Incorrect PIN.")
        except ValueError:
            print("Invalid PIN. Please use numbers only.")
    else:
        print("Too many incorrect attempts. Exiting...")
        sys.exit()

# Start program
get_pin()
