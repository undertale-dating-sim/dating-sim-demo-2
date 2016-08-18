

init -9 python:

    class Napstablook(Monster):
        def __init__(self):
            Monster.__init__(self)
            self.default_event = Event("Napstablook_manager_default",True,self)
            self.name = "Napstablook"
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

            


label initialize_napstablook:
    #here is where the sprites go

    define napstablook = ('Napstablook')
    define napstablookChar = Character('Napstablook', color="#FFFFFF")
    python:
        def napstablook(text, *args, **kwargs):
               napstablookChar(text, *args, **kwargs)
    return

label Napstablook_manager_default(owner = False):


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
