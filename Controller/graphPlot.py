import matplotlib.pyplot as plt
import  pandas as pd

class graphPlot:

    def createGraph(self):
        df = pd.read_csv('static/Reliance.csv')[:100]

        stock_prices = df

        plt.figure()

        up = stock_prices[stock_prices['Close'] >= stock_prices['Open']]

        down = stock_prices[stock_prices['Close'] < stock_prices['Open']]

        col1 = 'red'

        col2 = 'green'
        width = .3
        width2 = .03

        plt.bar(up.index, up.Close - up.Open, width, bottom=up.Open, color=col1)
        plt.bar(up.index, up.High - up.Close, width2, bottom=up.Close, color=col1)
        plt.bar(up.index, up.Low - up.Open, width2, bottom=up.Open, color=col1)

        plt.bar(down.index, down.Close - down.Open, width, bottom=down.Open, color=col2)
        plt.bar(down.index, down.High - down.Open, width2, bottom=down.Open, color=col2)
        plt.bar(down.index, down.Low - down.Close, width2, bottom=down.Close, color=col2)

        plt.xticks(rotation=30, ha='right')

        plt.rcParams["figure.figsize"] = [7.50, 3.50]
        plt.rcParams["figure.autolayout"] = True

        plt.savefig("myimage.jpg")
