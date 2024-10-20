import tkinter as tk
from PIL import Image, ImageDraw, ImageFont, ImageTk


def create_watermark_overlay(watermark_text):
    """ Create a full-screen transparent overlay with a watermark that allows interaction with other windows. """
    root = tk.Tk()

    # Make the window full-screen
    root.attributes('-fullscreen', True)  # Set full screen
    root.overrideredirect(True)  # Remove window decorations (borderless)
    root.attributes('-topmost', True)  # Keep window always on top
    root.attributes('-alpha', 0.5)  # Set transparency (50% visible)

    # Create a canvas to display the watermark
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    canvas = tk.Canvas(root, width=screen_width, height=screen_height, highlightthickness=0)
    canvas.pack()

    # Create a blank transparent image for the watermark
    watermark_image = Image.new('RGBA', (screen_width, screen_height), (255, 255, 255, 0))  # Transparent background

    # Create a drawing context
    draw = ImageDraw.Draw(watermark_image)

    # Load a font (you may need to adjust the font path)
    try:
        font = ImageFont.truetype("arial.ttf", 100)  # Use a TTF font
    except IOError:
        font = ImageFont.load_default()

    # Get the bounding box for the text
    bbox = draw.textbbox((0, 0), watermark_text, font=font)
    text_width = bbox[2] - bbox[0]  # Width of the text
    text_height = bbox[3] - bbox[1]  # Height of the text

    # Position for the watermark
    position = (screen_width // 2 - text_width // 2, screen_height // 2 - text_height // 2)  # Center the text

    # Draw the watermark text with increased visibility
    draw.text(position, watermark_text, fill=(255, 255, 255, 120), font=font)  # More visible white text

    # Convert the watermark image to a format that Tkinter can display
    tk_image = ImageTk.PhotoImage(watermark_image)
    canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)

    # Allow interaction with applications beneath this overlay
    root.wm_attributes("-transparentcolor", "white")  # Set the background color to transparent

    # Keep the overlay running continuously
    root.mainloop()


if __name__ == "__main__":
    watermark_text = "Your Watermark"  # Customize your watermark text here
    create_watermark_overlay(watermark_text)
