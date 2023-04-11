import matplotlib.pyplot as plt #画像を表示するためのモジュール
import cv2  #OpenCVをインポート
import numpy as np #numpyをインポート
 
img = cv2.imread("20202.jpg") #画像の読み込み
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #色配置の変換 BGR→RGB
 
img_array = np.asarray(img) #numpyで扱える配列をつくる
print(img_array)
 
plt.imshow(img_array)
plt.show()
 
cv2.imwrite("20202_result.jpg", img_array)
print(img_array.shape)