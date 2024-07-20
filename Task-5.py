import tkinter as tk
from tkinter import ttk
import requests

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("USD Currency Converter")

        self.api_url = "https://api.exchangerate-api.com/v4/latest/USD"
        self.currencies = self.get_currencies()

        self.create_widgets()

    def get_currencies(self):
        response = requests.get(self.api_url)
        data = response.json()
        return data['rates']

    def convert_currency(self):
        amount = float(self.usd_entry.get())
        target_currency = self.currency_combobox.get()
        conversion_rate = self.currencies[target_currency]
        converted_amount = amount * conversion_rate
        self.result_label.config(text=f"{amount} USD = {converted_amount:.2f} {target_currency}")

    def create_widgets(self):
        # Input field for USD amount
        self.usd_label = tk.Label(self.root, text="Amount in USD:")
        self.usd_label.grid(column=0, row=0, padx=10, pady=10)

        self.usd_entry = tk.Entry(self.root)
        self.usd_entry.grid(column=1, row=0, padx=10, pady=10)

        # Dropdown menu for target currencies
        self.currency_label = tk.Label(self.root, text="Convert to:")
        self.currency_label.grid(column=0, row=1, padx=10, pady=10)

        self.currency_combobox = ttk.Combobox(self.root, values=list(self.currencies.keys()))
        self.currency_combobox.grid(column=1, row=1, padx=10, pady=10)
        self.currency_combobox.current(0)

        # Button to perform conversion
        self.convert_button = tk.Button(self.root, text="Convert", command=self.convert_currency)
        self.convert_button.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

        # Label to display the conversion result
        self.result_label = tk.Label(self.root, text="")
        self.result_label.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    converter = CurrencyConverter(root)
    root.mainloop()
