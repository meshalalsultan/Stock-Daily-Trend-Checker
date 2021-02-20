# Stock Daily Trend Checker

## The Trend is the king ,  Do not trade againest the trend , and many more WARNINGS from the trend wave .

In stock market if you want the best way to lose any trade , trade the other side of trend .

The trend side can hert our trading account or give us a good step to beet the market in our posotion .

I use python to git the Daily Trend for Stock and Index .

### Get the data :

i use investpy lib to get the data 

### Plot and dataframe :
- I use pandas to get the data within dataframe
- use matplotlib to plot the data 
- statsmodels to get the trend 

### The trend :
- drop the Currancy columns . becouse i not need it 
- plot the Open & Close price to find the price range .
- plot the Close price to get idea about close trend line .
- get the roolingmean for past (12) day on the open and close .
- Concat the rolling mean of open and close to get the liner trend .
- use statsmodels hpfilter on close price  to get the trend 

### The HP filter removes a smooth trend, T, from the data x. by solving

min sum((x[t] - T[t])**2 + lamb*((T[t+1] - T[t]) - (T[t] - T[t-1]))**2)

