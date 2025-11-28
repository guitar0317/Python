import cv2
import os
# 取得目前程式檔案所在的目錄路徑
dir_path = os.path.dirname(os.path.realpath(__file__))
# 組合出圖片的完整路徑
img_path = os.path.join(dir_path, 'test.JPG')

img = cv2.imread(img_path)
cv2.imshow('oxxo',img)
cv2.waitKey(0)
cv2.destroyAllWindows() 