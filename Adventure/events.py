'''
Created on Nov 21, 2017
@author: ngm7
'''
import random
from player import *
from night_time import *
from GUI import *

class CreateEvent():
    '''
    An event should be created after every night and takes place during the day
    An event should display text describing a situation and then allowing the user to choose what to do (either by choosing an item or choice)
    This will then cause something to happen to the player (health change, item change)
    '''
    def __init__(self,player,gui,event_number=None):
        '''
        Constructs a random event (unless given event number to use)
        '''
        #If event number was specified make it the event number
        if event_number is not None:
            self.event_number=event_number
        #Otherwise check if the event randomlly has occured before to the player, if so get a new random event
        else:
            while True:
                self.event_number=random.randint(1,10)
        
                #Checks if the player has already had th event chosen and if so gets a new number
                
                if self.event_number in player.get_events_experienced():
                    continue
                else:
                    break
                
        
        if self.event_number==1:
            self.event=Event1(player,gui)
        elif self.event_number==2:
            self.event=Event2(player,gui)
        elif self.event_number==3:
            self.event=Event3(player,gui)
        elif self.event_number==4:
            self.event=Event4(player,gui)
        elif self.event_number==5:
            self.event=Event5(player,gui)
        elif self.event_number==6:
            self.event=Event6(player,gui)
        elif self.event_number==7:
            self.event=Event6(player,gui)
        elif self.event_number==8:
            self.event=Event8(player,gui)
        elif self.event_number==9:
            self.event=Event9(player,gui)
        elif self.event_number==10:
            self.event=Event10(player,gui)

        

    
