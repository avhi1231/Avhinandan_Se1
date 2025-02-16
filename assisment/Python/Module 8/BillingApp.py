import tkinter as tk
from tkinter import ttk

class BillingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Billing Software")
        self.root.geometry("900x500")
        self.root.configure(bg="darkblue")
        
        # Title
        title = tk.Label(self.root, text="Billing Software", font=("Arial", 18, "bold"), bg="darkblue", fg="white")
        title.pack(fill=tk.X)
        
        # Customer Details Frame
        customer_frame = tk.Frame(self.root, bd=5, relief=tk.RIDGE, bg="darkblue")
        customer_frame.place(x=10, y=40, width=880, height=60)
        
        tk.Label(customer_frame, text="Customer Name", fg="white", bg="darkblue", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5)
        self.cust_name = tk.Entry(customer_frame)
        self.cust_name.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(customer_frame, text="Phone No", fg="white", bg="darkblue", font=("Arial", 12)).grid(row=0, column=2, padx=10, pady=5)
        self.phone = tk.Entry(customer_frame)
        self.phone.grid(row=0, column=3, padx=10, pady=5)
        
        tk.Label(customer_frame, text="Bill No.", fg="white", bg="darkblue", font=("Arial", 12)).grid(row=0, column=4, padx=10, pady=5)
        self.bill_no = tk.Entry(customer_frame)
        self.bill_no.grid(row=0, column=5, padx=10, pady=5)
        
        # Sections for Products
        self.create_product_section("Cosmetics", ["Bath Soap", "Face Cream", "Face Wash", "Hair Spray", "Body Lotion"], 10, 110)
        self.create_product_section("Grocery", ["Rice", "Food Oil", "Daal", "Wheat", "Sugar"], 300, 110)
        self.create_product_section("Others", ["Maza", "Coke", "Frooti", "Nimkos", "Biscuits"], 590, 110)
        
        # Bill Area
        bill_frame = tk.Frame(self.root, bd=5, relief=tk.RIDGE, bg="white")
        bill_frame.place(x=590, y=250, width=300, height=190)
        tk.Label(bill_frame, text="Bill Area", font=("Arial", 12, "bold"), bg="white").pack()
        self.bill_text = tk.Text(bill_frame, height=10, width=35)
        self.bill_text.pack()
        
        # Button Section
        button_frame = tk.Frame(self.root, bg="darkblue")
        button_frame.place(x=10, y=400, width=880, height=50)
        
        tk.Button(button_frame, text="Total", width=10, font=("Arial", 12), command=self.calculate_total).grid(row=0, column=0, padx=10, pady=5)
        tk.Button(button_frame, text="Generate Bill", width=15, font=("Arial", 12), command=self.generate_bill).grid(row=0, column=1, padx=10, pady=5)
        tk.Button(button_frame, text="Clear", width=10, font=("Arial", 12), command=self.clear_data).grid(row=0, column=2, padx=10, pady=5)
        tk.Button(button_frame, text="Exit", width=10, font=("Arial", 12), command=root.quit).grid(row=0, column=3, padx=10, pady=5)

    def create_product_section(self, title, items, x_pos, y_pos):
        frame = tk.LabelFrame(self.root, text=title, font=("Arial", 12, "bold"), bg="darkblue", fg="white")
        frame.place(x=x_pos, y=y_pos, width=250, height=180)
        
        for i, item in enumerate(items):
            tk.Label(frame, text=item, fg="white", bg="darkblue", font=("Arial", 10)).grid(row=i, column=0, padx=10, pady=5, sticky="w")
            entry = tk.Entry(frame, width=5)
            entry.grid(row=i, column=1, padx=10, pady=5)
        
    def calculate_total(self):
        self.bill_text.insert(tk.END, "\nTotal Calculated!\n")
        
    def generate_bill(self):
        self.bill_text.insert(tk.END, "\nBill Generated!\n")
        
    def clear_data(self):
        self.bill_text.delete(1.0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = BillingApp(root)
    root.mainloop()