import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(20, 8))
    plt.scatter(data=df,
                x="Year",
                y="CSIRO Adjusted Sea Level"
              );
    
    # Create first line of best fit
    # Get slope and intercept from linregress() to plot y_pred = intercept + slope * x_pred
    lr = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    intercept, slope = lr.intercept, lr.slope
    x_pred = pd.Series(year for year in range(1880, 2051))
    y_pred = intercept + slope * x_pred
    plt.plot(x_pred, y_pred, color='red', linestyle='--', linewidth=2);

    # Create second line of best fit
    # Get slope and intercept from linregress() to plot y_pred = intercept + slope * x_pred
    df_recent = df[df["Year"] >= 2000]
    lr_recent = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    intercept, slope = lr_recent.intercept, lr_recent.slope
    x_pred = pd.Series(year for year in range(2000, 2051))
    y_pred = intercept + slope * x_pred
    plt.plot(x_pred, y_pred, color='black', linestyle='--', linewidth=2);

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level");
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()