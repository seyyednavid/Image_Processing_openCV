import cv2 as cv
import qrcode 


qrcode_img = cv.imread("./img/qrcode2.png")

# Detect QR code
detector = cv.QRCodeDetector()
value, box, _ = detector.detectAndDecode(qrcode_img)
box = box.astype(int)
cv.rectangle(qrcode_img, (box[0][0][0], box[0][0][1]),(box[0][2][0], box[0][2][1]), (255,255,0), 2)


# Generate QR code
# generated_qr_code = qrcode.make("Learn Python")
# generated_qr_code.save("./img/qrcode2.png")


cv.imshow("qrcode_img", qrcode_img)
cv.waitKey(0)
cv.destroyAllWindows()