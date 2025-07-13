import os
import shutil
from tkinter import Tk
from tkinter.filedialog import askdirectory

# Function to select a directory using Tkinter
def select_directory():
    root = Tk()
    root.withdraw()
    selected_dir = askdirectory(title="Select the folder containing your files")
    root.destroy()
    return selected_dir

# Ask the user to select a directory
folder_path = select_directory()
if not folder_path:
    print("No directory was selected. Exiting.")
    exit()

process_folder = os.path.join(folder_path, "process")

# Create the 'process' folder if it doesn't exist
os.makedirs(process_folder, exist_ok=True)

# List all files in the selected folder
files = os.listdir(folder_path)

# Get the names of jpg files without the extension
jpg_files = {os.path.splitext(f)[0] for f in files if f.lower().endswith(".jpg")}

# For each CR3 file, check if a JPG with the same name exists
for f in files:
    if f.lower().endswith(".cr3"):
        name_without_ext = os.path.splitext(f)[0]
        if name_without_ext in jpg_files:
            # Move the CR3 file to the 'process' folder
            src = os.path.join(folder_path, f)
            dst = os.path.join(process_folder, f)
            shutil.move(src, dst)
            print(f"Moved: {f}")

print("Done.")
