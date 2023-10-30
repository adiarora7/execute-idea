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

        # Frame1 contains Idea Name and settings button
        self.frame1 = tk.Frame(bg="black")
        self.frame1.pack(fill=tk.X)

        self.task_label = tk.Label(master=self.frame1, fg="#F0F8FA", bg="black", text="Name of Idea", font=("Inter", 38, "bold italic"), anchor="w")
        self.task_label.pack(side=tk.LEFT, fill=tk.BOTH, padx=(20,0), pady=(10,0))

        self.settings_button = tk.Button(master=self.frame1, text="+" ,bg="black", bd=0, highlightthickness=0, relief=tk.FLAT, highlightbackground="black", command=self.open_settings)
        self.settings_button.pack(side=tk.RIGHT,padx=(0,20))

        # Frame2 contains time countdown
        self.frame2 = tk.Frame(bg="black")
        self.frame2.pack(fill=tk.X)

        self.time_label = tk.Label(master=self.frame2, fg="#F0F8FA", bg="black", text="--", font=("Lexend", 68, "bold italic"), anchor="nw")
        self.time_label.pack(fill=tk.BOTH, padx=(20,0))

        # Frame3 contains static footer text
        self.frame3 = tk.Frame(bg="black")
        self.frame3.pack(fill=tk.X)

        self.tagline_label = tk.Label(master=self.frame3, fg="#F0F8FA", bg="black",text="Till the death of your idea.", font=("Inter", 32, "bold italic"), anchor="nw")
        self.tagline_label.pack(fill=tk.BOTH, padx=(20,0), pady=(0,12))

        self.deadline = None  # Initialize a deadline attribute to None
        self.update_timer()  # Start the timer

    def open_settings(self):
        self.settings_window = SettingsWindow(self)

    def update_timer(self):
        if self.deadline:  # Only update the timer if a deadline has been set
            remaining_time = self.deadline - datetime.now()
            total_seconds = int(remaining_time.total_seconds())  # Get the total remaining seconds
            hours, remainder = divmod(total_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)  # Modified this line to get seconds
            self.time_label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")  # Modified this line to include seconds

        self.after(1000, self.update_timer)  # Update the timer every 1000 milliseconds (1 second)


class SettingsWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Settings")
        self.geometry("300x200")

        self.idea_entry = tk.Entry(self)
        self.idea_entry.pack(pady=5)
        self.idea_entry.insert(0, master.task_label.cget("text"))  # Get current idea name

        self.time_entry = tk.Entry(self)
        self.time_entry.pack(pady=5)
        self.time_entry.insert(0, master.time_label.cget("text"))  # Get current time

        self.confirm_button = tk.Button(self, text="Confirm", command=lambda: self.update_settings(master))
        self.confirm_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.cancel_button = tk.Button(self, text="Cancel", command=self.destroy)
        self.cancel_button.pack(side=tk.RIGHT, padx=5, pady=5)

    def update_settings(self, master):
        new_idea = self.idea_entry.get()
        new_time = self.time_entry.get()

        master.task_label.config(text=new_idea)
        hours, minutes = map(int, new_time.split(':'))
        master.deadline = datetime.now() + timedelta(hours=hours, minutes=minutes)

        self.destroy()  # Close the settings window

if __name__ == "__main__":
    widget = TimerWidget()
    widget.mainloop()


# import tkinter as tk
# from datetime import datetime, timedelta


# class TimerWidget(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         #Configure window
#         self.title("Death of an Idea")
#         self.configure(bg="black")
#         self.geometry("480x220")
#         self.resizable(0, 0) 

#         #Frame1 contains Idea Name and settings button
#         self.frame1 = tk.Frame(bg="black")
#         self.frame1.pack(fill=tk.X)

#         self.task_label = tk.Label(master=self.frame1, fg="#F0F8FA", bg="black", text="Name of Idea", font=("Inter", 38, "bold italic"), anchor="w")
#         self.task_label.pack(side=tk.LEFT, fill=tk.BOTH, padx=(20,0), pady=(10,0))

#         self.settings_button = tk.Button(master=self.frame1, text="+" ,bg="black", bd=0, highlightthickness=0, relief=tk.FLAT, highlightbackground="black")
#         self.settings_button.pack(side=tk.RIGHT,padx=(0,20))

#         #Frame2 contains time countdown
#         self.frame2 = tk.Frame(bg="black")
#         self.frame2.pack(fill=tk.X)

#         self.time_label = tk.Label(master=self.frame2, fg="#F0F8FA", bg="black", text="2 3 : 5 9 hrs", font=("Lexend", 68, "bold italic"), anchor="nw")
#         self.time_label.pack(fill=tk.BOTH, padx=(20,0))

#         #Frame3 contains static footer text
#         self.frame3 = tk.Frame(bg="black")
#         self.frame3.pack(fill=tk.X)

#         self.tagline_label = tk.Label(master=self.frame3, fg="#F0F8FA", bg="black",text="Till the death of your idea.", font=("Inter", 32, "bold italic"), anchor="nw")
#         self.tagline_label.pack(fill=tk.BOTH, padx=(20,0), pady=(0,12))



#         self.settings_button.config(command=self.open_settings)  # Configure the settings button to open the settings window







#         self.deadline = None  # Initialize a deadline attribute to None
#         self.update_timer()  # Start the timer

#     def open_settings(self):
#         self.settings_window = SettingsWindow(self)

#     def update_timer(self):
#         if self.deadline:  # Only update the timer if a deadline has been set
#             remaining_time = self.deadline - datetime.now()
#             hours, remainder = divmod(remaining_time.seconds, 3600)
#             minutes = remainder // 60
#             self.time_label.config(text=f"{hours:02}:{minutes:02} hrs")

#         self.after(1000, self.update_timer)  # Update the timer every 1000 milliseconds (1 second)

# class SettingsWindow(tk.Toplevel):
#     def __init__(self, master):
#         super().__init__(master)

#         self.title("Settings")
#         self.geometry("300x200")

#         self.idea_entry = tk.Entry(self)
#         self.idea_entry.pack(pady=5)
#         self.idea_entry.insert(0, master.task_label.cget("text"))  # Get current idea name

#         self.time_entry = tk.Entry(self)
#         self.time_entry.pack(pady=5)
#         self.time_entry.insert(0, master.time_label.cget("text"))  # Get current time

#         self.confirm_button = tk.Button(self, text="Confirm", command=lambda: self.update_settings(master))
#         self.confirm_button.pack(side=tk.LEFT, padx=5, pady=5)

#         self.cancel_button = tk.Button(self, text="Cancel", command=self.destroy)
#         self.cancel_button.pack(side=tk.RIGHT, padx=5, pady=5)

#     def update_settings(self, master):
#         new_idea = self.idea_entry.get()
#         new_time = self.time_entry.get()

#         master.task_label.config(text=new_idea)
#         master.time_label.config(text=new_time)

#         self.destroy() 



# if __name__ == "__main__":
#     widget = TimerWidget()
#     widget.mainloop()