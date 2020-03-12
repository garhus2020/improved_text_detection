import numpy as np
import argparse
import imutils
import cv2
import pytesseract

def remove_noise(image):
    return cv2.medianBlur(image,3)


def convert(image):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Users\huseyng\AppData\Local\Tesseract-OCR\tesseract.exe"
    image_to_text = pytesseract.image_to_string(image, lang='eng')
 
    return image_to_text




def modify(image):
    
    image=imutils.resize(image,width=1050)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    t2 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,17,2)
    t2=remove_noise(t2)
    #t2 = cv2.erode(t2, None, iterations = 1)
    #t2 = cv2.erode(t2, None, iterations = 1)
    

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    t2 = cv2.morphologyEx(t2, cv2.MORPH_CLOSE, kernel)
    #cv2.imshow('sed',t2)
    return t2




