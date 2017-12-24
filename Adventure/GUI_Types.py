from tkinter import *


class DisplayGUI():
    '''
    A class which determines the things displayed in the window in top left (should mostly be backgrounds except for store)
    '''
    def __init__(self,window):
        '''
        Creates the frame for the pictures, a canvas in the same space, and puts a default picture in the frame
        '''
        #Picture display
        self.display_frame=Frame(window, width=900 , height=480)
        self.display_frame.grid(row=0, column=0)
        
        self.display_canvas = Canvas(self.display_frame,bg = 'white',highlightthickness=0,width=900 , height=480)
        self.display_canvas.grid(row=0, column=0)
        
        self.background_image=PhotoImage(file="pictures/intro.gif")
        self.background_canvas = self.display_canvas.create_image(450,240,image=self.background_image,tags="background")
        
        self.window=window
        

        
    
    def set_background(self,newImagePath):
        '''
        A function which changes the background image of the event display
        '''
        self.new_background=PhotoImage(file=newImagePath)
        self.display_canvas.itemconfigure(self.background_canvas,image=self.new_background)
        self.current_image=newImagePath
        
    def damage(self):
        '''
        A function which gives a visual representation of when damage is done to the player
        '''
        self.new_background=PhotoImage(file="pictures/damage.gif")
        self.display_canvas.itemconfigure(self.background_canvas,image=self.new_background)
        self.window.after(200,self.damage_animation)
        
    def damage_animation(self):
        '''
        The function the after calls in damage which sets the background back to previous image
        '''    
        self.set_background(self.current_image)
    
        

class TextGUI():
    def __init__(self,window):
        '''
        Initializes the bottom window and displays default text
        '''
        #Text display
        self.text_frame=Frame(window, width=900 , height=240, bg="#%02x%02x%02x" % (178,151,114))
        self.text_frame.grid(row=1, column=0)
        #Taken from Effbot on grid
        self.text_frame.grid_propagate(False)
        self.text=StringVar()
        self.text.set("Welcome to the game! In this game, you are traveling to your destination through the woods. Your progress is displayed on the bottom of the screen. Your health is displayed every night and you eat one food and one water each night as well. If you become sick the chances of you succeeding in a task become greatly lowered. Press the arrow to start the game.")
        self.text_label = Label(self.text_frame, textvariable=self.text,font=("Courier New", 17),bg="#%02x%02x%02x" % (178,151,114),wraplength=860,justify=LEFT)
        self.text_label.grid(row=0, column=0, sticky=W)
        
        #Creates a button which should be used to advance 
        self.next_button = Button(self.text_frame, text="-->",font=("Courier New", 15),width=4)
        self.next_button.place(x=900,y=240,anchor=SE)
        
        #Creates buttons for yes/choice 1 and no/choice2
        self.button1 = Button(self.text_frame, text="",font=("Courier New", 15),width=4,state=DISABLED)
        self.button2 = Button(self.text_frame, text="",font=("Courier New", 15),width=4,state=DISABLED)
        self.button1.place(x=900,y=160,anchor=SE)
        self.button2.place(x=900,y=200,anchor=SE)
        
        #Creates a location marker image
        self.location_image = PhotoImage(file="pictures/marker/location1.gif")
        self.location_label = Label(self.text_frame,image=self.location_image,width=826,bg="#%02x%02x%02x" % (178,151,114))
        #original is 419
        self.location_label.place(x=409,y=241, anchor=S)
        
    def change_location(self,newImagePath):
        '''
        A function which changes the location marker image to the correct place
        '''
        self.new_location_image= PhotoImage(file=newImagePath)
        self.location_label.config(image=self.new_location_image)
        
    def enable_buttons(self):
        '''
        A function which enables the choice buttons while disabling the next button
        '''
        self.button1.config(state=NORMAL)
        self.button2.config(state=NORMAL)
        self.next_button.config(state=DISABLED)
        
        
    def enable_next_button(self):
        '''
        A function which enables the next button while disabling the choice buttons
        '''
        self.next_button.config(state=NORMAL)
        self.button1.config(state=DISABLED)
        self.button2.config(state=DISABLED)
    
    def disable_buttons(self):
        '''
        A function which disables all buttons (to be used when selecting from inventory)
        '''
        self.next_button.config(state=DISABLED)
        self.button1.config(state=DISABLED)
        self.button2.config(state=DISABLED)
        
    def set_text(self,newText):
        '''
        A function which sets the textbox to a new line of text and waits for user input
        '''
        self.text.set(newText)
         
    
