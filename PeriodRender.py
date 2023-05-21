import cv2
import numpy as np

#note to self: add colored images
class PeriodRender:

    def __init__(self,I,D,S,D1):

        self.Image = cv2.imread('Input\\' + I,0)
        
        self.height, self.width = self.Image.shape 
        self.DownRes = D
        self.DownRes1 = D1

        self.WidthRatio = int(self.width/self.DownRes)
        self.HeightRatio = int(self.height/self.DownRes)

        if(self.DownRes1==0):
            self.WidthRatio1 = self.WidthRatio
            self.HeightRatio1 = self.HeightRatio
            self.PixelImage = [[] for _ in range(self.HeightRatio)]
        
        else:

            self.WidthRatio1 = int(self.width/self.DownRes)
            self.HeightRatio1 = int(self.height/self.DownRes1)

            self.PixelImage = [[] for _ in range(self.HeightRatio1)]

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

        cv2.imwrite('Output/output_image.jpg', self.Image)

        return self.Image

    
    def FinalRender(self):

        if(self.DownRes1==0):
            self.DownRes1 = self.DownRes


        self.Image = self.ConvertBinary()

        for rows in range(self.HeightRatio1):
            
            for pixel in range(self.WidthRatio):
                
                Current = self.Image[rows*self.DownRes1][pixel*self.DownRes] 

                if(Current==255): #white
                    self.PixelImage[rows].append(self.Symbols[1])

                elif(Current==0): #black
                    self.PixelImage[rows].append(self.Symbols[0])

            
        with open('store.txt', 'w',encoding='utf-8') as file:
            for rows in range(self.HeightRatio1):
                for Pixel in range(self.WidthRatio):
                    file.write(self.PixelImage[rows][Pixel])
                
                file.write("\n")




#Recommended: D = x, D1 = 2x.
#set D1 Equal to zero to not interfere with size/resolution of output
Ratio = 5
PeriodRender(I="Waltuh.png",D=Ratio,S="emoji",D1=Ratio*2).FinalRender() #first parm of S is black, second is white. D= rows (length) and D1 = Collumns (Height)

