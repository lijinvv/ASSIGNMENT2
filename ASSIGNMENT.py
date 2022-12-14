# importing the packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# function for transposing the data from the world bank csv file


def trans_file(file_data):
    """
    To read and sort the file and to transpose the data
    file_data: name of the file
    """
    datas = pd.read_csv(file_data)
    datas = datas.transpose()
    datas.columns = datas.iloc[0]
    datas = datas.iloc[47:57]
    return datas

# Line plot of Arable land and forest land


def line_plot(data_line, years, countriz, lab1, lab2, head, img):
    """
    data_line : name of the file
    years : years mentioned in the graph
    countriz : countries plotted in the graph
    lab1 : label x axis
    lab2 : label y axis
    head : title of the line plot
    img : destination of figure
    """

    plt.figure(figsize=(15, 10))
    plt.plot(years, data_line[countriz], label=countriz)
    plt.xlabel(lab1, fontsize=10)  # adding label to x axis and y axis
    plt.ylabel(lab2, fontsize=10)
    plt.title(head, fontsize=25, color="red")
    plt.legend(loc="upper right", fontsize=10)
    plt.savefig(img)
    plt.show()
    return


# Filtering data for bar plot

def filter_bar_data(data):
    """defining function to filter data
    data : name of the file"""
    filter_data = data[['Country Name', 'Indicator Name',
                        '1990', '1994', '1996', '2000', '2010', '2014']]
    filter_data = filter_data[(filter_data["Country Name"] == "Thailand") |
                              (filter_data["Country Name"] == "Peru") |
                              (filter_data["Country Name"] == "Chile") |
                              (filter_data["Country Name"] == "Bangladesh") |
                              (filter_data["Country Name"] == "Iceland") |
                              (filter_data["Country Name"] == "Bahrain")]
    return filter_data


# bar plot of Population growth and fossil fuel energy  consumption

def bar_plot(data_bar, lab1, lab2, title, img):
    """
    data_bar : name of the data
    lab1 : label x axis
    lab2 : label y axis
    title : title of bar plot
    img: destination of figure
    """

    plt.figure(figsize=(28, 20))
    sub = plt.subplot(1, 1, 1)
    arr = np.arange(6)
    width = 0.2

    # plotting the bar graph for the year 1990,1994 and 2014

    bar1 = sub.bar(
        arr, data_bar["1990"], width, label=1990, color="teal")
    bar2 = sub.bar(
        arr+width, data_bar["1994"], width, label=1994, color="magenta")
    bar3 = sub.bar(
        arr+width*2, data_bar["2014"], width, label=2014, color="gold")

    # giving labels to x axis and y axis

    sub.set_xlabel(lab1, fontsize=20)
    sub.set_ylabel(lab2, fontsize=20)
    sub.set_title(title, fontsize=40)
    sub.set_xticks(arr, countriz, fontsize=20, rotation=90)
    sub.legend(loc="upper right", fontsize=20)

    sub.bar_label(bar1, padding=2, rotation=90, fontsize=18)
    sub.bar_label(bar2, padding=2, rotation=90, fontsize=18)
    sub.bar_label(bar3, padding=2, rotation=90, fontsize=18)
    plt.savefig(img)
    plt.show()
    return


def average_fossil_consumption(data_mean):
    """ 
    the function to find the mean of foosil fuel
    data_mean : name of the file
    """

    print("The mean of fossil fuel consumption in the year of 2012 is :",
          np.mean(data_mean))
    return


# filter countries for data

countriz = ['Thailand', 'Peru', 'Chile', 'Bangladesh', 'Iceland', 'Bahrain']


"""
Assigning the indicators to the variables
"""

arable_land = trans_file("arable land.csv")
forest_land = trans_file("forest area.csv")

fossil = pd.read_csv("fossil fuels.csv")
fossil = filter_bar_data(fossil)

population = pd.read_csv("population growth.csv")
population = filter_bar_data(population)


"""invoking functions for plotting line graph, bar graph and to find the average"""

# invoking line plot function

line_plot(arable_land, arable_land.index, countriz, "years",
          "change in arable land", "ARABLE LAND", "arable.png")
line_plot(forest_land, forest_land.index, countriz, "years",
          "change in forest land", "FOREST LAND", "forest.png")


# invoking bar plot

bar_plot(fossil, "Countries", "fossil consumption",
         "Fossil fuel energy consumption", "fossil.png")
bar_plot(population, "Countries", "Population growth",
         "The population growth", "population.png")

# invoking the function to find average

average_fossil_consumption(fossil["1996"])
