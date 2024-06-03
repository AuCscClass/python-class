# GRP-5 Auto-Fill Software Documentation

## Introduction
The Auto-Fill App is a Python script designed to automate the process of filling in login credentials on websites. This script utilizes the Selenium library to interact with web elements and perform autofill functions.

## How To Use
1. **Download Webdriver**: Ensure you have a compatible webdriver installed, such as Chrome webdriver, Edge webdriver, etc. The script relies on this webdriver to function properly. For this demonstration, the script uses the msedgedriver(Microsoft Edge driver).

2. **Configure Driver Path**: In the `main.py` file, set the `driver_path` variable to the path where you have downloaded the webdriver.

3. **Execute the Script**: Run the `main.py` script to initiate the autofill process.

### To download the dependencies used by this project just use this command `pip install -r requirements.txt`


## Script Overview
The script follows these main steps:
- Import necessary libraries from Selenium.
- Initialize the WebDriver with the specified webdriver executable path.
- Open the login page of the target website.
- Locate the username and password fields on the webpage.
- Fill in the username and password fields with predefined values.
- Submit the form.
- Optionally, wait for a specified duration before closing the browser.


## Code Explanation
- `from selenium import webdriver`: Imports the Selenium webdriver module.
- `from selenium.webdriver.common.keys import Keys`: Imports the Keys module for keyboard interaction.
- `import time`: Imports the time module for adding delays.
- `from selenium.webdriver.edge.service import Service`: Imports the Service class for configuring the Edge webdriver service.
- `driver_path = "The script will get the msedgedriver.exe by it self, because it's inside the project"`: Specifies the path to the msedgedriver executable.
- `driver = webdriver.Edge(service=Service(driver_path))`: Initializes the WebDriver using the Edge webdriver service and the specified driver path.
- `driver.get("the script will get it by it self since the html file is in the script directory")`: Opens the login page of the target website.
- `username_field = driver.find_element(by="id", value="username")`: Finds the username field by its ID.
- `username_field.send_keys("Group 5 Auto Fill")`: Enters the username into the username field.
- `password_field = driver.find_element(by="id", value="password")`: Finds the password field by its ID.
- `password_field.send_keys("123456789.")`: Enters the password into the password field.
- `password_field.send_keys(Keys.RETURN)`: Submits the form by pressing the Enter key.
- `time.sleep(700)`: Delays the script execution for 700 seconds (optional).
- `driver.quit()`: Closes the browser and terminates the WebDriver session.

### There shouldn't be anything wrong with the code, provided you install the dependencies needed for the project to run
## Conclusion
The Auto-Fill App simplifies the process of logging in to websites by automating the entry of login credentials. By following the provided instructions, users can easily configure and utilize the script to enhance their browsing experience.
