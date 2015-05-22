import os

#Local Path (Works with py2exe)
path = os.path.dirname(__file__).replace('\\library.zip','')
phone_log_path = path + '\persistent-list\\'
current_list_name = ''
list_data = list()


#Check if path exists
def check_path(path):
    if not os.path.exists(path):
        os.makedirs(path)

#Check if file exists
def check_file(path, file):
    if os.path.isfile(path + file) == False:
        f = open(path + file, 'a')
        f.write('')
        f.close()
        return False
    else:
        return True

#Load or create new list file
def Load(listname):
    global phone_log_path
    global current_list_name
    global list_data
    current_list_name = listname
    check_path(phone_log_path)
    check_file(phone_log_path, listname)
    f = open(phone_log_path + listname, 'r')
    data = f.read()
    data = data.split(',')
    list_data = list()
    for data in data:
        if data != '':
            list_data.append(data)

#Commit changes to list file
def Save():
    global phone_log_path
    global current_list_name
    global list_data
    f = open(phone_log_path + current_list_name, 'w')
    output = ''
    for data in list_data:
        if data == '':
            continue
        output += str(data) + ','
    f.write(output)
    f.close()
    
#Add an item
def AddItem(item):
    global list_data
    list_data.append(item)
    
#See if an item is in a list
def CheckItem(item):
    global list_data
    if item in list_data:
        return True
    else:
        return False

#Output list
def GiveList():
    global list_data
    return list_data