class Event1():
    '''
    An Event 1 Class (THE WOLF ATTACK) (the GUI forces me to do a weird chain system (blah)) 
    '''
    
    def __init__(self,player,gui):
        '''
        Constructs a wolf attack event using player and gui. Also pauses and waits for the user to press the next button
        '''
        #WOLF ATTACK
        self.player=player
        self.gui=gui
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.text1)

    def text1(self):
        '''
        Displays text 1
        '''
        self.gui.text_message="You encounter a wolf pack closing in on you from the forest, they seem to be starved for food..."
        self.gui.text_change()
        self.gui.textgui.next_button.config(command=self.text2)
    
    def text2(self):
        '''
        Displays text 2
        '''
        self.gui.text_message="Please choose an item to use in this situation"
        self.gui.text_change()
        #Makes the inventory clickable to choose an item
        self.gui.event_inv_clickable()
    
    def stepActionRifle(self):
        '''
        A function which specifies what happens when one chooses the rifle in event 1
        '''        
        result=self.player.success_prob_physical(.7)
        if result == "success":
            self.gui.text_message="You shoot your gun towards the wolves. You scare the wolves off and even kill one of them which you can use for extra food. Your gun breaks..."
            self.gui.text_change()
            self.player.inventory.AddInventory("food",2)
            self.gui.inventorygui.set_inventory_num("food",self.player.inventory.get_inventory_item("food"))
            
        elif result == "failure":
            self.player.health.take_damage(1) 
            self.gui.text_message="You shoot your gun towards the wolves but can't seem to shoot straight. They run you down and attack you but you are able to fight them off after a few bites. Your gun breaks..."
            self.gui.text_change() 
        self.player.completedEvent(1)
        self.player.set_location()
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.stepResult)
        
    def stepActionKnife(self):
        '''
        A function which specifies what happens when one chooses the knife in event 1
        '''        
        result=self.player.success_prob_physical(.5)
        if result == "success":
            self.gui.text_message="You take out your knife and attempt to ward off the wolves in close combat. A wolf breaks out of the pack and rushes at you. You are able to stab the wolf through the head killing it instantly. The rest of the wolves disperse while you gather up the wolf for food. Your knife breaks..."
            self.gui.text_change()
            self.player.inventory.AddInventory("food",2)
            self.gui.inventorygui.set_inventory_num("food",self.player.inventory.get_inventory_item("food"))
            
        elif result == "failure":
            self.player.health.take_damage(1) 
            self.gui.text_message="You take out your knife and attempt to ward off the wolves in close combat. A wolf breaks out of the pack and rushes at you. The wolf clamps onto your arm as you attempt to swing your knife at it, creating deep teeth marks in the flesh. You are able to throw the wolf away and escape the wolves. Your knife breaks in the struggle..."
            self.gui.text_change() 
        self.player.completedEvent(1)
        self.player.set_location()
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.stepResult)
        
    def stepActionRope(self):
        '''
        A function which specifies what happens when one chooses the rope in event 1
        '''        
        result=self.player.success_prob_physical(.25)
        if result == "success":
            self.gui.text_message="You start swinging around some rope crazily. Surprisingly, the wolves seem confused and frightened by the action and eventually disperse. Your rope gets tangled in some branches, you don't want to stick around until the wolves come back and leave it."
            self.gui.text_change()
            
        elif result == "failure":
            self.player.health.take_damage(1) 
            self.gui.text_message="You start swinging around some rope crazily. Unsurprisingly the wolves are unimpressed and attempt to converge on you. You are able to escape eventually but not before becoming a chewing toy for the wolves. You leave your rope behind while running..."
            self.gui.text_change() 
        self.player.completedEvent(1)
        self.player.set_location()
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.stepResult)
        
    def stepActionFood(self):
        '''
        A function which specifies what happens when one chooses the food in event 1
        '''        
        result=self.player.success_prob(.7)
        if result == "success":
            self.gui.text_message="You throw some of your food off into the forest to divert the wolves attention. It seems to work and you escape unharmed."
            self.gui.text_change()
            
        elif result == "failure":
            self.player.health.take_damage(1) 
            self.gui.text_message="You throw some of your food off into the forest to divert the wolves attention. The wolves seem to find you much more appetizing though, and continue chasing you. You are able to escape eventually but not before becoming a chewing toy for the wolves."
            self.gui.text_change() 
        self.player.completedEvent(1)
        self.player.set_location()
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.stepResult)
    
    def stepActionWater(self):
        '''
        A function which specifies what happens when one chooses the water in event 1
        '''        
        result=self.player.success_prob(.21)
        if result == "success":
            self.gui.text_message="As a wolf attempts to run you down you throw water into its face. It startles the animal and the rest of the pack. They disperse leaving you unharmed."
            self.gui.text_change()
            
        elif result == "failure":
            self.player.health.take_damage(1) 
            self.gui.text_message="As a wolf attempts to run you down you throw water into its face. It becomes startled for a second but quickly starts biting at you. You are able to escape eventually but not before becoming a chewing toy for the wolves."
            self.gui.text_change() 
        self.player.completedEvent(1)
        self.player.set_location()
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.stepResult)
    
    def stepActionNoItem(self):
        '''
        A function which specifies what happens when one chooses no item in event 1
        '''
        result=self.player.success_prob(.21)
        if result == "success":
            self.gui.text_message="As a wolf attempts to run you down you start throwing out punches. One punch hits the animal in the nose, startling it. The pack disperses leaving you unharmed."
            self.gui.text_change()
            
        elif result == "failure":
            self.player.health.take_damage(1) 
            self.gui.text_message="As a wolf attempts to run you down, you attempt to punch the animal. It becomes startled for a second but quickly starts biting at you. You are able to escape eventually but not before becoming a chewing toy for the wolves."
            self.gui.text_change() 
        self.player.completedEvent(1)
        self.player.set_location()
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.stepResult)
    
    def stepResult(self):
        '''
        The ending function which takes the user to the night time
        '''        
        self.gui.text_message="Night finally approaches!"
        self.gui.text_change()
        self.gui.textgui.next_button.config(command=self.gui.night_start_gui)


class Event2():
    '''
    A class which models an event 2 (HERB FIND) (Also models the first dual choice event instead of inventory)
    '''
    def __init__(self,player,gui):
        '''
        Constructs a new event setting gui and player and having the player press the next button to continue
        '''
        self.player=player
        self.gui=gui
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.text1)

    def text1(self):
        '''
        Displays text 1
        '''
        self.gui.text_message="You stumble across a plant that looks like a medicinal herb you read about in a survival magazine."
        self.gui.text_change()
        self.gui.textgui.next_button.config(command=self.text2)
        
    def text2(self):
        '''
        Displays text 2
        '''
        self.gui.text_message="Do you wish to try one and confirm your suspicions?"
        self.gui.text_change()
        #Makes the inventory clickable to choose an item
        self.gui.textgui.enable_buttons()
        self.gui.textgui.button1.config(command=self.stepActionYes, text="Yes")
        self.gui.textgui.button2.config(command=self.stepActionNo, text="No")
        
    def stepActionYes(self):
        '''
        A function which models what happens when the player chooses yes
        '''
        #Determines if the player will be successful
        result=self.player.success_prob(.5)
        if result == "success":
            self.gui.text_message=("You take a nibble of the herb and it is exactly what you suspected it was, an all purpose healing herb. "
                                   "You gain health and, when the herb is fresh it seems to cure sickness as well. "
                                   "You take an extra herb with you (it acts as a first aid kit)")
            self.gui.text_change()
            self.player.inventory.AddInventory("first aid kit",1)
            self.player.health.add_health()
            self.player.health.heal_sickness()
            self.gui.inventorygui.set_inventory_num("first aid kit",self.player.inventory.get_inventory_item("first aid kit"))
            
        elif result == "failure":
            self.player.health.take_damage(1) 
            self.player.health.induce_sickness()
            self.gui.text_message="You take a nibble of the herb and begin to feel bad. You seem to have made a mistake (you have been hurt and become sick)."
            self.gui.text_change() 
        self.player.completedEvent(2)
        self.player.set_location()
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.stepResult)
    
    def stepActionNo(self):
        self.gui.text_message="You choose not to use the plant. The rest of the day passes uneventfully."
        self.gui.text_change()
        self.player.completedEvent(2)
        self.player.set_location()
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.stepResult)
    
    def stepResult(self):
        '''
        The ending function which takes the user to the night time
        '''        
        self.gui.text_message="Night finally approaches!"
        self.gui.text_change()
        self.gui.textgui.next_button.config(command=self.gui.night_start_gui)
        
        
