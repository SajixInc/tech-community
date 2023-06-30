import cv2
import numpy as np
import pytesseract
import os
import datetime
import base64
import boto3
#
# C:\Program Files\Tesseract-OCR\tesseract.exe
# poppler_path=r'D:\downloads\poppler-0.68.0_x86\poppler-0.68.0\bin'
poppler_path = r'C:\Users\vivif\Desktop\convert\poppler-0.68.0\bin'
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Mongodb
from pymongo import MongoClient

# output_file = r'D:\projects\pytesseract\images'  ## give images folder path
output_file = r'C:\Users\vivif\Desktop\dummy original images 2'
folder_path = r'C:\Users\vivif\Desktop\dummy images 1'  ## give pdf's folder path
# creation of MongoClient
client = MongoClient()
he = []

import urllib.parse

Username = 'devops_admin'
Password = 'Devops1234'
username = urllib.parse.quote_plus(Username)
password = urllib.parse.quote_plus(Password)
# Connect with the portnumber and host
client = MongoClient('mongodb://localhost:27017/')
# client = MongoClient('mongodb://%s:%s@13.234.70.44:27017' % (username,password))

# Access database
mydatabase = client['Data_conversion3']

# Access collection of the database
mycollection = mydatabase['mad143']
mycollection2 = mydatabase['mad143']
myimage = mydatabase['test2']

# dictionary to be added in the database
rec = {
    'title': 'MongoDB and Python',
    'description': 'MongoDB is no SQL database',
    'tags': ['mongodb', 'database', 'NoSQL'],
    'viewers': 104
}

# Time kosam

dt = datetime.datetime.now()
print(dt)
lis = ["", ""]

count = 0


def imgetobase(file, img_file):
    global count
    f = f"slip{count}-{img_file}.png"
    b_name = "ivin-pro-data-conversion"

    cv2.imshow('slip window', file)
    img = cv2.imwrite(f, file)
    cv2.waitKey(3)

    # cv2.putText(f, 'Rectangle', (100,100), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    # s3 = boto3.client("s3")
    # b_res = s3.list_buckets()
    # for i in b_res['Buckets']:
    #         print(i)
    # serial = cv2.imread(file)
    # rect = cv2.rectangle(file, (0, 0), (330, 90), (0, 0, 255), 5)
    # cv2.imshow("serial", rect)
    # cv2.waitKey(3)
    with open(f, 'rb') as img:
        im3=cv2.imread(f)
        print(im3.shape[1])
        rect = cv2.rectangle(im3, (180, 10), (300, 80), (0, 0, 255), 5)
        print(im3.shape)
        crop_img = im3[10:90, 10:330]

        config = config = ('--psm 13 osm 1 -c tessedit_char_whitelist=0123456789')
        crop = cv2.imshow("serial number", crop_img)
        text =pytesseract.image_to_string(crop_img,config=config )
        print('---------- 78 ------- ', text)
        global serialnumber
        serialnumber = text
        # cv2.imshow("im3",rect)
        cv2.waitKey(3)
    count = 1 + count
    # with open(f, 'rb') as img:
    #     s3.upload_fileobj(img, b_name, img_file + f)
    return f


# def pagetobase(image):
#     image = open(image, 'rb')
#     image_read = image.read()
#     image_64_encode = base64.encodebytes(image_read) #encodestring also works aswell as decodestring
#     # print('This is the image in base64: ' + str(image_64_encode))
#     return str(image_64_encode)


def page(image):
    text = pytesseract.pytesseract.image_to_string(image)
    # print(text)
    text.replace('Photo', "")
    # print(text)
    f = open('text.txt', 'w')
    f.write(text + "\n")
    f.close()
    fi = open('text.txt', 'r')
    x = fi.readlines()
    for i in x:
        if "Assembly" in i:
            lis[0] = i
        elif "Section" in i:
            lis[1] = i
    fi.close()


# print(lis)


c = 1


