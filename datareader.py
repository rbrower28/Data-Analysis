from hashlib import new
from itertools import count
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class DataReader:

    def __init__(self):
        self.db_name = "realtor-data.csv"
        self.test_db = "test-data.csv"
        self.data = pd.read_csv(self.db_name).drop_duplicates(subset=None, keep='first', inplace=False)

        # self.test()
        # self.read_data()


    def test(self):

        print(pd.unique(self.data["state"]))

        data = self.data.nlargest(n=40, columns=["price"])
        print(data.to_string())


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


    def get_homes(self, end, quant):

        if end == "high":
            new_df = self.data.nlargest(n=quant, columns=["price"])
            print(new_df[["price", "bed", "bath", 
                        "acre_lot", "city", "state", 
                        "house_size"]].to_string())

            print()

            states_list = pd.unique(new_df["state"])

            total_listings = 0

            for state in states_list:
                state_data = new_df["state"] == state
                instances = str(state_data).count("True")
                total_listings += instances
                print(f"Listings in {state}: {instances}")
                
            print(f"Total listings: {total_listings}")

        elif end == "low":
            new_df = self.data.nsmallest(n=quant, columns=["price"])
            print(new_df[["price", "acre_lot", "city", 
                        "state", "house_size"]].to_string())
            
            print()

            states_list = pd.unique(new_df["state"])

            total_listings = 0

            for state in states_list:
                f = new_df["state"] == state
                p = str(f).count("True")
                total_listings += p
                print(f"Listings in {state}: {p}")
                
            print(f"Total listings: {total_listings}")