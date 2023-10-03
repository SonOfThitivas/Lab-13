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
        self.vol = IntVar(value=1)
        self.freq = IntVar(value=1)
        
        self.create_widgets()
        
    def create_widgets(self):
        fLeft = Frame(self)
        Label(fLeft, text="Voltage: ", font=("Calibri", 25)).grid(row=0, column=0, padx=10, pady=10)
        self.vol_ent = Entry(fLeft,  font=("Calibri", 25), textvariable=self.vol)
        Label(fLeft, text="Frequency: ", font=("Calibri", 25)).grid(row=1, column=0, padx=10, pady=10)
        self.fre_ent = Entry(fLeft, font=("Calibri", 25), textvariable=self.freq)
        btn = Button(fLeft, text="Compute", font=("Calibri", 25), command=self.setValue)
        
        self.vol_ent.grid(row=0, column=1, padx=10, pady=10)
        self.fre_ent.grid(row=1,  column=1, padx=10, pady=10)
        btn.grid(row=2, column=1, padx=10, pady=10)
        
        self.fRight = Frame(self)
        self.plotter()
        
        fLeft.grid(row=0,column=0)
        self.fRight.grid(row=0,column=1)
        
    def plotter(self):
        self.figure = Figure(dpi=100)
        self.plot_canvas = FigureCanvasTkAgg(self.figure, self.fRight)
        self.axes = self.figure.add_subplot(111)
        times = np.arange(0.0, 1.0, 0.01)
        sin = np.sin(2 * np.pi * times * self.freq.get())  * self.vol.get()
        self.axes.plot(times, sin)
        self.axes.set_title(f"Waveform: {self.vol.get()}V, {self.freq.get()}Hz")
        self.axes.set_xlabel("Time (s)")
        self.plot_canvas.draw()
        self.plot_canvas.get_tk_widget().grid(column=0, row=0, sticky="nsew")
        
    def setValue(self):
        newvol = self.vol_ent.get()
        newfreq = self.fre_ent.get()
        self.vol.set(newvol)
        self.freq.set(newfreq)
        self.axes.clear()
        self.plotter()
        
if __name__ == "__main__":
    app = App()
    app.mainloop()