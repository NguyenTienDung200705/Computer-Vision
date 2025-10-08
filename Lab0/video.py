import cv2
import matplotlib.pyplot as plt
video_path = r'D:\HUS\Computer Vision\6922889342033.mp4'
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret :
        break
    cv2.imshow('Frame' , frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()