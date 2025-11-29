import cv2
import os
# 取得目前程式檔案所在的目錄路徑
dir_path = os.path.dirname(os.path.realpath(__file__))
# 組合出圖片的完整路徑
img_path = os.path.join(dir_path, 'family.jpg')

img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
cv2.imwrite('family_gray.jpg',img, [cv2.IMWRITE_JPEG_QUALITY, 20])
cv2.imwrite('family_gray2.jpg',img)
cv2.imshow('oxxo',img)  
cv2.waitKey(0)
cv2.destroyAllWindows()