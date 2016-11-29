

init -9 python:

    class Toriel(Monster):
        def __init__(self):
            Monster.__init__(self)
            self.default_event = Event("Toriel_manager_default",True,self)
            self.default_room = "Toriel's Room"
            self.name = "Toriel"
            self.FP = 20
            self.seed_default_schedule()
            self.default_sprite = "toriel normal"

        def give_gift(self,item):
            renpy.say(self.name,"Oh? What do you have there?")

            if isinstance(item,Spider_Cider):
                renpy.say(self.name,"Thank you! I love this!")
                self.FP += 20
                return True

            if isinstance(item,Spider_Donut):
                renpy.say(self.name,"I don't like donuts.")
                self.FP -= 20
                return False
            return
        def seed_default_schedule(self):
            self.reset_schedule() 
            #night
            self.update_schedule("Sunday","Night","Toriel's Room",self.default_event)
            self.update_schedule("Monday","Night","Toriel's Room",self.default_event)
            self.update_schedule("Tuesday","Night","Toriel's Room",self.default_event)
            self.update_schedule("Wednesday","Night","Toriel's Room",self.default_event)
            self.update_schedule("Thursday","Night","Toriel's Room",self.default_event)
            self.update_schedule("Friday","Night","Toriel's Room",self.default_event)
            self.update_schedule("Saturday","Night","Toriel's Room",self.default_event)
            #morning
            self.update_schedule("Sunday","Morning","Kitchen",self.default_event)
            #self.update_schedule("Monday","Morning","Kitchen",self.default_event)
            self.update_schedule("Monday","Morning","Basement Door",self.default_event)
            self.update_schedule("Tuesday","Morning","Kitchen",self.default_event)
            self.update_schedule("Wednesday","Morning","Kitchen",self.default_event)
            self.update_schedule("Thursday","Morning","Kitchen",self.default_event)
            self.update_schedule("Friday","Morning","Kitchen",self.default_event)
            self.update_schedule("Saturday","Morning","Kitchen",self.default_event)
            #day
            self.update_schedule("Sunday","Day","Cave Room",self.default_event)
            #self.update_schedule("Monday","Day","",self.default_event)
            self.update_schedule("Tuesday","Day","Cave Room",self.default_event)
            #self.update_schedule("Wednesday","Day","",self.default_event)
            self.update_schedule("Thursday","Day","Cave Room",self.default_event)
            #self.update_schedule("Friday","Day","",self.default_event)
            self.update_schedule("Saturday","Day","Cave Room",self.default_event)
            #afternoon
            self.update_schedule("Sunday","Afternoon","Spider Bakery",self.default_event)
            self.update_schedule("Monday","Afternoon","Dummy Room",self.default_event)
            self.update_schedule("Tuesday","Afternoon","Sassy Rock Room",self.default_event)
            self.update_schedule("Wednesday","Afternoon","Dummy Room",self.default_event)
            self.update_schedule("Thursday","Afternoon","Sassy Rock Room",self.default_event)
            self.update_schedule("Friday","Afternoon","Dummy Room",self.default_event)
            self.update_schedule("Saturday","Afternoon","Sassy Rock Room",self.default_event)
            #evening
            self.update_schedule("Sunday","Evening","Toriel's Room",self.default_event)
            self.update_schedule("Monday","Evening","Living Room",self.default_event)
            self.update_schedule("Tuesday","Evening","Living Room",self.default_event)
            self.update_schedule("Wednesday","Evening","Toriel's Room",self.default_event)
            self.update_schedule("Thursday","Evening","Living Room",self.default_event)
            self.update_schedule("Friday","Evening","Toriel's Room",self.default_event)
            self.update_schedule("Saturday","Evening","Living Room",self.default_event)
            


label initialize_toriel:
        
    image toriel placeholder = "characters/Toriel/toriel_ph.png"
    image toriel angry = "characters/Toriel/Toriel_Angry_colored.png"
    image toriel annoyed = "characters/Toriel/Toriel_Annoyed_colors.png"
    image toriel awkward = "characters/Toriel/Toriel_Awkward_colors.png"
    image toriel blushing = "characters/Toriel/Toriel_Blushing_colors.png"
    image toriel laughing = "characters/Toriel/Toriel_Laughing_colors.png"
    image toriel normal = "characters/Toriel/Toriel_Neutral_colors.png"
    image toriel reallysad = "characters/Toriel/Toriel_ReallySad_colors.png"

    define toriel = ('Toriel')
    define torielChar = Character('Toriel', color="#FFFFFF")
    python:
        def toriel(text, *args, **kwargs):
               torielChar(text, *args, **kwargs)
    return

#this is Toriels default scene
label Toriel_manager_default(owner = False,pause = True):
    
    if owner.FP < 20:
        show toriel reallysad
    elif owner.FP < 40:
        show toriel awkward
    elif owner.FP < 60:
        show toriel normal
    elif owner.FP < 80:
        show toriel laughing
    else:
        show toriel blushing

    if pause:
        $renpy.pause()
    call show_buttons from _call_show_buttons

    "Good morning!"
    
    menu:
        "Toriel"
        "Raise FP 10":
            $ owner.FP += 10
        "Lower FP 10":
            $ owner.FP -= 10
        "Give Gift" if len(inventory.items) > 0:
            show screen gift_item_menu(owner)
            "What should you give them?"
        "Exit":
            "okay."

    
    return
