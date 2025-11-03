# SER416 - Fall'25 B
# ndavispe
# exercise1.py

import tkinter as tk
from tkinter import ttk, messagebox
import sys

class PvannCalculator:
    DEFAULT_PMT = 10000
    DEFAULT_RATE = 8.0
    DEFAULT_PERIODS = 20
    
    def __init__(self, root):
        self.root = root
        self.root.title("Pvann Calculator")
        
        # Set a fixed window size
        self.root.geometry("400x250")
        
        # Create a main container frame with visible background
        self.main_frame = tk.Frame(self.root, bg='white', padx=20, pady=20)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
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
        # PMT Row - with explicit backgrounds and borders
        pmt_frame = tk.Frame(self.main_frame, bg='white')
        pmt_frame.pack(fill=tk.X, pady=8)
        
        tk.Label(pmt_frame, text="PMT:", bg='white', fg='black', 
                font=('Helvetica', 11)).pack(side=tk.LEFT)
        
        pmt_entry = tk.Entry(pmt_frame, textvariable=self.pmt_var, 
                           width=15, font=('Helvetica', 11),
                           relief=tk.SUNKEN, bd=2)
        pmt_entry.pack(side=tk.LEFT, padx=8)
        
        tk.Label(pmt_frame, text="₹", bg='white', fg='black',
                font=('Helvetica', 11)).pack(side=tk.LEFT)
        
        # Rate Row
        rate_frame = tk.Frame(self.main_frame, bg='white')
        rate_frame.pack(fill=tk.X, pady=8)
        
        tk.Label(rate_frame, text="Rate:", bg='white', fg='black',
                font=('Helvetica', 11)).pack(side=tk.LEFT)
        
        rate_entry = tk.Entry(rate_frame, textvariable=self.rate_var,
                            width=15, font=('Helvetica', 11),
                            relief=tk.SUNKEN, bd=2)
        rate_entry.pack(side=tk.LEFT, padx=8)
        
        tk.Label(rate_frame, text="%", bg='white', fg='black',
                font=('Helvetica', 11)).pack(side=tk.LEFT)
        
        # Periods Row
        periods_frame = tk.Frame(self.main_frame, bg='white')
        periods_frame.pack(fill=tk.X, pady=8)
        
        tk.Label(periods_frame, text="Periods:", bg='white', fg='black',
                font=('Helvetica', 11)).pack(side=tk.LEFT)
        
        periods_entry = tk.Entry(periods_frame, textvariable=self.periods_var,
                               width=15, font=('Helvetica', 11),
                               relief=tk.SUNKEN, bd=2)
        periods_entry.pack(side=tk.LEFT, padx=8)
        
        tk.Label(periods_frame, text="years", bg='white', fg='black',
                font=('Helvetica', 11)).pack(side=tk.LEFT)
        
        # Result
        result_label = tk.Label(self.main_frame, textvariable=self.result_var,
                               bg='white', fg='blue', 
                               font=('Helvetica', 12, 'bold'))
        result_label.pack(pady=15)
        
        # Buttons
        button_frame = tk.Frame(self.main_frame, bg='white')
        button_frame.pack(pady=15)
        
        calculate_btn = tk.Button(button_frame, text="Calculate", 
                                 command=self.calculate, width=12,
                                 font=('Helvetica', 11),
                                 bg='#4CAF50', fg='white')  # Green button
        calculate_btn.pack(side=tk.LEFT, padx=8)
        
        reset_btn = tk.Button(button_frame, text="Reset",
                             command=self.reset_to_defaults, width=12,
                             font=('Helvetica', 11),
                             bg='#f44336', fg='white')  # Red button
        reset_btn.pack(side=tk.LEFT, padx=8)

    def _validate_inputs(self):
        try:
            pmt = float(self.pmt_var.get())
            rate = float(self.rate_var.get().rstrip('%')) / 100  # Fixed: was self.pmt_var
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