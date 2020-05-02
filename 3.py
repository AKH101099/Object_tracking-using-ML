import cv2
import numpy as np

def get_frame(cap,scalling_factor):
	ret, frame = cap.read() 
	frame = cv2.resize(frame, None, fx = scalling_factor, fy = scalling_factor, interpolation = cv2.INTER_AREA)
	return frame

if __name__=='__main__':
	cap = cv2.VideoCapture('video3.mp4') 
	scalling_factor = 1.0
	while True:
		frame = get_frame(cap,scalling_factor)
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		lower = np.array([20,100,100])
		upper = np.array([30,255,255])
		mask = cv2.inRange(hsv,lower,upper)
		img_bitwise_and = cv2.bitwise_and(frame,frame,mask=mask)
		img_median_blurred = cv2.medianBlur(img_bitwise_and,5)
		cv2.imshow('Object Tracking',img_median_blurred)
		cv2.imshow('Video',frame)
		if cv2.waitKey(33) == 27: 
			break
cv2.destroyAllWindows()
		