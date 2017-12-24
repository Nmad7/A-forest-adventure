'''
A model of an inventory
Created on Nov 20, 2017
@author: ngm7
'''



class Inventory():
    '''
    A class which keeps track of player inventory and allows changes to it
    '''
    def __init__(self):
        '''
        Initializes an empty inventory and item classes
        '''
        self.itemInventory = {'food':0,'water':0,'rope':0,'knife':0,'rifle':0,'painkiller':0,'first aid kit':0,'antibiotic':0}
        
        #Painkiller data
        self.painkiller_counter = 0
        self.painkiller_active= False
        self.painkiller_damage= False
    
    def AddInventory(self,item,amount):
        '''
        A function that adds a certain number of items to the inventory dictionary
        '''
        self.itemInventory[item]=self.itemInventory[item]+amount
    
    def SubInventory(self,item,amount=1):
        '''
        A function that subtracts a certain number of items to the inventory dictionary
        '''
        self.itemInventory[item]=self.itemInventory[item]-amount
    
    def get_inventory_item(self,item):
        '''
        Returns the number of a certain item in the inventory
        '''
        return self.itemInventory[item]
    
    def get_inventory(self):
        '''
        returns the full inventory
        '''         
        inventory_string_display=""
        for key in self.itemInventory:
            inventory_string_display+= str(self.itemInventory[key])+"-"+key+"~~~"
        return inventory_string_display
    
    def in_inventory(self,item):
        '''
        A function that checks if an item is actually in a players inventory
        returns True or False
        '''
        if (item in self.itemInventory) and self.get_inventory_item(item) > 0:
            return True
        else:
            return False

    
    def camp_meal(self):
        '''FIXMEEEEEEEE (does not do what I want it to)
        A function which removes one food and one water from inventory.
        '''
        if self.itemInventory['food'] == 0 and self.itemInventory['water']==0:
            return "starving and thirsty"
        
        elif self.itemInventory['food'] == 0:
            return "starving"
        elif self.itemInventory['water'] == 0:
            return "thirsty"
        else:
            return "good"
        
    #PAINKILLER FUNCTIONS
    def painkiller_use(self,player):
        '''
        When a painkiller is used, a timer is set that will remove the health benefit from painkillers after a certain number of days
        Also sets painkiller active to True so painkillers cannot be used again
        '''
        self.painkiller_counter = 2
        player.health.add_health(2)
        self.painkiller_active= True
        
    def painkiller_wearoff(self,player):
        '''
        A function that occurs at the end of every night and checks if the painkiller counter reaches zero
        '''
        #Checks if counter is zero and if painkiller is active and if so gives damage
        if self.painkiller_counter == 0 and self.painkiller_active == True:
            player.health.take_damage(2)
            self.painkiller_active=False
            self.painkiller_damage=True
        #If just active 1 is subtracted from the counter
        elif self.painkiller_active == True:
            self.painkiller_counter-=1
    
        

if __name__=="__main__":
    inventory = Inventory()
    print(inventory.get_inventory_item('food'))
