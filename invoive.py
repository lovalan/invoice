def calculate_invoice_totals(items):
    net_total = sum(item["value"] for item in items)
    gst = net_total * 0.05  # GST (5%)
    pst = net_total * 0.08  # PST (8%)
    total = net_total + gst + pst
    return net_total, gst, pst, total


def generate_invoice():
    invoice_number = input("Enter Invoice Number: ")
    customer_number = input("Enter Customer Number: ")
    customer_name = input("Enter Customer Name: ")

    items = []
    while True:
        if len(items) >= 10:
            break
        description = input("Enter item description (or 'done' to finish): ")
        if description.lower() == 'done':
            break
        value = float(input("Enter item value: "))
        items.append({"description": description, "value": value})

    net, gst, pst, total = calculate_invoice_totals(items)

    print("\nInvoice Number (PO):", invoice_number)
    print("Customer Number (Supplier):", customer_number)
    print("Customer Name (Supplier):", customer_name)
    print("------------------------------")
    print("Items with their values:")
    for item in items:
        print(f"{item['description']}: {item['value']:.2f}")
    print("------------------------------")
    print("Net:", net)
    print("GST (5%):", gst)
    print("PST (8%):", pst)
    print("Total:", total)


def main():
    while True:
        print("\nMenu:")
        print("1. Generate Invoice")
        print("2. Generate Purchase Order (PO)")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            print("\nGenerating Invoice:")
            generate_invoice()
        elif choice == '2':
            print("\nGenerating Purchase Order (PO):")
            generate_invoice()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()