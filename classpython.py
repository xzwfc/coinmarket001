# def determine_big_or_small (variable_name, variable_value):
# 	print (variable_name, ":", variable_value)
# 	if (variable_value>)



#if conditional statement

# x =-3
# if x< 0:
# 	print ("X is negative.")
# elif x>0:
# 	print ("X is positive")
# elif x==0:
# 	print ("X is zero")
# else:
# 	print ("there is an error")

# write elif as many as possible

# a=10
# print (a)

# b=10.0
# print (b)

x = 2.2 * 4.0
y = 8.8
# print (x==y)
import math
print (math.isclose(x,y))

# c=2.2 *3.4
# d=3.4 *2.2
# import math
# if (math.isclose(c, d)):
# 	print ("equal")
# else:
# 	print ("not equal")


#for loop
# animals = ['cat','dog','turtle','bird']
# print (animals)

# for ani in animals:
# 	print ("I love", ani)
	# print ("and")

# n=[1,2,3,4,5,6,7,8,9,10]
# for i in n:
# 	print((i*2)**2)

# numbers =range(1, 11)
# for i in numbers:
# 	print((i*2)**2)

#conditional while loop
# def fib (n): #fib sequence
# 	result =[]
# 	a, b=0, 1
# 	while a<n: #keep doing it while a<n it will end until a>n
# 		result.append (a)
# 		a, b =b, a+b
# 	return result
# print(fib(1000))

	# pass #function do nothing
	# command c is shortcut for breaking the infinite loop

#numpy
import numpy as np
data = np.arange (20).reshape(4,5) #columns are transposed as rows
print (data)

#pandas
import numpy as np
import pandas as pd
n=100
t=pd.date_range ("20200101", periods=n)
print (t)

df =pd.DataFrame (np.random.randn(n, 10), index=t, columns=list("ABCDEFGHIJ"))
print (df)

# print (df["A"])

# print (df.head())
print (df.describe())
print (df[0:3])
print (df[df.C>0])

