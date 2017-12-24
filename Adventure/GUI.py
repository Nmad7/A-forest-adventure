"""
Author:ngm7
INFORMATION:
Images taken from opengameart.org to be copyright free or created by myself
Specific game sprites can scale strangely on different machines, be aware...
"""

from tkinter import *
from GUI_Types import *
from shop import *
from events import *
from night_time import *

class GUI():
    '''
    This class compiles the various GUI's so they can work together to create various states which will then be switched to by events during the main loop 
    '''
    def __init__(self):
        
        self.root = Tk()
        self.root.title("Adventury Thing")
        
        #Prevents window from resizing and gives a set resolution
        #Taken from https://mail.python.org/pipermail/tutor/2001-September/008504.html and https://stackoverflow.com/questions/21958534/setting-the-window-to-a-fixed-size-with-tkinter
        self.root.geometry("1280x720")   
        self.root.resizable(0,0) 
        #End of taken section
        
        self.displaygui=DisplayGUI(self.root)
        self.inventorygui=InventoryGUI(self.root)
        self.textgui=TextGUI(self.root)
        
        self.player=Player(self)
        self.shop=Shop()
        
        #Creates a blank text_message variable
        self.text_message=""
        
    
    def set_text_message(self,text):
        '''
        A function which sets the text
        '''
        self.text_message=text
    
    def intro_gui(self):
        '''
        A function which creates an intro GUI that, when the arrow is pressed, the shop gui is activated
        '''    
        #We should already be in the intro screen and this sets the arrow button to activate shop_gui
        self.textgui.next_button.config(command=self.shop_gui)
    
        
    def shop_gui(self):
        '''
        A function which creates a shop GUI in the display window
        This shop GUI has the items displayed along with their price
        '''
        #Set the background to be the shop
        self.displaygui.set_background("pictures/shop.gif")
        
        #Creates an text box that says INVENTORY
        self.displaygui.display_canvas.create_text(450,0,text='STORE',font=("Courier New", 20, "bold underline italic"),anchor=N,tags="store_item")
        
        #CREATION OF ITEM PICTURES AND PRICE
        self.displaygui.rifle_image=PhotoImage(file="pictures/rifle.gif")
        self.displaygui.display_canvas.create_image(150,90,image=self.displaygui.rifle_image,tags=("store_item","store_rifle"))
        self.displaygui.display_canvas.create_text(150,140,text='500',font=("Courier New", 15, "bold"),tags=("store_item","store_rifle"))
        
        self.displaygui.knife_image=PhotoImage(file="pictures/knife.gif")
        self.displaygui.display_canvas.create_image(300,90,image=self.displaygui.knife_image,tags=("store_item","store_knife"))
        self.displaygui.display_canvas.create_text(300,140,text='200',font=("Courier New", 15, "bold"),tags=("store_item","store_knife"))
        
        self.displaygui.rope_image=PhotoImage(file="pictures/rope.gif")
        self.displaygui.display_canvas.create_image(450,90,image=self.displaygui.rope_image,tags=("store_item","store_rope"))
        self.displaygui.display_canvas.create_text(450,140,text='200',font=("Courier New", 15, "bold"),tags=("store_item","store_rope"))
        
        self.displaygui.painkiller_image=PhotoImage(file="pictures/painkiller.gif")
        self.displaygui.display_canvas.create_image(600,90,image=self.displaygui.painkiller_image,tags=("store_item","store_painkiller"))
        self.displaygui.display_canvas.create_text(600,140,text='100',font=("Courier New", 15, "bold"),tags=("store_item","store_painkiller"))

        self.displaygui.antibiotic_image=PhotoImage(file="pictures/antibiotic.gif")
        self.displaygui.display_canvas.create_image(750,90,image=self.displaygui.antibiotic_image,tags=("store_item","store_antibiotic"))
        self.displaygui.display_canvas.create_text(750,140,text='300',font=("Courier New", 15, "bold"),tags="store_item")
        
        self.displaygui.firstaidkit_image=PhotoImage(file="pictures/firstaidkit.gif")
        self.displaygui.display_canvas.create_image(150,200,image=self.displaygui.firstaidkit_image,tags=("store_item","store_firstaidkit"))
        self.displaygui.display_canvas.create_text(150,250,text='300',font=("Courier New", 15, "bold"),tags="store_item")
        
        self.displaygui.food_image=PhotoImage(file="pictures/food.gif")
        self.displaygui.display_canvas.create_image(300,200,image=self.displaygui.food_image,tags=("store_item","store_food"))
        self.displaygui.display_canvas.create_text(300,250,text='100',font=("Courier New", 15, "bold"),tags="store_item")
        
        self.displaygui.water_image=PhotoImage(file="pictures/water.gif")
        self.displaygui.display_canvas.create_image(450,200,image=self.displaygui.water_image,tags=("store_item","store_water"))
        self.displaygui.display_canvas.create_text(450,250,text='100',font=("Courier New", 15, "bold"),tags="store_item")
        
        #Creation of purse
        self.purse_num=StringVar()
        self.purse_num.set(str(self.shop.purse))
        self.purse_id=self.displaygui.display_canvas.create_text(450,420,text="Purse: "+self.purse_num.get(),font=("Courier New", 20, "underline italic"),anchor=N,tags="store_item")
        
        #Raises the items above the background
        self.displaygui.display_canvas.tag_raise("store_item")
        
        #Activates the canvas for clicking items
        self.displaygui.display_canvas.tag_bind("store_rifle",'<Button-1>',self.store_click_check)
        self.displaygui.display_canvas.tag_bind("store_knife",'<Button-1>',self.store_click_check)
        self.displaygui.display_canvas.tag_bind("store_rope",'<Button-1>',self.store_click_check)
        self.displaygui.display_canvas.tag_bind("store_painkiller",'<Button-1>',self.store_click_check)
        self.displaygui.display_canvas.tag_bind("store_antibiotic",'<Button-1>',self.store_click_check)
        self.displaygui.display_canvas.tag_bind("store_firstaidkit",'<Button-1>',self.store_click_check)
        self.displaygui.display_canvas.tag_bind("store_food",'<Button-1>',self.store_click_check)
        self.displaygui.display_canvas.tag_bind("store_water",'<Button-1>',self.store_click_check)  
        
        #Change text to tell the player what to do
        self.textgui.set_text("Please choose the items you wish to buy and bring with you on your adventure by clicking their pictures. When finished click the next arrow.")
        
        self.textgui.next_button.config(command=self.event_start_gui)


    def set_purse_num(self,amount):
        '''
        A function used to change the text value for the purse amount
        '''
        self.displaygui.display_canvas.itemconfig(self.purse_id, text="Purse: "+str(amount))
    
    def store_click_check(self,event):
        '''
        A function is run when an image in the store is clicked while store_clickable is active
        '''
        id=self.displaygui.display_canvas.find_closest(event.x,event.y)
        item=self.displaygui.display_canvas.gettags(id)
        item=item[1]
        if item=="store_rifle":
            self.shop.buying(self.player,"rifle")
            self.set_purse_num(self.shop.purse)
            self.inventorygui.set_inventory_num("rifle",self.player.inventory.get_inventory_item("rifle"))
        elif item=="store_knife":
            self.shop.buying(self.player,"knife")
            self.set_purse_num(self.shop.purse)
            self.inventorygui.set_inventory_num("knife",self.player.inventory.get_inventory_item("knife"))
        elif item=="store_rope":
            self.shop.buying(self.player,"rope")
            self.set_purse_num(self.shop.purse)
            self.inventorygui.set_inventory_num("rope",self.player.inventory.get_inventory_item("rope"))
        elif item=="store_painkiller":
            self.shop.buying(self.player,"painkiller")
            self.set_purse_num(self.shop.purse)
            self.inventorygui.set_inventory_num("painkiller",self.player.inventory.get_inventory_item("painkiller"))
        elif item=="store_antibiotic":
            self.shop.buying(self.player,"antibiotic")
            self.set_purse_num(self.shop.purse)
            self.inventorygui.set_inventory_num("antibiotic",self.player.inventory.get_inventory_item("antibiotic"))
        elif item=="store_firstaidkit":
            self.shop.buying(self.player,"first aid kit")
            self.set_purse_num(self.shop.purse)
            self.inventorygui.set_inventory_num("first aid kit",self.player.inventory.get_inventory_item("first aid kit"))
        elif item=="store_food":
            self.shop.buying(self.player,"food")
            self.set_purse_num(self.shop.purse)
            self.inventorygui.set_inventory_num("food",self.player.inventory.get_inventory_item("food"))
        elif item=="store_water":
            self.shop.buying(self.player,"water")
            self.set_purse_num(self.shop.purse)
            self.inventorygui.set_inventory_num("water",self.player.inventory.get_inventory_item("water"))
    
    def clean_gui(self):
        '''
        A function to clean the store items from the display gui
        '''
        self.displaygui.display_canvas.delete("store_item")
    
    def text_change(self):
        '''
        A function which sets the text
        '''
        self.textgui.set_text(self.text_message)
            
    def inv_unclickable(self):
        '''
        A function which unbinds clicking from the inventory
        '''
        gui.inventorygui.inv_canvas.tag_unbind("rifle_image",'<Button-1>')
        gui.inventorygui.inv_canvas.tag_unbind("knife_image",'<Button-1>')
        gui.inventorygui.inv_canvas.tag_unbind("rope_image",'<Button-1>')
        gui.inventorygui.inv_canvas.tag_unbind("painkiller_image",'<Button-1>')
        gui.inventorygui.inv_canvas.tag_unbind("antibiotic_image",'<Button-1>')
        gui.inventorygui.inv_canvas.tag_unbind("firstaidkit_image",'<Button-1>')
        gui.inventorygui.inv_canvas.tag_unbind("food_image",'<Button-1>')
        gui.inventorygui.inv_canvas.tag_unbind("water_image",'<Button-1>') 
        gui.inventorygui.inv_canvas.tag_unbind("noitem_image",'<Button-1>') 
              
    def event_inv_clickable(self):
        '''
        A functions which binds all images in the inventory to go to a check for which item was clicked and then do something (for an event)
        '''
        #disables all buttons so one has to click the inventory
        self.textgui.disable_buttons()
        
        gui.inventorygui.inv_canvas.tag_bind("rifle_image",'<Button-1>',self.event_inv_click_check)
        gui.inventorygui.inv_canvas.tag_bind("knife_image",'<Button-1>',self.event_inv_click_check)
        gui.inventorygui.inv_canvas.tag_bind("rope_image",'<Button-1>',self.event_inv_click_check)
        gui.inventorygui.inv_canvas.tag_bind("painkiller_image",'<Button-1>',self.event_inv_click_check)
        gui.inventorygui.inv_canvas.tag_bind("antibiotic_image",'<Button-1>',self.event_inv_click_check)
        gui.inventorygui.inv_canvas.tag_bind("firstaidkit_image",'<Button-1>',self.event_inv_click_check)
        gui.inventorygui.inv_canvas.tag_bind("food_image",'<Button-1>',self.event_inv_click_check)
        gui.inventorygui.inv_canvas.tag_bind("water_image",'<Button-1>',self.event_inv_click_check)
        gui.inventorygui.inv_canvas.tag_bind("noitem_image",'<Button-1>',self.event_inv_click_check)
        
 
    def event_inv_click_check(self,event):
        '''
        A function is run when an image in the inventory is clicked while inv_clickable is active
        '''
        item_id=gui.inventorygui.inv_canvas.find_closest(event.x,event.y)
        item=gui.inventorygui.inv_canvas.gettags(item_id)
        item=item[0]
        if item=="rifle_image":
            if self.player.inventory.in_inventory("rifle")==True:
                self.player.inventory.SubInventory("rifle")
                self.inventorygui.set_inventory_num("rifle",self.player.inventory.get_inventory_item("rifle"))
                self.inv_unclickable()
                self.createdEvent.event.stepActionRifle()
                
        elif item=="knife_image":
            if self.player.inventory.in_inventory("knife")==True:
                self.player.inventory.SubInventory("knife")
                self.inventorygui.set_inventory_num("knife",self.player.inventory.get_inventory_item("knife"))
                self.inv_unclickable()
                self.createdEvent.event.stepActionKnife()
                
        elif item=="rope_image":
            if self.player.inventory.in_inventory("rope")==True:
                self.player.inventory.SubInventory("rope")
                self.inventorygui.set_inventory_num("rope",self.player.inventory.get_inventory_item("rope"))
                self.inv_unclickable()
                self.createdEvent.event.stepActionRope()
                
        #Medicine items should not be used during an event
        elif item=="painkiller_image":
            return

        elif item=="antibiotic_image":
            return
        elif item=="firstaidkit_image":
            return
        
        elif item=="food_image":
            if self.player.inventory.in_inventory("food")==True:
                self.player.inventory.SubInventory("food")
                self.inventorygui.set_inventory_num("food",self.player.inventory.get_inventory_item("food"))
                self.inv_unclickable()
                self.createdEvent.event.stepActionFood()
        elif item=="water_image":
            if self.player.inventory.in_inventory("water")==True:
                self.player.inventory.SubInventory("water")
                self.inventorygui.set_inventory_num("water",self.player.inventory.get_inventory_item("water"))
                self.inv_unclickable()
                self.createdEvent.event.stepActionWater()
        
        elif item=="noitem_image":
            self.inv_unclickable()
            self.createdEvent.event.stepActionNoItem()

    def night_inv_clickable(self):
        '''
        A functions which binds all images in the inventory to go to a check for which item was clicked and then do something(for the night)
        '''
        #Disables buttons so one cannot press next or the choices
        self.textgui.disable_buttons()
        
        gui.inventorygui.inv_canvas.tag_bind("rifle_image",'<Button-1>',self.night_inv_click_check)
        gui.inventorygui.inv_canvas.tag_bind("knife_image",'<Button-1>',self.night_inv_click_check)
        gui.inventorygui.inv_canvas.tag_bind("rope_image",'<Button-1>',self.night_inv_click_check)
        gui.inventorygui.inv_canvas.tag_bind("painkiller_image",'<Button-1>',self.night_inv_click_check)
        gui.inventorygui.inv_canvas.tag_bind("antibiotic_image",'<Button-1>',self.night_inv_click_check)
        gui.inventorygui.inv_canvas.tag_bind("firstaidkit_image",'<Button-1>',self.night_inv_click_check)
        gui.inventorygui.inv_canvas.tag_bind("food_image",'<Button-1>',self.night_inv_click_check)
        gui.inventorygui.inv_canvas.tag_bind("water_image",'<Button-1>',self.night_inv_click_check)
        gui.inventorygui.inv_canvas.tag_bind("noitem_image",'<Button-1>',self.night_inv_click_check)
            
    def night_inv_click_check(self,event):
        '''
        A function is run when an image in the inventory is clicked while inv_clickable is active (for the night choice)
        '''
        item_id=gui.inventorygui.inv_canvas.find_closest(event.x,event.y)
        item=gui.inventorygui.inv_canvas.gettags(item_id)
        item=item[0]
        if item=="painkiller_image":
            if self.player.inventory.in_inventory("painkiller")==True:
                self.inv_unclickable()
                self.night_time.stepAskPainkiller()

        elif item=="antibiotic_image":
            if self.player.inventory.in_inventory("antibiotic")==True:
                self.inv_unclickable()
                self.night_time.stepAskAntibiotic()
                
        elif item=="firstaidkit_image":
            if self.player.inventory.in_inventory("first aid kit")==True:
                self.inv_unclickable()
                self.night_time.stepAskFirstaidkit()
        
        elif item=="noitem_image":
            self.inv_unclickable()
            self.night_time.stepActionNoItem()
    
    
    def event_start_gui(self):
        '''
        A function which creates an event for during te day
        '''
        
        #Make it a while True loop later once its finished 
        self.clean_gui()
        gui.displaygui.set_background("pictures/forest.gif")
        #Don't think this goes through (not a big deal -same with night)
        self.set_text_message("You start a new day")
        self.text_change()
        self.textgui.enable_next_button()
        self.textgui.next_button.config(command=self.text_change)
        self.createdEvent=CreateEvent(self.player,self)
        self.createdEvent.event.text1()
    
    
    def night_start_gui(self):  
        '''
        A function which puts the player into the nighttime
        '''
        gui.displaygui.set_background("pictures/night.gif")
        self.set_text_message("It is now night")
        self.text_change()
        self.textgui.next_button.config(command=self.text_change)
        self.night_time=Night_Time(self.player,self)
        



if __name__ == '__main__':
    gui=GUI()
    gui.intro_gui()
    gui.root.mainloop()
        