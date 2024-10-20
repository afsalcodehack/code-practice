from PIL import Image

def encode_steganographic_info(image, info):
    """
    Modify pixel values in the image to encode the user information.
    The least significant bit (LSB) of the red color channel is modified to store binary data.
    """
    # Convert image to RGB if it's not already in that format
    if image.mode != 'RGB':
        image = image.convert('RGB')

    pixels = image.load()  # Access pixels of the image

    # Convert the user info (string) to binary format and add a terminator
    info_bin = ''.join(format(ord(char), '08b') for char in info) + '11111111'
    info_index = 0  # Keep track of where we are in the binary info string

    for i in range(image.size[0]):  # Loop through the width of the image
        for j in range(image.size[1]):  # Loop through the height of the image
            if info_index < len(info_bin):  # Ensure we still have binary data to encode
                r, g, b = pixels[i, j][:3]  # Get current pixel values (only RGB)
                r = (r & ~1) | int(info_bin[info_index])  # Change LSB of red channel to match the binary info
                info_index += 1  # Move to the next bit of the binary info

                # Update the pixel with modified red value
                pixels[i, j] = (r, g, b)

    return image  # Return the modified image with steganographic encoding

def extract_lsb_data(image):
    """
    Extract binary data from the LSB of the red channel for each pixel.
    """
    # Convert image to RGB if it's not already in that format
    if image.mode != 'RGB':
        image = image.convert('RGB')

    pixels = image.load()  # Access pixels of the image
    binary_data = ""       # String to store the binary data

    for i in range(image.size[0]):  # Loop through the width of the image
        for j in range(image.size[1]):  # Loop through the height of the image
            r, g, b = pixels[i, j][:3]  # Get the current pixel's RGB values
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
            if char_code == 255:  # Check for the terminator
                break
            if char_code != 0:  # Skip null characters
                decoded_text += chr(char_code)

    return decoded_text

# Example usage for encoding:
def main_encode():
    image_path = "local_img.png"  # Path to the image where you want to encode data
    secret_message = "Your secret message"  # The message you want to encode
    image = Image.open(image_path)  # Load the image
    encoded_image = encode_steganographic_info(image, secret_message)  # Encode the message
    encoded_image.save("encoded_image.png")  # Save the modified image

# Example usage for decoding:
def main_decode():
    encoded_image_path = "in5.png"  # Path to the encoded image
    encoded_image = Image.open(encoded_image_path)  # Load the encoded image

    # Extract binary data from the image
    binary_data = extract_lsb_data(encoded_image)

    # Convert binary data to readable text and print
    decoded_text = binary_to_text(binary_data)
    print("Decoded text:", decoded_text)

if __name__ == "__main__":
    #main_encode()  # Uncomment to encode data
    main_decode()  # Uncomment to decode data
