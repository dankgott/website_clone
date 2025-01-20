import qrcode
from PIL import Image




# rediect to the catlog page
url = "http://127.0.0.1:5500/templates/catlog.html"

# Load the logo image
logo = Image.open('brand.png')
logo = logo.resize((100, 100))



# Generate QR code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill='black', back_color='white').convert('RGBA')

#calculate dimensions for the logo
qr_width, qr_height = img.size
logo_width, logo_height = logo.size
logo_position = ((qr_width - logo_width) // 2, (qr_height - logo_height) // 2)

# Convert the QR code image to RGBA mode
img = img.convert("RGBA")

# Paste the logo on the QR Code
img.paste(logo, logo_position)

# save the qr code with logo
img.save('qr_code_with_logo.png')

# Display the QR code
img.show()


# Save the QR code image
img.save('qr_code.png')
