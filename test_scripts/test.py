import cv2
from cv2 import aruco as aruco
import numpy as np
import os


def detectAruco(img, markerSize=6, totalMarker=250, draw=True):
    imgGS = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    key = getattr(aruco, f'DICT_{markerSize}X{markerSize}_{totalMarker}')
    arucoDict = aruco.Dictionary_get(key)
    arucoParams = aruco.DetectorParameters_create()
    boundBox, ids, rejected = aruco.detectMarkers(imgGS, arucoDict, parameters = arucoParams)
    print(ids)
    if draw:
        aruco.drawDetectedMarkers(img, boundBox)

def main():
    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()
        cv2.imshow("img", img)
        detectAruco(img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
