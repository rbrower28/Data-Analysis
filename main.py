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