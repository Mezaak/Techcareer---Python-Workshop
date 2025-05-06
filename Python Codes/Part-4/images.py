import cv2 
image = cv2.imread("pppic.jpg")

if image is None:
    print("hata: görüntü dosyası bulunamadı")
    exit()
cv2.imshow("orjinal görüntü",image) # görüntüyü açıyo
cv2.waitKey(0)
cv2.destroyAllWindows()

#boyutlandırma

h,w,c = image.shape

print(f"görüntü boyutları: {w}x{h} piksel {c} kanal sayısı")

image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imwrite("gray_logo.jpg",image_gray)