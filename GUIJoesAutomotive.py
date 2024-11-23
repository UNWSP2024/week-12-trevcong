import tkinter

class GUIJoesAutomotive:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.configure(bg='blue')
        self.main_window.geometry('600x600')
        self.main_window.title("Joe's Automotive")

        self.test1_frame = tkinter.Frame(self.main_window, bg='blue')
        self.result_frame = tkinter.Frame(self.main_window, bg='blue')
        self.button_frame = tkinter.Frame(self.main_window, bg='blue')

        self.services = [
            ("Oil Change", 30),
            ("Lube Job", 20),
            ("Radiator Flush", 40),
            ("Transmission Fluid", 100),
            ("Inspection", 35),
            ("Muffler Replacement", 200),
            ("Tire Rotation", 20)
        ]

        self.service_vars = {}

        for service, price in self.services:
            var = tkinter.IntVar() 
            self.service_vars[service] = (var, price)
            check = tkinter.Checkbutton(
                self.test1_frame,
                text=f"{service} - ${price:.2f}",
                variable=var,
                bg='blue',
                fg='white',
                anchor='w',
                selectcolor='black'
            )
            check.pack(anchor='w')

        # Label and variable to display the total
        self.result_label = tkinter.Label(
            self.result_frame,
            text="Total Cost: ",
            bg='blue',
            fg='white',
            font=("Arial", 14)
        )
        self.total_var = tkinter.StringVar(value="$0.00")
        self.total_label = tkinter.Label(
            self.result_frame,
            textvariable=self.total_var,
            bg='blue',
            fg='white',
            font=("Arial", 14)
        )
        self.result_label.pack(side='left', padx=10)
        self.total_label.pack(side='left')

        # Buttons
        self.calc_button = tkinter.Button(
            self.button_frame,
            text='Calculate Total',
            command=self.calculate_total
        )
        self.quit_button = tkinter.Button(
            self.button_frame,
            text='Quit',
            command=self.main_window.destroy
        )

        self.calc_button.pack(side='left', padx=10)
        self.quit_button.pack(side='left', padx=10)

        self.test1_frame.pack(pady=10)
        self.result_frame.pack(pady=10)
        self.button_frame.pack(pady=10)

        tkinter.mainloop()

    def calculate_total(self):
        total = 0
        for var, price in self.service_vars.values():
            if var.get() == 1:
                total += price
        self.total_var.set(f"${total:.2f}")

if __name__ == '__main__':
    GUIJoesAutomotive()
