"""Expense Tracker Application
This application allows users to track their daily expenses. Users can add new expenses, view all recorded expenses,
calculate the total and average expenses, and clear all expenses.
"""

print("Welcome to the Daily Expense Tracker!")

# Display menu once
print("\nMenu:")
print("1. Add a new expense")
print("2. View all expenses")
print("3. Calculate total and average expense")
print("4. Clear all expenses")
print("5. Exit")

# Initialize an empty list to store expenses
expenses = []

while True:
    # Get user choice
    choice = input("Please select an option (1-5): ")
    
    if choice == "1":
        # Add a new expense
        amount = float(input())
        expenses.append(amount)
        print("Expense added successfully!")

    elif choice == "2":
        # View all expenses
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            print("Your expenses:")
            for i in range(len(expenses)):
                print(f"{i + 1}. {expenses[i]}")
    elif choice == "3":
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else: 
            # Calculate total and average expense
            total_expense = sum(expenses)
            average_expense = total_expense / len(expenses)
            print(f"Total expense: {total_expense}")
            print(f"Average expense: {average_expense}")
    elif choice == "4":
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            expenses.clear()
            print("All expenses cleared.")   
    elif choice == "5":
        # Exit the program
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break