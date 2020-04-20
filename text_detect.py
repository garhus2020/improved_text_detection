import pytesseract
import cv2
import numpy as np
import imutils
import glob
import cv2
from back import modify

def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
def remove_noise(image):
    return cv2.medianBlur(image,5)





def rotate_image(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result


def text(str):
    new=str.find("anything")
    if(new!=-1  ):
     return 1
    return 0


def convert(image):
    pytesseract.pytesseract.tesseract_cmd = r"path_to_tesseract.exe"
    image_to_text = pytesseract.image_to_string(image, lang='eng')
 
    return image_to_text


def rotate_check(image):
    sum=0
    temp=convert(image)
    img1=rotate_image(image,5)
    temp1=convert(img1)
    img2=rotate_image(image,355)
    temp2=convert(img2)
    sum=sum+text(temp)+text(temp1)+text(temp2)
    #print(temp)
    return sum

def check(image):
    sum=0
    img=cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    img1=cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    sum=sum+rotate_check(img)+rotate_check(img1)+rotate_check(image)
    if(sum==0):
     return "no"
    return "yes"

def main(image):
     print(check(modify(image)))
