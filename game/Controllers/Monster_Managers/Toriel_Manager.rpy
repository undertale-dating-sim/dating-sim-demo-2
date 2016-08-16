

init -9 python:

    class Toriel(Monster):
        def __init__(self):
            Monster.__init__(self)
            self.default_event = Event("Toriel_manager_default",True,self)
            self.name = "Toriel"
            self.FP = 20

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

            


label initialize_toriel:
        
    image toriel placeholder = "characters/Toriel/toriel_ph.png"
    image toriel angry = "characters/Toriel/Toriel_Angry_colored.png"
    image toriel annoyed = "characters/Toriel/Toriel_Annoyed_colors.png"
    image toriel awkward = "characters/Toriel/Toriel_Awkward_colors.png"
    image toriel blushing = "characters/Toriel/Toriel_Blushing_colors.png"
    image toriel laughing = "characters/Toriel/Toriel_Laughing_colors.png"
    image toriel normal = "characters/Toriel/Toriel_Neutral_colors.png"
    image toriel reallysad = "characters/Toriel/Toriel_ReallySad_colors.png"
    return

#this is Toriels default scene
label Toriel_manager_default(owner = False):
    
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

    call show_buttons
    $ renpy.pause()

    menu:
        "Raise FP 10":
            $ owner.FP += 10
        "Lower FP 10":
            $ owner.FP -= 10
        "Give Gift" if len(inventory.items) > 0:
            show screen gift_item_menu(owner)
            "What should you give them?"

    
    return
