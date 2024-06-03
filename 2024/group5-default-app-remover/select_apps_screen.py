import tkinter as tk
from tkinter import ttk
import get_windows_default_apps
import subprocess


# Function to uninstall selected default apps
def uninstall_app(app_vars, progress_label, root):
    total_apps = len(app_vars)
    completed_apps = 0
    for app_name in app_vars:
        # Construct PowerShell command to uninstall the app
        command = [
            'powershell',
            '-Command',
            f'Get-AppxPackage -Name "{app_name}" | Remove-AppxPackage'
        ]
        # Execute the PowerShell command
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # Update GUI while the uninstallation process is ongoing
        while process.poll() is None:
            root.update_idletasks()
        completed_apps += 1
        # Update progress label to show the number of apps uninstalled
        progress_label.config(text=f"Progress: {completed_apps}/{total_apps} apps uninstalled", font=("Helvetica", 8))


# Dictionary to store selected apps
selectedApps = {}


# Function to add or remove apps from the selectedApps dictionary
def addToSelectedApps(app_name, app_var):
    if app_name not in selectedApps:
        selectedApps[app_name] = app_var
    else:
        del selectedApps[app_name]


# Function to display the screen for selecting default apps to uninstall
def displaySelectAppsScreen():
    root = tk.Tk()
    root.title("Default App Remover - Delete Apps")
    root.geometry("400x700")
    root.resizable(False, False)

    # Label to instruct the user to select apps for deletion
    label = tk.Label(
        root, text="Select the apps you want to delete",
        font=("Helvetica", 15)
    )
    label.pack()

    # Label to display progress of app uninstallation
    progress_label = tk.Label(root, text="", font=("Helvetica", 12))
    progress_label.pack()

    # Button to initiate uninstallation of selected apps
    delete_button = ttk.Button(root, text="Delete Selected Apps",
                               command=lambda: uninstall_app(selectedApps, progress_label, root))
    delete_button.pack(pady=20)

    # Retrieve default apps
    default_apps = get_windows_default_apps.get_default_apps()

    # Create canvas for displaying app list with scrollbar
    canvas = tk.Canvas(root)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)

    frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=frame)

    # Populate frame with checkboxes for each default app
    for app_name in default_apps:
        app_var = tk.IntVar()
        checkbox = ttk.Checkbutton(
            frame,
            text=app_name.removeprefix("Microsoft."), variable=app_var,
            command=lambda an=app_name, av=app_var: addToSelectedApps(an, av)
        )
        checkbox.pack(anchor='w', padx=10, pady=5)

    frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))

    root.mainloop()
