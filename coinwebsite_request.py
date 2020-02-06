import urllib.request

f = open("coin6.html", "wb") #wb = binary write

response = urllib.request.urlopen('https://coinmarketcap.com/')

html=response.read()

f.write (html)
# print (html)
f.close() #do not forget to close it



# import urllib.request
# import time
# for i in range (5):
# 	f = open("coinmarketcap"+str(i)+".html", "wb") #wb = binary write
# 	response = urllib.request.urlopen('https://coinmarketcap.com/')
# # print (response)
#     html=response.read()

#     f.write (html) #save the html file
# # print (html)
#     f.close() #do not forget to close it

# 	time.sleep (20)



# import urllib.request
# import time
# import datetime
# import os

# if not os.path.exists ("try1"): #check the name of the folder exists or not
#     os.mkdir ("try1") #creat a folder

# for i in range (5):
# 	current_time_stamp = datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
# 	# print(current_time_stamp)
# 	f = open("coinmarketcap"+current_time_stamp+".html", "wb") #everytime the file name is different
# 	response = urllib.request.urlopen('https://coinmarketcap.com/') # for loop of the multiple page scrapping could be added here
#     html=response.read()

#     f.write (html)

#     f.close() #do not forget to close it
# 	time.sleep (300)
# 	# time.sleep (100+random) # make it like human



# from bs4 import BeautifulSoup

# f= open("coin1.html", 'r')
# soup=BeautifulSoup(f.read(), "html.parser")

# f.close()


# print (soup)


# for loop of the multiple page scrapping
# import urllib.request
# import time
# import datetime
# import os

# if not os.path.exists ("try1"): #check the name of the folder exists or not
#     os.mkdir ("try1") #creat a folder

# for i in range (5):
# 	current_time_stamp = datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
# 	# print(current_time_stamp)
# 	f = open("coinmarketcap"+current_time_stamp+".html", "wb") #everytime the file name is different
# 	response = urllib.request.urlopen('https://coinmarketcap.com/')
#     html=response.read()

#     f.write (html)

#     f.close() #do not forget to close it
# 	time.sleep (300)
# 	# time.sleep (100+random) # make it like human


38:try1 xzw$ git config --global user.name "Chungsang Tom Lam"
38:try1 xzw$ global user.name "xzwfc"
-bash: global: command not found
38:try1 xzw$ git init
Initialized empty Git repository in /Users/xzw/ml/econ807/try1/.git/
38:try1 xzw$ touch .gitignore
38:try1 xzw$ git add.
git: 'add.' is not a git command. See 'git --help'.

The most similar command is
	add
38:try1 xzw$ git commit -m"init"
On branch master

Initial commit

Untracked files:
	.Rhistory
	.gitignore
	1.txt
	b.md
	c.md
	classnotes1.md
	classpython.py
	classpython2.py
	coin1.html
	coin2.html
	coin3.html
	coin4.html
	coin5.html
	coin6.html
	coinmarketcap.html
	coinwebsite_parse.py
	coinwebsite_request.py
	hello.py
	parse.py

nothing added to commit but untracked files present
38:try1 xzw$ git config --global user.name "Chungsang Tom Lam"xzwfc"
> git init
> git add.
> git remote add origin git @git remote add origin https://github.com/xzwfc/coinmarket001.git
> git remote add origin https://github.com/xzwfc/coinmarket001.git
> git push -u origin master
> 













