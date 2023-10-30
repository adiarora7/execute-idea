#!/opt/homebrew/bin/python3

import tkinter as tk
from datetime import datetime, timedelta

class TimerWidget(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("Death of an Idea")
        self.configure(bg="black")
        self.geometry("480x220")
        self.resizable(0, 0) 

        # Frame1 - Idea Name and settings button
        self.frame1 = tk.Frame(bg="black")
        self.frame1.pack(fill=tk.X)

        self.task_label = tk.Label(master=self.frame1, fg="#F0F8FA", bg="black", text="Name of Idea", font=("Inter", 38, "bold italic"), anchor="w")
        self.task_label.pack(side=tk.LEFT, fill=tk.BOTH, padx=(20,0), pady=(10,0))

        self.settings_button = tk.Button(master=self.frame1, text="+" ,bg="black", bd=0, highlightthickness=0, relief=tk.FLAT, highlightbackground="black", command=self.open_settings)
        self.settings_button.pack(side=tk.RIGHT,padx=(0,20))

        # Frame2 - time countdown
        self.frame2 = tk.Frame(bg="black")
        self.frame2.pack(fill=tk.X)

        self.time_label = tk.Label(master=self.frame2, fg="#F0F8FA", bg="black", text="--", font=("Lexend", 68, "bold italic"), anchor="nw")
        self.time_label.pack(fill=tk.BOTH, padx=(20,0))

        # Frame3 - static footer text
        self.frame3 = tk.Frame(bg="black")
        self.frame3.pack(fill=tk.X)

        self.tagline_label = tk.Label(master=self.frame3, fg="#F0F8FA", bg="black",text="till the death of your idea.", font=("Inter", 32, "bold italic"), anchor="nw")
        self.tagline_label.pack(fill=tk.BOTH, padx=(20,0), pady=(0,12))

        self.deadline = None  # Initialize a deadline attribute to None
        self.update_timer()  # Start the timer

    def open_settings(self):
        print("open_settings called")  # Debugging print statement
        self.settings_button.config(state=tk.DISABLED)  # Disable the settings button
        self.settings_window = SettingsWindow(self, self.re_enable_settings_button)

    def re_enable_settings_button(self):
        print("re_enable_settings_button called")  # Debugging print statement
        self.settings_button.config(state=tk.NORMAL)  # Re-enable the settings button

    def update_timer(self):
        if self.deadline:  # Only update the timer if a deadline has been set
            remaining_time = self.deadline - datetime.now()
            total_seconds = int(remaining_time.total_seconds())  # Get the total remaining seconds
            hours, remainder = divmod(total_seconds, 3600)
            minutes, seconds = divmod(remainder, 60) 
            self.time_label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}") 

        self.after(1000, self.update_timer)  # Update the timer every 1000 milliseconds (1 second)


class SettingsWindow(tk.Toplevel):
    def __init__(self, master, on_close_callback):
        print("__init__ of SettingsWindow called")  # Debugging print statement
        super().__init__(master)
        self.on_close_callback = on_close_callback
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        #configure settings window
        self.title("Settings")
        self.geometry("300x200")
        
        #Idea input - Label & Entry 
        self.idea_entry_label = tk.Label(self, text="Name of Idea", font=("arial", 16, "bold"), anchor="w")
        self.idea_entry_label.pack(fill=tk.BOTH, pady=(5,0), padx=10)
        self.idea_entry = tk.Entry(self)
        self.idea_entry.pack(fill=tk.BOTH, padx=10, pady=5)
        self.idea_entry.insert(0, master.task_label.cget("text"))  # Get current idea name

        #Deadline input - Label, Example of input format & Entry
        self.time_entry_label = tk.Label(self, text="Deadline", font=("arial", 16, "bold"), anchor="w")
        self.time_entry_label.pack(fill=tk.BOTH, pady=(5,0), padx=10)
        self.time_entry_label = tk.Label(self, text="ex. 12:00 for 12 hours -  73:00 for 73 hours etc.", font=("arial", 12), anchor="w").pack(fill=tk.BOTH, padx=10)
        self.time_entry = tk.Entry(self)
        self.time_entry.pack(fill=tk.BOTH, padx=10, pady=5)
        self.time_entry.insert(0, master.time_label.cget("text"))  # Get current time

        #Confirm button ->  Updates settings and then closes settings window.
        self.confirm_button = tk.Button(self, text="Confirm", command=lambda: self.update_settings(master))
        self.confirm_button.pack(side=tk.LEFT, padx=5, pady=5)

        #Cancel Button -> Closes settings windows
        self.cancel_button = tk.Button(self, text="Cancel", command=self.on_close)
        self.cancel_button.pack(side=tk.RIGHT, padx=5, pady=5)

    def on_close(self):
        print("on_close called")  # Debugging print statement
        self.on_close_callback()
        self.destroy()

    #Updates values for main window - retrieves user input values from settings window, and then sets main window values
    def update_settings(self, master):
        print("update_settings called")  # Debugging print statement
        new_idea = self.idea_entry.get()
        new_time = self.time_entry.get()

        master.task_label.config(text=new_idea)
        hours, minutes = map(int, new_time.split(':'))
        master.deadline = datetime.now() + timedelta(hours=hours, minutes=minutes)

        self.on_close()  # Close the settings window

if __name__ == "__main__":
    widget = TimerWidget()
    widget.mainloop()
