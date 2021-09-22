import cv2
import numpy as np
import time
SSIZE =0
STIME = time.time()
startCount =0



def getVid():
    global image
    print('Enter the source of the Video Stream. Enter 0 to use the camera of this computer: ')
    m = input()
    if m =='0':
        m = 0
    cap = cv2.VideoCapture(m)
    while True:
        _,image = cap.read()
        frm, img2 = findsmoke(image)
        cv2.imshow('Original Scene', img2)
        cv2.imshow('Detection Scene', frm)
        #findCard(image)
        #cv2.imshow('Test', image)
        if cv2.waitKey(2) == 27:
            break

def findsmoke(img):
    global STIME, startCount, SSIZE
    img2 = img.copy()
    blur = cv2.GaussianBlur(img2,(15,15),0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    low_v = np.array([0,0,0], dtype='uint8')
    high_v = np.array([0,0,255], dtype='uint8')

    smoke_mask = cv2.inRange(hsv,low_v, high_v)
    size= cv2.countNonZero(smoke_mask)
    output = cv2.bitwise_and(img2, hsv, mask=smoke_mask)
    print (size)
    output = cv2.resize(output,(0,0), fx=0.25, fy=0.25)
    h = output.shape[0]
    w = output.shape[1]
    tnow = time.time()

    
    if startCount < 30:
        #temp.append(size)
        output = cv2.putText(output,'Studying Intensity ' + str(30 - startCount) , (0, h//2),cv2.FONT_HERSHEY_SIMPLEX,0.6, (255,255,255),3)
        if  tnow - STIME >= 1.0:
            startCount +=1
            print ('Intensity =', size, 'Time study (Seconds) =', startCount )
            STIME = tnow
            #take the highest value of the intensity at the surrounding
            # Uncomment the if statement when working in a dark environment
            #if size > SSIZE:
            SSIZE = size    
            
           
    else:
        if (size > SSIZE + 1000):
            print('Fire detected')
            output = cv2.putText(output,'Fire Detected', (w//2 -10, h//2),cv2.FONT_HERSHEY_SIMPLEX,0.6, (255,255,255),3)
            h1= img.shape[0]
            w1=img.shape[1]
            img = cv2.putText(img,'Fire Detected', (w1//2 - 20, h1//2),cv2.FONT_HERSHEY_SIMPLEX,0.6, (255,255,255),3)
            

    
    return output, img

if __name__ == "__main__":
    getVid()

