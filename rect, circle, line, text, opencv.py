import cv2
path = r"C:\Users\USER\Pictures\Screenshots\Screenshot 2025-03-15 161038.png"
image = cv2.imread(path)
# cv2.imshow('Original image', image)

# Line 
imageLine = image.copy()
imageLine = cv2.line(imageLine, (250, 50), (600, 50), (0, 255, 0), thickness = 50, lineType = cv2.LINE_AA)

# text 
text = "YEAH"
fontScale = 3.5
fontFace = cv2.FONT_HERSHEY_PLAIN
fontColor = (255, 0, 0)
fontThickness = 2

imageLine = cv2.putText(imageLine, text,(390, 65), fontFace, fontScale, fontColor, fontThickness, cv2.LINE_AA)

# rectangle 
imageLine = cv2.rectangle(imageLine, (250, 250), (600, 800), (0, 255, 0), thickness = 5, lineType = cv2.LINE_8);

# circle 
imageLine = cv2.circle(imageLine, (425, 250), 175, (0, 255, 0), thickness = 5, lineType = cv2.LINE_8)

cv2.imshow('final image', imageLine)
cv2.waitKey(0)
cv2.destroyAllWindows()
