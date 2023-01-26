# importing the packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# function for transposing the data from the world bank csv file
def trans_file(file_data):
    """
    This function is to read and transpose the data with sorting the datas as required.
    The function returns two attribues, one with the orginal data and the other 
    with modified data
    file_data: name of the csv file.
    """
    datas = pd.read_csv(file_data)
    data_trans = datas.transpose()
    data_trans.columns = data_trans.iloc[0]
    data_trans = data_trans.iloc[50:63]
    return datas, data_trans


# Line plot of Arable land and forest land
def line_plot(data_line, years, countriz, lab1, lab2, head, img):
    """
    The function is to plot the line graph with the appropriate data.
    data_line : name of the file.
    years : years mentioned in the graph.
    countriz : countries plotted in the graph.
    lab1 : label x axis.
    lab2 : label y axis.
    head : title of the line plot.
    img : destination of figure to be saved.
    """

    plt.figure(figsize=(15, 10))
    plt.plot(years, data_line[countriz].values, label = countriz)
    plt.xlabel(lab1, fontsize=20)  # adding label to x axis and y axis
    plt.ylabel(lab2, fontsize=20)
    plt.title(head, fontsize=30, color="blue")
    plt.legend(loc="upper right", fontsize=10)
    plt.savefig(img)
    plt.show()
    return


# Filtering data for bar plot

def filter_bar_data(data):
    """
    defining function to filter data
    data : name of the file
    """
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

    plt.figure(figsize=(15, 9))
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

    sub.set_xlabel(lab1, fontsize=30)
    sub.set_ylabel(lab2, fontsize=30)
    sub.set_title(title, fontsize=75, color = "blue")
    sub.set_xticks(arr, countriz, fontsize=30, rotation=90)
    sub.legend(loc="upper right", fontsize=30)

    sub.bar_label(bar1, padding=2, rotation=90, fontsize=20)
    sub.bar_label(bar2, padding=2, rotation=90, fontsize=20)
    sub.bar_label(bar3, padding=2, rotation=90, fontsize=20)
    plt.savefig(img)
    plt.show()
    return


def mean_fossil_analysis(data_mean):
    """ 
    the function to find the mean of foosil fuel
    data_mean : name of the file
    """

    print("The mean of fossil fuel consumption in the year of 1994 is :",
          np.mean(data_mean))
    return

def pop_stdDevitn_analysis(data_std):
    """ 
    the function to find the mean of foosil fuel
    data_mean : name of the file
    """

    print("The Standard deviation of fossil fuel consumption in the year of 1996 is :",
          np.mean(data_std))



# filter countries for data

countriz = ['Thailand', 'Tonga', 'Chile', 'Bangladesh', 'Iceland', 'Bulgaria']


"""
Assigning the indicators to the variables
"""

arable_data, arable_land = trans_file("renewable.csv")
arable_land = arable_land.apply(pd.to_numeric)
forest_data, forest_land = trans_file("electricity.csv")

fossil = pd.read_csv("fossil fuels.csv")
fossil = filter_bar_data(fossil)

population = pd.read_csv("population growth.csv")
population = filter_bar_data(population)

trial = ['2006', '2007', '2008', '2009', '2010', '2011', '2012']
"""
invoking functions for plotting line graph, bar graph and to find the average
"""

# invoking line plot function


line_plot(arable_land, arable_land.index.values, countriz, "years",
          "change in arable land", "ARABLE LAND", "arable.png")
line_plot(forest_land, forest_land.index, countriz, "years",
          "change in forest land", "FOREST LAND", "forest.png")


# invoking bar plot

bar_plot(fossil, "Countries", "fossil consumption",
         "Fossil fuel energy consumption", "fossil.png")
bar_plot(population, "Countries", "Population growth",
         "The population growth", "population.png")

# invoking the function to find average

mean_fossil_analysis(fossil["1994"])
pop_stdDevitn_analysis(population["1996"])

