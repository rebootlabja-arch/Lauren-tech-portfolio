import csv
from datetime import datetime

TAX_RATE = 0.15
RATE_PER_UNIT = 25

customers = {}

def add_customer_bill():
    print("\n--- Add Customer Bill ---")

    customer_id = input("Enter Customer ID: ")
    name = input("Enter Customer Name: ")
    units = float(input("Enter Electricity Units Used: "))

    subtotal = units * RATE_PER_UNIT
    tax = subtotal * TAX_RATE
    total = subtotal + tax

    bill = {
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Units Used": units,
        "Subtotal": subtotal,
        "Tax": tax,
        "Total": total
    }

    if customer_id not in customers:
        customers[customer_id] = {
            "Name": name,
            "Bills": []
        }

    customers[customer_id]["Bills"].append(bill)

    print("\nBill added successfully!")

def view_customers():
    print("\n--- Customer List ---")

    if not customers:
        print("No customers found.")
        return

    for customer_id, info in customers.items():
        print(f"""
Customer ID: {customer_id}
Name: {info['Name']}
Total Bills: {len(info['Bills'])}
----------------------------
""")

def search_customer():
    print("\n--- Search Customer ---")

    customer_id = input("Enter Customer ID: ")

    if customer_id in customers:
        info = customers[customer_id]

        print(f"""
Customer ID: {customer_id}
Name: {info['Name']}
Bills Recorded: {len(info['Bills'])}
""")

    else:
        print("Customer not found.")

def generate_receipt():
    print("\n--- Generate Receipt ---")

    customer_id = input("Enter Customer ID: ")

    if customer_id not in customers:
        print("Customer not found.")
        return

    bills = customers[customer_id]["Bills"]

    if not bills:
        print("No bills available.")
        return

    latest_bill = bills[-1]

    print("\n====== ELECTRICITY RECEIPT ======")
    print(f"Date: {latest_bill['Date']}")
    print(f"Customer ID: {customer_id}")
    print(f"Customer Name: {customers[customer_id]['Name']}")
    print(f"Units Used: {latest_bill['Units Used']}")
    print(f"Subtotal: ${latest_bill['Subtotal']:.2f}")
    print(f"Tax: ${latest_bill['Tax']:.2f}")
    print(f"TOTAL: ${latest_bill['Total']:.2f}")
    print("================================")

def view_bill_history():
    print("\n--- Bill History ---")

    customer_id = input("Enter Customer ID: ")

    if customer_id not in customers:
        print("Customer not found.")
        return

    bills = customers[customer_id]["Bills"]

    if not bills:
        print("No bill history available.")
        return

    print(f"\nBill History for {customers[customer_id]['Name']}")

    for index, bill in enumerate(bills, start=1):
        print(f"""
Bill #{index}
Date: {bill['Date']}
Units Used: {bill['Units Used']}
Subtotal: ${bill['Subtotal']:.2f}
Tax: ${bill['Tax']:.2f}
Total: ${bill['Total']:.2f}
------------------------------
""")

def save_to_csv():
    with open("customer_bill_history.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Customer ID",
            "Customer Name",
            "Date",
            "Units Used",
            "Subtotal",
            "Tax",
            "Total"
        ])

        for customer_id, info in customers.items():
            for bill in info["Bills"]:
                writer.writerow([
                    customer_id,
                    info["Name"],
                    bill["Date"],
                    bill["Units Used"],
                    bill["Subtotal"],
                    bill["Tax"],
                    bill["Total"]
                ])

    print("\nData saved to customer_bill_history.csv")

def menu():
    while True:
        print("""
====== SMART UTILITY BILLING SYSTEM ======

1. Add Customer Bill
2. View Customers
3. Search Customer
4. Generate Receipt
5. View Bill History
6. Save Data
7. Exit

=========================================
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_customer_bill()

        elif choice == "2":
            view_customers()

        elif choice == "3":
            search_customer()

        elif choice == "4":
            generate_receipt()

        elif choice == "5":
            view_bill_history()

        elif choice == "6":
            save_to_csv()

        elif choice == "7":
            print("Exiting program...")
            break

        else:
            print("Invalid option.")

menu()