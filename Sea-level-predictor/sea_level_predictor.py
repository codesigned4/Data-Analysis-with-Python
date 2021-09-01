import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # Read data from file
  df=pd.read_csv("epa-sea-level.csv")
  df.plot.scatter(x='Year', y="CSIRO Adjusted Sea Level",alpha=0.5,label="original data")
  years = np.arange(1880, 2051)

    # First best line
  slope, intercept, r, p, e  = linregress(df['Year'], df["CSIRO Adjusted Sea Level"])
  plt.plot(years, intercept + slope*years, 'r', label='best fit line')

    # Second best line after year 2000
  recent = df[df['Year'] >= 2000]
  slope, intercept, r, p, e  = linregress(recent['Year'], recent["CSIRO Adjusted Sea Level"])

  years2 = np.arange(2000, 2051)
  plt.plot(years2, intercept + slope*years2, 'g', label='second best fit line')

  plt.title("Rise in Sea Level")
  plt.xlabel("Year")
  plt.ylabel("Sea Level (inches)")
  plt.legend()

  plt.savefig('sea_level_plot.png')
  return plt.gca()
  #plt.show()

#draw_plot()   
