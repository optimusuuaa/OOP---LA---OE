import tkinter as tk

your_name = "CHRISTINE_OWAPIN"
section = "BSIT-2B"

root = tk.Tk()
root.title("OOP LA28 ")
root.geometry("500x500")
root.configure(bg="white")

label = tk.Label(text=f"OOP LA29 {your_name} {section}")
label.grid(row=0, column=0, padx=150, pady=100)

root.mainloop() 