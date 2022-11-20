from dronekit import connect, VehicleMode, LocationGlobalRelative
from pymavlink import mavutil
import time
import argparse
import cv2
from cv2 import aruco as aruco
import numpy as np
import os
import func_definition


parser=argparse.ArgumentParser()
parser.add_argument('--connect',default='127.0.0.1:14550')
args = parser.parse_args()

#connect to the Vehicle
print ('Connecting to vehicle on: %s' % args.connect)
vehicle = connect(args.connect, baud=921600, wait_ready=True)
#921600 is the baudrate that you have set in the mission plannar or qgc

# global variable(s)
x_max = 1024  # width of pi camera image
y_max = 768   # height of pi camera image
x_center = x_max / 2  # center value used for readability/ease of editing
y_center = y_max / 2  # center value used for readability/ease of editing

def main():
    # Initialize the takeoff sequence to 15m
    func_definition.arm_and_takeoff(15) #->to intialise the function

    # Hover for 10 seconds
    time.sleep(15)

    print("Now let's land")
    vehicle.mode = VehicleMode("LAND")

    # Close vehicle object
    vehicle.close()#in the main flow program

if __name__ == "__main__":
    main()









