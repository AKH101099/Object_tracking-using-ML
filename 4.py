import cv2
import numpy as np

def get_frame(cap,scalling_factor):
	ret, frame = cap.read() 
	frame = cv2.resize(frame, None, fx = scalling_factor, fy = scalling_factor, interpolation = cv2.INTER_AREA)
	return frame

if __name__=='__main__':
	cap = cv2.VideoCapture('video4.mp4')
	bg_subtractor = cv2.createBackgroundSubtractorMOG2()
	history = 100
	learning_rate = 1.0/history 
	scalling_factor = 1.0
	while True:
		frame = get_frame(cap,scalling_factor)
		mask = bg_subtractor.apply(frame,learningRate=learning_rate)
		mask = cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
		cv2.imshow('Object Tracking',mask & frame)
		cv2.imshow('Video',frame)
		if cv2.waitKey(33) == 27: 
			break
cap.release()
cv2.destroyAllWindows()
		