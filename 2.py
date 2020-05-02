import cv2

def frame_diff(prev_frame,cur_frame,next_frame):
	diff_frame_1 = cv2.absdiff(next_frame,cur_frame)
	diff_frame_2 = cv2.absdiff(cur_frame,prev_frame)
	return cv2.bitwise_and(diff_frame_1,diff_frame_2)

def get_frame(cap,scalling_factor):
	ret, frame = cap.read() 
	frame = cv2.resize(frame, None, fx = scalling_factor, fy = scalling_factor, interpolation = cv2.INTER_AREA)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	return gray

if __name__=='__main__':
	cap = cv2.VideoCapture('video2.mp4') 
	scalling_factor = 0.5
	prev_frame = get_frame(cap,scalling_factor)
	cur_frame = get_frame(cap,scalling_factor)
	next_frame = get_frame(cap,scalling_factor)
	while True:
		cv2.imshow('Object Movement',frame_diff(prev_frame,cur_frame,next_frame))
		cv2.imshow('Video',cur_frame)
		prev_frame = cur_frame
		cur_frame = next_frame
		next_frame = get_frame(cap,scalling_factor)
		if cv2.waitKey(33) == 27: 
			break
cv2.destroyAllWindows()
		