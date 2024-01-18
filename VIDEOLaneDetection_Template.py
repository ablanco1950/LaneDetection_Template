
# https://docs.opencv.org/3.4/d4/dc6/tutorial_py_template_matching.html
import cv2 as cv
import numpy as np
#from matplotlib import pyplot as plt
import time
dirVideo="VID_PoorVisiBility.mp4"
MaxAttempts=2
stepIncThreshold=0.08
HitLanes=0
FailureLanes=0
TimeIni=time.time()
# in  14 minutes = 800 seconds finish  
TimeLimit=800



cap = cv.VideoCapture(dirVideo)

# https://levelup.gitconnected.com/opencv-python-reading-and-writing-images-and-videos-ed01669c660c
fourcc = cv.VideoWriter_fourcc(*'MP4V')
fps=5.0
# https://medium.com/@fernando.dijkinga/python-simulating-human-vision-mapping-using-neural-networks-yolov8-80722fd4942f
#out = cv2.VideoWriter('visioneye-pinpoint.avi', cv2.VideoWriter_fourcc(*'MJPG'), fps, (w, h))
#
#

# Videos from camera of a cheap movil
frame_width = 720
frame_height = 1280

cap.set(cv.CAP_PROP_FRAME_WIDTH, frame_width)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, frame_height)
size = (int(cap.get(cv.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
 
video_writer = cv.VideoWriter('demonstration.mp4',fourcc,fps, size) 
ContFrames=0

template = cv.imread('Template1.jpg', cv.IMREAD_GRAYSCALE)
assert template is not None, "file could not be read, check with os.path.exists()"
w, h = template.shape[::-1]

while (cap.isOpened()):
        ret, img_rgb = cap.read()
        
        if ret != True: break
        
        else:
            ContFrames=ContFrames+1
            
            cv.imwrite("pp.jpg", img_rgb)
            #cv.imwrite("pp.jpg",img)
            img_gray = cv.imread('pp.jpg', cv.IMREAD_GRAYSCALE)
            assert img_gray is not None, "file could not be read, check with os.path.exists()"
            
            res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
            
            #threshold = 0.65
            threshold=((255 - np.average(img_gray)) /255) + 0.2
           
            # https://stackoverflow.com/questions/59923076/how-to-automatically-adjust-the-threshold-for-template-matching-with-opencv
            # https://stackoverflow.com/questions/59401389/how-to-isolate-everything-inside-of-a-contour-scale-it-and-test-the-similarity/59402625
            
            cont=0
            contAttempts=0
            while cont==0:
                #print("threshold = " + str(threshold))
                loc = np.where( res >= threshold)
                contAttempts=contAttempts+1
                if contAttempts > MaxAttempts:break
                #if contAttempts > 1:print("TRATA OTRA VEZ")
                threshold=threshold- stepIncThreshold
                for pt in zip(*loc[::-1]):
                     cont=cont+1
                     cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (255,0,0), 2)
            if cont > 0:
                print("Xtarget = " + str(pt[0]) + " Ytarget = " + str(pt[1]))
                HitLanes=HitLanes+1
            else:          
                FailureLanes=FailureLanes+1     
            cv.imshow('Frame', img_rgb)
            # Press Q on keyboard to exit
            if cv.waitKey(25) & 0xFF == ord('q'): break 
            # saving video
            video_writer.write(img_rgb)    
            # a los 10 minutos = 600 segundos acaba     
            #if time.time() - TimeIni > TimeLimit:
                    
            #        break
                   
            #if ContFrames > 4 :
            #    cv.destroyAllWindows()
            #    ContFrames =1
cap.release()
video_writer.release()
cv.destroyAllWindows()
print("")
print ("Hit Lanes = " + str(HitLanes) + " Failure Lanes = " + str(FailureLanes))
