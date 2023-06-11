import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', parse_dates=True)

    # Create scatter plot
    fig = plt.figure(figsize=(20,15))
    x_axis = df['Year']
    y_axis = df['CSIRO Adjusted Sea Level']
    scatter_plot = plt.scatter(x=x_axis, y=y_axis)

    # Create first line of best fit
    lin = linregress(x=x_axis, y=y_axis)
    slope, intercept = lin.slope, lin.intercept
    x_line = np.arange(1880, 2051)
    y_line = slope * x_line + intercept
    plt.plot(x_line, y_line, color='red')
    plt.xlim(1870, 2060)

    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    x_axis = df_2000['Year']
    y_axis = df_2000['CSIRO Adjusted Sea Level']
    lin_2000 = linregress(x=x_axis, y=y_axis)
    slope_2000, intercept_2000 = lin_2000.slope, lin_2000.intercept
    x_line_2000 = np.arange(2000, 2051)
    y_line_2000 = slope_2000 * x_line_2000 + intercept_2000
    plt.plot(x_line_2000, y_line_2000, color='purple')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year', fontsize=16)
    plt.ylabel('Sea Level (inches)', fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
