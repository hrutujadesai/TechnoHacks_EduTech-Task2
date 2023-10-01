class ATM:
    
    def __init__(self, balance=0):
        self.balance = balance
        

    def check_balance(self):
        return f"Your account balance is ${self.balance:.2f}"
    
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount:.2f} successfully. Your new balance is ${self.balance:.2f}"
        
        else:
            return "Invalid deposit amount. Please enter a positive amount."
        

    def withdraw(self, amount):
        
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount:.2f} successfully. Your new balance is ${self.balance:.2f}"
        
        elif amount <= 0:
            return "Invalid withdrawal amount. Please enter a positive amount."
        
        else:
            return "Insufficient funds. Your account balance is not enough for this withdrawal."

def main():
    
    atm = ATM()  

    while True:
        print("\nATM Simulator Menu:")
        print("1. Check Balance")
        print("2. Deposit Funds")
        print("3. Withdraw Funds")
        print("4. Exit")

        choice = input("Please select an option (1/2/3/4): ")

        if choice == "1":
            print(atm.check_balance())
            
        elif choice == "2":
            amount = float(input("Enter the deposit amount: "))
            print(atm.deposit(amount))
            
        elif choice == "3":
            amount = float(input("Enter the withdrawal amount: "))
            print(atm.withdraw(amount))
            
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")
            

if __name__ == "__main__":
    main()
