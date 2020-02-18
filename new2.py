import urllib.request
import time
import datetime
import os
import random

if not os.path.exists ("parsed_files"): #check the name of the folder exists or not
    os.mkdir ("parsed_files") #creat a folder

for i in range (3):
	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
	print(current_time_stamp)
	f = open("coinmarketcap"+current_time_stamp+".html", "wb") #everytime the file name is different
	response = urllib.request.urlopen('https://coinmarketcap.com/') # for loop of the multiple page scrapping could be added here
	html=response.read()
	f.write (html)

	f.close() #do not forget to close it
	# time.sleep (300)
	timedelay = random.randrange(10,30)
	time.sleep (timedelay) # make it like human

	#command c to stop the linux process