
import tkinter as tk
from tkinter import ttk
import agreement_license
from select_apps_screen import displaySelectAppsScreen


class HomePage:
    def __init__(self):
        # Function to open the screen for selecting default apps
        def openSelectAppsScreen():
            # Show loading text
            loading_label.pack()
            # Update the root and add the loading_label component, until all our idle tasks have been completed
            root.update_idletasks()
            # Simulate delay (replace with actual retrieval logic)
            root.after(2000, lambda: showSelectAppsScreen())

        # Function to display the screen for selecting default apps
        def showSelectAppsScreen():
            # Hide loading spinner
            loading_label.pack_forget()
            # Open selected apps screen
            displaySelectAppsScreen()

        # Function to exit the application
        def exitApplication():
            # Close all open windows
            root.quit()

        # Create the main application window
        root = tk.Tk()
        root.title("Windows Default App Remover")
        root.resizable(width=False, height=False)

        # Center the window on the screen
        window_width = 500  # this is our own app width
        window_height = 500  # this is our own app height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        x = (screen_width - window_width) // 2  # This is to place the app screen at the center horizontally when opened
        y = (screen_height - window_height) // 2  # This is to place the app screen at the center Vertically, which
        # overall centers the app
        root.geometry(f"{window_width}x{window_height}+{x}+{y}")  # this is used to then set the position of the app
        # screen

        # Create a frame for the application
        app_frame = ttk.Frame(root)
        app_frame.pack(expand=True)

        # Display application logo
        app_logo = ttk.Label(app_frame, text='W-DAR', font=('Helvetica', 30))
        app_logo.pack()

        # Display application name
        app_name_label = ttk.Label(app_frame, text='Default App Remover', font=('Helvetica', 15))
        app_name_label.pack(pady=(5, 20))

        developed_by_label = ttk.Label(app_frame, text='Developed by GRP-5', font=('Helvetica', 10))
        developed_by_label.pack(pady=(5, 20))

        # Display license agreement
        read_license = ttk.Label(app_frame, justify='left', text=agreement_license.get_agreement_license(),
                                 font=('Helvetica', 10,), wraplength=400)
        read_license.pack()

        # Create loading label
        loading_label = ttk.Label(app_frame, text='Loading...windows apps...please wait..', font=('Helvetica', 12))

        # Create frame for buttons
        button_frame = ttk.Frame(app_frame)
        button_frame.pack(pady=(20, 10))

        # Create exit button
        exit_button = ttk.Button(button_frame, text='I don\'t Agree', command=lambda: exitApplication(), padding=20)
        exit_button.pack(side=tk.LEFT, padx=5)

        # Create proceed button
        proceed_button = ttk.Button(
            button_frame, text='I Agree',
            style='Custom.TButton',
            command=lambda: openSelectAppsScreen(),
            padding=20
        )
        proceed_button.pack(side=tk.RIGHT, padx=5)

        # Run the application
        root.mainloop()
