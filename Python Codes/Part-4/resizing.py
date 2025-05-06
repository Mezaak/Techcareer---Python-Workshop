import cv2
image = cv2.imread("pppic.jpg")
if image is None:
    print("hata: görüntü dosyası bulunamadı")
    exit()
new_width = 400
new_height = int(image.shape[0] * (new_width / image.shape[1]))  # boyutu koru, 0 genişliği 1 uzunluğu

resized_image = cv2.resize(image,(new_width,new_height))

cv2.imwrite("resized_logo.jpg",resized_image)

h,w,c = image.shape

print(f"görüntü boyutları: {w}x{h} piksel {c} kanal sayısı")

rotated_90 = cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite("rotated_90.jpg",rotated_90)

cropped_image = image[50:250,50:250]

cv2.imshow("rotated_90.jpg",cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()