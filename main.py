#!/opt/homebrew/bin/python3

import tkinter as tk
from datetime import datetime, timedelta


class TimerWidget(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tkinter widget")
        self.geometry("720x550")
        self.resizable(True, True) 

        
    #     self.title("Timer Widget")
        
    #     self.task_entry = tk.Entry(self)
    #     self.task_entry.pack()
        
    #     self.time_entry = tk.Entry(self)
    #     self.time_entry.pack()
        
    #     self.countdown_label = tk.Label(self)
    #     self.countdown_label.pack()
        
    #     self.update_countdown()
    
    # def update_countdown(self):
    #     now = datetime.now()
    #     target_time_str = self.time_entry.get()
    #     target_time = datetime.strptime(target_time_str, "%Y-%m-%d %H:%M:%S")
    #     remaining_time = target_time - now
        
    #     self.countdown_label.config(text=str(remaining_time))
    #     self.after(1000, self.update_countdown)

if __name__ == "__main__":
    widget = TimerWidget()
    widget.mainloop()