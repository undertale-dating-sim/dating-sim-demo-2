

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

        def handle_schedule(self):
            #night
            self.update_schedule("Sunday","Night","Frisk's Room",self.default_event)
            self.update_schedule("Monday","Night","Frisk's Room",self.default_event)
            self.update_schedule("Tuesday","Night","Frisk's Room",self.default_event)
            self.update_schedule("Wednesday","Night","Frisk's Room",self.default_event)
            self.update_schedule("Thursday","Night","Frisk's Room",self.default_event)
            self.update_schedule("Friday","Night","Frisk's Room",self.default_event)
            self.update_schedule("Saturday","Night","Frisk's Room",self.default_event)
            #morning
            self.update_schedule("Sunday","Morning","Overlook",self.default_event)
            self.update_schedule("Monday","Morning","Grass Room",self.default_event)
            self.update_schedule("Tuesday","Morning","Grass Room",self.default_event)
            self.update_schedule("Wednesday","Morning","Frisk's Room",self.default_event)
            self.update_schedule("Thursday","Morning","Dummy Room",self.default_event)
            self.update_schedule("Friday","Morning","Frisk's Room",self.default_event)
            self.update_schedule("Saturday","Morning","Dummy Room",self.default_event)
            #day
            self.update_schedule("Sunday","Day","Snail Hunting Room",self.default_event)
            self.update_schedule("Monday","Day","Snail Hunting Room",self.default_event)
            self.update_schedule("Tuesday","Day","Snail Hunting Room",self.default_event)
            self.update_schedule("Wednesday","Day","Snail Hunting Room",self.default_event)
            self.update_schedule("Thursday","Day","Snail Hunting Room",self.default_event)
            self.update_schedule("Friday","Day","Snail Hunting Room",self.default_event)
            self.update_schedule("Saturday","Day","Snail Hunting Room",self.default_event)
            #afternoon
            self.update_schedule("Sunday","Afternoon","Black Tree Room",self.default_event)
            self.update_schedule("Monday","Afternoon","Black Tree Room",self.default_event)
            self.update_schedule("Tuesday","Afternoon","Frisk's Room",self.default_event)
            self.update_schedule("Wednesday","Afternoon","Black Tree Room",self.default_event)
            self.update_schedule("Thursday","Afternoon","Frisk's Room",self.default_event)
            self.update_schedule("Friday","Afternoon","Black Tree Room",self.default_event)
            self.update_schedule("Saturday","Afternoon","Frisk's Room",self.default_event)
            #evening
            self.update_schedule("Sunday","Evening","Living Room",self.default_event)
            #self.update_schedule("Monday","Evening","Living Room",self.default_event)
            self.update_schedule("Tuesday","Evening","Frisk's Room",self.default_event)
            #self.update_schedule("Wednesday","Evening","Toriel's Room",self.default_event)
            self.update_schedule("Thursday","Evening","Frisk's Room",self.default_event)
            #self.update_schedule("Friday","Evening","Toriel's Room",self.default_event)
            self.update_schedule("Saturday","Evening","Frisk's Room",self.default_event)

            


label initialize_frisk:
    #here is where the sprites go

    define frisk = ('Frisk')
    define friskChar = Character('Frisk', color="#FFFFFF")
    python:
        def frisk(text, *args, **kwargs):
               friskChar(text, *args, **kwargs)
    return

#this is Toriels default scene
label Frisk_manager_default(owner = False,pause = True):


    call show_buttons from _call_show_buttons_6
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
