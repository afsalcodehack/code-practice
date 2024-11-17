import tkinter as tk
import os
from PIL import Image, ImageTk
import ctypes


def get_logged_in_user():
    """Get the currently logged-in user."""
    return os.getlogin() + 'some more text from afsal and epo data sample'


def encode_steganographic_info(image, info):
    """
    Modify pixel values in the image to encode the user information.
    The least significant bit (LSB) of the red color channel is modified to store binary data.
    """
    pixels = image.load()  # Access pixels of the image

    # Convert the user info (string) to binary format
    info_bin = ''.join(format(ord(char), '08b') for char in info) + '11111111'  # Add a terminator
    info_index = 0  # Keep track of where we are in the binary info string

    for i in range(image.size[0]):  # Loop through the width of the image
        for j in range(image.size[1]):  # Loop through the height of the image
            if info_index < len(info_bin):  # Ensure we still have binary data to encode
                r, g, b = pixels[i, j]  # Get current pixel values
                r = (r & ~1) | int(info_bin[info_index])  # Change LSB of red channel to match the binary info
                info_index += 1  # Move to the next bit of the binary info

                # Update the pixel with modified red value
                pixels[i, j] = (r, g, b)

    return image  # Return the modified image with steganographic encoding


def create_overlay():
    """Create a full-screen overlay with steganographic watermark."""
    root = tk.Tk()
    root.attributes("-topmost", True)  # Keeps window always on top
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
    root.overrideredirect(True)  # Removes window decorations (borderless)
    root.attributes("-alpha", 0.10)  # Set transparency (20% visible)

    # Make the window click-through on Windows
    hwnd = ctypes.windll.user32.GetForegroundWindow()
    styles = ctypes.windll.user32.GetWindowLongW(hwnd, -20)
    ctypes.windll.user32.SetWindowLongW(hwnd, -20, styles | 0x80000 | 0x20)

    # Create a canvas to display the steganographically modified image
    canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), highlightthickness=0)
    canvas.pack()

    # Create a blank white image as the base for modification
    screen_image = Image.new('RGB', (root.winfo_screenwidth(), root.winfo_screenheight()), (255, 255, 255))

    # Get logged-in user info
    user_info = get_logged_in_user()

    # Modify the image with steganographic user info
    modified_image = encode_steganographic_info(screen_image, user_info)

    # Convert the modified image into a format that Tkinter can display
    tk_image = ImageTk.PhotoImage(modified_image)
    canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)

    # Keep a reference to the image to prevent garbage collection
    canvas.image = tk_image

    # Keep the overlay running continuously
    root.mainloop()


if __name__ == "__main__":
    create_overlay()
