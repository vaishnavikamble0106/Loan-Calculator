import tkinter as tk
from tkinter import messagebox

def calculate_emi():
    try:
        
        loan_amount = float(loan_amount_entry.get())
        loan_tenure = int(loan_tenure_entry.get())
        interest_rate = float(interest_rate_entry.get())

        if loan_amount <= 0 or loan_tenure <= 0 or interest_rate <= 0:
            raise ValueError("Values must be greater than zero")

        
        interest_rate /= 12 * 100  # Monthly interest rate
        emi = (loan_amount * interest_rate * (1 + interest_rate) ** loan_tenure) / ((1 + interest_rate) ** loan_tenure - 1)
        total_payment = emi * loan_tenure
        total_interest = total_payment - loan_amount

        
        emi_result_label.config(text=f"EMI Amount: {emi:.2f}")
        total_interest_label.config(text=f"Total Interest Payable: {total_interest:.2f}")
        total_payment_label.config(text=f"Total Payment: {total_payment:.2f}")

    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve))

def clear_entries():
    loan_amount_entry.delete(0, 'end')
    loan_tenure_entry.delete(0, 'end')
    interest_rate_entry.delete(0, 'end')
    emi_result_label.config(text="")
    total_interest_label.config(text="")
    total_payment_label.config(text="")


root = tk.Tk()
root.title("Loan Calculator")
root.geometry("900x700")


font_size = 30

loan_amount_label = tk.Label(root, text="Loan Amount:", font=("Helvetica", font_size))
loan_amount_label.grid(row=0, column=0, padx=10, pady=10)

loan_tenure_label = tk.Label(root, text="Loan Tenure (months):", font=("Helvetica", font_size))
loan_tenure_label.grid(row=1, column=0, padx=10, pady=10)

interest_rate_label = tk.Label(root, text="Interest Rate (%):", font=("Helvetica", font_size))
interest_rate_label.grid(row=2, column=0, padx=10, pady=10)

emi_result_label = tk.Label(root, text="", font=("Helvetica", font_size))
emi_result_label.grid(row=4, column=0, columnspan=2, pady=10)

total_interest_label = tk.Label(root, text="", font=("Helvetica", font_size))
total_interest_label.grid(row=5, column=0, columnspan=2, pady=10)

total_payment_label = tk.Label(root, text="", font=("Helvetica", font_size))
total_payment_label.grid(row=6, column=0, columnspan=2, pady=10)


entry_font_size = 20

loan_amount_entry = tk.Entry(root, font=("Helvetica", entry_font_size))
loan_amount_entry.grid(row=0, column=1, padx=10, pady=10)

loan_tenure_entry = tk.Entry(root, font=("Helvetica", entry_font_size))
loan_tenure_entry.grid(row=1, column=1, padx=10, pady=10)

interest_rate_entry = tk.Entry(root, font=("Helvetica", entry_font_size))
interest_rate_entry.grid(row=2, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate EMI", command=calculate_emi, font=("Helvetica", font_size))
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

clear_button = tk.Button(root, text="Clear", command=clear_entries, font=("Helvetica", font_size))
clear_button.grid(row=3, column=3, columnspan=2, pady=10)

root.mainloop()
