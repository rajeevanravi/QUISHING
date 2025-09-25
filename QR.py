# Install the library first:
# pip install qrcode[pil]

import qrcode

# Data to encode
data = input("Enter the link to generate QR code: ")

# Generate QR code
qr = qrcode.QRCode(
    version=1,  # controls size (1 = smallest, 40 = largest)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # high error correction
    box_size=10,  # size of each "box"
    border=4,  # border thickness
)

qr.add_data(data)
qr.make(fit=True)

# Create image
img = qr.make_image(fill_color="black", back_color="white")

# Save to file
img.save("qrcode.png")

print("QR code generated and saved as qrcode.png")
