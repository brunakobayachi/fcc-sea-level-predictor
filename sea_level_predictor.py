import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', float_precision='high')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    linreg = linregress(x, y)
    m = linreg.slope
    b = linreg.intercept
    plt.plot(range(1880, 2051), m * range(1880, 2051) + b)

    # Create second line of best fit
    df2000 = df[df['Year'] >=2000]
    x = df2000['Year']
    y = df2000['CSIRO Adjusted Sea Level']
    linreg = linregress(x,y)
    m = linreg.slope
    b = linreg.intercept
    plt.plot(range(2000, 2051), m*range(2000, 2051) + b)

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()