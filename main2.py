import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import os
import cv2
from PIL import ImageTk, Image
from signature import match

# Match Threshold
THRESHOLD = 85


def browse_file(entry):
    filename = askopenfilename(filetypes=(
        ("Image Files", "*.jpeg;*.jpg;*.png"),
        ("All Files", "*.*")
    ))
    entry.delete(0, tk.END)
    entry.insert(tk.END, filename)


def capture_image(entry):
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("Capture Image")

    while True:
        ret, frame = cam.read()
        if not ret:
            print("Failed to grab frame")
            break
        cv2.imshow("Capture Image", frame)

        key = cv2.waitKey(1)
        if key % 256 == 27:
            print("Escape hit, closing...")
            break
        elif key % 256 == 32:
            if not os.path.isdir('temp'):
                os.mkdir('temp', mode=0o777)
            filename = "./temp/test_img.png"
            cv2.imwrite(filename, frame)
            print(f"{filename} written!")
            break

    cam.release()
    cv2.destroyAllWindows()
    entry.delete(0, tk.END)
    entry.insert(tk.END, filename)


def check_similarity(window, image1_path, image2_path):
    result = match(path1=image1_path, path2=image2_path)
    if result <= THRESHOLD:
        messagebox.showerror("Failure: Signatures Do Not Match", f"Signatures are {result}% similar!!")
    else:
        messagebox.showinfo("Success: Signatures Match", f"Signatures are {result}% similar!!")


root = tk.Tk()
root.title("Signature Verification")
root.geometry("700x400")

frame1 = tk.Frame(root)
frame1.pack(side=tk.LEFT, padx=10, pady=10)

label1 = tk.Label(frame1, text="Signature 1")
label1.pack()

entry1 = tk.Entry(frame1, width=50)
entry1.pack(pady=5)

browse_button1 = tk.Button(frame1, text="Browse", command=lambda: browse_file(entry1))
browse_button1.pack(pady=5)

capture_button1 = tk.Button(frame1, text="Capture", command=lambda: capture_image(entry1))
capture_button1.pack(pady=5)

frame2 = tk.Frame(root)
frame2.pack(side=tk.LEFT, padx=10, pady=10)

label2 = tk.Label(frame2, text="Signature 2")
label2.pack()

entry2 = tk.Entry(frame2, width=50)
entry2.pack(pady=5)

browse_button2 = tk.Button(frame2, text="Browse", command=lambda: browse_file(entry2))
browse_button2.pack(pady=5)

capture_button2 = tk.Button(frame2, text="Capture", command=lambda: capture_image(entry2))
capture_button2.pack(pady=5)

compare_button = tk.Button(root, text="Compare", font=("Arial", 16, "bold"),
                           command=lambda: check_similarity(window=root,
                                                           image1_path=entry1.get(),
                                                           image2_path=entry2.get()))
compare_button.pack(pady=10)

image_frame1 = tk.Frame(root, width=300, height=300, bd=1, relief=tk.SOLID)
image_frame1.pack(side=tk.LEFT, padx=10, pady=10)

image_frame2 = tk.Frame(root, width=300, height=300, bd=1, relief=tk.SOLID)
image_frame2.pack(side=tk.LEFT, padx=10, pady=10)

def display_image(image_path, image_frame):
    image = Image.open(image_path)
    image = image.resize((250, 250))
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(image_frame, image=photo)
    label.image = photo
    label.pack(padx=10, pady=10)

def update_images():
    image_path1 = entry1.get()
    image_path2 = entry2.get()
    if image_path1:
        display_image(image_path1, image_frame1)
    else:
        for widget in image_frame1.winfo_children():
            widget.destroy()

    if image_path2:
        display_image(image_path2, image_frame2)
    else:
        for widget in image_frame2.winfo_children():
            widget.destroy()

    root.after(500, update_images)

root.after(500, update_images)
root.mainloop()
