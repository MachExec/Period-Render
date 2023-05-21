import cv2
import numpy as np


class PeriodRender:

    def __init__(self,I,D):

        self.Image = cv2.imread('Input\\' + I,0)
        self.height, self.width = self.Image.shape 
        self.DownRes = D

        self.WidthRatio = int(self.width/self.DownRes)
        self.HeightRatio = int(self.height/self.DownRes)

        self.PixelImage = [[] for _ in range(self.HeightRatio)]



    def ConvertBinary(self):
        for rows in range(self.height):
            for pixel in range(self.width):
                
                if(self.Image[rows][pixel]>127):

                    self.Image[rows][pixel] = 255
                
                elif(self.Image[rows][pixel]<=127):

                    self.Image[rows][pixel] = 0

        return self.Image

    
    def FinalRender(self):

        self.Image = self.ConvertBinary()

        for rows in range(self.HeightRatio):
            
            for pixel in range(self.WidthRatio):
                
                Current = self.Image[rows*self.DownRes][pixel*self.DownRes] 

                if(Current==255): #white
                    self.PixelImage[rows].append(" ")

                elif(Current==0): #black
                    self.PixelImage[rows].append(".")

            
        with open('store.txt', 'w') as file:
            for rows in range(self.HeightRatio):
                for Pixel in range(self.WidthRatio):
                    file.write(self.PixelImage[rows][Pixel])
                
                file.write("\n")



#cv2.imwrite('Output/output_image.jpg', PixelImage)

PeriodRender(I="Walter_White_S5B.png",D=1).FinalRender()