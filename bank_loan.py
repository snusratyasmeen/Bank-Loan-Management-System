print("🏦 Bank Loan Management System")

loans = []

while True:
    print("\n1. Add Loan")
    print("2. View Loans")
    print("3. Search Loan")
    print("4. Update Loan Status")
    print("5. Delete Loan")
    print("6. Calculate Total Loans")
    print("7. Count Loans")
    print("8. Exit")

    choice = input("Enter your choice: ")

    # Add Loan
    if choice == "1":
        loan_id = input("Enter loan ID: ")
        customer = input("Enter customer name: ")
        loan_type = input("Enter loan type: ")
        amount = float(input("Enter loan amount: "))

        loan = {
            "id": loan_id,
            "customer": customer,
            "type": loan_type,
            "amount": amount,
            "status": "Pending"
        }

        loans.append(loan)

        print("✅ Loan added successfully!")

    # View Loans
    elif choice == "2":
        if len(loans) == 0:
            print("❌ No loan records found.")
        else:
            print("\n📋 Loan Details")
            print("--------------------------")

            for loan in loans:
                print("Loan ID:", loan["id"])
                print("Customer Name:", loan["customer"])
                print("Loan Type:", loan["type"])
                print("Loan Amount:", loan["amount"])
                print("Status:", loan["status"])
                print("--------------------------")

    # Search Loan
    elif choice == "3":
        search_id = input("Enter loan ID to search: ")

        found = False

        for loan in loans:
            if loan["id"] == search_id:
                print("\n✅ Loan Found")
                print("Loan ID:", loan["id"])
                print("Customer Name:", loan["customer"])
                print("Loan Type:", loan["type"])
                print("Loan Amount:", loan["amount"])
                print("Status:", loan["status"])

                found = True
                break

        if not found:
            print("❌ Loan not found.")

    # Update Loan Status
    elif choice == "4":
        update_id = input("Enter loan ID: ")

        found = False

        for loan in loans:
            if loan["id"] == update_id:

                print("\n1. Pending")
                print("2. Approved")
                print("3. Rejected")
                print("4. Closed")

                status_choice = input("Choose new status: ")

                if status_choice == "1":
                    loan["status"] = "Pending"
                elif status_choice == "2":
                    loan["status"] = "Approved"
                elif status_choice == "3":
                    loan["status"] = "Rejected"
                elif status_choice == "4":
                    loan["status"] = "Closed"
                else:
                    print("❌ Invalid status!")
                    break

                print("✅ Loan status updated successfully!")

                found = True
                break

        if not found:
            print("❌ Loan not found.")

    # Delete Loan
    elif choice == "5":
        delete_id = input("Enter loan ID to delete: ")

        found = False

        for loan in loans:
            if loan["id"] == delete_id:
                loans.remove(loan)

                print("✅ Loan deleted successfully!")

                found = True
                break

        if not found:
            print("❌ Loan not found.")

    # Calculate Total Loans
    elif choice == "6":
        total = 0

        for loan in loans:
            total = total + loan["amount"]

        print("💰 Total Loan Amount:", total)

    # Count Loans
    elif choice == "7":
        print("🏦 Total Loans:", len(loans))

    # Exit
    elif choice == "8":
        print("Thank you for using Bank Loan Management System! 🏦")
        break

    else:
        print("❌ Invalid choice!")
