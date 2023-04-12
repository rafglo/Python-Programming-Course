import qrcode, os, cv2

def qr_generator(message, out_path, name):
    img = qrcode.make(message)
    qr_name = name + ".png"
    qr_path = os.path.join(out_path, qr_name)
    img.save(qr_path)

qr_generator("cos", r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\lista 3", "kot")

def qr_decode(qr_path, )
