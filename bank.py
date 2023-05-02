from tkinter import *
from tkinter import messagebox

# Create the main window
screen = Tk()
screen.geometry("350x250")
screen.title("WEB blocker")
screen.configure(bg="black")
screen.resizable(False, False)

# Create a label and a text field for the website
Label(screen, text="WEBSITE BLOCKER", bg="blue").place(x=150, y=10)
Label(screen, text="Enter website to block:").place(x=20, y=50)
webs = Text(screen, width=20, height=1)
webs.place(x=150, y=50)

# Define the file path and IP address for blocking/unblocking
file_host_path = "C:\Windows\System32\drivers\etc\hosts"
ip_address = "127.0.0.1"

# Define the function to block websites
def block():
    websites = webs.get(1.0, END)
    Webs = list(websites.split(","))
    with open(file_host_path, 'r+') as main_file:
        file_content = main_file.read()
        for web in Webs:
            if web in file_content:
                messagebox.showerror("", "Website already blocked")
            else:
                main_file.write(ip_address + " " + web + '\n')
                messagebox.showinfo("", "Website blocked")

# Define the function to unblock websites
def Unblock():
    websites = webs.get(1.0, END)
    Webs = list(websites.split(","))
    with open(file_host_path, 'r+') as host_file:
        file_content = host_file.readlines()
        host_file.seek(0)
        for line in file_content:
            if not any(web in line for web in Webs):
                host_file.write(line)
        host_file.truncate()
    messagebox.showinfo("", "Websites unblocked")

# Create the block and unblock buttons
button = Button(screen, text="BLOCK", fg="black", command=block, bg="#990000")
button2 = Button(screen, text="UNBLOCK", fg="black", command=Unblock, bg="#990000")
button.place(x=130, y=100)
button2.place(x=190, y=100)
# Run the main event loop
screen.mainloop()