import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from PIL import ImageTk, Image
from signature import match

# Match Threshold
THRESHOLD = 85

# Define color constants
BG_COLOR = "#F8F8F8"
BUTTON_COLOR = "#4CAF50"
BUTTON_TEXT_COLOR = "white"

def browse_file(entry):
    filename = askopenfilename(filetypes=(
        ("Image Files", "*.jpeg;*.jpg;*.png"),
        ("All Files", "*.*")
    ))
    entry.delete(0, tk.END)
    entry.insert(tk.END, filename)

def check_similarity(image1_path, image2_path):
    result = match(path1=image1_path, path2=image2_path)
    if result <= THRESHOLD:
        messagebox.showerror("Failure: Signatures Do Not Match", f"Signatures are {result}% similar!!")
    else:
        messagebox.showinfo("Success: Signatures Match", f"Signatures are {result}% similar!!")

root = tk.Tk()
root.title("Signature Verification")
root.geometry("700x400")
root.configure(bg=BG_COLOR)

frame1 = tk.Frame(root, bg=BG_COLOR)
frame1.pack(side=tk.LEFT, padx=10, pady=10)

label1 = tk.Label(frame1, text="Signature 1", bg=BG_COLOR)
label1.pack()

entry1 = tk.Entry(frame1, width=50)
entry1.pack(pady=5)

browse_button1 = tk.Button(frame1, text="Browse", command=lambda: browse_file(entry1), bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR)
browse_button1.pack(pady=5)

frame2 = tk.Frame(root, bg=BG_COLOR)
frame2.pack(side=tk.LEFT, padx=10, pady=10)

label2 = tk.Label(frame2, text="Signature 2", bg=BG_COLOR)
label2.pack()

entry2 = tk.Entry(frame2, width=50)
entry2.pack(pady=5)

browse_button2 = tk.Button(frame2, text="Browse", command=lambda: browse_file(entry2), bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR)
browse_button2.pack(pady=5)

compare_button = tk.Button(root, text="Compare", font=("Arial", 16, "bold"),
                           command=lambda: check_similarity(entry1.get(), entry2.get()),
                           bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR)
compare_button.pack(pady=10)

root.mainloop()
