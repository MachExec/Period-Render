import cv2
import numpy as np





# Read the image
image = cv2.imread('Input\Walter_White_S5B.png',0)
height, width = image.shape 
count = 0
DownRes = 4
PixelImage = [[] for _ in range(int(height/DownRes))]

WaterWidth = int(width/DownRes)
WaterHeight = int(height/DownRes)

for rows in range(height):
    for pixel in range(width):
        
        if(image[rows][pixel]>127):

            image[rows][pixel] = 255
        
        elif(image[rows][pixel]<=127):

            image[rows][pixel] = 0



for rows in range(WaterHeight):
    
    for pixel in range(WaterWidth):
        
        Current = image[rows*DownRes][pixel*DownRes] 

        if(Current==255): #white
            PixelImage[rows].append(" ")

        elif(Current==0): #black
            PixelImage[rows].append(".")

    


with open('store.txt', 'w') as file:
    for rows in range(WaterHeight):
        for Pixel in range(WaterWidth):
            file.write(PixelImage[rows][Pixel])
        
        file.write("\n")



#cv2.imwrite('Output/output_image.jpg', PixelImage)