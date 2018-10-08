# filename  : Martinada_e1.py
#author     : Erica Martinada
# description :  this is a python program
#                that classifies a tropical
#               cyclone wrt its sustained winds
#               

import sys
#Convert str sustained_winds to float
sustained_winds = sys.argv [1]

#Compare sustained_winds to preset range and display proper classification  
sustained_winds = float(sustained_winds)

if sustained_winds >= 220.0:
    print ("Super Typhoon")
elif sustained_winds >= 118.0:
    print ("Typhoon")
elif sustained_winds >= 89.0:
    print ("Severe Tropical Storm")
elif sustained_winds >= 62.0:
    print ("Tropical Storm")
else:
    print ("I do not know")