import qrcode
data = "http://j-coders.com"
qr = qrcode.QRCode(
    version = 2,
    box_size = 10,
    border = 2
)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", black_color="white")
img.save("qrcode.jpg")

 





