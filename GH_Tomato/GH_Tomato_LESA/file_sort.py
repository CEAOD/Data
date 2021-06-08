import os
import shutil
import time
import datetime
import string


'''
The purpose of this program is to take a list of files and 
sort them into their respective folders. Start at the directory outside
the new_data folder and run this file sorting algorithm to organize it into 
their respective buckets
'''

'''
name folder of capture as 

'''

data_folder = "./data"
folder_names = ["python_files","top_down_images","side_view_images","txt_files"]


top_dir = './top_down_images/'
side_dir = './side_view_images/'
py_dir = './python_files/'
txt_dir = './txt_files/'


#Finds side of camera angle
def split_side(name_of_image_file):
    spl = name_of_image_file.split("_")
    tos = spl[4]
    return tos

#Splits time of image
def split_time(name_of_image_file):
    spl = name_of_image_file.replace("_ContinuousSide.jpg","")
    spl = spl.replace("_ContinuousTop.jpg","")
    return spl


def folder(name):
    if not os.path.exists('./'+name):
        os.makedirs('./'+name)
        print ('Created:', name)


#This sorts raspberri pi data into top and side directories
#Takes filename and new folder name as input
def sort_capture_rpi(filename, name):
    img_dir = './data/' + filename + '/'
    img_files = os.listdir(img_dir)

    if not os.path.exists('./top_down_images/'+name):
        os.makedirs('./top_down_images/'+name)
        print ('Created:', name)

    if not os.path.exists('./side_view_images/'+name):
        os.makedirs('./side_view_images/'+name)
        print ('Created:', name)

    for j in range(int(len(img_files)/2)):
        str1 = img_files[j*2]
        str2 = img_files[j*2 + 1]
        if not os.path.exists('./top_down_images/'+name+'/' +str(img_files[j*2])):
            shutil.move(img_dir +  str(img_files[j*2]),'./top_down_images/'+name)
        if not os.path.exists('./side_view_images/'+name+'/' +str(img_files[j*2+1])):
            shutil.move(img_dir + str(img_files[j*2+1]),'./side_view_images/'+name)

def camera_type(name):
    spl = name.split("_")
    spl = str(spl[1])
    return spl.strip()






#Only sorts text, python, and capture data where it goes top -> side in order
def sort(current):
    files = os.listdir(current)

    for name in folder_names:
        folder(name)

    for file in os.listdir(current):
        if file.endswith('.txt'):
            dest = './txt_files'
            src = './data/'+ str(file)
            shutil.move(src,dest)
        if file.endswith('.py'):
            src = './data/'+ str(file)
            dest = 'python_files'
            shutil.move(src,dest)
        if os.path.isdir('./data/'+file):
            cam_type = str(camera_type(str(file)))
            if cam_type == 'RPI':
                sort_capture_rpi(str(file),str(file))
    files = os.listdir('./data/')

def clean(current):
    for file in os.scandir(current):
        os.rmdir(file.path)

sort(data_folder)

print("Sorting the files...")


