import numpy as np
import tensorflow as tf
import re
import time
import investpy
import pandas as pd
import matplotlib.pyplot as plt
import math
from sklearn.preprocessing import MinMaxScaler

index = 's&P 500'

#SP500
df = investpy.get_index_recent_data(index=index,
                                    country='United States')

#df.drop(['Currency','Volume'] , axis=1 , inplace=True)      
#Drop not need
df.drop('Currency',axis=1,inplace=True)

#Plot the mean
#Featch the trend
df['Close'].plot(figsize=(16,8), linewidth=5, fontsize=10)
plt.title('Close',fontsize=20)
plt.savefig('IndexPlot/ ' + index + ' Close.png')

close = df[['Close']]
close.rolling(12).mean().plot(figsize=(16,8), linewidth=5, fontsize=10)
plt.title('Close Rolling Mean',fontsize=20)
plt.savefig('IndexPlot/ ' + index +' Close Rolling 12.png')


open_price = df[['Open']]
open_price.rolling(12).mean().plot(figsize=(16,8), linewidth=5, fontsize=10)
plt.title('Open Rolling Mean',fontsize=20)
plt.savefig('IndexPlot/ ' + index +' Open.png')

df_rm = pd.concat([close.rolling(12).mean(), open_price.rolling(12).mean()], axis=1)
df_rm.plot(figsize=(16,8), linewidth=5, fontsize=20);
plt.title('Close And Trend Rolling Mean',fontsize=20)
plt.savefig('IndexPlot/ ' + index + 'Concat Rolling 12.png')

#Take The Trend from data
import statsmodels.api as sm
df['Close'].plot(figsize=(16,8),fontsize=18)
plt.title('Close' , fontsize=20)
jpy_open , jpy_close  = sm.tsa.filters.hpfilter(df['Close'])

df['trend'] = jpy_close
df[['Close' , 'trend']].plot(figsize=(16,8),fontsize=18);
plt.title('SP500 Daily Trend' , fontsize=20)
plt.savefig('IndexPlot/ ' + index +' Close Trend.png')


#Visulalize the closing and trend 
#Data
plt.figure(figsize=(16,8))
plt.title('SP500 Price History',fontsize=18)
plt.plot(df)
plt.xlabel('Date' , fontsize=18)
plt.ylabel('SP500 Price USD ($)' ,fontsize=18)
#plt.set_title('USD/JPY Daily Trend')
plt.show()
plt.savefig('IndexPlot/ ' + index + 'Price History.png')

#Trend
plt.figure(figsize=(16,8))
plt.title(index + 'Trend Price History' ,fontsize=18)
plt.plot(df['trend'])
plt.xlabel('Date' , fontsize=18)
plt.ylabel('trend Price USD ($)' ,fontsize=18)
plt.show()
plt.savefig('IndexPlot/ ' + index + 'Trend Price History.png')

df.to_csv('Data/' + index + 'Daily Trend.csv')