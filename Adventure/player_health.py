'''
A class which models the player
Created on Nov 20, 2017
@author: ngm7
'''
class Health():
    '''
    A class which keeps track of player health
    '''
    def __init__(self, gui, health=None, notSick=None):
        '''
        Initializes a players health to the default value of healthy
        5 is healthy, 4 is slightly damaged, 3 is hurt, 2 is deeply wounded, 1 is near death, 0 is dead
        '''
        if health is not None:
            self._health = health
        else:
            self._health = 5
            
        if notSick is not None:
            self._notSick = notSick
        else:
            self._notSick = True
            
        self.gui=gui


        
    def __str__(self):
        '''
        When the class is called as a string give a message detailing character's condition
        '''
        if self._health >= 9:
            #What occurs when you overdose
            self._health=5
            health_message= "You overdose on medicine. Your health resets (5)"
        elif self._health == 8:
            health_message= "You feel very lively thats for sure, you took too much medicine. You are this close to an overdose...(8)"
        elif self._health == 7:
            health_message= "You feel INCREDIBLY HEALTHY, you probably took too much medicine. Hopefully you won't overdose...(7)"
        elif self._health == 6:
            health_message= "You feel healthier than normal, you probably had more medicine than you needed but it's probably fine...(6)"
        elif self._health == 5: 
            health_message= "You feel normal, you can continue adventuring with ease.(5)"
        elif self._health == 4:
            health_message= "You feel slightly damaged, you are fine to keep going.(4)"
        elif self._health == 3:
            health_message= "You feel wounded, you should think of healing soon.(3)"
        elif self._health == 2:
            health_message= "You feel deeply wounded, you almost cannot keep going.(2)"
        elif self._health == 1:
            health_message= "You feel near death, you can scarcely even move and cannot keep going.(1)"
        elif self._health <= 0:
            return "You have died..."
        if self._notSick == False:
            return health_message+" You feel under the weather."
        else:
            return health_message
        
    def get_health(self):
        '''
        A function to get the integer value of health
        '''
        return int(self._health)
        
    def take_damage(self,damage=1):
        '''
        Induces damage on the character decreasing the characters health
        '''
        
        self._health = self._health - damage 
        #calls the gui to display the damage animation
        self.gui.displaygui.damage()
    
    def add_health(self,increase=1):
        '''
        Does the opposite of take_damage and adds health instead
        '''
        self._health = self._health + increase
    
    def heal_sickness(self):
        '''
        This function is called to heal the player of sickness
        '''
        self._notSick=True
    
    def induce_sickness(self):
        '''
        This function is called to make a player sick
        '''
        self._notSick=False
        
    def is_not_sick(self):
        '''
        A check for if the player is not sick
        '''
        return self._notSick
    
if __name__=="__main__":   
    player_health=Health()
    player_health.take_damage(5)