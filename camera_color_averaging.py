import numpy as np
import cv2

FILENAME = 'colorful.png'
BOX_SIZE = 25

cap = cv2.VideoCapture(0)

while True:
    ret, bgr = cap.read()
    #bgr = cv2.imread(FILENAME,cv2.IMREAD_COLOR)
    hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
    bgr_median = np.zeros_like(bgr)
    hsv_median = np.zeros_like(hsv)
    
    rows, cols, colors = hsv.shape

    row0 = 0
    row1 = BOX_SIZE
    while True:
    
        col0 = 0
        col1 = BOX_SIZE
        while True:
            bgr_box = bgr[row0:row1, col0:col1, :]
            hsv_box = hsv[row0:row1, col0:col1, :]
            for iColor in range(colors):
                bgr_median[row0:row1, col0:col1, iColor] = np.median(bgr_box[:,:,iColor])
                hsv_median[row0:row1, col0:col1, iColor] = np.median(hsv_box[:,:,iColor])
            col0 += BOX_SIZE
            col1 += BOX_SIZE
            if col1 > cols:
                break
            
        row0 += BOX_SIZE
        row1 += BOX_SIZE
        if row1 > rows:
            break
        
    if True:
        cv2.imshow("bgr", bgr)
        cv2.imshow("hsv_median", cv2.cvtColor(hsv_median, cv2.COLOR_HSV2BGR))
        cv2.imshow("bgr_median", bgr_median)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
