#AUTHOR: TREVOR CONGER UNWSP
#DATE: 11/22/2024
#PURPOSE: CALCULATE THE MILES PER GALLON OF A CAR

import tkinter

class MPH:
    def __init__(self):
    
        self.main_window = tkinter.Tk()
        self.main_window.configure(bg='blue')
        self.test1_frame = tkinter.Frame(self.main_window)
        self.test2_frame = tkinter.Frame(self.main_window)
        self.avg_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)


        self.test1_label = tkinter.Label(self.test1_frame, text='Enter the car\'s fuel tank capacity in gallons :')
        self.test1_entry = tkinter.Entry(self.test1_frame, width=10)
        self.test1_label.pack(side='left')
        self.test1_entry.pack(side='left')

        self.test2_label = tkinter.Label(self.test2_frame, text='Enter the number of miles you can travel on a full tank :')
        self.test2_entry = tkinter.Entry(self.test2_frame, width=10)
        
        self.test2_label.pack(side='left')
        self.test2_entry.pack(side='left')

        self.result_label = tkinter.Label(self.avg_frame, text='MPG: ')
        self.avg = tkinter.StringVar()
        self.avg_label = tkinter.Label(self.avg_frame, textvariable=self.avg)
        
        self.result_label.pack(side='left')
        self.avg_label.pack(side='left')

        self.calc_button = tkinter.Button(self.button_frame, text='Average', command=self.calc_MPG)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)
        

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')
        self.test1_frame.pack()
        self.test2_frame.pack()
        self.avg_frame.pack()
        self.button_frame.pack()

        tkinter.mainloop()

    #CALCULATE THE MILES PER GALLON
    #INPUT: FUEL TANK CAPACITY AND MILES YOU CAN TRAVEL ON A FULL TANK
    #OUTPUT: MILES PER GALLON
    def calc_MPG(self):
        self.test1 = float(self.test1_entry.get())
        self.test2 = float(self.test2_entry.get())

        self.MPG = (self.test2 / self.test1)
        self.avg.set(self.MPG)


if __name__ == '__main__':
    test_avg = MPH()
