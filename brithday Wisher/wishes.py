import pywhatkit
import pandas as pd
import datetime
import openpyxl as py

df =pd.read_excel('data.xlsx')
# print(df)
currnt_today = datetime.datetime.now().strftime(" %d -%m")
# print(today)
currnt_year = datetime.datetime.now().strftime(" %Y")
# print(year)
writeIND = []
for index, item in df.iterrows():
    # print(index ,item['Date'])
    brithday_date = item['Date'].strftime(" %d -%m")
    # print(brithday_date)
    brithday_year = str(item['Year'])
    print(brithday_year)
    Number = str(item['Number'])
    Message = str(item['Message'])
    if currnt_today == brithday_date and str(currnt_year) is not brithday_year :
            # pywhatkit.sendwhatmsg('+91'+(Number), Message, 21, 5)
            writeIND.append(index )
for i in writeIND:
    yr = df.loc[i,'Year']
    df.loc[i,'Year'] = str (yr) + ',' +str( currnt_year)
    print(df.loc[i,'Year'])

df.to_excel('data.xlsx', index= False)
# print(df)
