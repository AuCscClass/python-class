import pyautogui
import pytesseract
from PIL import Image, ImageDraw, ImageTk
from tkinter import filedialog, messagebox, Tk, Button, Label, Text, Scrollbar, RIGHT, END, Y

# Function to manually select an area of the screen to capture with a red rectangle
def capture_area():
    root.withdraw()  # Hide the Tkinter root window
    messagebox.showinfo("Capture Area", "Please select the top-left corner of the area to capture by clicking...")
    x1, y1 = pyautogui.position()
    messagebox.showinfo("Capture Area", "Please select the bottom-right corner of the area to capture by clicking...")
    x2, y2 = pyautogui.position()
    root.deiconify()  # Show the Tkinter root window again

    region = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))
    draw = ImageDraw.Draw(region)
    draw.rectangle((0, 0, region.width, region.height), outline="red", width=5)
    region.show()
    return region

# Function to perform OCR (Optical Character Recognition) on the captured image
def perform_ocr(image):
    text = pytesseract.image_to_string(image)
    return text

# Function to handle the "Capture" button click event
def capture_button_clicked():
    region = capture_area()
    extracted_text = perform_ocr(region)
    output_text.delete(1.0, END)
    output_text.insert(END, extracted_text)

# Function to handle the "Open File" button click event
def open_file_button_clicked():
    file_path = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image Files", ".png;.jpg;.jpeg;.bmp")])
    if file_path:
        captured_image = Image.open(file_path)
        extracted_text = perform_ocr(captured_image)
        output_text.delete(1.0, END)
        output_text.insert(END, extracted_text)

# Create Tkinter root window
root = Tk()
root.title("OCR Application")

# Set the background image
bg_image = Image.open("capture_bg.jpg")  # Path to the background image
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# Create labels
label1 = Label(root, text="Text Extractor", font=("Arial", 24, "bold"), fg="black",bg="beige")
label1.pack(pady=10)

# Create buttons
capture_button = Button(root, text="Capture", command=capture_button_clicked, bg="purple", fg="white", font=("Comic Sans MS", 16, "bold"))
capture_button.pack(pady=10)

open_file_button = Button(root, text="Open File", command=open_file_button_clicked, bg="purple", fg="white", font=("Comic Sans MS", 16, "bold"))
open_file_button.pack(pady=5)

# Create output text box with scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

output_text = Text(root, wrap="word", yscrollcommand=scrollbar.set, font=("Arial", 12))
output_text.pack()

scrollbar.config(command=output_text.yview)

# Set Tesseract OCR executable path (update with your installation path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Start the Tkinter event loop
root.mainloop()
