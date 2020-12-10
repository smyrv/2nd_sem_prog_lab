from tkinter import *
import game as g
import tkinter.messagebox


class MainGame:
    """class with "start game" window"""
    def __init__(self):
        self._window_config()

    def _window_config(self):
        root = Tk()
        root.title("made by Myrvoda")
        root.geometry('300x200')
        
        # creating and showing Label widget on the screen
        Label1 = Label(root, text="Welcome to the game!")
        Label1.pack()

        # creating a menu and submenu
        main_menu = Menu()
        file_menu = Menu(tearoff=0)
        file_menu.add_command(label="New", command=self._new_game)

        main_menu.add_cascade(label="File", menu=file_menu)
        main_menu.add_cascade(label="Exit", command=quit)
        root.config(menu=main_menu)

        # creating button widgets
        button1 = Button(root, text="Start", command=self._game, bg="yellow", width=12, height=2)
        button1.pack()
        button2 = Button(root, text="Rules", command=self._game_rules, bg="yellow", width=12, height=2)
        button2.pack()
        self._button1 = button1
        self._button2 = button2
        self._root = root
        root.mainloop()

    def _game(self):
        """imports information from game.py and displays new window with the game field """
        top = Toplevel()
        top.title("Game")
        self._button1.configure(state=DISABLED)
        g.GameField(top)
        top.resizable(width=False, height=False)

    def _new_game(self):
        """restarts new game"""
        self._button1.configure(state=ACTIVE)

    def _game_rules(self):
        tkinter.messagebox.showinfo(title="RULES", message="Мета: очистити поле від всіх фігур\n Як грати: за допомогою кліку мишки поміняй місцями будь-які 2 фігури\n Виконавець: Мирвода Софія к11")


MainGame()
