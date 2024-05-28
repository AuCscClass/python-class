import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfMerger
import os


def select_pdf_files():
    file_paths = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    if file_paths:
        for file_path in file_paths:
            pdf_merger.append(file_path)
        selected_files_label.config(text=f"Selected files: {', '.join(file_paths)}")
        #This lines of codes (line 9 to line 14) allows the program acess to the file explorer and allows you to select certain PDF'S you wish to work with

def merge_pdfs():
    # Specify the output directory (change this to your preferred directory)
    output_directory = "/Users/Oyele/OneDrive/Documents/" #You have to change the directoty on your device user
    output_filename = os.path.join(output_directory, "Merged.pdf")
    pdf_merger.write(output_filename)
    pdf_merger.close()
    result_label.config(text=f"PDFs merged successfully! Saved as {output_filename}")
    open_button.config(state=tk.NORMAL)  # Enable the "Open Merged PDF" button
    #This lines of code (line 17 to line 24 ) allows you to merge the selected pdfs together

def open_merged_pdf():
    output_filename = "Merged.pdf"
    if os.path.exists(output_filename):
        os.system(f"start {output_filename}")  # Open the merged PDF file
    else:
        result_label.config(text="Merged PDF file not found!")
#This lines of code (Line 27 to line 32) allows you to open the merged PDF'S
# Initialize the main window
root = tk.Tk()
root.title("PDF Merger")
root.configure(bg="white")  
# Set background color to black

# Create a PdfMerger instance
pdf_merger = PdfMerger()

# Add widgets
select_button = tk.Button(root, text="Select PDF Files", command=select_pdf_files, bg="blue", fg="white")
select_button.pack(pady=10)

selected_files_label = tk.Label(root, text="", bg="blue", fg="white")
selected_files_label.pack()

merge_button = tk.Button(root, text="Merge PDFs", command=merge_pdfs, bg="blue", fg="white")
merge_button.pack(pady=10)

result_label = tk.Label(root, text="", bg="blue", fg="white")
result_label.pack()

open_button = tk.Button(root, text="Open Merged PDF", command=open_merged_pdf, state=tk.DISABLED, bg="blue", fg="white")
open_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
