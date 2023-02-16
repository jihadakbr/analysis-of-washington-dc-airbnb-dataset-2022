## for data
import numpy as np
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

## for plotting
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns


###############################################################################
###############################################################################


def filter_outliers(data, column):
    q1 = data[column].quantile(0.25)
    q3 = data[column].quantile(0.75)
    upper_limit = q3 + 1.5 * (q3-q1)
    lower_limit = q1 - 1.5 * (q3-q1)

    data = data[data[column] > lower_limit]
    data = data[data[column] < upper_limit]
    
    return data

def outliers_graph(data, col1):
    plt.figure(figsize=(12, 4))
    sns.set_style("whitegrid")
    custom_palette = sns.color_palette("muted")
    sns.boxplot(y=data[col1], color=custom_palette[0])  
    plt.ylabel("Price", fontsize=14)
    plt.grid(False)
    plt.gca().spines["right"].set_visible(False)
    plt.gca().spines["top"].set_visible(False)
    plt.show()