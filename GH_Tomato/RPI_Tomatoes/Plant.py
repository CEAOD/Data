import os
import shutil
import time
import string
from functools import cmp_to_key
from datetime import datetime


#Takes data point for sorting
class Plant_Time_Data:

	def __init__(self,carbon_dioxide,humidity,temperature,time):
		self.co2 = carbon_dioxide
		self.hm = humidity
		self.tmp = temperature
		self.time = time

		ymd = (time.split('_'))[0]
		hms = (time.split('_'))[1]
		y = int(ymd.split('-')[0])
		mo = int((ymd.split('-')[1]).strip('0'))
		d = int(ymd.split('-')[2])
		h = int(hms[0] + hms[1])
		mi = int(hms[2] + hms[3])
		s = int(hms[4] + hms[5])

		self.date_time = datetime(y,mo,d,h,mi,s)

		#Getter functions of time/co2/hm/tmp
		def get_time(self):
			return self.date_time

		def get_co2(self):
			return self.co2

		def get_hm(self):
			return self.hm

		def get_tmp(self):
			return self.tmp

		#equals function for self and x to compare
		def equals(self,x):
			if (self.time == x.time and self.hm == x.hm and self.tmp == x.tmp and self.co2 == x.co2):
				return True
			else:
				return False



#Object class of Plant
class Plant:
	def __init__(self):
		self.Plant_Array = []
		self.size = 0


	def __init__(self,Plant_Array):
		self.Plant_Array = Plant_Array
		self.size = len(Plant_Array)

	#Comparator for self and x object in Plant Class
	def compare(self,x):
		return self[0].get_time() - x[0].get_time()

	#Sort function for sorting the plant
	def sort(self):
		from functools import cmp_to_key
		self.Plant_Array.sort(key=lambda x: x.date_time, reverse=False)


	#Type testing functions
	def ret_co2(type):
		if type == 'CO2' or 'CO2:':
			return True
		else:
			return False

	def ret_hm(type):
		if type == 'temp' or 'temp:':
			return True
		else:
			return False

	def ret_rh(type):
		if type == 'rh' or 'rh:':
			return True
		else:
			return False

	#Stripper functions
	#Strips number class
	def str_num(str):
		str = str.strip('\n')
		str = str.strip(',')
		str = str.strip('C')
		str = str.strip('\'')
		str = str.strip('%')
		str = str.strip('ppm')
		str = str.strip('\'')
		return str

	#Strips types in class
	def str_type(str):
		str = str.strip('\n')
		str = str.strip(' ')
		str = str.strip(':')	

	#Add matrix
	def add_matrix(txt_dir,matrix):
		try:
			f = open(txt_dir)
			lines = f.readlines()

			for line in lines:
				#please feed time into add_matrix first, rest is goint str -> num
				#in co2 -> num -> temp -> num -> hm -> num
				m = line.split(' ')

				time = str(m[0])
				type1 = str(m[1])
				type1_data = float(str(str_num(str(m[2]))))
				type2 = str(m[3])
				type2_data = float(str(str_num(str(m[4]))))
				type3 = str(m[5])
				type3_data = float(str(str_num(str(m[6]))))
				
				#Adding type and data to array
				co2 = 0
				hm = 0
				rh = 0
				#checks data type to make sure which one it is
				if ret_co2(type1):
					co2 = type1_data
				if ret_hm(type2):
					hm = type2_data
				if ret_rh(type3):
					rh = type3_data
				#point added to point matrix
				point = Plant_Time_Data(co2,hm,rh,time)
				#Making sure that point is not in matrix
				if point not in matrix:
					matrix.append(point)

		finally:
			pass


	#Create new folder
	def folder(name):
	    if not os.path.exists('./'+name):
	        os.makedirs('./'+name)
	        print ('Created:', name)

	#Create plant matrix
	def create_array():
		input_dir = input("Where are the data files? ex: mnt/c/Users/..../txt_files\n")

		matrix = []
		files = os.listdir(input_dir)

		for file in files:
			print("Sorting..."+str(file) + '\n')
			add_matrix(input_dir + '/' + file,matrix)
		
		plant = Plant(matrix)
		plant.sort()
		return plant

