import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pyparsing import col

class DataReader:

    def __init__(self):
        self.db_name = "realtor-data.csv"
        self.test_db = "test-data.csv"
        self.test()
        # self.read_data()


    def test(self):

        data = pd.read_csv(self.db_name)
        # print(data)

        data = data.nlargest(n=10, columns=["price"])
        print(data)


    def read_data(self):

        data = pd.read_csv(self.db_name)

        # print(data.to_string())

        plt.plot(data['acre_lot'], data['price'], label='price')


        # x-coordinates of left sides of bars 
        left = range(len(data))

        # heights of bars
        height = data['price']

        states = pd.unique(data['state'])

        # labels for bars
        tick_label = states

        # plotting a bar chart
        plt.bar(left, height, tick_label = tick_label,
                width = 0.8, color = ['green'])

        # naming the x-axis
        plt.xlabel('x - axis')
        # naming the y-axis
        plt.ylabel('y - axis')
        # plot title
        plt.title('My bar chart!')

        # function to show the plot
        plt.show()

DataReader()