from datareader import DataReader
import matplotlib.pyplot as plt

class Main:

    def __init__(self):
        self.done = False

        # creates a new instance of data reader, which deals with the .csv file
        self.dr = DataReader()
        # self.draw_chart()

        while self.done == False:
            self.operate()

        
    def operate(self):

        user_input = input(
            """----- What question would you like to answer? -----
            1.) Where are the most expensive homes?
            2.) Where are the cheapest homes?
            3.) What is the average listing price by state?
            4.) What is the highest listing price by state?
            5.) What is the lowest listing price by state?
            6.) Search by price
            7.) quit
            """)

        if user_input in ("1", "2"):
            self.req_homes(user_input)

        elif user_input in ("3", "4", "5"):
            self.req_by_state(user_input)

        elif user_input in ("6"):
            self.req_price()

        elif user_input == "7":
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
        pass


    def req_price(self):
        pass


    def draw_chart(self):

        # x-coordinates of left sides of bars 
        left = [1, 2, 3, 4, 5]

        # heights of bars
        height = [10, 24, 36, 40, 5]

        # labels for bars
        tick_label = ['one', 'two', 'three', 'four', 'five']

        # plotting a bar chart
        plt.bar(left, height, tick_label = tick_label,
                width = 0.8, color = ['red', 'green'])

        # naming the x-axis
        plt.xlabel('x - axis')
        # naming the y-axis
        plt.ylabel('y - axis')
        # plot title
        plt.title('My bar chart!')

        # function to show the plot
        plt.show()

if __name__ == "__main__":
    Main()