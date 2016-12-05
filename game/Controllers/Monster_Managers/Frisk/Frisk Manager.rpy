

init -9 python:

    class Frisk(Monster):
        def __init__(self):
            Monster.__init__(self)
            self.default_event = Event("Frisk_manager_default",True,self)
            self.default_sprite = "frisk normal"
            self.name = "Frisk"
            self.FP = 20
            self.consumables_given = 0

        def give_item(self,item = False):

            # give_Gift_name_itemclassname
            # builds the label and calls it with current count + 1
            label_name = "give_Gift_%s_%s" % (self.name,item.get_class_name())

            if renpy.has_label(label_name):

                if self.given_today_count >= 5:
                    if not item.equip:
                        renpy.call_in_new_context("Frisk_Consumable_Reject",self)
                    else:
                        renpy.call_in_new_context("Frisk_Equip_Reject",self)

                else:
                    
                    response = renpy.call_in_new_context(label_name,self.get_total_specific_item(item) + 1,self)
                    
                    if response:
                        self.given_items[item.get_class_name()] = self.get_total_specific_item(item) + 1
                        #dirty check, but its easier than hiding it somewhere
                        if self.given_today_count == 0:
                            self.consumables_given = 0

                        self.given_today_count += 1

                        if not item.equip:
                            self.consumables_given += 1

                        if self.consumables_given == 3:
                            renpy.call_in_new_context("Frisk_Consumable_Warning")
                        elif self.given_today_count == 4:
                            renpy.call_in_new_context("Frisk_Equip_Warning")

                        

            else:
                renpy.call_in_new_context("give_Gift_%s_Unknown" % self.name)
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

    image frisk angry  = "characters/Frisk/Frisk_Angry.png"
    image frisk annoyed = "characters/Frisk/Frisk_Annoyed.png"
    image frisk bigsmile = "characters/Frisk/Frisk_BigSmile.png"
    image frisk disappointed = "characters/Frisk/Frisk_Disappointed.png"
    image frisk distant = "characters/Frisk/Frisk_Distant.png"
    image frisk normal = im.Scale("characters/Frisk/Frisk_Neutral.png",265,590)
    image frisk smallsmile = "characters/Frisk/Frisk_SmallSmile.png"
    image frisk soulless = "characters/Frisk/Frisk_Soulless.png"
    image frisk surprised = "characters/Frisk/Frisk_Surprised.png"
    image frisk tearyeyes = "characters/Frisk/Frisk_TearyEyes.png"
    image frisk upset = "characters/Frisk/Frisk_Upset.png"
    image frisk whatno = "Capture.PNG"
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
