import datetime

from pymongo import MongoClient
from bson.objectid import ObjectId

# Connect to the MongoDB server
client = MongoClient('mongodb://localhost:27017/')
db = client['Data_conversion163']
dt = datetime.datetime.now()
# Access the collection
collection = db['Madugula148']
collection2 = db['Madugula']
data = collection.find()

dic = {}
counter = 0
new_list = []
c = 0
for document in data:
    c = c + 1
    _idd = document['_id']
    try:
        if document['details']:
            x = (document['details'])
            lines = x.split('\n')
            dic['VoterId'] = lines[0]
            # print(lines)
            for i in lines:
                # print(i)
                if i.startswith('Name'):
                    if i[5:].startswith(':'):
                        dic['Name'] = i[6:]
                    elif i[5:].startswith('-'):
                        dic['Name'] = i[6:]
                    else:
                        dic['Name'] = i[5:]
                    a = dic['Name'].split(" ")
                    dic['FirstName'] = a[1]
                    dic['LastName'] = a[2]
                elif "Age" in i and "Gender" in i:
                    # print(i)
                    ag = i.split('Gender')
                    # print(ag)
                    dic['Age'] = ag[0][4:]
                    if ag[1] == ': MALE Photo is' or ag[1] == ': MALE Available' or ag[1] == ': MALE':
                        dic['Gender'] = ag[1][2:6]
                    elif ag[1] == ': FEMALE Photo is' or ag[1] == ': FEMALE Available' or ag[1] == ': FEMALE':
                        dic['Gender'] = ag[1][2:8]
                elif i.startswith("Gender"):
                    dic['Gender'] = i[8:]
                elif i.startswith('House'):
                    a = i.split('House')
                    dic['Home'] = a[1][9:15]


                elif i.startswith('Husband') or i.startswith('Father') or i.startswith('Mother') or i.startswith(
                        'Wife') or i.startswith('Other'):
                    if ':' in i:
                        g = i.split(':')
                        a = g[0].replace("'s Name", "")
                        dic['Relation_Type'] = a
                        dic['Guardian'] = g[1]
                    else:
                        g = i.split('-')
                        # print(g)
                        dic['Guardian'] = g[1]
            counter = counter + 1
            dic['ivin_id'] = c
            print(dic['ivin_id'])
            dic['_id'] = ObjectId()
            # print(dic['_id'])
            # print(dic['_id'])
        if document['votere_slip']:
            x = document['votere_slip']
            y = (x.split('slip'))
            dic['Voter_Slip'] = 'slip' + y[1]
            # print(dic['Voter_Slip'])

        if document['Voter_file_tracker']:
            # print(document['image name'])
            x = (document['Voter_file_tracker'])

            # print(x)

            # Split the string into a list of lines
            lines = x.split('_')
            dic['State'] = lines[0]
            dic['District'] = lines[1]
            dic['Constituency'] = lines[2]
            dic['Polling_Station_Number'] = lines[3]
            dic['Mandal'] = lines[4]
            dic['Polling_Station_Name'] = lines[5]

            a = lines[5]
            new_string = a.replace(".pdf", "")
            new_string = new_string.replace(".png", "")
            dic['Polling_Station_Location'] = new_string
            dic["CreatedOn"] = dt
            dic["UpdatedOn"] = dt

        if document['Mandal']:
            x = (document['Mandal'])
            dic['Mandal'] = x
        if document['Main_TownORVillage']:
            x = (document['Main_TownORVillage'])
            dic['Main_TownORVillage'] = x
        if document['Revenue_Division']:
            x = (document['Revenue_Division'])
            dic['Revenue_Division'] = x
        if document['District']:
            x = (document['District'])
            dic['District']
        dic['Voter_file_tracker'] = document['Voter_file_tracker']

        if document['Section']:
            x = (document['Section'])
            lines = x.split(':')
            dic['Section_No_and_Name'] = lines[1]

            #
            #     # print(new_string)
            # print(a)
        if document['Assembly Name']:
            x = (document['Assembly Name'])
            line = x.split(':')
            # print(line)
            dic['Assembly_Constituency_No_and_Name'] = line[1]
            x = collection2.insert_one(dic)
            # print(lines)

    except:
        dic['_id'] = ObjectId()
        dic['ivin_id'] = c
        print(dic['ivin_id'])
        dic['VoterId'] = 'Null'
        dic['Name'] = 'Null'
        dic['FirstName'] = 'Null'
        dic['LastName'] = 'Null'
        dic['Age'] = 'Null'
        dic['Gender'] = 'Null'
        dic['Home'] = 'Null'

        dic['Relation_Type'] = 'Null'
        dic['Guardian'] = 'Null'
        dic['State'] = 'Null'
        dic['District'] = 'Null'
        dic['Constituency'] = 'Null'
        dic['Polling_Station_Number'] = 'Null'
        dic['Polling_Station_Name'] = 'Null'
        dic['Polling_Station_Location'] = 'Null'
        # dic['Assembly Constituency No and Name'] = 'Null'
        # dic['Section No and Name'] = 'Null'
        dic['Voter_Slip'] = 'Null'
        dic['Mandal'] = 'Null'
        dic['Main_TownORVillage'] = 'Null'
        dic['Revenue_Division'] = 'Null'
        dic['District'] = 'Null'
        dic['Voter_file_tracker'] = 'Null'
        dic["CreatedOn"] = dt
        dic["UpdatedOn"] = dt
        x = collection2.insert_one(dic)































# import datetime
#
# from pymongo import MongoClient
# from bson.objectid import ObjectId
#
# # Connect to the MongoDB server
# client = MongoClient('mongodb://localhost:27017/')
# db = client['Data_conversion2']
#
# dt = datetime.datetime.now()
# # Access the collection
# collection = db['Anakapalli']
# collection2 = db['Anakapalli2']
# data = collection.find()
# # import datatime
# from pymongo import MongoClient
#
# # from bson.objectid import  ObjectId
#
# # Connect to the MongoDB server
# client = MongoClient('mongodb://localhost:27017/')
# db = client['Data_conversion3']
# # dt = datatime.datatime.now()
# # Access the collection
# collection = db['Anakapalli3']
# collection2 = db['Anakapalli3']
# data = collection.find()
#
# from pymongo import MongoClient
#
# # from bson.objectid import  ObjectId
#
# # Connect to the MongoDB server
# client = MongoClient('mongodb://localhost:27017/')
# db = client['Data_conversion8']
# # dt = datatime.datatime.now()
# # Access the collection
# collection = db['Anakapalli']
# collection2 = db['Anakapalli']
# data2 = collection.find()
#
# # print(data)
# for i in range(5):
#     print(data[i]['Voter_file_tracker'])
    # print(data[i]['votere_slip'])
    # print(data[i]['Assembly Name'])
    # print(data[i]['details'])
    # # print(data2[i]['voter_tacker_file'])
    # print(data2[i]['Main Town/Village'])
    # print(data2[i]['Police Station'])
    # print(data2[i]['District'])
    # print(data2[i]['Revenue Division'])
    # print(data2[i]['Mandal'])

# for i in data2:
#     print(i)
#     print(i['voter_tacker_file'])
#     print(i['Main Town/Village'])
#     print(i['Police Station'])
#     print(i['District'])
#     print(i['Revenue Division'])
#     print(i['Mandal'])
