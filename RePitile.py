import tkinter as tk
import time

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
        
    #Function call to destroy root program   
    def quitprogram(self):
    
        self.destroy()
        
#Class for Main Window        
class MainFrame(tk.Frame):
    
    def __init__(self, parent, controller):
    
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #Label for clock
        self.clock_label = tk.Label(self, text=time.strftime("%I:%M %p"), font=("Times", 60))
        self.clock_label.grid(column = 1)

        #Label for Temp1
        temp1_label = tk.Label(self, text = "Temp 1", font = ("Consolas 20 underline"))
        temp1_label.grid(row = 1, column = 0, pady = 20)

        #Label for Temp2
        temp2_label = tk.Label(self, text = "Temp 2", font = ("Consolas 20 underline"))
        temp2_label.grid(row = 1, column = 1)

        #Label for Humidity
        humidity_label = tk.Label(self, text = "Humidity", font = ("Consolas 20 underline"))
        humidity_label.grid(row = 1, column = 2)

        #Data for Temp1
        temp1_data = tk.Label(self, text = "100ºF", font = ("Times 65"))
        temp1_data.grid(row = 2, column = 0)
        
        #Data for Temp2
        temp1_data = tk.Label(self, text = "100ºF", font = ("Times 65"))
        temp1_data.grid(row = 2, column = 1)
        
        #Data for Humidity
        temp1_data = tk.Label(self, text = "100%", font = ("Times 65"))
        temp1_data.grid(row = 2, column = 2)

        #Label for current profile
        profile_label = tk.Label(self, text = "Current Profile: Snake", font = ("Times 25"))
        profile_label.grid(row = 3, column = 1, pady = 10)

        #Quit Button
        quit_button = tk.Button(self, text = "Quit", font = ("12"), width = 20, height = 7,
                                command = lambda: controller.quitprogram())
        quit_button.grid(row = 4, columnspan = 1, padx = 30)
        
        #Settings Button
        settings_button = tk.Button(self, text = "Settings", font = ("12"), width = 20, height = 7,
                                command = lambda: controller.showframe("SettingsFrame"))
        settings_button.grid(row = 4, column = 2)

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

        back_button = tk.Button(self, text = "Back", width = 20, height = 7,
                                command = lambda: controller.showframe("MainFrame"))
        back_button.pack(side = "left")

#Main program code
if __name__ == "__main__":
    
    app = RePitile()
    app.geometry("800x480")
    app.overrideredirect(1)
    app.resizable(False, False)
    app.frames["MainFrame"].clocktick()
    app.mainloop()
