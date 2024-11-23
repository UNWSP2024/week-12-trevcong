#AUTHOR: TREVOR CONGER UNWSP
#DATE: 11/22/2024
#PURPOSE: CALCULATE THE COST OF LONG DISTANCE CALLS

import tkinter
from tkinter import messagebox

class CallChargesApp:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Call Charges Calculator")
        self.main_window.geometry("300x250")
        self.main_window.configure(bg="lightblue")

        self.rate_frame = tkinter.Frame(self.main_window, bg="lightblue")
        self.minutes_frame = tkinter.Frame(self.main_window, bg="lightblue")
        self.button_frame = tkinter.Frame(self.main_window, bg="lightblue")

        self.rate_var = tkinter.StringVar()
        self.rate_var.set("Daytime") 

        self.daytime_button = tkinter.Radiobutton(self.rate_frame, text="Daytime ($0.02/min)", variable=self.rate_var, value="Daytime", bg="lightblue")
        self.evening_button = tkinter.Radiobutton(self.rate_frame, text="Evening ($0.12/min)", variable=self.rate_var, value="Evening", bg="lightblue")
        self.offpeak_button = tkinter.Radiobutton(self.rate_frame, text="Off-Peak ($0.05/min)", variable=self.rate_var, value="Off-Peak", bg="lightblue")

        self.daytime_button.pack(anchor="w")
        self.evening_button.pack(anchor="w")
        self.offpeak_button.pack(anchor="w")

        self.minutes_label = tkinter.Label(self.minutes_frame, text="Enter Minutes:", bg="lightblue")
        self.minutes_entry = tkinter.Entry(self.minutes_frame, width=10)

        self.minutes_label.pack(side="left", padx=5, pady=5)
        self.minutes_entry.pack(side="left", padx=5, pady=5)

        self.calculate_button = tkinter.Button(self.button_frame, text="Calculate", command=self.calculate_charge, bg="green", fg="white")
        self.quit_button = tkinter.Button(self.button_frame, text="Quit", command=self.main_window.destroy, bg="red", fg="white" )

        self.calculate_button.pack(side="left", padx=10, pady=10)
        self.quit_button.pack(side="left", padx=10, pady=10)

        self.rate_frame.pack(pady=10)
        self.minutes_frame.pack(pady=10)
        self.button_frame.pack(pady=10)

        tkinter.mainloop()

    def calculate_charge(self):
        try:
            minutes = float(self.minutes_entry.get())
            rate = 0.0

            if self.rate_var.get() == "Daytime":
                rate = 0.02
            elif self.rate_var.get() == "Evening":
                rate = 0.12
            elif self.rate_var.get() == "Off-Peak":
                rate = 0.05

            charge = rate * minutes

            messagebox.showinfo("Charge", f"The total charge is ${charge:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of minutes.")

if __name__ == "__main__":
    app = CallChargesApp()