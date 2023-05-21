import cv2
import numpy as np


class PeriodRender:

    def __init__(self,I,D,S):

        self.Image = cv2.imread('Input\\' + I,0)
        self.height, self.width = self.Image.shape 
        self.DownRes = D

        self.WidthRatio = int(self.width/self.DownRes)
        self.HeightRatio = int(self.height/self.DownRes)

        self.PixelImage = [[] for _ in range(self.HeightRatio)]

        self.Symbols = S

    def CommonSymbols(self):

        if(self.Symbols=="emoji" or self.Symbols=="Emoji"):
            self.Symbols = ["⬛","⬜"]
            return self.Symbols

        elif(self.Symbols=="sqre" or self.Symbols=="Sqre"):
            self.Symbols = ["⠶"," "]
            return self.Symbols
        
        elif(self.Symbols=="rect" or self.Symbols=="Rect"):
            self.Symbols = ["⣿"," "]
            return self.Symbols
        
        elif(self.Symbols=="line" or self.Symbols=="Line"):
            self.Symbols = ["⠉"," "]
            return self.Symbols
        

        
        else:
            return self.Symbols

    def ConvertBinary(self):

        self.Symbols = self.CommonSymbols()

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
                    self.PixelImage[rows].append(self.Symbols[1])

                elif(Current==0): #black
                    self.PixelImage[rows].append(self.Symbols[0])

            
        with open('store.txt', 'w',encoding='utf-8') as file:
            for rows in range(self.HeightRatio):
                for Pixel in range(self.WidthRatio):
                    file.write(self.PixelImage[rows][Pixel])
                
                file.write("\n")



#cv2.imwrite('Output/output_image.jpg', PixelImage)

PeriodRender(I="Walter_White_S5B.png",D=3,S="Line").FinalRender() #first parm of S is black, second is white