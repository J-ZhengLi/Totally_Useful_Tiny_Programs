import cv2
v = cv2.VideoCapture('sample_video')
fc = int(v.get(cv2.CAP_PROP_FRAME_COUNT)); delay = int(1000/v.get(cv2.CAP_PROP_FPS))
for i in range(1, fc):
    v.set(cv2.CAP_PROP_POS_FRAMES, fc-i-1)
    _, frame = v.read()
    cv2.imshow('output', frame)
    if cv2.waitKey(delay) == ord('q'): break
v.release(); cv2.destroyAllWindows()