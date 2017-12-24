'''
Creates a game class which creates objects for the game as well as a loop
Created on Nov 20, 2017
@author: ngm7
'''
#Imports necesary classes
from tkinter import *
from shop import *
from events import *
from player_states import *
from GUI import *

class Game():
    '''
    A class which creates the game's objects, GUI, and a loop
    '''
    def __init__(self):
        
        #Initialization of objects
        self.player=Player()
        self.player_states=Player_States()
        
        #GUI ELEMENTS
        root = Tk()
        root.title("TEST")
        
        #FIXME: Got ONlINE
        root.geometry("1280x720")   
        root.resizable(0,0) 
        displaygui=DisplayGUI(root)
        inventorygui=InventoryGUI(root)
        textgui=TextGUI(root)
        displaygui.shop_gui()
        shop=Shop(self.player)
    
    
    def gameLoop(self):
        '''
        Creates a main loop of the game so events and night state repeat one after another until either death or a win at which point the game is quit
        '''
        while True:
            self.event=CreateEvent(self.player,self.player_states)
            
            

if __name__=="__main__":
    game=Game()
    game.gameLoop()
    