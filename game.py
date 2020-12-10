from tkinter import *
import file1 as f
import tkinter.messagebox



class GameField():
    """creates table"""
    def __init__(self, master):
        """construct a table with a parent MASTER"""
        self.frame = master
        seed=f.seed_create()
        self.NewTable = f.Table(seed)
        self.Figures()

    def Figures(self):
        """puts buttons in table"""
        for i in range(5):
            for j in range(5):
                NewTile = Tile(self.frame, self.NewTable, i, j)
                self.NewTable.buttonfield[i][j] = NewTile


class Tile(Button):
    """Button widgets"""
    def __init__(self, master, table, row, col):
        """construct a button widget with parent MASTER"""
        Button.__init__(self, master, bg="white", command=self._click, padx=25, pady=25, image=table.Field[row][col])
        self.tablica = table
        self.master = master
        self.row = row
        self.col = col
        self.grid(row=row, column=col)


    def _click(self):
        """you can`t click the same figure twice
        if field cleaned from figures it shows message and ends game"""
        self.state = self.tablica.clicked(self.row, self.col, self)
        if self.state:
            self.configure(state=DISABLED)
        if self.tablica.winningcounter==0:
            self.master.destroy()
            tkinter.messagebox.showinfo(title="CONGRATULATIONS", message="YOU ARE THE WINNER")