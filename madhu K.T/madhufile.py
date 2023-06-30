from pymongo import MongoClient
import pytesseract

import cv2
import os
from pymongo import MongoClient

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
mydatabase = client['Data_conversion163']

# Access collection of the database
mycollection = mydatabase['Madugula148']
# mycollection2 = mydatabase['Anakapalli143']
myimage = mydatabase['test2']

# dictionary to be added in the database
rec = {
    'title': 'MongoDB and Python',
    'description': 'MongoDB is no SQL database',
    'tags': ['mongodb', 'database', 'NoSQL'],
    'viewers': 104
}
# Connect to the MongoDB server
client = MongoClient('mongodb://localhost:27017/')
db2 = client['Data_conversion14']
collection2 = db2['Madugula1'] ## Mandal data collection table
db = client['Data_conversion14']
collection = db['Madugula data']     ## voter details collection table
data = collection.find()
data2 = collection2.find()

# l = os.listdir(folder_path)
# print(l)
# for i in range(len(l)):
#     print(l[i])
#     converting_pdftoimg(pdf_path=f'{folder_path}\{l[i]}')

# l = os.listdir()
for i in range(220525):
    dic = {}
    # print(i)
    # print(data[i])
    pdf = data[i]['Voter_file_tracker'].split('pdf')[0][:-1]
    print(pdf + ".png")
    daata = collection2.find_one({'Voter_file_tracker': pdf + ".png"})
    print(daata)
    votere_slip = (data[i]['votere_slip'])
    Assembly = (data[i]['Assembly Name'])
    section = (data[i]['Section'])
    details = (data[i]['details'])
    # print(data2[i]['voter_tacker_file'])
    main = (daata['Main_TownORVillage'])
    station = (daata['Police_Station'])
    man = (daata['Mandal'])
    reven = (daata['Revenue_Division'])
    Dis = (daata['District'])
    #
    dic['Voter_file_tracker'] = pdf
    dic['votere_slip'] = votere_slip
    dic['Assembly Name'] = Assembly
    dic['Section'] = section
    dic['details'] = details
    dic['Main_TownORVillage'] = main
    dic['Police_Station'] = station
    dic['Mandal'] = man
    dic['Revenue_Division'] = reven
    dic['District'] = Dis
    rec = mycollection.insert_one(dic)

