import numpy as np
import matplotlib as mtp
mtp.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Oscilloscope")
        # initialise the integer variables
        self.vol = IntVar(value=1)
        self.freq = IntVar(value=1)
        # create widgets
        self.create_widgets()
        
    def create_widgets(self):
        # left frame for input
        fLeft = Frame(self)
        Label(fLeft, text="Voltage: ", font=("Calibri", 25)).grid(row=0, column=0, padx=10, pady=10)
        self.vol_ent = Entry(fLeft,  font=("Calibri", 25), textvariable=self.vol)
        Label(fLeft, text="Frequency: ", font=("Calibri", 25)).grid(row=1, column=0, padx=10, pady=10)
        self.fre_ent = Entry(fLeft, font=("Calibri", 25), textvariable=self.freq)
        btn = Button(fLeft, text="Compute", font=("Calibri", 25), command=self.setValue)
        
        self.vol_ent.grid(row=0, column=1, padx=10, pady=10)
        self.fre_ent.grid(row=1,  column=1, padx=10, pady=10)
        btn.grid(row=2, column=1, padx=10, pady=10)
        # right frame for display graph
        self.fRight = Frame(self)
        self.plotter()
        # pack to window
        fLeft.grid(row=0,column=0)
        self.fRight.grid(row=0,column=1)
        
    def plotter(self):
        # initialise the graph
        self.figure = Figure(dpi=100)
        self.plot_canvas = FigureCanvasTkAgg(self.figure, self.fRight) # display the scale
        self.axes = self.figure.add_subplot(111) # scale setup
        x = np.arange(0.0, 1.0, 0.01) # x scale from 0.0 to 1.0 with scale 0.01
        amplitude = np.sin(2 * np.pi * x * self.freq.get())  * self.vol.get() # get sin wave amplitude up with voltage, amount of wave with frequency
        self.axes.plot(x, amplitude) # ready to plot
        self.axes.set_title(f"Waveform: {self.vol.get()}V, {self.freq.get()}Hz") # head title
        self.axes.set_xlabel("Time (s)") # x-label axis
        self.plot_canvas.draw() # plot it and display
        self.plot_canvas.get_tk_widget().grid(column=0, row=0, sticky="nsew") # pack to right frame
        
    def setValue(self):
        newvol = self.vol_ent.get() # get the value from the voltage entry 
        newfreq = self.fre_ent.get() # get the value from the frequency enttry
        self.vol.set(newvol) # set the variable
        self.freq.set(newfreq) # set the variable
        self.axes.clear() # clear graph
        self.plotter() # plot again wiht new values
        
if __name__ == "__main__":
    app = App()
    app.mainloop()