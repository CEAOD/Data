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

valid_types = ['RPI']

def camera_type(name):
    spl = name.split("_")
    spl = str(spl[1])
    return spl.strip()


input_directory = input("What is the filepath of your new data folder?\n")
input_name = input("What is the name of your plant? Example: Tomato_RPI_1 is the first Tomato you are recording.\n")

while camera_type(input_name) not in valid_types:
    print('Type the input name properly! Plantname_camera_1, for example. Valid types are currently [\'RPI\']\n')
    input_name = input("What is the name of your plant? Example: Tomato_RPI_1 is the first Tomato you are recording.\n")

while not os.path.exists(input_directory):
    print('Is that a valid directory??\n')
    input_directory = input("What is the filepath of your new data folder?\n")



folder_names = ["python_files","top_down_images","side_view_images","txt_files"]


top_dir = './top_down_images/'
side_dir = './side_view_images/'
py_dir = './python_files/'
txt_dir = './txt_files/'

def folder(name):
    if not os.path.exists('./'+name):
        os.makedirs('./'+name)
        print ('Created:', name)


#This sorts raspberri pi data into top and side directories
#Takes filename and new folder name as input
def sort_capture_rpi(filepath, name):
    img_files = os.listdir(filepath)

    if not os.path.exists('./top_down_images/'+name):
        os.makedirs('./top_down_images/'+name)
        print ('Created:', name)

    if not os.path.exists('./side_view_images/'+name):
        os.makedirs('./side_view_images/'+name)
        print ('Created:', name)

    if not os.path.exists('./redundant_images/'+name):
        os.makedirs('./redundant_images/'+name)
        print('Created: ', name)

    for j in range(int(len(img_files))):
        str1 = img_files[j]
        if('ContinuousTop' in str1):
            if os.path.exists('./top_down_images/'+name):
                if not os.path.exists('./top_down_images/'+name+ '/'+ str(img_files[j])):
                    shutil.move(filepath + '/' + str(img_files[j]),'./top_down_images/'+name)
        if('ContinuousSide' in str1):
            if os.path.exists('./side_view_images/'+name):
                if not os.path.exists('./side_view_images/'+name+ '/'+ str(img_files[j])):
                    shutil.move(filepath + '/' + str(img_files[j]),'./side_view_images/'+name)

'''
def time_sort(current):
    files = os.listdir(current)

    for i= 1 to len(files)
        if len(files) > 1:
                mid = len(files) // 2  # Finding the mid of the array
                left = files[:mid]  # Dividing the array elements
                right = files[mid:]  # into 2 halves

                time_sort(left)
                time_sort(right)

                i = j = k = 0

                #  data to temp arrays L[] and R[]
                while i < len(left) and j < len(right):
                    if left[i] < right[j]:
                        time_sort[k] = left[i]
                        i += 1
                    else:
                        time_sort[k] = right[j]
                        j += 1
                    k += 1

                # Checking if any element was left
                while i < len(left):
                    unsorted_array[k] = left[i]
                    i += 1
                    k += 1

                while j < len(right):
                    unsorted_array[k] = right[j]
                    j += 1
                    k += 1

'''

def sort(current, name_of_plant):
    files = os.listdir(current)
    src = input_directory

    for file in files:
        print("Sorting..."+str(file) + '\n')
    for name in folder_names:
        folder(name)

    for file in os.listdir(current):
        print(str(file))
        if file.endswith('.txt'):
            dest = './txt_files'
            shutil.move(src,dest)
        if file.endswith('.py'):
            dest = './python_files'
            shutil.move(src,dest)
        if os.path.isdir(src + '/'+str(file)):
            cam_type = str(camera_type(name_of_plant))
            if cam_type == 'RPI':
                sort_capture_rpi(src + '/'+str(file), name_of_plant)


def clean(current):
    for file in os.scandir(current):
        os.rmdir(file.path)


sort(input_directory, input_name)
print("Sorting the files...")


