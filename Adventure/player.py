'''

Created on Nov 20, 2017
@author: ngm7
'''
from player_health import *
from inventory import *
import random

class Player():
    '''
    Puts together the player health into a single entity
    '''
    def __init__(self,gui):
        '''
        Gives the player health and an inventory
        '''
        #Sets health to the default amount for the player
        self.health = Health(gui)
        #Sets an inventory for the player
        self.inventory = Inventory()
        #Keeps track of events the player completed
        self.events_experienced = []
        
        self.location=1
        
        self.gui=gui
    
    def get_events_experienced(self):
        '''
        A mutator for events experienced
        '''
        return self.events_experienced
    
    def completedEvent(self,event_number):
        '''
        A function which adds the event completed by the player
        '''
        self.events_experienced.append(event_number)
    
    def success_prob(self,success):
        '''
        A function which calculates the fail and success of an event using the probability of success given in decimal form
        '''    
        result = random.random()
    
        if success>result:
            return "success"
        else:
            return "failure"
        
    def success_prob_physical(self,success):
        '''
        A function which calculates the fail and success of an event if the event should include sickness as a factor
        '''
        #A check which makes the probability of success less than normal if an event is physical
        if self.health.is_not_sick()==False:
            if success>.20:
                success-=.20
        result = random.random()
        if success>result:
            return "success"
        else:
            return "failure"
        
    def set_location(self):
        '''
        Sets how far the player has traveled (different from daynumber as when one is near death one cannot progress until healed) and also calls a gui to change the location image
        '''
        self.location+=1
        self.gui.textgui.change_location("pictures/marker/location"+str(self.location)+".gif")
    

if __name__=="__main__": 
    player = Player()  
    print(player._inventory)