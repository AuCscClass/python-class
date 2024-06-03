Certainly! Here's the updated documentation with explanations for each function in the application:

---

# Default App Remover Application Documentation

## Introduction
The Default App Remover is a Python application designed to assist users in removing default applications from their Windows systems. It provides a graphical user interface (GUI) for users to interact with, allowing them to select and uninstall default apps conveniently.

## Features
- Graphical user interface for ease of use.
- Ability to select multiple default apps for removal.
- Progress tracking during the uninstallation process.
- Integration with PowerShell commands for system interaction.

## Dependencies
- Python 3.x
- `tkinter` library for GUI development.
- `subprocess` module for executing PowerShell commands.
- `ctypes` module for administrative privileges check.

## Components
### 1. `HomePage` Class
- **Explanation**: Initializes the main window of the application and provides functionality for user interaction.
  
- **Functions**:
    - `__init__()`: Initializes the main window and sets up the layout and components.
    - `openSelectAppsScreen()`: Opens the screen for selecting default apps.
    - `showSelectAppsScreen()`: Displays the screen for selecting default apps after loading.
    - `exitApplication()`: Closes the application when the user chooses to exit.

### 2. `displaySelectAppsScreen()` Function
- **Explanation**: Displays the screen for selecting default apps to remove and manages the uninstallation process.
  
- **Functions**:
    - `uninstall_app(app_vars, progress_label, root)`: Uninstalls selected default apps using PowerShell commands and updates the progress label.
    - `addToSelectedApps(app_name, app_var)`: Manages the selection state of default apps.
  
### 3. `get_default_apps()` Function
- **Explanation**: Retrieves a list of default apps installed on the system using PowerShell commands.
  
- **Functionality**:
    - Executes PowerShell commands to query information about default apps.
    - Processes the output to extract the names of default apps.
  
## Usage
1. Launch the Default App Remover application.
2. Navigate through the GUI to select default apps for removal.
3. Click the "Delete Selected Apps" button to initiate the uninstallation process.
4. Monitor the progress of app removal through the provided progress indicator.

## Error Handling
- Errors during the execution of PowerShell commands are gracefully handled, ensuring smooth operation of the application.
- Administrative privileges are checked to ensure the application has the required permissions for system interaction.

## Integration
- The application integrates seamlessly with PowerShell commands to provide users with a comprehensive solution for managing default apps on their Windows systems.

## Conclusion
The Default App Remover application streamlines the process of removing default applications from Windows systems. Its user-friendly interface, coupled with powerful system interaction capabilities, makes it a valuable tool for users seeking to customize their system configurations.

For further information or support, refer to the code documentation or contact the developer.

---

This documentation provides an overview of the Default App Remover application, including explanations for each function in the application. It serves as a comprehensive guide for understanding and utilizing the application effectively. Feel free to distribute it to your team for reference!