class Event3():
    '''
    A class which models an event 3 (FRUIT FIND) 
    '''
    def __init__(self,player,gui):
        '''
        Constructs a new event setting gui and player and having the player press the next button to continue
        '''
        self.player=player
        self.gui=gui
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.text1)

    def text1(self):
        '''
        Displays text 1
        '''
        self.gui.text_message="You stumble across a bush that is full of ripe red berries"
        self.gui.text_change()
        self.gui.textgui.next_button.config(command=self.text2)
        
    def text2(self):
        '''
        Displays text 2
        '''
        self.gui.text_message="Do you wish to see if they are edible?"
        self.gui.text_change()
        #Makes the inventory clickable to choose an item
        self.gui.textgui.enable_buttons()
        self.gui.textgui.button1.config(command=self.stepActionYes, text="Yes")
        self.gui.textgui.button2.config(command=self.stepActionNo, text="No")
        
    def stepActionYes(self):
        '''
        A function which models what happens when the player chooses yes
        '''
        #Determines if the player will be successful
        result=self.player.success_prob(.5)
        if result == "success":
            self.gui.text_message=("You take a nibble of the berry and it is incredibly juicy and delicious."
                                   "You take a few with you for the journey.")
            self.gui.text_change()
            self.player.inventory.AddInventory("food",2)
            self.gui.inventorygui.set_inventory_num("food",self.player.inventory.get_inventory_item("food"))
            
        elif result == "failure":
            self.player.health.take_damage(1) 
            self.player.health.induce_sickness()
            self.gui.text_message="You take a nibble of the berry and begin to feel bad. The berry tastes awful and immediately upsets your stomach (you have been hurt and become sick)."
            self.gui.text_change() 
        self.player.completedEvent(3)
        self.player.set_location()
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.stepResult)
    
    def stepActionNo(self):
        self.gui.text_message="You choose not to eat the berry. The rest of the day passes uneventfully."
        self.gui.text_change()
        self.player.completedEvent(3)
        self.player.set_location()
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.stepResult)
    
    def stepResult(self):
        '''
        The ending function which takes the user to the night time
        '''        
        self.gui.text_message="Night finally approaches!"
        self.gui.text_change()
        self.gui.textgui.next_button.config(command=self.gui.night_start_gui)
        
        
