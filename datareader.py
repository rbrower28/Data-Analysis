import pandas as pd


class DataReader:

    def __init__(self):
        # Initializes the data and the test data
        self.db_name = "realtor-data.csv"
        self.test_db = "test-data.csv"

        # Removes duplicate listings
        self.data = pd.read_csv(self.db_name).drop_duplicates(subset=None, keep='first', inplace=False)
        self.all_states = pd.unique(self.data["state"])


    def add_commas(self, number):
        # Turns a raw number into a comma'd one
        # Ex: 60000000 into 60,000,000
        return ("{:,}".format(number))

    
    def get_all_states(self):
        # Returns a list of all the states
        return self.all_states


    def get_homes(self, end, quant):
        # Gets the highest or lowest priced homes on the market

        if end == "high":

            # Creates a new data frame with the highest prices
            new_df = self.data.nlargest(n=quant, columns=["price"])

            # Adds commas to everything
            new_df["price"] = new_df["price"].apply(self.add_commas)
            new_df["house_size"] = new_df["house_size"].apply(self.add_commas)

            # Prints the data
            print(new_df[["price", "bed", "bath", 
                        "acre_lot", "full_address", 
                        "house_size"]].to_string(index=False))

        elif end == "low":

            # Creates a new data frame with the lowest prices
            new_df = self.data.nsmallest(n=quant, columns=["price"])

            # Adds commas to everything
            new_df["price"] = new_df["price"].apply(self.add_commas)
            new_df["house_size"] = new_df["house_size"].apply(self.add_commas)

            # Prints the data
            print(new_df[["price", "acre_lot", "full_address",
                        "house_size"]].to_string(index=False))

        print()

        # Gets a list of the states in the data
        states_list = pd.unique(new_df["state"])

        total_listings = 0

        for state in states_list:
            # Gets the data for each one and searches how many
            # times it comes up in the data. It prints them out
            # one by one

            state_data = new_df["state"] == state
            instances = str(state_data).count("True")
            total_listings += instances
            print(f"Listings in {state}: {instances}")
            
        # Prints total listings
        print(f"Total listings: {total_listings}")


    def get_by_state(self, state):
        # Gets listing information by state
        
        # Retrieves all the homes that are in the specified state
        state_df = self.data[self.data["state"].isin([state])]

        print(f"\n      State -- {state}\n")

        print("    Most expensive homes:\n")

        # Get the 10 most expensive homes and print
        highest_homes = state_df.nlargest(n=10, columns=["price"])
        highest_homes["price"] = highest_homes["price"].apply(self.add_commas)
        print(highest_homes[["price", "bed", "bath", 
                        "acre_lot", "full_address", 
                        "house_size"]].to_string(index=False))

        print("\n    Least expensive homes:\n")

        # Get the 10 least expensive homes and print
        lowest_homes = state_df.nsmallest(n=10, columns=["price"])
        lowest_homes["price"] = lowest_homes["price"].apply(self.add_commas)
        print(lowest_homes[["price", "bed", "bath", 
                        "acre_lot", "full_address", 
                        "house_size"]].to_string(index=False))

        # Find the average listing price in the state and print
        average_raw = round(state_df["price"].mean())
        average = ("{:,}".format(average_raw))

        print(f"\n    Average listing price in this state -- ${average}")


    def get_by_price(self, price):
        # Get home listings around a certain price.

        print("\n    Slightly higher:\n")

        # Creates a new data frame above the specified price
        upper_df = self.data[self.data["price"] > price]

        # Takes the smallest 20 of the frame
        # These are the 20 right above the given price.
        upper_cut = upper_df.nsmallest(n=20, columns=["price"])

        # Adds commas
        upper_cut["price"] = upper_cut["price"].apply(self.add_commas)
        upper_cut["house_size"] = upper_cut["house_size"].apply(self.add_commas)
        upper_cut = upper_cut[::-1]

        # Prints the data
        print(upper_cut[["price", "bed", "bath", 
                        "acre_lot", "full_address", 
                        "house_size"]].to_string(index=False))

        print("\n    Slightly lower:\n")

        # Creates a new data frame below the specified price
        lower_df = self.data[self.data["price"] < price]

        # Takes the largest 20 of the frame
        # These are the 20 right below the given price.
        lower_cut = lower_df.nlargest(n=20, columns=["price"])

        # Adds commas
        lower_cut["price"] = lower_cut["price"].apply(self.add_commas)
        lower_cut["house_size"] = lower_cut["house_size"].apply(self.add_commas)

        # Prints the data
        print(lower_cut[["price", "bed", "bath", 
                        "acre_lot", "full_address", 
                        "house_size"]].to_string(index=False))
