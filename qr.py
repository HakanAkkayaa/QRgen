import qrcode
import image
qr=qrcode.QRCode(
    version=15, 
    box_size= 10,
    border= 5,
)

data=input("linki giriniz ")
qr.add_data(data)
qr.make(fit=True)
image=qr.make_image(fill="black",back_color="white")
save=input("qr ismini girin ")
image.save(save + ".png")
kapatma=input("programı kapatmak için bir tuşa basın")
