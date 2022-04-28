import tkinter as tk
from tkinter import filedialog, Text
import os

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class program:

    def __init__(self):
        # connect to csv
        self.df = pd.read_csv("CountryHappinessRank.csv", delimiter=",")

        self.bodycolor = 'yellow'

        self.root = tk.Tk()

        # back ground
        self.canvas = tk.Canvas(self.root, height=800, width=700, bg="#263D42")
        self.canvas.pack()

        # frame
        self.frame = tk.Frame(self.canvas, bg='#91f2ab')
        self.frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

        # Title
        self.title = tk.Label(self.frame, text="Welcome to Happiness searching", borderwidth=1, relief='solid'
                              , bg="#bef7d2")
        self.title.config(font=("Courier", 20))

        self.title.pack(pady=20)

        # body
        self.body = tk.Frame(self.frame, bg=self.bodycolor)
        self.body.place(relwidth=0.8, relheight=0.75, relx=0.1, rely=0.15)

        self.menu()

        # return
        back = tk.Button(self.frame, text='Home', command=self.menu, padx=50, bg='#0e3b15', fg='white')
        back.config(font=("Courier", 10))
        back.place(relwidth=0.2, relheight=0.1, relx=0.4, rely=0.9)
        self.root.mainloop()

    def menu(self):
        self.clean()

        # create menu
        # search
        searchButton = tk.Button(self.body, text='Search by country name', command=self.search, padx=50)
        searchButton.config(font=("Courier", 10))
        searchButton.pack(pady=10)

        # plot top ten
        plottopten = tk.Button(self.body, text='Plot top ten', command=self.plottopten, padx=50)
        plottopten.config(font=("Courier", 10))
        plottopten.pack(pady=10)

        # plot by region
        plottopregion = tk.Button(self.body, text='Plot by region', command=self.plotbyregion, padx=50)
        plottopregion.config(font=("Courier", 10))
        plottopregion.pack(pady=10)

        #Sort by region

    def plotbyregion(self):

        dftemp = self.df.copy()
        dftemp = dftemp[['Region', 'Happiness Score']].groupby('Region').sum()
        dftemp = dftemp.reset_index()


        plt.barh(dftemp['Region'], dftemp['Happiness Score'], align='center')
        plt.title("Region comparision")
        plt.
        plt.show()

    def plottopten(self):
        """
        f = plt.Figure(figsize=(1, 10), dpi=100, frameon=False)

        ax = f.add_subplot(1, 1, 1)
        bar = FigureCanvasTkAgg(f, self.body)
        bar.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Custom plot
        dftemp = self.df[['Country', 'Happiness Score']].head(10)

        # Type plot
        ax.barh(dftemp['Country'], dftemp['Happiness Score'], align='center')
        plt.barh(dftemp['Country'], dftemp['Happiness Score'], align='center')
        # Head
        ax.set_title('Top ten ranking')
        :return:
        """
        dftemp = self.df[['Country', 'Happiness Score']].head(10)
        plt.barh(dftemp['Country'], dftemp['Happiness Score'], align='center')
        plt.title("Top ten ranking")
        plt.show()

    def search(self):
        self.clean()

        # Title
        title = tk.Label(self.body, text="Enter country below", bg=self.bodycolor)
        title.config(font=("Courier", 15))
        title.pack(pady=10)

        # Entry
        entry_text = tk.StringVar()
        entry = tk.Entry(self.body, width=40, textvariable=entry_text)
        entry.config(font=("Courier", 10))
        entry.pack(pady=10)

        # result
        output = tk.Label(self.body, text="", bg="#e8f5d5")
        output.config(font=("Courier", 15))

        searchButton = tk.Button(self.body, text='Search', command=lambda: self.searchsubmit(entry, output), padx=50)
        searchButton.config(font=("Courier", 10))
        searchButton.pack(pady=10)
        output.pack(pady=10)

    def searchsubmit(self, entry, output):
        value = entry.get()
        result = self.df[self.df["Country"] == value]
        output.config(text=result)

        if result.empty == False:

            # string = "Result:"+str(result['Happiness Rank'].values[0])
            string = "Result:" + str(result['Happiness Rank'].values[0])
            output.config(text=string)
            # output = tk.Label(self.body, text=string, bg="#e8f5d5")

        else:
            string = text = "Not found " + value
            output.config(text=string)

    def clean(self):
        # Clean widget
        for widget in self.body.winfo_children():
            widget.destroy()


def main():
    test = program()


if __name__ == '__main__':
    main()
