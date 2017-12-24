'''
A class which models events that can occur on the trip
Created on Nov 21, 2017
@author: ngm7
'''

import sys
from player import *
from shop import *
from GUI import *

class Night_Time():
    '''
    A which contains checks that should happen at night and the general night events 
    Essentially involves a list of functions that should be called with buttons during the night time
    '''
    def __init__(self,player,gui):
        '''
        Initializes the night and starts the event chain ...        
        '''
        #Might put in later
        #self._dayNumber = 1    
    
        self.player=player
        self.gui=gui
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.stepPainkiller)
    
        
        
    def stepPainkiller(self):
        '''
        A step which preforms painkiller functions and checks the status of the player in regards to painkillers

        '''
        #Calls the wearoff function of painkiller 
        self.player.inventory.painkiller_wearoff(self.player)
        if self.player.inventory.painkiller_damage==True:
            self.player.inventory.painkiller_damage=False
            self.gui.text_message="Your painkillers wear off..."
            self.gui.text_change()
            self.gui.textgui.next_button.config(command=self.stepInitial)
        elif self.player.inventory.painkiller_active==True:
            self.gui.text_message="You still have painkillers in your system..."
            self.gui.text_change()
            self.gui.textgui.next_button.config(command=self.stepInitial)
        else:
            self.stepInitial()
            
    def stepInitial(self):   
        '''
        Creates an state which checks if the user has died from the last event, has reached the goal, or is still traveling
        If the player is still traveling the player is given a summary of their status (health, inventory)
        Also eats food at the end of the night and drinks water.
        '''
        #Removes one water and one food as well as damage the player if they do not have enough food
        if self.player.inventory.camp_meal() == "starving and thirsty":
            self.player.health.take_damage(2)
            self.gui.text_message="You are starving and dying of thirst."
            self.gui.text_change()
            
        elif self.player.inventory.camp_meal() == "starving":
            self.player.health.take_damage(1)
            self.player.inventory.itemInventory['water']=self.player.inventory.itemInventory['water']-1
            self.gui.inventorygui.set_inventory_num("water",self.player.inventory.get_inventory_item("water"))
            self.gui.text_message="You drink water but have run out of food. You are starving."
            self.gui.text_change()
        elif self.player.inventory.camp_meal() == "thirsty":
            self.player.health.take_damage(1)
            self.player.inventory.itemInventory['food']=self.player.inventory.itemInventory['food']-1 
            self.gui.inventorygui.set_inventory_num("food",self.player.inventory.get_inventory_item("food"))
            self.gui.text_message="You eat food but have run out of water. You are dehydrated."
            self.gui.text_change()
        elif self.player.inventory.camp_meal() == "good":
            self.player.inventory.itemInventory['food']=self.player.inventory.itemInventory['food']-1 
            self.gui.inventorygui.set_inventory_num("food",self.player.inventory.get_inventory_item("food"))
            self.player.inventory.itemInventory['water']=self.player.inventory.itemInventory['water']-1
            self.gui.inventorygui.set_inventory_num("water",self.player.inventory.get_inventory_item("water"))
            self.gui.text_message="You eat and drink your fill for the day."
            self.gui.text_change()
  
        #Checks if the player is dead or has won
        if self.player.health.get_health() <= 0:
            #FIXME:Add images to these to switch to
            self.gui.text_message="You have unfortunately died..."
            self.gui.text_change()
            self.gui.displaygui.set_background("pictures/death.gif")
            self.gui.textgui.next_button.config(command=self.quit)
            
        elif self.player.location == 10:
            self.gui.text_message="You have completed your journey!"
            self.gui.text_change()
            #FIXME: add more functionality to end (Have not actually tested as I never could make it to the end of the game)
            self.gui.textgui.next_button.config(command=self.quit)
            
        else:
            #The player has lived and the next step is put on the button
            self.gui.textgui.next_button.config(command=self.stepHealth)
            
    def stepHealth(self):
        '''
        The night step where the health of the player is displayed
        '''
        self.gui.text_message=self.player.health
        self.gui.text_change()
        self.gui.textgui.next_button.config(command=self.stepMedicineAsk)

    def stepMedicineAsk(self):
        '''
        A function which asks if you wish to use medicine and activates the buttons for the choice
        '''
        self.gui.text_message="Do you wish to use any medicine?"
        self.gui.text_change()
        self.gui.textgui.enable_buttons()
        self.gui.textgui.button1.config(command=self.stepMedicineYes, text="Yes")
        self.gui.textgui.button2.config(command=self.stepMedicineNo, text="No")
    
    def stepMedicineNo(self):  
        '''
        A function which occurs when the player decides not to use any more items
        it loops the player to a new event which then leads back to the night time, creating an infinite loop until either win or death
        '''
        self.gui.event_start_gui()
    
    
    def stepMedicineYes(self):
        '''
        If the player chooses yes then the inventory is made clickable and the player can choose which item to use
        '''
        if self.player.inventory.in_inventory("painkiller")==True or self.player.inventory.in_inventory("antibiotic")==True or self.player.inventory.in_inventory("first aid kit")==True:
            self.gui.text_message="Please select any medicine you wish to use from your inventory."
            self.gui.text_change()
            self.gui.night_inv_clickable()
        
        else:
            self.gui.text_message="You do not have any medicine."
            self.gui.text_change()
            self.gui.textgui.enable_next_button()
            self.gui.textgui.next_button.config(command=self.gui.event_start_gui)
            
    def stepAskPainkiller(self):
        """
        Asks if the user is sure they wish to uses the painkiller
        """
        self.gui.text_message="Are you sure you wish to use the painkiller?"
        self.gui.text_change()
        self.gui.textgui.enable_buttons()
        self.gui.textgui.button1.config(command=self.stepActionPainkiller, text="Yes")
        self.gui.textgui.button2.config(command=self.stepMedicineAsk, text="No")
        

    def stepActionPainkiller(self):
        '''
        A function which uses the painkiller on the player if the painkiller effect is not already active
        '''
        #Checks if painkillers are already active 
        self.gui.textgui.enable_next_button()
        if self.player.inventory.painkiller_active==False:
            self.player.inventory.painkiller_use(self.player)
            self.player.inventory.SubInventory("painkiller")
            self.gui.inventorygui.set_inventory_num("painkiller",self.player.inventory.get_inventory_item("painkiller"))
            self.gui.text_message=("You use the painkillers and feel different. "+str(self.player.health))
            self.gui.text_change()
            self.gui.textgui.next_button.config(command=self.stepMedicineAsk)
        else:
            self.gui.text_message="You still have painkillers in your system, you do not want to overdose..."
            self.gui.text_change()
            self.gui.textgui.next_button.config(command=self.stepMedicineAsk)
    
    def stepAskFirstaidkit(self):
        '''
        Asks if the user is sure they wish to uses the first aid kit
        '''
        self.gui.text_message="Are you sure you wish to use the first aid kit?"
        self.gui.text_change()
        self.gui.textgui.enable_buttons()
        self.gui.textgui.button1.config(command=self.stepActionFirstaidkit, text="Yes")
        self.gui.textgui.button2.config(command=self.stepMedicineAsk, text="No")
        

    def stepActionFirstaidkit(self):
        '''
        A function which uses the firstaidkit
        '''
        self.gui.textgui.enable_next_button()
        self.player.health.add_health()
        self.player.inventory.SubInventory("first aid kit")
        self.gui.inventorygui.set_inventory_num("first aid kit",self.player.inventory.get_inventory_item("first aid kit"))
        self.gui.text_message=("You use the first aid kit and feel different. "+str(self.player.health))
        self.gui.text_change()
        self.gui.textgui.next_button.config(command=self.stepMedicineAsk)
        
    def stepAskAntibiotic(self):
        '''
        Asks if the user is sure they wish to uses the Antibiotics
        '''
        self.gui.text_message="Are you sure you wish to use the antibiotics?"
        self.gui.text_change()
        self.gui.textgui.enable_buttons()
        self.gui.textgui.button1.config(command=self.stepActionAntibiotic, text="Yes")
        self.gui.textgui.button2.config(command=self.stepMedicineAsk, text="No")
        

    def stepActionAntibiotic(self):
        '''
        A function which uses the Antibiotics
        '''
        self.gui.textgui.enable_next_button()
        if self.player.health.is_not_sick():
            self.gui.text_message="You are not sick..."
            self.gui.text_change()
            self.gui.textgui.next_button.config(command=self.stepMedicineAsk)
        else:
            self.player.inventory.SubInventory("antibiotic")
            self.gui.inventorygui.set_inventory_num("antibiotic",self.player.inventory.get_inventory_item("antibiotic"))
            self.player.health.heal_sickness()
            self.gui.text_message=("You use the antibiotics and feel different. "+str(self.player.health))
            self.gui.text_change()
            self.gui.textgui.next_button.config(command=self.stepMedicineAsk)
    
    def stepActionNoItem(self):
        '''
        A function which uses no item
        '''
        self.stepMedicineAsk()

                    
            
        
        #Might add later
        #self._dayNumber+=1
    def quit(self):
        '''
        A function to call when the game should be exited (due to death mostly)
        '''
        sys.exit("Exited")
    



if __name__=="__main__":
    player=Player()
    shop=Shop()
    player_states=Player_States()
    player_states.buyingState(player,shop)
    
    
    
    