import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
#Ανοίγω το αρχείο σε ένα path και το μετατρέπω σε DataFrame
setYourPath = 'C:/Users/Constantine/.spyder-py3/finance_liquor_sales.csv'
df = pd.read_csv(setYourPath)
#Δημιουργώ μία στήλη με χρονολογία και κάνω extract, μόνο τον χρόνο από την ημερομηνία
df['Year'] = pd.to_datetime(df['date']).dt.strftime('%Y')
#Δημιουργώ τα DataFrames με την συγκεκριμένη πληροφορία που ζητά η άσκηση. Εύρος 2016-2019
d1 = df[(df['Year'] == '2016')]
d2 = df[(df['Year'] == '2017')]
d3 = df[(df['Year'] == '2018')]
d4 = df[(df['Year'] == '2019')]
#Ενώνω τα DataFrames σε ένα για να απεικονίσω τις ζητούμενες πληροφορίες
dd1 = pd.concat([d1,d2])
dd2 = pd.concat([d3,d4])
d = pd.concat([dd1,dd2])
#Δημιουργώ λίστες, όπου θα βάλω τις τιμές και τα ονόματα των items προς επεξεργασία και απεικόνιση
zcl = []
ptl = []

sl = []
stl = []
#Γεμίζω λίστες και τις μετατρέπω σε πίνακες και 1-D
zcl.append(d['zip_code'])
zcl = np.array(zcl)
zcl = zcl.flatten()
ptl.append(d['item_description'])
ptl = np.array(ptl)
ptl = ptl.flatten()

sl.append(d['sale_dollars'])
sl = np.array(sl)
sl = sl.flatten()
stl.append(d['store_name'])
stl = np.array(stl)
stl = stl.flatten()
#Απεικονίζω με Οριζόντιες μπάρες
plt.figure(figsize=(10,10))
style.use('ggplot')
plt.barh(ptl,zcl)
plt.title('Most Popular Item Per Zip Code by Bar Visual')
plt.xlabel('Zip Code')
plt.ylabel('Item')
plt.grid()
plt.show()
#Απεικονίζω με Scatter
plt.figure(figsize=(10,10))
style.use('ggplot')
plt.scatter(zcl,ptl)
plt.title('Most Popular Item Per Zip Code by Scatter Visual')
plt.xlabel('Zip Code')
plt.ylabel('Item')
plt.grid()
plt.show()
#Απεικονίζω με Pie Chart
plt.figure(figsize=(10,10))
plt.pie(sl,labels=stl,autopct='%1.1f%%',shadow=True,startangle=90)
plt.title('Percentage Of Sales Per Store Using Pie Chart')
plt.axis('equal')
plt.show()
