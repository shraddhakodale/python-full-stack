
# Banking Console Application
# Kiran Academy - Internship Task 03

balance = 10000

print("================================")
print("      Welcome to Kiran Bank")
print("================================")
print(f"Opening Balance: Rs. {balance:.2f}")

while True:
    print("\n---------- BANK MENU ----------")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print(f"Current Balance: Rs. {balance:.2f}")

    elif choice == "2":
        try:
            amount = float(input("Enter deposit amount: Rs. "))

            if amount <= 0:
                print("Error: Amount must be greater than zero.")
            else:
                balance += amount
                print("Deposit successful!")
                print(f"Updated Balance: Rs. {balance:.2f}")

        except ValueError:
            print("Error: Please enter a valid number.")

    elif choice == "3":
        try:
            amount = float(input("Enter withdrawal amount: Rs. "))

            if amount <= 0:
                print("Error: Amount must be greater than zero.")
            elif amount > balance:
                print("Transaction failed: Insufficient balance.")
                print(f"Current Balance: Rs. {balance:.2f}")
            else:
                balance -= amount
                print("Withdrawal successful!")
                print(f"Updated Balance: Rs. {balance:.2f}")

        except ValueError:
            print("Error: Please enter a valid number.")

    elif choice == "4":
        print("Thank you for banking with us. Goodbye!")
        break

    else:
        print("Invalid choice! Please select between 1 and 4.")
