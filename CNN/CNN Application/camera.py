import cv2
from matplotlib import pyplot as plt

class CameraReal():
    def __init__(self, camera_index = 0):
        self.idnex = camera_index
        self.cap = cv2.VideoCapture(camera_index)
        self.savedNum = 0
    
    def getindex(self):
        return self.idnex
    
    def changeIndex(self, newIndex):
        self.index = newIndex
        self.cap = cv2.VideoCapture(self.index)
    
    def imread(self):
        ret, frame = self.cap.read()
        return ret, frame

    def imshow(self):
        if not ret:
            ret, frame = self.imread()
            print('No image readed')
            return
        else:
            plt.imshow(frame)

    def reset_savedNum(self):
        self.savedNum = 0

    def isClear(self, frame):
        img2gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        imageVar = cv2.Laplacian(img2gray, cv2.CV_64F).var()
        return imageVar



    def imsave(self, path = ""):
        if not ret:
            print("No image readed")
            return
        mypath = path + 'fig' + str(self.savedNum) + '.jpg'
        cv2.imwrite(mypath, frame)
        self.savedNum += 1
