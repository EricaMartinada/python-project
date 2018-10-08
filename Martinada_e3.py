# filename  : Martinada_e3.py
#author     : Erica Martinada
# description :  this is a python program
#                that computes and displays
#                the sum of each number squared
#               


#Prompt for input
data = input ("Enter a comma separated list of numbers")

#Compute sum of squares
total = sum ([float (k) **2 for k in data.split(",")])

#Print Result
print ("Sum of squares: {:,2f}".format(total)) 