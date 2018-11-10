import cv2
import numpy
face_cascade=cv2.CascadeClassifier(r'C:\Users\Admin\Desktop\image processing\face_detection\haarcascade_frontalface_default.xml')
img=cv2.imread(r"C:\Users\Admin\Desktop\image processing\Image size converter\size0L6A0730.JPG")
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


faces=face_cascade.detectMultiScale\
    (gray_img,
     scaleFactor=1.25,
     minNeighbors=5)
print(faces)
count=1
for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,226,0),1)
    crop_img = img[y:y + h, x:x + w]
    print(crop_img)
    cv2.imshow('single_faces',crop_img)
    cv2.waitKey(2000)
    cv2.imwrite(str(count)+'faces cropped.jpg',crop_img)
    count+=1
cv2.imshow('faces',img)
cv2.waitKey(0)
cv2.destroyAllWindows()