import cv2
import numpy as np
from pyzbar.pyzbar import decode


def dekoder(image):
    # Menggunakan format BGR
    trans_img = cv2.cvtColor(image, 0)
    BarCode = decode(trans_img)

    for obj in BarCode:
        points = obj.polygon
        (x,y,w,h) = obj.rect
        pts = np.array(points, np.int32)
        # ukuran box
        pts = pts.reshape((-1,1,2))
        thickness = 2
        isClosed = True
        # berikan warna
        line_color = (0,0,255)
        cv2.polylines(image, [pts], isClosed, line_color, thickness)

        # baca qrcode (deteksi dan dekodekan qr code)
        BarCodeData = obj.data.decode("utf-8")
        BarCodeType = obj.type
        the_text = "Data: "+ str(BarCodeData)

        org = (x,y)
        txt_color = (0, 255, 0)
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        cv2.putText(image, the_text, org, font, 0.9, txt_color, 2)
        # cetak data
        print("Datanya adalah : "+ BarCodeData + " & Tipe Datanya : " + BarCodeType)

if __name__ == "__main__":
    video = cv2.VideoCapture(0)
    while True:
        ret, frame = video.read()
        dekoder(frame)
        cv2.imshow('Image', frame)
        code = cv2.waitKey(1)
        if code == ord('q'):
            break

    cv2.destroyAllWindows()
