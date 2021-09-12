import cv2

img = cv2.imread("C:\\Users\\Veeru\\PycharmProjects\\Neo_Python\\neo.jpg",
                 1)  # here 1 is colored image (3 dimension) & 0 will be black and white
print(type(img)) # type converted image
#print(img) #image array structure
print(img.shape) # its shows image size
cv2.imshow("Legend",img) # displays the image with given name
cv2.waitKey(2222) # display image only 2222 mile sec only after the its close
cv2.destroyAllWindows()
