# Importing library
import qrcode

# Data to be encoded
data = input("Enter Url for QR-CODE! ")

qr = qrcode.QRCode(version=1,
                   box_size=10,
                   border=5)

qr.add_data(data) 
qr.make( fit=True )

# Encoding data using make() function
img = qr.make_image(filcolor = "green",
                    Backcolor = "White")

# Saving as an image file
img.save('MyQRCode.png')

