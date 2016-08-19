

init -9 python:

    class Frisk(Monster):
        def __init__(self):
            Monster.__init__(self)
            self.default_event = Event("Frisk_manager_default",True,self)
            self.name = "Frisk"
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

            


label initialize_frisk:
    #here is where the sprites go

    define frisk = ('Frisk')
    define friskChar = Character('Frisk', color="#FFFFFF")
    python:
        def frisk(text, *args, **kwargs):
               friskChar(text, *args, **kwargs)
    return

#this is Toriels default scene
label Frisk_manager_default(owner = False):


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