class InventoryGUI():
    '''
    A GUI for the top left window that displays the number of an item the player has
    '''
    def __init__(self,window):
        '''
        Creates pictures of the items in the inventory and sets a default amount of the item in text form
        '''
        #Inventory display
        self.inv_frame=Frame(window, width=380 , height=720,bg="#%02x%02x%02x" % (178,151,114))
        self.inv_frame.grid(row=0,column=1,rowspan=2)
        
        #Taken from Effbot on grid
        self.inv_frame.grid_propagate(False)
        self.inv_canvas = Canvas(self.inv_frame,bg = "#%02x%02x%02x" % (178,151,114),width=380,height=720,highlightthickness=0)
        self.inv_canvas.grid(row=0, column=0)
        
        #Creates an text box that says INVENTORY
        self.inv_canvas.create_text(190,0,text='INVENTORY',font=("Courier New", 20, "bold underline"),anchor=N)
        
        #Creates an text box that says MEDICINE
        self.inv_canvas.create_text(190,400,text='MEDICINE',font=("Courier New", 20, "bold underline"),anchor=N)
        
        #CREATION OF ITEM PICTURES AND AMOUNTS
        self.rifle_image=PhotoImage(file="pictures/rifle.gif")
        self.rifle_check=self.inv_canvas.create_image(47.5,90,image=self.rifle_image,tags="rifle_image")
        self.rifle_num=StringVar()
        self.rifle_num.set('0')
        self.rifle_id=self.inv_canvas.create_text(33.5,140,text=self.rifle_num.get(),font=("Courier New", 15, "bold"))
        
        self.knife_image=PhotoImage(file="pictures/knife.gif")
        self.inv_canvas.create_image(190,90,image=self.knife_image,tags="knife_image")
        self.knife_num=StringVar()
        self.knife_num.set('0')
        self.knife_id=self.inv_canvas.create_text(167,140,text=self.knife_num.get(),font=("Courier New", 15, "bold"))
        
        self.rope_image=PhotoImage(file="pictures/rope.gif")
        self.inv_canvas.create_image(332.5,90,image=self.rope_image,tags="rope_image")
        self.rope_num=StringVar()
        self.rope_num.set('0')
        self.rope_id=self.inv_canvas.create_text(309.5,140,text=self.rope_num.get(),font=("Courier New", 15, "bold"))
        
        self.painkiller_image=PhotoImage(file="pictures/painkiller.gif")
        self.inv_canvas.create_image(47.5,490,image=self.painkiller_image,tags="painkiller_image")
        self.painkiller_num=StringVar()
        self.painkiller_num.set('0')
        self.painkiller_id=self.inv_canvas.create_text(33.5,540,text=self.painkiller_num.get(),font=("Courier New", 15, "bold"))

        self.antibiotic_image=PhotoImage(file="pictures/antibiotic.gif")
        self.inv_canvas.create_image(190,490,image=self.antibiotic_image,tags="antibiotic_image")
        self.antibiotic_num=StringVar()
        self.antibiotic_num.set('0')
        self.antibiotic_id=self.inv_canvas.create_text(167,540,text=self.antibiotic_num.get(),font=("Courier New", 15, "bold"))
        
        self.firstaidkit_image=PhotoImage(file="pictures/firstaidkit.gif")
        self.inv_canvas.create_image(332.5,490,image=self.firstaidkit_image,tags="firstaidkit_image")
        self.firstaidkit_num=StringVar()
        self.firstaidkit_num.set('0')
        self.firstaidkit_id=self.inv_canvas.create_text(309.5,540,text=self.firstaidkit_num.get(),font=("Courier New", 15, "bold"))
        
        self.food_image=PhotoImage(file="pictures/food.gif")
        self.inv_canvas.create_image(47.5,220,image=self.food_image,tags="food_image")
        self.food_num=StringVar()
        self.food_num.set('0')
        self.food_id=self.inv_canvas.create_text(33.5,270,text=self.food_num.get(),font=("Courier New", 15, "bold"))
        
        self.water_image=PhotoImage(file="pictures/water.gif")
        self.inv_canvas.create_image(190,220,image=self.water_image,tags="water_image")
        self.water_num=StringVar()
        self.water_num.set('0')
        self.water_id=self.inv_canvas.create_text(167,270,text=self.water_num.get(),font=("Courier New", 15, "bold"))
        
        self.noitem_image=PhotoImage(file="pictures/noitem.gif")
        self.inv_canvas.create_image(330,697,image=self.noitem_image,tags="noitem_image")

    def set_inventory_num(self,item,amount):
        '''
        A function used to change the text values in the inventory for items taking the item in question and the amount of the item
        '''
        if item=='rifle':
            self.inv_canvas.itemconfig(self.rifle_id, text=str(amount))
        elif item=='knife':
            self.inv_canvas.itemconfig(self.knife_id, text=str(amount))
        elif item=='rope':
            self.inv_canvas.itemconfig(self.rope_id, text=str(amount))
        elif item=='painkiller':
            self.inv_canvas.itemconfig(self.painkiller_id, text=str(amount))
        elif item=='antibiotic':
            self.inv_canvas.itemconfig(self.antibiotic_id, text=str(amount))
        elif item=='first aid kit':
            self.inv_canvas.itemconfig(self.firstaidkit_id, text=str(amount))
        elif item=='food':
            self.inv_canvas.itemconfig(self.food_id, text=str(amount))
        elif item=='water':
            self.inv_canvas.itemconfig(self.water_id, text=str(amount))



        
        
if __name__ == '__main__':
    root = Tk()
    root.title("TEST")
    #FIXME: Got ONlINE
    root.geometry("1280x720")   
    root.resizable(0,0) 
    
    displaygui=DisplayGUI(root)
    inventorygui=InventoryGUI(root)
    textgui=TextGUI(root)
    displaygui.shop_gui()
    inventorygui.inv_clickable()
    displaygui.set_purse_num(100)
    root.mainloop()
   

    