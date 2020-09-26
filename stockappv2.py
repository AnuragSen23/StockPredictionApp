import pandas_datareader.data as web
import pandas as pd
import streamlit as st
from PIL import Image
import os

#image file "stockcoin.jpg"
image = Image.open(os.path.join('stockcoin.jpg'))
st.image(image)

st.title('Stock Market Price Prediction App')
'-------------------------------------------------------------'
st.write("""
### This interface is used for catagorizing Stock data on a period of 10days. ###
### The Stock Tabular representation on **Closing Price** and **Volume**
""")
#stocksymbol or the tickersymbol of the company to be entered
stockSymbol = st.text_input("Enter the Stock Code of company","GOOGL")

st.write("""
### **StockSymbol entered is:** """, stockSymbol)

#starting date of the stock session
start_date= st.text_input("Enter Starting date: ","2020-09-10")
st.write("""
### **Starting date entered is:** """, start_date)

#ending date of the stock session
end_date= st.text_input("Enter Ending date: ","2020-10-03")
st.write("""
### **Ending date entered is:**""", end_date)

#data is retrieved from the web using the input parameters and yahoofinance.
data= web.DataReader(stockSymbol,'yahoo', start_date, end_date)

st.title('Stock Market Data ' + "of " + stockSymbol )

'-------------------------------------------------------------'

#graphical representation of the Closing price of the stock along time.
st.write("""
### **Closing Price of Stock over the time**
""")
st.line_chart(data["Close"])

#graphical representation of the highest price of the stock sold along time.
st.write("""
### **Highest value price of Stock sold over the time**
""")
st.line_chart(data["High"])

#tabular representation of the data paramenters retrieved from yahoofinance.
data


st.title('Data Prediction')
'---------------------------------------------------------'

#for the estimation of the mean value, day count is taken as 10.
avg= 10

st.write("""
### ** Estimated Prediction is for 10** days""")

#the average or mean statistical value is calculated using data over time.
#average closing value is calculated using the rolling function
#window describes the estimated time period or the mean time period
#min_periods describes the statistical frame or window capacity at a time.
data["avg_close"] = data['Close'].rolling(window = int(avg),min_periods=1).mean()

st.write("""
### **Prediction Plot of Closing Price of the Stock on the Moving Average in comparision to the actual Closing Price: ** """)

#graphical and tabular representation of average closing price over time
st.line_chart(data[["avg_close","Close"]])
data["avg_close"]


#the average or mean statistical value is calculated using data over time.
#average highest value is calculated using the rolling function
#window describes the estimated time period or the mean time period
#min_periods describes the statistical frame or window capacity at a time.
data["avg_High"] = data['High'].rolling(window = int(avg),min_periods=1).mean()


st.write("""
### **Prediction Plot of Highest price of the Stock sold on the Moving Average in comparision to the actual Highest price: ** """)


#graphical and tabular representation of average high price of stock over time
st.line_chart(data[["avg_High","High"]])
data["avg_High"]


st.title("Reference")
'------------------------------------------------------'
'All Stock data is retrieved from Google Stock Database based on Yahoo Finance'
'Enter the StockSymbol and execution date accurately'

st.write("""
### **Analysed and Designed by PS05_BeastCoders** """)
'* Tushar Saxena (@HS108_PS5_tushar) [Leader]'
'* Anurag Sen (@HS108_PS5_anurag)'
'* Tanmay Padhi (@HS108_PS5_tanmay)'
'* Arindam Datta (@HS108_PS5_arindam)'
