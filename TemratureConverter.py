import tkinter as tk
from tkinter import ttk, messagebox

def convert_temperature():
    try:
        temp = float(entry.get())
        unit = unit_var.get()
        
        if unit == "Celsius":
            fahrenheit = (temp * 9/5) + 32
            kelvin = temp + 273.15
            label_fahrenheit_value.config(text=f"{fahrenheit:.2f} °F")
            label_kelvin_value.config(text=f"{kelvin:.2f} K")
            label_celsius_value.config(text=f"{temp:.2f} °C")
        elif unit == "Fahrenheit":
            celsius = (temp - 32) * 5/9
            kelvin = celsius + 273.15
            label_celsius_value.config(text=f"{celsius:.2f} °C")
            label_kelvin_value.config(text=f"{kelvin:.2f} K")
            label_fahrenheit_value.config(text=f"{temp:.2f} °F")
        elif unit == "Kelvin":
            celsius = temp - 273.15
            fahrenheit = (celsius * 9/5) + 32
            label_celsius_value.config(text=f"{celsius:.2f} °C")
            label_fahrenheit_value.config(text=f"{fahrenheit:.2f} °F")
            label_kelvin_value.config(text=f"{temp:.2f} K")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number.")

#main window
window = tk.Tk()
window.title("Temperature Converter")
window.geometry("400x250")
window.resizable(True, True)

# Style
style = ttk.Style()
style.configure("TButton", font=("Arial", 12, "bold"), padding=10)
style.configure("TLabel", font=("Arial", 12, "bold"))
style.configure("TEntry", font=("Arial", 12))
style.configure("TCombobox", font=("Arial", 12))

# background color
window.configure(bg='#f0f0f0')

# Input field
input_frame = ttk.Frame(window, padding=10, relief="solid", borderwidth=2)
input_frame.grid(row=0, column=0, columnspan=2, padx=20, pady=10, sticky=tk.W+tk.E)

entry_label = ttk.Label(input_frame, text="Enter Temperature:")
entry_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)
entry = ttk.Entry(input_frame, width=20)
entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

# Dropdown menu 
unit_label = ttk.Label(input_frame, text="Select Unit:")
unit_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
unit_var = tk.StringVar(value="Celsius")
unit_menu = ttk.Combobox(input_frame, textvariable=unit_var, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
unit_menu.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

# Convert button
convert_button = ttk.Button(window, text="Convert", command=convert_temperature)
convert_button.grid(row=1, column=0, columnspan=2, padx=20, pady=15)

# Output labels
output_frame = ttk.Frame(window, padding=10, relief="solid", borderwidth=2)
output_frame.grid(row=2, column=0, columnspan=2, padx=20, pady=15, sticky=tk.W+tk.E)

label_celsius = ttk.Label(output_frame, text="Celsius:")
label_celsius.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
label_celsius_value = ttk.Label(output_frame, text="0.00 °C")
label_celsius_value.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

label_fahrenheit = ttk.Label(output_frame, text="Fahrenheit:")
label_fahrenheit.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
label_fahrenheit_value = ttk.Label(output_frame, text="0.00 °F")
label_fahrenheit_value.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

label_kelvin = ttk.Label(output_frame, text="Kelvin:")
label_kelvin.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
label_kelvin_value = ttk.Label(output_frame, text="0.00 K")
label_kelvin_value.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

#main loop
window.mainloop()
