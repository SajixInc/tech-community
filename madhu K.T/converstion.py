import pytesseract

import cv2
import os
from pymongo import MongoClient

# output_file = r'D:\projects\pytesseract\images'  ## give images folder path
# output_file = r'C:\Users\vivif\Desktop\image1'
# folder_path = r'C:\Users\vivif\Desktop\dummy pdfs'  ## give pdf's folder path
folder_path = r'C:\Users\vivif\Desktop\images 2'

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
mydatabase = client['Data_conversion14']

# Access collection of the database
mycollection = mydatabase['Madugulafirstimages2']
myimage = mydatabase['test2']

# dictionary to be added in the database
rec = {
    'title': 'MongoDB and Python',
    'description': 'MongoDB is no SQL database',
    'tags': ['mongodb', 'database', 'NoSQL'],
    'viewers': 104
}

poppler_path = r'C:\Users\vivif\Desktop\convert\poppler-0.68.0\bin'
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def main_convert(x, y, w, h, im2, img_file=None):
    print(h)
    # try:4
    width = int(w / 3)
    im2 = cv2.imread(im2)
    f = open('test.txt', 'a')
    rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 5)
    cropped = im2[y:y + h, x:x + w]
    img = cv2.resize(rect, (1020, 750))
    cv2.imshow('d', img)
    cv2.waitKey(1)
    # count=count+1
    text = pytesseract.image_to_string(cropped, config='--psm 6 --oem 3 tessedit_char_whitelist=0123456789 ')
    # print(text)
    f = open('sample.txt', 'w')
    f.write(text)
    f.close()


# image_path = r'C:\Users\vivif\pythonProject\pythonProject3\SAMPLE'
l = os.listdir(folder_path)
for i in l:
    file = i
    print(file)
    main_convert(1750, 1700, 2000, 1500, im2=f"{folder_path}\{i}")

    f = open('sample.txt', 'r')
    x = f.readlines()
    dic = {}
    for i in x:
        dic['Voter_file_tracker'] = file.split('pdf')[0] + 'png'
        if "Mandal" in i:
            dic['Mandal'] = i.replace('Mandal', '').replace('>', '').replace('\n', '').replace(" ", "").replace("-", "")
            print(i)
        # i.replace("-", "")):
        #     print(i)

        elif 'Main Town/Village' in i:
            x = i.replace('Main Town/Village', '').replace('>', '').replace('\n', '').replace(" ", "").replace("-", "")
            dic['Main_TownORVillage'] = x
            print(i)
        elif 'Police Station' in i:
            dic['Police_Station'] = i.replace('Police Station', '').replace('>', '').replace('\n', '').replace(" ","").replace("-", "")
            print(i)
        elif 'Revenue Division' in i:
            dic['Revenue_Division'] = i.replace('Revenue Division', '').replace('>', '').replace('\n', '').replace(" ","").replace("-", "")
            print(i)
        elif 'District' in i:
            dic['District'] = i.replace('District', '').replace('>', '').replace('\n', '').replace(" ", "").replace("-", "")
            print(i)
        elif 'Pin Code' in i:
            dic['Pin_Code'] = i.replace('Pin Code', '').replace('>', '').replace('\n', '').replace(" ","").replace("-", "")
            print(i)


    rec = mycollection.insert_one(dic)
