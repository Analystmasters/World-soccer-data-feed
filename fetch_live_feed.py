
# coding: utf-8

# In[2]:


import pandas as pd
from datetime import datetime, timezone
import numpy as np # linear algebra
import csv
import pytz
import requests
import io
import math

CSV_URL = 'https://s3.amazonaws.com/analyst-masters/amasters.csv'
data = requests.get(CSV_URL)

with open('out.csv', 'w') as f:
    reader = csv.reader(data.text.splitlines())
        
df = pd.read_csv(io.StringIO(data.text))   

M=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

def what_is_it(datin):
    if (str(datin[20]) != "nan" and str(datin[48]) != "nan"):
        Dtype='Mode 1'
        print("- It is {dtype}, to kick off on {wday}, Date: {day}/{month}, Time: {hh}:{mm}, CET, The match is between {t1} and {t2}.\n{vhome} experts voted for home win, {vdraw} voted for draw and {vaway} ones for Away win. \nIn total {tbetter} placed bets where {phome}% bet on home, {pdraw}% bet on draw and {paway}% chose to bet on away. \n Samples of Category I data: They are ranked as {R1} and {R2} among {tteams}\n They played {GP1} and {GP2} matches and scored {P1} and {P2} points respectively while the highest and lowest points in the league are {Pmax} and {Pmin}. \nPrioir probability of home, draw and away is {Ph}%, {Pd}% and {Pa}%. \nMore Category I data is availble from Col 16 to 36 \nSamples of Category II data: On overage, they scored {TG} and {TH} before Full-time and Half-Time in their last 6 head to head matches. More Category II data is availble from Col 39 to 54 \n".format(dtype=Dtype,wday=datin[3],day=int(datin[4]),month=int(datin[5]),hh=int(datin[7]),mm=int(datin[8]),        t1=datin[13],t2=datin[14],tbetter=int(datin[9]),vhome=int(datin[0]),vdraw=int(datin[1]),vaway=int(datin[2]),phome=int(datin[10]),pdraw=int(datin[11]),paway=int(datin[12]),         R1=int(datin[15]),R2=int(datin[16]),tteams=int(datin[9]),GP1=int(datin[18]),GP2=int(datin[19]),P1=int(datin[20]),P2=int(datin[21]),Pmax=int(datin[22]),Pmin=int(datin[23]),        Ph=int(100*datin[51]**(-1)),Pd=int(100*datin[52]**(-1)),Pa=int(100*datin[53]**(-1)),TG=datin[47],TH=datin[48]))
        
    elif str(datin[20]) != "nan" and str(datin[48]) == "nan":
        Dtype='Mode 2'
        print("- It is {dtype}, to kick off on {wday}, Date: {day}/{month}, Time: {hh}:{mm}, CET, The match is between {t1} and {t2}.\n{vhome} experts voted for home win, {vdraw} voted for draw and {vaway} ones for Away win. \nIn total {tbetter} placed bets where {phome}% bet on home, {pdraw}% bet on draw and {paway}% chose to bet on away. \n Samples of Category I data: They are ranked as {R1} and {R2} among {tteams}\n They played {GP1} and {GP2} matches and scored {P1} and {P2} points respectively while the highest and lowest points in the league are {Pmax} and {Pmin}. \n Prioir probability of home, draw and away is {Ph}%, {Pd}% and {Pa}%. \nMore Category I data is availble from Col 16 to 36 \nNo Category II data is availble \n".format(dtype=Dtype,wday=datin[3],day=int(datin[4]),month=int(datin[5]),hh=int(datin[7]),mm=int(datin[8]),        t1=datin[13],t2=datin[14],tbetter=int(datin[9]),vhome=int(datin[0]),vdraw=int(datin[1]),vaway=int(datin[2]),phome=int(datin[10]),pdraw=int(datin[11]),paway=int(datin[12]),         R1=int(datin[15]),R2=int(datin[16]),tteams=int(datin[9]),GP1=int(datin[18]),GP2=int(datin[19]),P1=int(datin[20]),P2=int(datin[21]),Pmax=int(datin[22]),Pmin=int(datin[23]),        Ph=int(100*datin[51]**(-1)),Pd=int(100*datin[52]**(-1)),Pa=int(100*datin[53]**(-1))))
    elif str(datin[20]) == "nan" and str(datin[48]) != "nan":
        Dtype='Mode 3'
        print("- It is {dtype}, to kick off on {wday}, Date: {day}/{month}, Time: {hh}:{mm}, CET, The match is between {t1} and {t2}.\n{vhome} experts voted for home win, {vdraw} voted for draw and {vaway} ones for Away win. \nIn total {tbetter} placed bets where {phome}% bet on home, {pdraw}% bet on draw and {paway}% chose to bet on away. \nNo Category I data is availble \nPrioir probability of home, draw and away is {Ph}%, {Pd}% and {Pa}%. \nSamples of Category II data: On overage, they scored {TG} and {TH} before Full-time and Half-Time in their last 6 head to head matches. \nMore Category II data is availble from Col 39 to 54 \n".format(dtype=Dtype,wday=datin[3],day=int(datin[4]),month=int(datin[5]),hh=int(datin[7]),mm=int(datin[8]),    t1=datin[13],t2=datin[14],tbetter=int(datin[9]),vhome=int(datin[0]),vdraw=int(datin[1]),vaway=int(datin[2]),phome=int(datin[10]),pdraw=int(datin[11]),paway=int(datin[12]),     Ph=int(100*datin[51]**(-1)),Pd=int(100*datin[52]**(-1)),Pa=int(100*datin[53]**(-1)),TG=datin[47],TH=datin[48]))
    elif str(datin[20]) == 'nan' and str(datin[48]) == "nan":
        Dtype='Mode 4'
        print("- It is {dtype}, to kick off on {wday}, Date: {day}/{month}, Time: {hh}:{mm}, CET, The match is between {t1} and {t2}.\n{vhome} experts voted for home win, {vdraw} voted for draw and {vaway} ones for Away win. \n In total {tbetter} placed bets where {phome}% bet on home, {pdraw}% bet on draw and {paway}% chose to bet on away. \nPrioir probability of home, draw and away is {Ph}%, {Pd}% and {Pa}%. \nNo Category I & II data is availble \n".format(dtype=Dtype,wday=datin[3],day=int(datin[4]),month=int(datin[5]),hh=int(datin[7]),mm=int(datin[8]),    t1=datin[13],t2=datin[14],tbetter=int(datin[9]),vhome=int(datin[0]),vdraw=int(datin[1]),vaway=int(datin[2]),phome=int(datin[10]),pdraw=int(datin[11]),paway=int(datin[12]),    Ph=int(100*datin[51]**(-1)),Pd=int(100*datin[52]**(-1)),Pa=int(100*datin[53]**(-1))))
        

tz = pytz.timezone('Europe/Berlin')
berlin_now = datetime.now(tz)
CET=berlin_now.strftime("%A , %m/%d/%Y, %H:%M:%S")

# explaining the first 2 upcoming matches
matches=2

for t in range(0,min(matches+1,len (df))):
    if t==0:
        print("Data was lastly saved on {} Date: {}/{}, at {}:{} CET , current CET time is: {} \n".format(df.iloc[t,3],int(df.iloc[t,4]),M[int(df.iloc[t,5]-1)],int(df.iloc[t,7]),int(df.iloc[t,8]),CET))
    else:
        if str(df.iloc[t,13]) != "nan":
            what_is_it(df.iloc[t,].values)


