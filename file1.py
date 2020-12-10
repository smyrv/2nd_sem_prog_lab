import random
import tkinter as tk
import os


def seed_create():
    """creates field with images"""
    seed = ["images/{}.png".format(i) for i in range(5)]
    for num, i in enumerate(seed):
        seed[num] = tk.PhotoImage(file=os.path.abspath(i))
    seed *= 5
    return seed


class Table():
    """puts figures in random order
    if 5 in a row - clear row
    if field  clean - game finished"""
    def __init__(self, seed):
        """construct game field"""
        self.flag = 0
        self.Field = []
        self.buttonfield = []
        self.winningcounter = 5
        self.fullline = []
        for i in range(5):
            self.Field.append([])
            self.buttonfield.append([])
            for j in range(5):
                self.Field[i].append(random.choice(seed))
                seed.remove(self.Field[i][j])
                self.buttonfield[i].append(1)

    def clicked(self, row, col, button):
        """remembers first button clicked"""
        if self.flag == 0:
            self.buttonclicked = button
            self.itsrow, self.itscol = row, col
            self.flag = 1
            return self.flag
        else:
            self.match(row, col, button)
            return self.flag

    def match(self, row, col, button):
        """change places of current and previous clicked buttons"""
        self.flag = 0
        button.configure(image=self.Field[self.itsrow][self.itscol])
        self.buttonclicked.configure(image=self.Field[row][col], state=tk.ACTIVE)
        self.Field[self.itsrow][self.itscol], self.Field[row][col] = self.Field[row][col], self.Field[self.itsrow][
            self.itscol]
        self.busy()

    def busy(self):
        """checks location of the figure"""
        kx = 0
        for i in range(5):
            if kx == 5:
                self.bingo(i - 1)
            kx = 1

            pockx = 0
            for j in range(5):
                if pockx:
                    if self.Field[i][j] == pockx:
                        kx += 1
                else:
                    pockx = self.Field[i][j]
        if kx == 5:
            self.bingo(i)

    def bingo(self, line):
        """destroys row"""
        if line not in self.fullline: #adds row in cleared if its not there yet
            self.winningcounter -= 1
            self.fullline.append(line)
        for i in range(5):
            self.buttonfield[line][i].destroy()