class Event4():
    '''
    An Event 4 Class (FISHING POND)
    '''
    
    def __init__(self,player,gui):
        '''
        Constructs a fishing pond event using player and gui. Also pauses and waits for the user to press the next button
        '''
        #WOLF ATTACK
        self.player=player
        self.gui=gui
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.text1)

    def text1(self):
        '''
        Displays text 1
        '''
        self.gui.text_message="As you walk in the forest you notice a pond off to the side of the path. After approaching, you see countless fish but the water of the pond seems too dirty to drink. The fish, though, seem palpable."
        self.gui.text_change()
        self.gui.textgui.next_button.config(command=self.text2)
    
    def text2(self):
        '''
        Displays text 2
        '''
        self.gui.text_message="Please choose an item to use in this situation"
        self.gui.text_change()
        #Makes the inventory clickable to choose an item
        self.gui.event_inv_clickable()
    
    def stepActionRifle(self):
        '''
        A function which specifies what happens when one chooses the rifle in event 4
        '''        
        result=self.player.success_prob_physical(.35)
        if result == "success":
            self.gui.text_message="You shoot your gun into the pond. You actually are able to hit some fish surprisingly. Your gun breaks..."
            self.gui.text_change()
            self.player.inventory.AddInventory("food",2)
            self.gui.inventorygui.set_inventory_num("food",self.player.inventory.get_inventory_item("food"))
            
        elif result == "failure": 
            self.gui.text_message="You shoot your gun towards the pond but can't seem to hit a fish. Your gun breaks..."
            self.gui.text_change() 
        self.player.completedEvent(4)
        self.player.set_location()
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.stepResult)
        
    def stepActionKnife(self):
        '''
        A function which specifies what happens when one chooses the knife in event 4
        '''        
        result=self.player.success_prob_physical(.21)
        if result == "success":
            self.gui.text_message="You take out your knife and attempt to stab the fish in the pond. You actually manage to hit one. Your knife breaks..."
            self.gui.text_change()
            self.player.inventory.AddInventory("food",1)
            self.gui.inventorygui.set_inventory_num("food",self.player.inventory.get_inventory_item("food"))
            
        elif result == "failure":
            self.gui.text_message="You take out your knife and attempt to slash the fish in the pond. It does not work. Your knife breaks..."
            self.gui.text_change() 
        self.player.completedEvent(4)
        self.player.set_location()
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.stepResult)
        
    def stepActionRope(self):
        #FINISH HEREREWRWJF:OIJSOD
        '''
        A function which specifies what happens when one chooses the rope in event 4
        '''        
        result=self.player.success_prob_physical(.8)
        if result == "success":
            self.gui.text_message="You take some rope and use a strand of it to make fishing line. You use some of your food and some wire to catch some fish."
            self.gui.text_change()
            self.player.inventory.AddInventory("food",2)
            self.gui.inventorygui.set_inventory_num("food",self.player.inventory.get_inventory_item("food"))
            
        elif result == "failure":
            self.gui.text_message="You take some rope and use a strand of it to make a fishing line. Unfortunately, you can't seem to catch any fish."
            self.gui.text_change() 
        self.player.completedEvent(4)
        self.player.set_location()
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.stepResult)
        
    def stepActionFood(self):
        '''
        A function which specifies what happens when one chooses the food in event 4
        '''        
        result=self.player.success_prob(.35)
        if result == "success":
            self.gui.text_message="You use some of your food in the pond to lure the fish close to you"
            self.gui.text_change()
            self.player.inventory.AddInventory("food",1)
            self.gui.inventorygui.set_inventory_num("food",self.player.inventory.get_inventory_item("food"))
            
        elif result == "failure":
            self.gui.text_message="You attempt to bait fish with your food. They do not seem to care about it..."
            self.gui.text_change() 
        self.player.completedEvent(4)
        self.player.set_location()
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.stepResult)
    
    def stepActionWater(self):
        '''
        A function which specifies what happens when one chooses the water in event 4
        '''        

        self.gui.text_message="You take some water and throw it into the pond. Nice"
        self.gui.text_change()
        self.player.completedEvent(4)
        self.player.set_location()
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.stepResult)
    
    def stepActionNoItem(self):
        '''
        A function which specifies what happens when one chooses no item in event 4
        '''        

        self.gui.text_message="You attempt to catch the fish with your hands. It does not work."
        self.gui.text_change()
        self.player.completedEvent(4)
        self.player.set_location()
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.stepResult)
    
    
    def stepResult(self):
        '''
        The ending function which takes the user to the night time
        '''        
        self.gui.text_message="Night finally approaches!"
        self.gui.text_change()
        self.gui.textgui.next_button.config(command=self.gui.night_start_gui)
        
        
