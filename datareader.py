import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class DataReader:


    def __init__(self):
        self.db_name = "realtor-data.csv"
        self.test_db = "test-data.csv"
        self.data = pd.read_csv(self.db_name).drop_duplicates(subset=None, keep='first', inplace=False)
        self.all_states = pd.unique(self.data["state"])

    def add_commas(self, number):
            return ("{:,}".format(number))

    
    def get_all_states(self):
        return self.all_states


    def get_homes(self, end, quant):

        if end == "high":

            new_df = self.data.nlargest(n=quant, columns=["price"])
            new_df["price"] = new_df["price"].apply(self.add_commas)
            new_df["house_size"] = new_df["house_size"].apply(self.add_commas)

            print(new_df[["price", "bed", "bath", 
                        "acre_lot", "full_address", 
                        "house_size"]].to_string(index=False))

        elif end == "low":

            new_df = self.data.nsmallest(n=quant, columns=["price"])
            new_df["price"] = new_df["price"].apply(self.add_commas)
            new_df["house_size"] = new_df["house_size"].apply(self.add_commas)

            print(new_df[["price", "acre_lot", "full_address",
                        "house_size"]].to_string(index=False))

        print()

        states_list = pd.unique(new_df["state"])

        total_listings = 0

        for state in states_list:
            state_data = new_df["state"] == state
            instances = str(state_data).count("True")
            total_listings += instances
            print(f"Listings in {state}: {instances}")
            
        print(f"Total listings: {total_listings}")


    def get_by_state(self, state):
        
        state_df = self.data[self.data["state"].isin([state])]

        print(f"\n      State -- {state}\n")

        print("    Most expensive homes:\n")

        highest_homes = state_df.nlargest(n=10, columns=["price"])
        highest_homes["price"] = highest_homes["price"].apply(self.add_commas)
        print(highest_homes[["price", "bed", "bath", 
                        "acre_lot", "full_address", 
                        "house_size"]].to_string(index=False))

        print("\n    Least expensive homes:\n")

        lowest_homes = state_df.nsmallest(n=10, columns=["price"])
        lowest_homes["price"] = lowest_homes["price"].apply(self.add_commas)
        print(lowest_homes[["price", "bed", "bath", 
                        "acre_lot", "full_address", 
                        "house_size"]].to_string(index=False))

        average_raw = round(state_df["price"].mean())
        average = ("{:,}".format(average_raw))

        print(f"\n    Average listing price in this state -- ${average}")


    def get_by_price(self, price):
        pass