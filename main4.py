import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from PIL import ImageTk, Image
from signature import match

# Match Threshold
THRESHOLD = 80

# Define color constants
BUTTON_COLOR = "#4CAF50"
BUTTON_TEXT_COLOR = "white"
LABEL_TEXT_COLOR = "#333333"
LABEL_FONT = ("Arial", 12, "bold")

def browse_file(entry):
    filename = askopenfilename(filetypes=(
        ("Image Files", "*.jpeg;*.jpg;*.png"),
        ("All Files", "*.*")
    ))
    entry.delete(0, tk.END)
    entry.insert(tk.END, filename)

def check_similarity(window, image1_path, image2_path):
    result = match(path1=image1_path, path2=image2_path)
    if result <= THRESHOLD:
        messagebox.showerror("Failure: Signatures Do Not Match", f"Signatures are {result}% similar!!")
    else:
        messagebox.showinfo("Success: Signatures Match", f"Signatures are {result}% similar!!")

def exit_program():
    root.destroy()

root = tk.Tk()
root.title("Signature Verification")
root.geometry(f"{1250}x{600}+{10}+{10}")

# Load and set the background image
background_image = ImageTk.PhotoImage(Image.open("Images/img7.jpg"))
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame1 = tk.Frame(root, bg="white")
frame1.pack(side=tk.LEFT, padx=10, pady=10)

label1 = tk.Label(frame1, text="Signature 1", bg="pink", fg=LABEL_TEXT_COLOR, font=LABEL_FONT)
label1.pack()

entry1 = tk.Entry(frame1, width=50)
entry1.pack(pady=5)

browse_button1 = tk.Button(frame1, text="Browse", bd='7',
                           activebackground="blue", font=("Classy Button", 14), cursor="hand2",
                           borderwidth=1, relief="solid", command=lambda: browse_file(entry1),
                           bg="green", fg="white")
browse_button1.pack(pady=5)

frame2 = tk.Frame(root, bg="white")
frame2.pack(side=tk.LEFT, padx=10, pady=10)

label2 = tk.Label(frame2, text="Signature 2", bg="pink", fg=LABEL_TEXT_COLOR, font=LABEL_FONT)
label2.pack()

entry2 = tk.Entry(frame2, width=50)
entry2.pack(pady=5)

browse_button2 = tk.Button(frame2, text="Browse", bd='7',
                           activebackground="blue", font=("Classy Button", 14), cursor="hand2",
                           borderwidth=1, relief="solid", command=lambda: browse_file(entry2),
                           bg="green", fg="white")
browse_button2.pack(pady=5)

compare_button = tk.Button(root, text="Compare", font=("Arial", 16, "bold"), bd='7',
                           activebackground="blue",
                           command=lambda: check_similarity(window=root,
                                                           image1_path=entry1.get(),
                                                           image2_path=entry2.get()),
                           bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR)
compare_button.place(x=840, y=525)

image_frame1 = tk.Frame(root, width=300, height=300, bd=1, relief=tk.SOLID, bg="white")
image_frame1.pack(side=tk.LEFT, padx=10, pady=10)

image_frame2 = tk.Frame(root, width=300, height=300, bd=1, relief=tk.SOLID, bg="white")
image_frame2.pack(side=tk.LEFT, padx=10, pady=10)

def display_image(image_path, image_frame):
    image = Image.open(image_path)
    image = image.resize((250, 250))
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(image_frame, image=photo, bg="white")
    label.image = photo
    label.pack(padx=10, pady=10)


def update_images():
    image_path1 = entry1.get()
    image_path2 = entry2.get()
    for widget in image_frame1.winfo_children():
        widget.destroy()
    for widget in image_frame2.winfo_children():
        widget.destroy()

    if image_path1:
        display_image(image_path1, image_frame1)
    if image_path2:
        display_image(image_path2, image_frame2)

    root.after(500, update_images)

exit_button = tk.Button(root, text="Exit", font=("Arial", 16, "bold"), bd='7',
                        activebackground="red", command=exit_program,
                        bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR)
exit_button.place(x=1040, y=525)

root.after(500, update_images)
root.mainloop()