class Event5():
    '''
    An Event 5 Class (HUNTING) 
    '''
    
    def __init__(self,player,gui):
        '''
        Constructs a hunting event using player and gui. Also pauses and waits for the user to press the next button
        '''
        #WOLF ATTACK
        self.player=player
        self.gui=gui
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.text1)

    def text1(self):
        '''
        Displays text 1
        '''
        self.gui.text_message="As you walk along the path you see some deer crossing the path in front of you."
        self.gui.text_change()
        self.gui.textgui.next_button.config(command=self.text2)
    
    def text2(self):
        '''
        Displays text 2
        '''
        self.gui.text_message="Please choose an item to use in this situation"
        self.gui.text_change()
        #Makes the inventory clickable to choose an item
        self.gui.event_inv_clickable()
    
    def stepActionRifle(self):
        '''
        A function which specifies what happens when one chooses the rifle in event 5
        '''        
        result=self.player.success_prob_physical(.8)
        if result == "success":
            self.gui.text_message="You shoot your gun towards the deer. You scare the deer off but kill two of them which you can use for extra food. Your gun breaks..."
            self.gui.text_change()
            self.player.inventory.AddInventory("food",2)
            self.gui.inventorygui.set_inventory_num("food",self.player.inventory.get_inventory_item("food"))
            
        elif result == "failure":
            self.gui.text_message="You shoot your gun towards the deer but can't seem to shoot straight. Your gun breaks..."
            self.gui.text_change() 
        self.player.completedEvent(5)
        self.player.set_location()
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.stepResult)
        
    def stepActionKnife(self):
        '''
        A function which specifies what happens when one chooses the knife in event 5
        '''        
        result=self.player.success_prob_physical(.3)
        if result == "success":
            self.gui.text_message="You run at the deer with your knife out and catch the group off guard. You jump on one of them, taking them down. Your knife breaks..."
            self.gui.text_change()
            self.player.inventory.AddInventory("food",1)
            self.gui.inventorygui.set_inventory_num("food",self.player.inventory.get_inventory_item("food"))
            
        elif result == "failure":
            self.gui.text_message="You attempt to run at the deer with you knife out. They run away. Your knife breaks..."
            self.gui.text_change() 
        self.player.completedEvent(5)
        self.player.set_location()
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.stepResult)
        
    def stepActionRope(self):
        '''
        A function which specifies what happens when one chooses the rope in event 5
        '''        
        result=self.player.success_prob_physical(.25)
        if result == "success":
            self.gui.text_message="You make your rope into a lasso and catch a deer with it. You rope becomes useless in the struggle."
            self.gui.text_change()
            self.player.inventory.AddInventory("food",1)
            self.gui.inventorygui.set_inventory_num("food",self.player.inventory.get_inventory_item("food"))
            
        elif result == "failure":
            self.gui.text_message="You attempt to make a lasso out of your rope to catch the deer but mess up the knots. Your rope becomes useless and the deer run off."
            self.gui.text_change() 
        self.player.completedEvent(5)
        self.player.set_location()
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.stepResult)
        
    def stepActionFood(self):
        '''
        A function which specifies what happens when one chooses the food in event 5
        '''        
        result=self.player.success_prob(.30)
        if result == "success":
            self.gui.text_message="You attempt to bait the deer with some of your food. They actually seem interested and fearlessly approach you. You jump on a deer and take it down for food."
            self.gui.text_change()
            self.player.inventory.AddInventory("food",1)
            self.gui.inventorygui.set_inventory_num("food",self.player.inventory.get_inventory_item("food"))
            
        elif result == "failure":
            self.gui.text_message="You attempt to bait the deer with some of your food. They seem to not care and run away."
            self.gui.text_change() 
        self.player.completedEvent(5)
        self.player.set_location()
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.stepResult)
    
    def stepActionWater(self):
        '''
        A function which specifies what happens when one chooses the water in event 5
        '''        
        self.gui.text_message="You throw some water at the deer as you run at them. Nice"
        self.gui.text_change()
        self.player.completedEvent(5)
        self.player.set_location()
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.stepResult)
    
    def stepActionNoItem(self):
        '''
        A function which specifies what happens when one chooses no item in event 5
        '''        
        self.gui.text_message="You run at the deer with your fists. They scamper off into the woods."
        self.gui.text_change()
        self.player.completedEvent(5)
        self.player.set_location()
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.stepResult)
    
    def stepResult(self):
        '''
        The ending function which takes the user to the night time
        '''        
        self.gui.text_message="Night finally approaches!"
        self.gui.text_change()
        self.gui.textgui.next_button.config(command=self.gui.night_start_gui)

