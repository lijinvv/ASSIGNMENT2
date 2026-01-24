# importing the packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Function for transposing the data from the world bank csv file
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
    plt.plot(years, data_line[countriz].values, label=countriz)
    plt.xlabel(lab1, fontsize=25)  # adding label to x axis and y axis
    plt.ylabel(lab2, fontsize=25)
    plt.title(head, fontsize=35, color="blue")
    plt.legend(loc="upper right", fontsize=20)
    plt.savefig(img)
    plt.show()
    return


# Filtering data for bar plot
def filter_bar_data(data):
    """
    Defining function to filter data used for plotting the bar graph.
    This returns the filtered data.
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


# Bar plot of Population growth and fossil fuel energy  consumption
def bar_plot(data_bar, lab1, lab2, title, img):
    """
    Function used to plot the bar graph
    data_bar : name of the data
    lab1 : label x axis
    lab2 : label y axis
    title : title of bar plot
    img: destination of figure
    """

    plt.figure(figsize=(30, 15))
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

    # Giving labels to x axis and y axis

    sub.set_xlabel(lab1, fontsize=39)
    sub.set_ylabel(lab2, fontsize=39)
    sub.set_title(title, fontsize=75, color="blue")
    sub.set_xticks(arr, countriz, fontsize=30, rotation=90)
    sub.legend(loc="upper right", fontsize=30)

    sub.bar_label(bar1, padding=2, rotation=90, fontsize=20)
    sub.bar_label(bar2, padding=2, rotation=90, fontsize=20)
    sub.bar_label(bar3, padding=2, rotation=90, fontsize=20)
    plt.savefig(img)
    plt.show()
    return

# To find the average of the fossil fuel consumption in the year 1994


def mean_and_standardDeviation_fossil(data_fossil):
    """ 
    The function to find the mean of fossil fuel consumption
    data_mean : the data file
    """
    mean_value = np.mean(data_fossil)
    print("\n \n \n       The mean of fossil fuel consumption in the year of 1994 is :",
          np.mean(mean_value))
    stdDeviation = np.std(data_fossil)
    return print("       The Standard deviation fossil fuel consumption in the year of 1994 is",
                 np.mean(stdDeviation))
    return

# the countries used to filter the data


countriz = ['Thailand', 'Tonga', 'Chile', 'Bangladesh', 'Iceland', 'Bulgaria']


"""
Assigning the indicators to the variables approriately
"""

renewable, renewable_data = trans_file("renewable.csv")
renewable_data = renewable_data.apply(pd.to_numeric)
electricity, electricity_data = trans_file("electricity.csv")

fossil = pd.read_csv("fossil fuels.csv")
fossil = filter_bar_data(fossil)

population = pd.read_csv("population growth.csv")
population = filter_bar_data(population)

"""
invoking functions for plotting line graph, bar graph and to find the average
"""

# invoking line plot function


line_plot(renewable_data, renewable_data.index.values, countriz, "Years",
          "Renwable resource consumption", "Change in renewable resource consumption", "renewable.png")
line_plot(electricity_data, electricity_data.index, countriz, "years",
          "Electricity consumption", "Change in electricity consumption", "electricity.png")


# invoking bar plot

bar_plot(fossil, "Countries", "fossil consumption",
         "Fossil fuel energy consumption", "fossil.png")
bar_plot(population, "Countries", "Population growth",
         "The population growth", "population.png")

# invoking the function to statistically analyze the data

mean_and_standardDeviation_fossil(fossil["1994"])

