#Librerias para moverse dentro de carpetas del sistema operativo
import sys
import os
import requests
import string
import csv
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import urllib
import urllib.request
import tkinter as tk
from PIL import Image, ImageTk
import re
import time

memeData = []

with open('memegenerator.csv', 'r', encoding='utf-16') as memedata:
    reader = csv.DictReader(memedata, delimiter='\t')
    for row in reader:
        memeData.append(row)

print('Total records in the memeData list:',len(memeData))

## set up the counter again, and create a dictionary for the types
memeCount = 52945
types = list()
counts = dict()

print('Here\'s the types and IDs from each row scanned:')
for record in memeData: 
    if memeCount > 57611:
        break
    memeCount = memeCount + 1
    memeID = record['Meme ID']
    kind = record['Base Meme Name']
    #uncomment the next row if you want to see the output as the loop goes through each row
    print(memeCount,kind,memeID)

    ## Using the counts dictionary, above, see if the type is already in the dictionary, 
    ## if not noted, add it, if it is noted, increase the count...
    if re.findall("[\/:*?<>|]", kind):
        continue
    else:
        target_dir = './templates/'+ kind +'/'
        #print(target_dir)
        ## Now add kind to the list of types
        if not os.path.exists(target_dir):
            os.mkdir(target_dir)
            url_imagen = record['Archived URL'] # El link de la imagen
            nombre_local_imagen = str(memeCount) + ".jpg" # El nombre con el que queremos guardarla
            try:
                imagen = requests.get(url_imagen, timeout=30).content
            except requests.ConnectionError as e:
                print("OOPS!! Connection Error. Make sure you are connected to Internet. Technical Details given below.\n")
                print(str(e))
                continue
            except requests.Timeout as e:
                print("OOPS!! Timeout Error")
                print(str(e))
                continue
            except requests.RequestException as e:
                print("OOPS!! General Error")
                print(str(e))
                continue
            except KeyboardInterrupt:
                print("Someone closed the program")

            with open(target_dir + nombre_local_imagen, 'wb') as handler:
                handler.write(imagen)
            continue
        else:
            url_imagen = record['Archived URL'] # El link de la imagen
            nombre_local_imagen = str(memeCount) + ".jpg" # El nombre con el que queremos guardarlarrrrrrrrreewq    |
            try:
                imagen = requests.get(url_imagen, timeout=30).content
            except requests.ConnectionError as e:
                print("OOPS!! Connection Error. Make sure you are connected to Internet. Technical Details given below.\n")
                print(str(e))            
                continue
            except requests.Timeout as e:
                print("OOPS!! Timeout Error")
                print(str(e))
                continue
            except requests.RequestException as e:
                print("OOPS!! General Error")
                print(str(e))
                continue
            except KeyboardInterrupt:
                print("Someone closed the program")
            with open(target_dir + nombre_local_imagen, 'wb') as handler:
                handler.write(imagen)
            continue