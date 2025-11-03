# SER416 - Fall'25 B
# ndavispe
# exercise1.py

import tkinter as tk
from tkinter import ttk, messagebox

class PvannCalculator:
    DEFAULT_PMT = 10000
    DEFAULT_RATE = 8.0
    DEFAULT_PERIODS = 20
    
    def __init__(self, root):
        self.root = root
        self.root.title("Pvann Calculator")
        
        # Create variables
        self.pmt_var = tk.StringVar()
        self.rate_var = tk.StringVar()
        self.periods_var = tk.StringVar()
        self.result_var = tk.StringVar()
        self.result_var.set("Future Value: --")
        
        # Create widgets
        self._create_widgets()
        self.reset_to_defaults()

    def _create_widgets(self):
        # PMT row
        ttk.Label(self.root, text="PMT:").grid(row=0, column=0, sticky="w")
        ttk.Entry(self.root, textvariable=self.pmt_var, width=10).grid(row=0, column=1)
        ttk.Label(self.root, text="₹").grid(row=0, column=2, sticky="w")
        
        # Rate row
        ttk.Label(self.root, text="Rate:").grid(row=1, column=0, sticky="w")
        ttk.Entry(self.root, textvariable=self.rate_var, width=10).grid(row=1, column=1)
        ttk.Label(self.root, text="%").grid(row=1, column=2, sticky="w")
        
        # Periods row
        ttk.Label(self.root, text="Periods:").grid(row=2, column=0, sticky="w")
        ttk.Entry(self.root, textvariable=self.periods_var, width=10).grid(row=2, column=1)
        ttk.Label(self.root, text="years").grid(row=2, column=2, sticky="w")
        
        # Result
        ttk.Label(self.root, textvariable=self.result_var).grid(row=3, column=0, columnspan=3, pady=5)
        
        # Buttons
        ttk.Button(self.root, text="Calculate", command=self.calculate).grid(row=4, column=0, pady=5)
        ttk.Button(self.root, text="Reset", command=self.reset_to_defaults).grid(row=4, column=1, pady=5)

    def _validate_inputs(self):
        try:
            pmt = float(self.pmt_var.get())
            rate = float(self.rate_var.get().rstrip('%')) / 100
            periods = int(float(self.periods_var.get()))
            
            if pmt <= 0 or rate <= 0 or periods <= 0:
                raise ValueError("Values must be positive")
                
            return pmt, rate, periods
            
        except ValueError:
            raise ValueError("Please enter valid numbers")

    def calculate_future_value(self, pmt, rate, periods):
        if rate == 0:
            return pmt * periods
        return pmt * ((1 + rate) ** periods - 1) / rate

    def calculate(self):
        try:
            pmt, rate, periods = self._validate_inputs()
            future_value = self.calculate_future_value(pmt, rate, periods)
            self.result_var.set(f"Future Value: ₹{future_value:,.2f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            self.result_var.set("Future Value: Error")

    def reset_to_defaults(self):
        self.pmt_var.set(str(self.DEFAULT_PMT))
        self.rate_var.set(str(self.DEFAULT_RATE))
        self.periods_var.set(str(self.DEFAULT_PERIODS))
        self.result_var.set("Future Value: --")

def main():
    root = tk.Tk()
    app = PvannCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()