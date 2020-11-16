import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
sales=pd.read_csv("Freq.csv")
sales.head()
customers=sales[['names','frequency']]
customers.head()
myplot = sales_totals.plot(kind='bar')
