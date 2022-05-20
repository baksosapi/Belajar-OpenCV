my10-Identifikasi kode QR

     Referensi
         https://github.com/NaturalHistoryMuseum/pyzbar
         Gunakan ZBar sebagai OpenCV Recognizer - Barcode + QR Code
         Perbandingan antara zbar dan zxing

     Instalasi
         Instal ZBar
             Ubuntu
                 sudo apt-get install libzbar0
             macOS Mojave or Catalina
                 brew install zbar

Aktifkan Venv

    ahmadyulianto@ahmads-mbp OpenCV-Python-belajar % source venv/bin/activate
    (venv) ahmadyulianto@ahmads-mbp OpenCV-Python-belajar %

Installasi 
    
    pip install opencv-python
    pip install pyzbar

....

    (venv) ahmadyulianto@ahmads-mbp OpenCV-Python-belajar % pip install pyzbar                                                               1 ↵
    Looking in indexes: https://mirrors.aliyun.com/pypi/simple
    Collecting pyzbar
      Downloading https://mirrors.aliyun.com/pypi/packages/6d/24/81ebe6a1c00760471a3028a23cbe0b94e5fa2926e5ba47adc895920887bc/pyzbar-0.1.9-py2.py3-none-any.whl (32 kB)
    Installing collected packages: pyzbar
    Successfully installed pyzbar-0.1.9
    (venv) ahmadyulianto@ahmads-mbp OpenCV-Python-belajar %

Penggunaan
         Penempatan robot Mobil Pintar, Raspberry Pi - Kamera


**Membuat kode QR**

     Referensi
         https://github.com/lincolnloop/python-qrcode
         Gunakan qrcode perpustakaan Python untuk menghasilkan kode QR

     Install
         pip install qrcode[pil]

     membuat

   
    import qrcode
    url='https://www.tokopedia.com/labcom/macbook-pro-13-2020-m1-16gb-512gb-1tb-cto-customise-order-16gb-256gb' 
    img = qrcode.make(url, border=6) 
    img.save('macbookPro.jpg')

    
```bash
    qr 'Some data' > test.png