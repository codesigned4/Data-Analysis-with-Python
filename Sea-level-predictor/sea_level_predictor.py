import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
   df=pd.read_csv("epa-sea-level.csv")
   yearData=np.array(list(df["Year"]))
   AdjustedSeaLevel=np.array(list(df["CSIRO Adjusted Sea Level"]))
   
   # Create scatter plot
   plt.scatter(yearData,AdjustedSeaLevel,alpha=0.5,label="original data")   
    # Create first line of best fit
   slope, intercept, r, p, se = linregress(yearData, AdjustedSeaLevel)
   #plt.plot(yearData, AdjustedSeaLevel, 'o', label='original data')
  
   plt.plot(np.linspace(1880,2050,171), intercept + slope*np.linspace(1880,2050,171), 'r', label='fitted line')
   
    # Create second line of best fit
   df_2000 = df[df['Year'] >= 2000]

   np.linspace(2000,2050,50)
   lineB = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
   xB = np.arange(2000,2050,1)
   yB = xB*lineB.slope + lineB.intercept

   plt.plot(xB,yB) 
   
  
   plt.legend()

    # Add labels and title
   plt.title('Rise in Sea Level')
   plt.xlabel('Year')
   plt.ylabel('Sea Level (inches)')

    
    # Save plot and return data for testing (DO NOT MODIFY)
   plt.savefig('sea_level_plot.png')
   return plt.gca()