class Event6():
    '''
    An Event 6 Class (rappelling)
    '''
    
    def __init__(self,player,gui):
        '''
        Constructs a rappelling event using player and gui. Also pauses and waits for the user to press the next button
        '''
        self.player=player
        self.gui=gui
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.text1)

    def text1(self):
        '''
        Displays text 1
        '''
        self.gui.text_message="As you walk along the path, you eventually come across a sheer cliff in front of you. It looks like at one point there was some sort of ladder leading down the cliff but its unusable from age. It would take much too long to go around, you will have to climb down."
        self.gui.text_change()
        self.gui.textgui.next_button.config(command=self.text2)
    
    def text2(self):
        '''
        Displays text 2
        '''
        self.gui.text_message="Please choose an item to use in this situation"
        self.gui.text_change()
        #Makes the inventory clickable to choose an item
        self.gui.event_inv_clickable()
    
    def stepActionRifle(self):
        '''
        A function which specifies what happens when one chooses the rifle in event 6
        '''        
        self.gui.text_message="You take out a gun and...attempt to use it to get down the cliff? You fail and fall down."
        self.gui.text_change() 
        self.player.health.take_damage(1) 
        self.player.completedEvent(6)
        self.player.set_location()
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.stepResult)
        
    def stepActionKnife(self):
        '''
        A function which specifies what happens when one chooses the knife in event 6
        '''        
        result=self.player.success_prob_physical(.4)
        if result == "success":
            self.gui.text_message="You take out your knife and attempt to use it use it to help you get down the cliff. The knife sticks into the rockwall and allows you to, with some effort, get down the cliff."
            self.gui.text_change()
            
        elif result == "failure":
            self.gui.text_message="You take out your knife and attempt to use it use it to help you get down the cliff. You knife breaks soon after you try and use it and you plummet down the cliff."
            self.gui.text_change() 
            self.player.health.take_damage(1) 
        self.player.completedEvent(6)
        self.player.set_location()
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.stepResult)
        
    def stepActionRope(self):
        '''
        A function which specifies what happens when one chooses the rope in event 4
        '''        
        result=self.player.success_prob_physical(.8)
        if result == "success":
            self.gui.text_message="You take some rope and secure it to a nearby stump. You use it to rappel down the cliff safely."
            self.gui.text_change()
            
        elif result == "failure":
            self.gui.text_message="You take some rope and secure it to a nearby stump. You use it to rappel down the cliff but fall when the stump pulls out of the ground."
            self.gui.text_change() 
            self.player.health.take_damage(1) 
            
        self.player.completedEvent(6)
        self.player.set_location()
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.stepResult)
        
    def stepActionFood(self):
        '''
        A function which specifies what happens when one chooses the food in event 6
        '''        
        self.gui.text_message="You take some food and attempt to use it to help you get down the cliff... You fall down the cliff."
        self.gui.text_change() 
        self.player.set_location()
        self.gui.textgui.enable_next_button()
        self.player.health.take_damage(6) 
        self.gui.textgui.next_button.config(command=self.stepResult)
    
    def stepActionWater(self):
        '''
        A function which specifies what happens when one chooses the water in event 4
        '''        

        self.gui.text_message="You take some water and attempt to use it to help you get down the cliff... You fall down the cliff."
        self.gui.text_change() 
        self.player.set_location()
        self.gui.textgui.enable_next_button()
        self.player.health.take_damage(6) 
        self.gui.textgui.next_button.config(command=self.stepResult)
    
    def stepActionNoItem(self):
        '''
        A function which specifies what happens when one chooses no item in event 4
        '''        

        result=self.player.success_prob_physical(.35)
        if result == "success":
            self.gui.text_message="You try and climb down the cliff with your bare hands. Through some effort you make it safely down."
            self.gui.text_change()
            
        elif result == "failure":
            self.gui.text_message="You try and climb down the cliff with your bare hands. During the descent, your hand slips and you fall down."
            self.gui.text_change() 
            self.player.health.take_damage(1) 
            
        self.player.completedEvent(6)
        self.player.set_location()
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.stepResult)
    
    
    def stepResult(self):
        '''
        The ending function which takes the user to the night time
        '''        
        self.gui.text_message="Night finally approaches!"
        self.gui.text_change()
        self.gui.textgui.next_button.config(command=self.gui.night_start_gui)
        
