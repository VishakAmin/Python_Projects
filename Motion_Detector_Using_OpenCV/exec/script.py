import cv2
import glob

img = glob.glob("*.jpg")

for image in img:
    im = cv2.imread(image,1)
    re = cv2.resize(im,(100,100))
    cv2.imshow("Hey",re)    
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image,re)
