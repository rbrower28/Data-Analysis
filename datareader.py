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


    # def p(self, low, high):
        
    #     data = self.data.sort_values("price")
    #     lowest = data.nsmallest(n=1, columns=["price"])
    #     highest = data.nlargest(n=1, columns=["price"])

    #     print(price, lowest["price"].to_string(index=False), highest["price"].to_string(index=False))

    #     print(float(lowest["price"].to_string(index=False)) + float(highest["price"].to_string(index=False)))
        
    #     closest = self.find_price(price, lowest["price"], highest["price"], data)


    def get_by_price(self, price):

        print("\n    Slightly higher:\n")

        upper_df = self.data[self.data["price"] > price]
        upper_cut = upper_df.nsmallest(n=20, columns=["price"])
        upper_cut["price"] = upper_cut["price"].apply(self.add_commas)
        upper_cut["house_size"] = upper_cut["house_size"].apply(self.add_commas)
        upper_cut = upper_cut[::-1]
        print(upper_cut[["price", "bed", "bath", 
                        "acre_lot", "full_address", 
                        "house_size"]].to_string(index=False))

        print("\n    Slightly lower\n")

        lower_df = self.data[self.data["price"] < price]
        lower_cut = lower_df.nlargest(n=20, columns=["price"])
        lower_cut["price"] = lower_cut["price"].apply(self.add_commas)
        lower_cut["house_size"] = lower_cut["house_size"].apply(self.add_commas)
        print(lower_cut[["price", "bed", "bath", 
                        "acre_lot", "full_address", 
                        "house_size"]].to_string(index=False))



    # def _find_price(self, goal, min, max, data):

    #     if max >= 0:
    
    #         middle = int((max - min) / 2) + min

    #         if max - min < 2:
    #             return min
    #         else:
    #             self._find_price(sorted_list, min, middle - 1, data)
    #             self._find_price(sorted_list, middle + 1, max, data)