class Event7():
    '''
    A class which models an event 7 (WATER FIND)
    '''
    def __init__(self,player,gui):
        '''
        Constructs a new event setting gui and player and having the player press the next button to continue
        '''
        self.player=player
        self.gui=gui
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.text1)

    def text1(self):
        '''
        Displays text 1
        '''
        self.gui.text_message="As you walk along the path you notice a creek running along side. The water looks clean but its hard to be sure."
        self.gui.text_change()
        self.gui.textgui.next_button.config(command=self.text2)
        
    def text2(self):
        '''
        Displays text 2
        '''
        self.gui.text_message="Do you wish to drink the water?"
        self.gui.text_change()
        #Makes the inventory clickable to choose an item
        self.gui.textgui.enable_buttons()
        self.gui.textgui.button1.config(command=self.stepActionYes, text="Yes")
        self.gui.textgui.button2.config(command=self.stepActionNo, text="No")
        
    def stepActionYes(self):
        '''
        A function which models what happens when the player chooses yes
        '''
        #Determines if the player will be successful
        result=self.player.success_prob(.5)
        if result == "success":
            self.gui.text_message=("You drink some of the water. It seems to be fine so you take a few extra bottles with you.")
            self.gui.text_change()
            self.player.inventory.AddInventory("water",3)
            self.gui.inventorygui.set_inventory_num("water",self.player.inventory.get_inventory_item("water"))
            
        elif result == "failure":
            self.player.health.take_damage(1) 
            self.player.health.induce_sickness()
            self.gui.text_message="You drink some of the water and begin to feel bad soon afterwards, the water seems to have been bad (you have been hurt and become sick)."
            self.gui.text_change() 
        self.player.completedEvent(7)
        self.player.set_location()
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.stepResult)
    
    def stepActionNo(self):
        self.gui.text_message="You choose not to drink from the stream. The rest of the day passes uneventfully."
        self.gui.text_change()
        self.player.completedEvent(7)
        self.player.set_location()
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.stepResult)
    
    def stepResult(self):
        '''
        The ending function which takes the user to the night time
        '''        
        self.gui.text_message="Night finally approaches!"
        self.gui.text_change()
        self.gui.textgui.next_button.config(command=self.gui.night_start_gui)
        
class Event8():
    '''
    A class which models an event 8 (Storage Find)
    '''
    def __init__(self,player,gui):
        '''
        Constructs a new event setting gui and player and having the player press the next button to continue
        '''
        self.player=player
        self.gui=gui
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.text1)

    def text1(self):
        '''
        Displays text 1
        '''
        self.gui.text_message="As you walk along the path you notice a cave off of the path. It looks like someone has lived in it in the past."
        self.gui.text_change()
        self.gui.textgui.next_button.config(command=self.text2)
        
    def text2(self):
        '''
        Displays text 2
        '''
        self.gui.text_message="Do you wish to enter the cave?"
        self.gui.text_change()
        #Makes the inventory clickable to choose an item
        self.gui.textgui.enable_buttons()
        self.gui.textgui.button1.config(command=self.stepActionYes, text="Yes")
        self.gui.textgui.button2.config(command=self.stepActionNo, text="No")
        
    def stepActionYes(self):
        '''
        A function which models what happens when the player chooses yes
        '''
        #Determines if the player will be successful
        result=self.player.success_prob(.5)
        if result == "success":
            self.gui.text_message=("You enter the cave and find a shelter and what looks to be a dead body, it seems like someone died of wounds in this cave. You take some of their items as they no longer need them.")
            self.gui.text_change()
            self.player.inventory.AddInventory("rifle",1)
            self.gui.inventorygui.set_inventory_num("rifle",self.player.inventory.get_inventory_item("rifle"))
            self.player.inventory.AddInventory("rope",1)
            self.gui.inventorygui.set_inventory_num("rope",self.player.inventory.get_inventory_item("rope"))
            
            
        elif result == "failure":
            self.player.health.take_damage(1) 
            self.gui.text_message="You enter the cave but are surprised by a bear which seems to have taken residence in this cave. The bear strikes at you throwing you backwards. You manage to escape the bear."
            self.gui.text_change() 
        self.player.completedEvent(8)
        self.player.set_location()
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.stepResult)
    
    def stepActionNo(self):
        self.gui.text_message="You choose not to enter the cave. The rest of the day passes uneventfully."
        self.gui.text_change()
        self.player.completedEvent(8)
        self.player.set_location()
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.stepResult)
    
    def stepResult(self):
        '''
        The ending function which takes the user to the night time
        '''        
        self.gui.text_message="Night finally approaches!"
        self.gui.text_change()
        self.gui.textgui.next_button.config(command=self.gui.night_start_gui)

#Temporary classes

