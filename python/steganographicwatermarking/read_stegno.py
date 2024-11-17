from PIL import Image

def extract_lsb_data(image):
    """
    Extract binary data from the LSB of the red channel for each pixel.
    """
    pixels = image.load()  # Access pixels of the image
    binary_data = ""       # String to store the binary data

    for i in range(image.size[0]):  # Loop through the width of the image
        for j in range(image.size[1]):  # Loop through the height of the image
            r, g, b = pixels[i, j]  # Get the current pixel's RGB values
            lsb = r & 1             # Get the LSB of the red channel
            binary_data += str(lsb) # Append the LSB to the binary data string

    return binary_data

def binary_to_text(binary_data):
    """
    Convert binary data to ASCII text.
    """
    # Split the binary string into bytes (8 bits each)
    data_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    decoded_text = ""

    for byte in data_bytes:
        if len(byte) == 8:  # Ensure we're processing complete bytes
            char_code = int(byte, 2)
            if char_code != 0:  # Skip null characters
                decoded_text += chr(char_code)

    return decoded_text

# Example usage:
# Load the image containing hidden data
encoded_image_path = "in4.png"
encoded_image = Image.open(encoded_image_path)

# Extract binary data from the image
binary_data = extract_lsb_data(encoded_image)

# Print the raw binary data for debugging
print("Binary data:", binary_data)

# Convert binary data to readable text and print
decoded_text = binary_to_text(binary_data)
print("Decoded text:", decoded_text)
