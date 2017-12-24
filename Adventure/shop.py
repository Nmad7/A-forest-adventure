'''
A class which models a shop which displays prices for items, keeps track of player money, and displays information about items. Requires an inventory to run
Created on Nov 20, 2017
@author: ngm7
'''
from player import *
from GUI import *

class Shop():
    '''
    A class which models a shop which displays prices for items, keeps track of player money, and displays information about items
    '''

    def __init__(self,purse=None):
        '''
        Gives a default amount of money to the player 
        '''
        #Sets default purse value if not provided 
        if purse is not None:
            self.purse=purse
        else:
            self.purse = 2000
        
        #Set the price of all items 
        self._itemPrice = {'food':100,'water':100,'rope':200,'knife':200,'rifle':500,'painkiller':100,'first aid kit':300,'antibiotic':300}
        
    
    
    def __str__(self):
        '''
        Returns the items in the shop and their prices in a nice looking form
        '''
        shop_string_display=""
        for key in self._itemPrice:
            shop_string_display+= key+" is "+str(self._itemPrice[key])+" dollars\n"
        return shop_string_display
    
    def buying(self,player,item):
        '''
        A function called when a shop object is created to put the user in a loop to buy things
        '''
        #Checks if the player has the money for the item and if so adds the item to their inventory
        if self._itemPrice[item] > self.get_purse():
            return "Cannot Buy"
        else:
            player.inventory.AddInventory(item,1)
            self.sub_purse(item,1)
    
    def get_purse(self):
        '''
        A function which returns the amount of money a player has
        '''
        return self.purse
    
    def sub_purse(self,item,amount):
        '''
        A function which subtracts the cost of an item from the purse
        '''
        self.purse=self.purse-self._itemPrice[item]*int(amount)

if __name__=="__main__": 
    player = Player()  
    shop = Shop()
    shop.buyingPhase()