class Event9():
    '''
    A class which models an event 7 as event 9 so as to run it again(WATER FIND)
    '''
    def __init__(self,player,gui):
        '''
        Constructs a new event setting gui and player and having the player press the next button to continue
        '''
        self.player=player
        self.gui=gui
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.text1)

    def text1(self):
        '''
        Displays text 1
        '''
        self.gui.text_message="As you walk along the path you notice a creek running along side. The water looks clean but its hard to be sure."
        self.gui.text_change()
        self.gui.textgui.next_button.config(command=self.text2)
        
    def text2(self):
        '''
        Displays text 2
        '''
        self.gui.text_message="Do you wish to drink the water?"
        self.gui.text_change()
        #Makes the inventory clickable to choose an item
        self.gui.textgui.enable_buttons()
        self.gui.textgui.button1.config(command=self.stepActionYes, text="Yes")
        self.gui.textgui.button2.config(command=self.stepActionNo, text="No")
        
    def stepActionYes(self):
        '''
        A function which models what happens when the player chooses yes
        '''
        #Determines if the player will be successful
        result=self.player.success_prob(.5)
        if result == "success":
            self.gui.text_message=("You drink some of the water. It seems to be fine so you take a few extra bottles with you.")
            self.gui.text_change()
            self.player.inventory.AddInventory("water",3)
            self.gui.inventorygui.set_inventory_num("water",self.player.inventory.get_inventory_item("water"))
            
        elif result == "failure":
            self.player.health.take_damage(1) 
            self.player.health.induce_sickness()
            self.gui.text_message="You drink some of the water and begin to feel bad soon afterwards, the water seems to have been bad (you have been hurt and become sick)."
            self.gui.text_change() 
        self.player.completedEvent(9)
        self.player.set_location()
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.stepResult)
    
    def stepActionNo(self):
        self.gui.text_message="You choose not to drink from the stream. The rest of the day passes uneventfully."
        self.gui.text_change()
        self.player.completedEvent(9)
        self.player.set_location()
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.stepResult)
    
    def stepResult(self):
        '''
        The ending function which takes the user to the night time
        '''        
        self.gui.text_message="Night finally approaches!"
        self.gui.text_change()
        self.gui.textgui.next_button.config(command=self.gui.night_start_gui)

class Event10():
    '''
    A class which models an event 8 but again as event 10 (Storage Find)
    '''
    def __init__(self,player,gui):
        '''
        Constructs a new event setting gui and player and having the player press the next button to continue
        '''
        self.player=player
        self.gui=gui
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.text1)

    def text1(self):
        '''
        Displays text 1
        '''
        self.gui.text_message="As you walk along the path you notice a cave off of the path. It looks like someone has lived in it in the past."
        self.gui.text_change()
        self.gui.textgui.next_button.config(command=self.text2)
        
    def text2(self):
        '''
        Displays text 2
        '''
        self.gui.text_message="Do you wish to enter the cave?"
        self.gui.text_change()
        #Makes the inventory clickable to choose an item
        self.gui.textgui.enable_buttons()
        self.gui.textgui.button1.config(command=self.stepActionYes, text="Yes")
        self.gui.textgui.button2.config(command=self.stepActionNo, text="No")
        
    def stepActionYes(self):
        '''
        A function which models what happens when the player chooses yes
        '''
        #Determines if the player will be successful
        result=self.player.success_prob(.5)
        if result == "success":
            self.gui.text_message=("You enter the cave and find a shelter and what looks to be a dead body, it seems like someone died of wounds in this cave. You take some of their items as they no longer need them.")
            self.gui.text_change()
            self.player.inventory.AddInventory("first aid kit",2)
            self.gui.inventorygui.set_inventory_num("first aid kit",self.player.inventory.get_inventory_item("first aid kit"))
            self.player.inventory.AddInventory("rope",1)
            self.gui.inventorygui.set_inventory_num("rope",self.player.inventory.get_inventory_item("rope"))
            
            
        elif result == "failure":
            self.player.health.take_damage(1) 
            self.gui.text_message="You enter the cave but are surprised by a bear which seems to have taken residence in this cave. The bear strikes at you throwing you backwards. You manage to escape the bear."
            self.gui.text_change() 
        self.player.completedEvent(10)
        self.player.set_location()
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.stepResult)
    
    def stepActionNo(self):
        self.gui.text_message="You choose not to enter the cave. The rest of the day passes uneventfully."
        self.gui.text_change()
        self.player.completedEvent(10)
        self.player.set_location()
        self.gui.textgui.enable_next_button()
        self.gui.textgui.next_button.config(command=self.stepResult)
    
    def stepResult(self):
        '''
        The ending function which takes the user to the night time
        '''        
        self.gui.text_message="Night finally approaches!"
        self.gui.text_change()
        self.gui.textgui.next_button.config(command=self.gui.night_start_gui)
        
if __name__=="__main__": 
    '''
    player = Player()
    player_states = Player_States()
    event1=Event(player,player_states,gui,1)
    event2=Event(player)
    event1=Event(player)
    event1=Event(player)
    event1=Event(player)
    event1=Event(player)
    event1=Event(player)
    event1=Event(player)
    event1=Event(player)
    '''
    
