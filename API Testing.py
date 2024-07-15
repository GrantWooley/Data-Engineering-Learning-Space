#Requests library most common Python library used for interacting with APIS
#Loading/Importing
#Packages = ["requests","psycopg2","matplotlib","numpy","pandas","scipy","mysql.connector"]
#print(Packages)
#print(dir())
#import requests
#for x in Packages:
  #  Result = "Package " + x + "has been loaded." 
  #  import x
   # #print(dir())
   # print(Result)

myfirstdataset = {
    'cars': ["BMW","Volvo","Ford"],
    'passing':[3,7,2]
}

print(myfirstdataset)

import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)
print(myvar["x"])