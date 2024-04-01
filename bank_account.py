import 
import random
from tkinter import *

randomlist = random.sample(range(1,15),5)
global button_GUI_states
        
class Display:
    def __init__(self, size_x, size_y, screen_x, screen_y):
        self.size_x = size_x
        self.size_y = size_y
        self.screen_x = screen_x
        self.screen_y = screen_y



    def create_screen(self):
        print('welcome to American Bank')
        self.bank_account_actions()
        '''
        x = 0
        y = 0

        gui = Tk()
        gui.geometry(str(self.screen_x)+'x'+str(self.screen_y))
        gui.configure(bg='blue')
        label=Button(gui, text = 'welcome to American Bank', font=('Calibri 12'), command= self.bank_account_actions())
        label.place(relx=.5 , rely=.5, anchor=CENTER)
        gui.mainloop()
        '''
    def bank_account_actions(self):
        print('')
        Button_functions = '1.deposit', '2.withdraw', '3.create account', '4.delete account'
        for button in Button_functions:
            print(button)
        choice = input('enter a number to perform a action')
INSERT INTO table_name
VALUES ()
board = Display(5, 5, 300, 300)

board.create_screen()