import tkinter as tk

root = tk.Tk()
root.title("Name")
width = 900
height = 600
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
x = (screenwidth // 2) - (width // 2)
y = (screenheight // 2) - (height // 2)
root.geometry(f"{width}x{height}+{x}+{y}")
root.config(bg="#f9b34f")
root.resizable(False,False)

TitleText = tk.Label(root,text="Login",font=("Helvetica", 45,"bold"), relief = "flat", bg="#f9b34f")
TitleText.place(x = 230,y = 65)
#---------------------------------------------------------------
UserNameText = tk.Label(root, text="User Name:", font=("Helvetica", 30, "bold"), bg="#f9b34f", relief= "flat")
UserNameText.place(x = 65, y= 200)
#---------------------------------------------------------------
PasswordText = tk.Label(root, text="Password:", font=("Helvetica", 30, "bold"),bg="#f9b34f", relief="flat")
PasswordText.place(x=65, y=300)
#---------------------------------------------------------------
InputPasswordText = tk.Entry(root, width=30, font=(60))
#---------------------------------------------------------------
InputPasswordText = tk.Entry(root, width=30, font=(60))
#---------------------------------------------------------------
root.mainloop()