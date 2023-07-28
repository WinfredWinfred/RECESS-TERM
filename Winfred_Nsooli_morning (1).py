import tkinter as tk

def calculate_total():
    quantity = int(quantity_entry.get())
    price = float(price_entry.get())
    total = quantity * price
    total_label.config(text=f"Total: ${total:.2f}")

def print_receipt():
    product_name = name_entry.get()
    quantity = int(quantity_entry.get())
    price = float(price_entry.get())
    total = quantity * price

    # Print the receipt
    print("----- Receipt -----")
    print(f"Product: {product_name}")
    print(f"Quantity: {quantity}")
    print(f"Price: ${price:.2f}")
    print(f"Total: ${total:.2f}")
    print("-------------------")

# Create main window
window = tk.Tk()
window.title("Winfred Receipt")

# Name of the Product
name_label = tk.Label(window, text="Product Name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

# Quantity
quantity_label = tk.Label(window, text="Quantity:")
quantity_label.pack()
quantity_entry = tk.Entry(window)
quantity_entry.pack()

# Price
price_label = tk.Label(window, text="Price:")
price_label.pack()
price_entry = tk.Entry(window)
price_entry.pack()

# Calculate Total button
calculate_button = tk.Button(window, text="Calculate Total", command=calculate_total)
calculate_button.pack()

# Total Label
total_label = tk.Label(window, text="Total: ")
total_label.pack()

# Print Receipt button
print_button = tk.Button(window, text="Print Receipt", command=print_receipt)
print_button.pack()

# Run the GUI event loop
window.mainloop()