# slips cutts
def covert(x, y, w, h, im2, img_file):
    # print(h)
    # try:
    width = int(w / 3)
    if h >= 400 and h < 1000:
        # print(h,w)
        width = int(w / 3)
        # print(width,'--------')
        f = open('test.txt', 'a')
        rect = cv2.rectangle(im2, (x, y), (x + width, y + h), (0, 255, 0), 5)

        if x == 0 and y == 0:
            pass
        else:
            cropped = im2[y:y + h, x:x + width]
            img = cv2.resize(rect, (1020, 750))
            cv2.imshow('d', cropped)
            cv2.waitKey(3)

            # serial_number = cropped[y:y+100, x:x+100]

            # # count=count+1
            text = pytesseract.image_to_string(cropped)
            f = open('text.txt', 'a')
            f.write(text)
            f.close()
            b = imgetobase(cropped, img_file)
            rec = mycollection.insert_one({
                'serial number':serialnumber,
                'Voter_file_tracker': img_file,
                "votere_slip": b,
                "Assembly Name": lis[0],
                "Section": lis[1],
                'details': text,
                'Created on': dt})


def ima(x, y, w, h, im2, img_file):
    # #print(x,y)
    im2 = cv2.imread(im2)
    cv2.putText(im2, 'Rectangle', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    # rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 5)
    # img = cv2.resize(rect, (1020, 750))
    # cv2.imshow('d', img)
    # print(x, y)
    covert(x, y, w, h, im2, img_file)
    W = int(w / 3)
    covert(x + W, y, w, h, im2, img_file)
    covert(x + W + W, y, w, h, im2, img_file)


area = []
value = []


# def img_detect(img_path, img_file):
#     lis.clear()
# page(img_path)
#
def img_detect(img_path, img_file):
    page(img_path)
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 50, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, 1, 2)

    for cnt in contours:
        x1, y1 = cnt[0][0]
        approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(cnt)

            ratio = float(w) / h
            if ratio >= 0.9 and ratio <= 1.1:
                pass
            else:
                area.append((h * w))
                value.append((h, w, x, y))
                he.append(h)
    for i in range(len(area)):
        # if value[i][1]>=0 and value[i][1]>100:
        xa = value[i][2]
        ya = value[i][3]
        l = value[i][0]
        w = value[i][1]
        # cv2.rectangle(img, (xa, ya), (xa + w, ya + l), (0, 255, 0), 2)
        ima(x=xa, y=ya, w=w, h=l, im2=img_path, img_file=img_file)


import os


def image_upload(image_file):
    print("count of images :", len(os.listdir(folder_path)))
    l = os.listdir(image_file)
    path = image_file
    print(l)
    for k in range(len(l)):
        print('sir done')
        print(k, 'started')
        area.clear()
        value.clear()
        he.clear()
        img_detect(img_path=f"{path}\{l[k]}", img_file=l[k])
        # os.remove(f"{path}\{l[k]}")          #this stop deleted images this line
        print(k, 'done')


def converting_pdftoimg(pdf_path):
    from pdf2image import convert_from_path
    # print(pdf_path)
    images = convert_from_path(pdf_path, 500, poppler_path=poppler_path)
    name = pdf_path.split("\\")
    print(name)
    for i, image in enumerate(images):
        print(i, 'is pdf converting into images')
        fname = f'{name[-1]}' + str(i) + '.png'
        # print(fname)
        image.save(f"{output_file}\{fname}", "PNG")


l = os.listdir(folder_path)
# print(l)
# for i in range(len(l)):
#    print(l[i])
#    converting_pdftoimg(pdf_path=f'{folder_path}\{l[i]}')
# yesy()

image_upload(f'{folder_path}')

# dt  = datetime.datetime.now()


















# #
# from PIL import Image
#
# black = (0,0,0)
# white = (255,255,255)
# threshold = (160,160,160)
# #
# # # Open input image in grayscale mode and get its pixels.
# img = Image.open(r"C:\Users\vivif\Desktop\dummy images 1\AP_Anakapalli_Narsipatnam_1_KRISHNADEVIPETA_MANDAL PARISHAD PRIMARY SCHOOL, OLD BUILDING KRISHNADEVIPETA.pdf3.png").convert("LA")
# pixels = img.getdata()
#
# newPixels = []
#
# # Compare each pixel
# for pixel in pixels:
#     if pixel < threshold:
#         newPixels.append(black)
#     else:
#         newPixels.append(white)
#
# # Create and save new image.
# newImg = Image.new("RGB",img.size)
# newImg.putdata(newPixels)
# newImg.save("newImage.jpg")
# #
#
# img = r"C:\Users\vivif\pythonProject\pythonProject3\newImage.jpg"
# text = pytesseract.image_to_string(img)
# print(text)
#
#
#
#
#
