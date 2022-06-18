from datareader import DataReader
import matplotlib.pyplot as plt

class Main:

    def __init__(self):
        self.done = False
        # creates a new instance of data reader, which deals with the .csv file
        self.dr = DataReader()

        while self.done == False:
            self.operate()


    def operate(self):

        user_input = input("""
----- What question would you like to answer? -----

    1.) Where are the most expensive homes?
    2.) Where are the cheapest homes?
    3.) Search by state
    4.) Search by price
    5.) quit
    """)

        if user_input in ("1", "2"):
            self.req_homes(user_input)

        elif user_input == "3":
            self.req_by_state()

        elif user_input == "4":
            self.req_by_price()

        elif user_input == "5":
            self.done = True


    def req_homes(self, choice):

        quant = int(input("How many listings do you want to see? (max 60): "))

        while quant < 0 or quant > 60:
            quant = int(input("Please try again. "))

        if choice == "1":
            self.dr.get_homes("high", quant)

        elif choice == "2":
            self.dr.get_homes("low", quant)


    def req_by_state(self):
        all_states = self.dr.get_all_states()

        print("Select a state for more information:\n")

        for i in range(len(all_states)):
            index = i + 1
            print(f"{index}.) {all_states[i]}")

        state_index = input("")
        state = all_states[int(state_index) - 1]

        self.dr.get_by_state(state)


    def req_by_price(self):
        
        sample = input("Enter a price between 0 and 60 million: ")

        while sample < 0 or sample > 60000000:
            sample = int(input("Please try again. "))

        self.dr.get_by_price(sample)


if __name__ == "__main__":
    Main()