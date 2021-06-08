import os
import shutil
import time
import datetime
import string

matrix_arr = []
class Plant_Time_Data:
	def __init__(self,carbon_dioxide,humidity,temperature,time):



class Plant:
	def __init__(self,Plant_Time_Data_Array):



def add_matrix(txt):
	try:
		f = open(fdir + '/' + txt)
		lines = f.readlines()
		matrix = []
		for line in lines:
			m = line.split(' ')
			time = m[0].strip(['.',' ',',',':'])
			type1 = m[1].strip(['.',' ',',',':'])
			type1_data = m[2].strip(['.',' ',',',':'])
			type2 = m[3].strip(['.',' ',',',':'])
			type2_data = m[4].strip(['.',' ',',',':'])
			type3 = m[5].strip(['.',' ',',',':'])
			type3_data = m[6].strip(['.',' ',',',':'])

			carbon_data = 0
			humidity_data = 0
			temperature_data = 0
			time_data = ''

			if type1 == 
	finally:
		pass

def read_text(fdir):
	txt_files = os.listdir(fdir)
	for txt in txt_files:
		try:
			f = open(fdir + '/' + txt)
			lines = f.readlines()
			matrix = []
			for line in lines:
				m = line.split(' ')
				time = m[0]



		finally:
			pass

def read_files():
	file_dir = './txt_files/'
	read_text(file_dir)

read_files()