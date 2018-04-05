import tkinter as tk
import time
import os

from tkinter import filedialog

#PATHNAME = ""

#Initialization of root window as Tk subclass
class RePitile(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        '''
        Container is used to stack the pages of each section
        of the GUI. When we want a different page to be visible,
        show_frame will raise the appropriate page to the front
        '''
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        for F in (MainFrame, SettingsFrame):
            
            page_name = F.__name__
            frame = F(parent = container, controller = self)
            self.frames[page_name] = frame
            
            frame.grid(row = 0, column = 0, sticky = "nsew")
            
        self.showframe("MainFrame")
    
    #Determines which class page to instantiate
    def showframe(self, page_name):
        
        frame = self.frames[page_name]
        frame.tkraise()
        
    #Method to destroy root program   
    def quitprogram(self):
    
        self.destroy()

    #Method to load configuration file
    def loadfile(self):

        file_name = filedialog.askopenfilename(initialdir=()) #Specify directory with PATHNAME @ top

        try:

            with open(file_name) as test_file:

                print(test_file.read())
        except:

            print("No file exists or no file selected")
        
#Class for Main Window        
class MainFrame(tk.Frame):
    
    def __init__(self, parent, controller):
    
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #Label for clock
        self.clock_label = tk.Label(self, text=time.strftime("%I:%M %p"), font=("Times", 60))
        self.clock_label.grid(row = 0, column = 2)

        #Label for Temp
        temp1_label = tk.Label(self, text = "Average Temp", font = ("Consolas 20 underline"))
        temp1_label.grid(row = 1, column = 1, pady = 20)

        #Label for Humidity
        humidity_label = tk.Label(self, text = "Humidity", font = ("Consolas 20 underline"))
        humidity_label.grid(row = 1, column = 3)

        #Data for Temp
        temp_data = tk.Label(self, text = "100 ºF", font = ("Times 65"))
        temp_data.grid(row = 2, column = 1)
        
        #Data for Humidity
        temp_data = tk.Label(self, text = "100%", font = ("Times 65"))
        temp_data.grid(row = 2, column = 3)

        #Label for current profile
        profile_label = tk.Label(self, text = "Current Profile: Snake", font = ("Times 25"))
        profile_label.grid(row = 3, column = 2, pady = 10)

        #Quit Button
        quit_button = tk.Button(self, text = "Quit", font = ("12"), width = 20, height = 7,
                                command = lambda: controller.quitprogram())
        quit_button.grid(row = 4, column = 1, padx = 30)
        
        #Settings Button
        settings_button = tk.Button(self, text = "Settings", font = ("12"), width = 20, height = 7,
                                command = lambda: controller.showframe("SettingsFrame"))
        settings_button.grid(row = 4, column = 3)

    #Function used to make clock label 'tick'
    def clocktick(self):

        curr_time = time.strftime("%I:%M %p")
        self.clock_label.config(text = curr_time)
        self.clock_label.after(1000, self.clocktick)

#Class for Settings Window
class SettingsFrame(tk.Frame):

    def __init__(self, parent, controller):
 
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.mintemp = tk.IntVar(0)
        self.maxtemp = tk.IntVar(0)
        self.humidity = tk.IntVar(0)

        #Create back button
        back_button = tk.Button(self, text = "Back", font = ("12"), width = 20, height = 7,
                                command = lambda: controller.showframe("MainFrame"))
        back_button.grid(row = 2, column = 0, pady = 10)

        #Create load button
        load_button = tk.Button(self, text = "Load Profile", font = ("12"), width = 20, height = 7,
                                command = lambda: controller.loadfile())
        load_button.grid(row = 0, column = 0, pady = 10)

        #Create save button
        save_button = tk.Button(self, text = "Save Profile", font = ("12"), width = 20, height = 7)
        save_button.grid(row = 1, column = 0, pady = 10)

        #Create arrow buttons for custom profile
        mintemp_up = tk.Button(self, text = "Min Temp\n\n▲", font = ("20"), width  = 10, height = 5,
                               command = self.incmintemp)
        mintemp_up.grid(row = 0, column = 1, padx = 50)

        maxtemp_up = tk.Button(self, text = "Max Temp\n\n▲", font = ("20"), width  = 10, height = 5,
                               command = self.incmaxtemp)
        maxtemp_up.grid(row = 0, column = 2, padx = 50)
        
        humidity_up = tk.Button(self, text = "Humidity\n\n▲", font = ("20"), width  = 10, height = 5,
                                command = self.inchumidity)
        humidity_up.grid(row = 0, column = 3, padx = 50)

        mintemp_down = tk.Button(self, text = "▼\n\nMin Temp", font = ("20"), width  = 10, height = 5,
                                 command = self.decmintemp)
        mintemp_down.grid(row = 2, column = 1)

        maxtemp_down = tk.Button(self, text = "▼\n\nMax Temp", font = ("20"), width  = 10, height = 5,
                                 command = self.decmaxtemp)
        maxtemp_down.grid(row = 2, column = 2)

        humidity_down = tk.Button(self, text = "▼\n\nHumidity", font = ("20"), width  = 10, height = 5,
                                  command = self.dechumidity)
        humidity_down.grid(row = 2, column = 3)

        #Create labels with custom profile info

        self.mintemp_label = tk.Label(self, text=str(
            self.mintemp.get()) + "ºC", font=("Times 60"))
        self.mintemp_label.grid(row=1, column=1)

        self.maxtemp_label = tk.Label(self, text=str(
            self.maxtemp.get()) + "ºC", font=("Times 60"))
        self.maxtemp_label.grid(row=1, column=2)

        self.humidity_label = tk.Label(self, text=str(
            self.humidity.get()) + "%", font=("Times 60"))
        self.humidity_label.grid(row=1, column=3)

    
    #Methods to increment/decrement values and update labels
    def incmintemp(self):
        self.mintemp.set(self.mintemp.get() + 1)
        self.mintemp_label["text"] = str(str(self.mintemp.get()) + "ºC")

    def decmintemp(self):
        self.mintemp.set(self.mintemp.get() - 1)
        self.mintemp_label["text"] = str(str(self.mintemp.get()) + "ºC")

    def incmaxtemp(self):
        self.maxtemp.set(self.maxtemp.get() + 1)
        self.maxtemp_label["text"] = str(str(self.maxtemp.get()) + "ºC")

    def decmaxtemp(self):
        self.maxtemp.set(self.maxtemp.get() - 1)
        self.maxtemp_label["text"] = str(str(self.maxtemp.get()) + "ºC")

    def inchumidity(self):
        self.humidity.set(self.humidity.get() + 1)
        self.humidity_label["text"] = str(str(self.humidity.get()) + "%")

    def dechumidity(self):
        self.humidity.set(self.humidity.get() - 1)
        self.humidity_label["text"] = str(str(self.humidity.get()) + "%")

#Main program code
if __name__ == "__main__":
    
    app = RePitile()
    app.geometry("800x480")
    #app.overrideredirect(1)
    app.resizable(False, False)
    app.frames["MainFrame"].clocktick()
    app.mainloop()
