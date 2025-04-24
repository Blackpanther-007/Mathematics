import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
import pandas as pd

#Data import and cleaning done
df = pd.read_csv('signal.inp', header=None, sep='\s+')
df.dropna(axis=1, inplace=True)
df.drop(index=0, inplace=True)
df.columns = ['time', 'signal_value']
time = df['time']
signal_values = df['signal_value']

fig, ax = plt.subplots()
ax.set_xlabel('Time')
ax.plot(time, signal_values, color='red')
# ax.scatter(time, signal_values)
plt.show()

