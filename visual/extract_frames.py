import cv2
vidcap = cv2.VideoCapture('Touhou - Bad Apple.mp4')
count = 0;
print('test');
success,image = vidcap.read()
print(success)
while success:
  print("test")
  success,image = vidcap.read()
  cv2.imwrite("frames/frame%d.jpg" % count, image)     # save frame as JPEG file
  if cv2.waitKey(10) == 27:                     # exit if Escape is hit
      break
  count += 1