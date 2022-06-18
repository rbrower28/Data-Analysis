from datareader import DataReader

class Main:

    def __init__(self):
        self.done = False
        # creates a new instance of data reader, which deals with the .csv file
        self.dr = DataReader()

        # Starts the operation loop
        while self.done == False:
            self.operate()


    def operate(self):
        # Runs countinually until the program is ended
        # This happpens when the user inputs the number 5

        user_input = input("""
----- What question would you like to answer? -----

    1.) Where are the most expensive homes?
    2.) Where are the cheapest homes?
    3.) Search by state
    4.) Search by price
    5.) quit
    """)

        # Divides out the responses into their own methods
        if user_input in ("1", "2"):
            self.req_homes(user_input)

        elif user_input == "3":
            self.req_by_state()

        elif user_input == "4":
            self.req_by_price()

        elif user_input == "5":
            self.done = True


    def req_homes(self, choice):
        # Gets top home information
        # Allows the user to input how many listings they want to see

        quant = int(input("How many listings do you want to see? (max 60): "))

        # Validates that the data is between 1 and 60
        while quant < 0 or quant > 60:
            quant = int(input("Please try again. "))

        # Redirects to the Data Reader file
        if choice == "1":
            self.dr.get_homes("high", quant)

        elif choice == "2":
            self.dr.get_homes("low", quant)


    def req_by_state(self):
        # This is for the state searching method

        # Returns a list of states from the csv file
        all_states = self.dr.get_all_states()

        print("Select a state for more information:\n")

        # Displays the states with their number next to them for easy selection
        for i in range(len(all_states)):
            index = i + 1
            print(f"{index}.) {all_states[i]}")

        state_index = input("")
        state = all_states[int(state_index) - 1]

        # Redirects to the Data Reader
        self.dr.get_by_state(state)


    def req_by_price(self):
        # The method for searching by price

        sample = int(input("Enter a price between 0 and 60 million: "))

        # validates that the number is between 0 and 60,000,000
        while sample < 0 or sample > 60000000:
            sample = int(input("Please try again. "))

        # Moves over to Data Reader
        self.dr.get_by_price(sample)


if __name__ == "__main__":
    Main()