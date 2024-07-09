import qrcode
phone_number = input("Enter your phone number: ")
Image_of_QR_Code = qrcode.make(phone_number)
Image_of_QR_Code.save("Phone_number.jpg")