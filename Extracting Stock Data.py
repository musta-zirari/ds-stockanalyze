#install both libraries
!pip install yfinance==0.2.4
!pip install pandas==1.3.3

#Using the Ticker module we can create an object that will allow us to access functions to extract data
#Ticker symbol for Apple company is: AAPL
apple = yf.Ticker("AAPL")

#you can filter and download the data using this:
#data = yf.download("AAPL", start="2017-01-01", end="2017-04-30")
#for my case I already have an apple.json file so I load it only
import json
with open('apple.json') as json_file:
    apple_info = json.load(json_file)
apple_info

#extracting share price and priting the top 5 rows.
apple_share_price_data = apple.history(period="max")
apple_share_price_data.head()

#we can plot the Open price against the Date
apple_share_price_data.plot(x="Date", y="Open")

#Extracting dividends,
#Dividends are the distribution of a companys profits to shareholders. In this case they are defined as an amount of money returned per share an investor owns
apple.dividends

#we can flot dividends overtime
apple.dividends.plot()
