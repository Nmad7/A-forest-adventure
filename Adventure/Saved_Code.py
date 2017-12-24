'''
Created on Nov 21, 2017

@author: ngm7
'''

#Went in the store class(need to add subtraction of money)
def buyingPhase(self):
        '''
        A function that should be called when the player is at the store buying items
        '''
        while True:
            print("Your inventory contains:\n"+player.inventory.get_inventory())
            input("Press Enter to continue")
            print("These are the items in the shop:\n"+str(shop))
            print("The money in your purse adds up to: "+str(shop.get_purse()))
            item=input("Please enter the name of an item you wish to purchase: ")
            amount=input("Please enter how many "+item+"s you wish to purchase: ")
            if self._itemPrice[item]*int(amount) > self._purse:
                print("That is too expensive for you!")
            else:
                player.inventory.AddInventory(item,int(amount))
                print("You have bought "+amount+" "+item)
            choice=input("Do you wish to keep shopping? Y/N: ")
            if choice == 'Y' or choice == 'y' or choice == 'yes' or choice == 'Yes':
                continue
            else:
                break
            
            
def shop_gui(self):
        '''
        A function which creates a shop GUI in the display window
        This shop GUI has the items displayed along with their price
        '''
        #Set the background to be the shop
        self.set_background("pictures/shop.gif")
        
        #Creates an text box that says INVENTORY
        self.display_canvas.create_text(450,0,text='STORE',font=("Courier New", 20, "bold underline italic"),anchor=N,tags="store_item")
        
        #CREATION OF ITEM PICTURES AND PRICE
        self.rifle_image=PhotoImage(file="pictures/rifle.gif")
        self.display_canvas.create_image(150,90,image=self.rifle_image,tags=("store_item","store_rifle"))
        self.display_canvas.create_text(150,140,text='500',font=("Courier New", 15, "bold"),tags=("store_item","store_rifle"))
        
        self.knife_image=PhotoImage(file="pictures/knife.gif")
        self.display_canvas.create_image(300,90,image=self.knife_image,tags=("store_item","store_knife"))
        self.display_canvas.create_text(300,140,text='200',font=("Courier New", 15, "bold"),tags=("store_item","store_knife"))
        
        self.rope_image=PhotoImage(file="pictures/rope.gif")
        self.display_canvas.create_image(450,90,image=self.rope_image,tags=("store_item","store_rope"))
        self.display_canvas.create_text(450,140,text='200',font=("Courier New", 15, "bold"),tags=("store_item","store_rope"))
        
        self.painkiller_image=PhotoImage(file="pictures/painkiller.gif")
        self.display_canvas.create_image(600,90,image=self.painkiller_image,tags=("store_item","store_painkiller"))
        self.display_canvas.create_text(600,140,text='100',font=("Courier New", 15, "bold"),tags=("store_item","store_painkiller"))

        self.antibiotic_image=PhotoImage(file="pictures/antibiotic.gif")
        self.display_canvas.create_image(750,90,image=self.antibiotic_image,tags=("store_item","store_antibiotic"))
        self.display_canvas.create_text(750,140,text='300',font=("Courier New", 15, "bold"),tags="store_item")
        
        self.firstaidkit_image=PhotoImage(file="pictures/firstaidkit.gif")
        self.display_canvas.create_image(150,200,image=self.firstaidkit_image,tags=("store_item","store_firstaidkit"))
        self.display_canvas.create_text(150,250,text='300',font=("Courier New", 15, "bold"),tags="store_item")
        
        self.food_image=PhotoImage(file="pictures/food.gif")
        self.display_canvas.create_image(300,200,image=self.food_image,tags=("store_item","store_food"))
        self.display_canvas.create_text(300,250,text='20',font=("Courier New", 15, "bold"),tags="store_item")
        
        self.water_image=PhotoImage(file="pictures/water.gif")
        self.display_canvas.create_image(450,200,image=self.water_image,tags=("store_item","store_water"))
        self.display_canvas.create_text(450,250,text='30',font=("Courier New", 15, "bold"),tags="store_item")
        
        #Creation of purse
        self.purse_num=StringVar()
        self.purse_num.set('2000')
        self.purse_id=self.display_canvas.create_text(650,0,text="Purse: "+self.purse_num.get(),font=("Courier New", 20, "underline italic"),anchor=N,tags="store_item")
        
        #Raises the items above the background
        self.display_canvas.tag_raise("store_item")
        
        #Activates the canvas for clicking items
        self.display_canvas.tag_bind("store_rifle",'<Button-1>',self.store_click_check)
        self.display_canvas.tag_bind("store_knife",'<Button-1>',self.store_click_check)
        self.display_canvas.tag_bind("store_rope",'<Button-1>',self.store_click_check)
        self.display_canvas.tag_bind("store_painkiller",'<Button-1>',self.store_click_check)
        self.display_canvas.tag_bind("store_antibiotic",'<Button-1>',self.store_click_check)
        self.display_canvas.tag_bind("store_firstaidkit",'<Button-1>',self.store_click_check)
        self.display_canvas.tag_bind("store_food",'<Button-1>',self.store_click_check)
        self.display_canvas.tag_bind("store_water",'<Button-1>',self.store_click_check)    
    
    def set_purse_num(self,amount):
        '''
        A function used to change the text value for the purse amount
        '''
        self.display_canvas.itemconfig(self.purse_id, text="Purse: "+str(amount))
    
    def store_click_check(self,event):
        '''
        A function is run when an image in the store is clicked while store_clickable is active
        '''
        id=self.display_canvas.find_closest(event.x,event.y)
        item=self.display_canvas.gettags(id)
        item=item[1]
        if item=="store_rifle":
            self.notClicked=False
            return "rifle"
        elif item=="store_knife":
            self.notClicked=False
            return
        elif item=="store_rope":
            self.notClicked=False
            return "rope"
        elif item=="store_painkiller":
            self.notClicked=False
            return "painkiller"
        elif item=="store_antibiotic":
            self.notClicked=False
            return "antibiotic"
        elif item=="store_firstaidkit":
            self.notClicked=False
            return "first aid kit"
        elif item=="store_food":
            self.notClicked=False
            return "food"
        elif item=="store_water":
            self.notClicked=False
            return "water"