balance = 5000
pin = "1234"

while True:
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    entered_pin = input("Enter ATM PIN: ")

    if entered_pin != pin:
        print("❌ Wrong PIN")
        continue

    choice = input("Choose option: ")

    if choice == "1":
        print("💰 Current Balance:", balance)

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print("✅ Amount Deposited")

    elif choice == "3":
        amount = float(input("Enter withdraw amount: "))
        if amount <= balance:
            balance -= amount
            print("✅ Please collect cash")
        else:
            print("❌ Insufficient balance")

    elif choice == "4":
        print("Thank you for using ATM 🙏")
        break

    else:
        print("Invalid option ❗")
