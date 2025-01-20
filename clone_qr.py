import qrcode

# Replace with the URL of your hosted HTML file
url = "http://yourdomain.com/images.html"  # e.g., https://username.github.io/repo-name/images.html

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image
img.save("qr_code_to_images.png")