import cv2
import os

# Read the image using the full file path
img = cv2.imread(r"C:\Users\dell\Downloads\sam-moghadam-cU5TUyEaZXQ-unsplash.jpg")

# Take user inputs
msg = input("Enter secret message:")
password = input("Enter a passcode:")

# Create dictionaries for encryption and decryption
d = {chr(i): i for i in range(256)}
c = {i: chr(i) for i in range(256)}

# Encryption process
rows, cols, _ = img.shape
if len(msg) > rows * cols:
    print("Message is too long for the given image.")
else:
    for i, char in enumerate(msg):
        row = i // cols
        col = i % cols
        img[row, col, 0] = d[char]

    # Save the encoded image
    cv2.imwrite("encryptedImage.jpg", img)
    os.system("start encryptedImage.jpg")  # Use 'start' to open the image on Windows

# Decryption process
message = ""
pas = input("Enter passcode for Decryption:")
if password == pas:
    for i in range(len(msg)):
        row = i // cols
        col = i % cols
        message += c[img[row, col, 0]]
    print("Decrypted message:", message)
else:
    print("YOU ARE NOT auth")
