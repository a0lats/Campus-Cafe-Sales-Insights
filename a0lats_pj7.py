#Author: Adeoluwa (Ade) Olateru-Olagbegi
#Project: Campus Café Sales Insights
#Date: 10/04/2025
#Description: this program analyzes daily café sales data to find top-selling items and busiest hours.
#it uses pandas for data cleaning and matplotlib for visualization, helping management understand sales patterns.

import pandas as pd
import matplotlib.pyplot as plt

#load dataset
import os
data=pd.read_csv(os.path.join(os.path.dirname(__file__),"cafe_sales.csv"))

#preview first 5 rows
print(data.head())

#convert time column to datetime
data['time']=pd.to_datetime(data['time'],format='%H:%M')

#extract hour from time
data['hour']=data['time'].dt.hour

#find top 5 best-selling items
top_items=data['item'].value_counts().head(5)
print("top 5 best-selling items:")
print(top_items)

#plot top-selling items
top_items.plot(kind='bar',title='top 5 best-selling items',xlabel='item',ylabel='units sold')
plt.tight_layout()
plt.show()

#calculate total sales by hour
hourly_sales=data.groupby('hour')['total'].sum()

#plot hourly sales trend
hourly_sales.plot(kind='line',marker='o',title='sales by hour',xlabel='hour of day',ylabel='total sales ($)')
plt.grid(True)
plt.tight_layout()
plt.show()

#generate summary report
summary=pd.DataFrame({
    'top_items':top_items.index,
    'units_sold':top_items.values
})
summary.to_csv("cafe_sales_summary.csv",index=False)
print("summary report saved as cafe_sales_summary.csv")

#test place
#you can write custom code here to check data or test changes
#example: print total sales by item category
total_sales_by_item=data.groupby('item')['total'].sum().sort_values(ascending=False)
print(total_sales_by_item.head(5))