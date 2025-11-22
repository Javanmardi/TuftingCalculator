import tkinter as tk
from tkinter import ttk
# from tkinter import messagebox
from fractions import Fraction
import math
import webbrowser

def calculate_tuft_weight(ga, st, pl, den, pile_type):
    """
    Calculate tufting carpet weight depending on pile type (loop or cut).
    """
    if pile_type == "Cut":
        tuft = (1/ga) * (1000/25.4) * st * 10 * ((pl * 2) + (10/st)) * 0.001 * (den / 9000)
    else:  # Loop
        tuft = (1/ga) * (1000/25.4) * st * 10 * ((pl * 2) + (20/st)) * 0.001 * (den / 9000)
    
    # Round up to next integer
    return math.ceil(tuft)

def parse_number(value):
    """
    Parse input as either float or fraction (e.g. '1/8').
    """
    try:
        return float(Fraction(value))
    except ValueError:
        return float(value)

def on_calculate():
    try:
        ga = parse_number(gauge_var.get())  # now comes from dropdown
        st = parse_number(entry_st.get())
        pl = parse_number(entry_pl.get())
        den = parse_number(entry_den.get())
        pile_type = pile_type_var.get()
        
        tuft_weight = calculate_tuft_weight(ga, st, pl, den, pile_type)
        result_var.set(f"Tufting carpet weight = {tuft_weight} gram/m\u00b2")
    except Exception:
        result_var.set("Please enter valid numeric or fraction values.")

def on_reset():
    gauge_var.set("1/8")  # reset to default gauge
    # Clear all entry fields
    entry_st.delete(0, tk.END)
    entry_pl.delete(0, tk.END)
    entry_den.delete(0, tk.END)
    pile_type_var.set("Cut")  # reset to default pile type
    # Clear result label
    result_var.set("")

# GUI setup
root = tk.Tk()
root.title("Tufting Carpet Weight Calculator")

def show_about():
    about_window = tk.Toplevel(root)
    about_window.title("About")
    about_window.geometry("340x250")
    about_window.resizable(False, False)

    ttk.Label(about_window, text="Tufting Carpet Weight Calculator", font=("Segoe UI", 10, "bold")).pack(pady=(10, 5))
    ttk.Label(about_window, text="Created by Behrouz Javanmardi").pack()
    ttk.Label(about_window, text="Special thanks to Dr. Mohsen Bahador").pack(pady=(2, 5))

    # Clickable email label
    def open_email():
        webbrowser.open("mailto:behrouz@javanmardi.org")

    email_label = tk.Label(about_window, text="behrouz@javanmardi.org", font=("Consolas", 9), fg="blue", cursor="hand2")
    email_label.pack()
    email_label.bind("<Button-1>", lambda e: open_email())

    ttk.Label(about_window, text="License: MIT").pack()
    ttk.Label(about_window, text="Version: 1.0.0").pack(pady=(0, 10))

    ttk.Label(about_window, text="GitHub:").pack()

    def open_github():
        webbrowser.open("https://github.com/Javanmardi/TuftingCalculator")

    link_button = ttk.Button(about_window, text="Visit GitHub", command=open_github)
    link_button.pack(pady=5)

# Menu bar
menu_bar = tk.Menu(root)
about_menu = tk.Menu(menu_bar, tearoff=0)
about_menu.add_command(label="About", command=show_about)
menu_bar.add_cascade(label="Help", menu=about_menu)
root.config(menu=menu_bar)

# Gauge dropdown
ttk.Label(root, text="Gauge (inch):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
gauge_var = tk.StringVar(value="1/8")
gauge_box = ttk.Combobox(root, textvariable=gauge_var, 
                         values=["1/10", "1/8", "5/32", "5/16"], state="readonly")
gauge_box.grid(row=0, column=1, padx=5, pady=5)

# Stitch rate
ttk.Label(root, text="Stitch rate (per dm):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_st = ttk.Entry(root)
entry_st.grid(row=1, column=1, padx=5, pady=5)

# Pile height
ttk.Label(root, text="Pile height (mm):").grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_pl = ttk.Entry(root)
entry_pl.grid(row=2, column=1, padx=5, pady=5)

# Yarn denier
ttk.Label(root, text="Yarn denier (den):").grid(row=3, column=0, padx=5, pady=5, sticky="e")
entry_den = ttk.Entry(root)
entry_den.grid(row=3, column=1, padx=5, pady=5)

# Pile type dropdown
ttk.Label(root, text="Pile type:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
pile_type_var = tk.StringVar(value="Cut")
pile_type_box = ttk.Combobox(root, textvariable=pile_type_var, values=["Cut", "Loop"], state="readonly")
pile_type_box.grid(row=4, column=1, padx=5, pady=5)

# Buttons
calc_button = ttk.Button(root, text="Calculate", command=on_calculate)
calc_button.grid(row=5, column=0, padx=5, pady=10)

reset_button = ttk.Button(root, text="Reset", command=on_reset)
reset_button.grid(row=5, column=1, padx=5, pady=10)

# Result label
result_var = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_var, foreground="blue")
result_label.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()


