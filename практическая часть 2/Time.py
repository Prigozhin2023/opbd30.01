import tkinter as tk
from tkinter import messagebox
import time
import threading

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer")

        
        self.time_frame = tk.Frame(self.root)
        self.time_frame.pack(side=tk.TOP, pady=10)

        self.minutes_label = tk.Label(self.time_frame, text="Минуты:")
        self.minutes_label.pack(side=tk.LEFT, padx=5)

        self.minutes_entry = tk.Entry(self.time_frame, width=5)
        self.minutes_entry.pack(side=tk.LEFT, padx=5)

        self.seconds_label = tk.Label(self.time_frame, text="Секунды:")
        self.seconds_label.pack(side=tk.LEFT, padx=5)

        self.seconds_entry = tk.Entry(self.time_frame, width=5)
        self.seconds_entry.pack(side=tk.LEFT, padx=5)

        
        self.start_button = tk.Button(self.root, text="Начать", command=self.start_timer)
        self.start_button.pack(side=tk.TOP, pady=10)

       
        self.time_label = tk.Label(self.root, text="00:00", font=("Helvetica", 24))
        self.time_label.pack(side=tk.TOP, pady=10)

       
        self.timer_thread = None

    def start_timer(self):
       
        try:
            minutes = int(self.minutes_entry.get())
            seconds = int(self.seconds_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for minutes and seconds.")
            return

        
        total_seconds = minutes * 60 + seconds

       
        self.timer_thread = threading.Thread(target=self.run_timer, args=(total_seconds,))
        self.timer_thread.start()

    def run_timer(self, total_seconds):
        
        while total_seconds > 0:
            minutes, seconds = divmod(total_seconds, 60)
            self.time_label.config(text=f"{minutes:02d}:{seconds:02d}")
            self.root.update()
            time.sleep(1)
            total_seconds -= 1

        
        messagebox.showinfo("Таймер завершен", "Время закончено.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()