

init -9 python:

    class Flowey(Monster):
        def __init__(self):
            Monster.__init__(self)
            self.default_event = Event("flowey_manager_default",True,0,self)
            self.name = "Flowey"
            self.handle_schedule()
            self.default_sprite = 'flowey normal'
            self.hover_sprite = "flowey annoyed"
            self.cell_phone_pic = "UI/flowey.png"



        def handle_relationship_requirements(self):

            self.d_1 = {}
            self.d_2 = {}
            self.d_3 = {}
            self.d_4 = {}
            self.dating_requirements = {}

            yellow = "#ffff00"
            red = "#f00"
            green = "#00ff00"


            if 'Flowey_Hangout_1_Complete' in player.variables:
                self.d_1["Complete!"] = True
            elif world.day > 0:
                self.d_1["Go find Flowey!"] = False
            else:
                self.d_1["Day > 0"] = world.day > 0


            if 'Flowey_Hangout_2_Complete' in player.variables:
                self.d_2["Complete!"] = True
            elif "Flowey_Hangout_1_Complete" in player.variables:
                self.d_2 = {"Go find Flowey!" : False}
            else:
                self.d_2 = {"Hangout 1 Complete": "Flowey_Hangout_1_Complete" in player.variables}


            if 'Flowey_Hangout_2_Complete' not in player.variables:
                self.dating_requirements["{color=%s}I'm Not Datable!{/color}" % red] = self.d_2
            else:
                self.dating_requirements["{color=%s}I'm Not Datable!{/color}" % green] = self.d_2

            if 'Flowey_Hangout_1_Complete' not in player.variables:
                self.dating_requirements["{color=%s}The Not Friendly Flower{/color}" % red] = self.d_1
            else:
                self.dating_requirements["{color=%s}The Not Friendly Flower{/color}" % green] = self.d_1



            return

        def handle_special_events(self):

            #hangout 1, done when the tutorial is over
            if "Flowey_Hangout_1_Complete" not in player.variables and world.day > 0 and world.current_timezone != "Evening":
                self.special_event = Event('flowey_hangout1',False,0,self)
            elif "Flowey_Hangout_2_Complete" not in player.variables and world.day > 0:
                self.special_event = Event('Flowey_Hangout_1_5',False,0,self)
            else:
                self.remove_event()
            return




    #update_schedule(self,day,timezone,location,event):

        def handle_schedule(self):
            #night
            self.update_schedule("Sunday","Night","Cave Room",self.default_event)
            self.update_schedule("Monday","Night","Cave Room",self.default_event)
            self.update_schedule("Tuesday","Night","Cave Room",self.default_event)
            self.update_schedule("Wednesday","Night","Cave Room",self.default_event)
            self.update_schedule("Thursday","Night","Cave Room",self.default_event)
            self.update_schedule("Friday","Night","Cave Room",self.default_event)
            self.update_schedule("Saturday","Night","Cave Room",self.default_event)
            #morning
            self.update_schedule("Sunday","Morning","Overlook",self.default_event)
            self.update_schedule("Monday","Morning","Cave Room",self.default_event)
            #self.update_schedule("Monday","Morning","Basement Door",self.default_event)
            self.update_schedule("Tuesday","Morning","Cave Room",self.default_event)
            self.update_schedule("Wednesday","Morning","Grass Room",self.default_event)
            self.update_schedule("Thursday","Morning","Cave Room",self.default_event)
            self.update_schedule("Friday","Morning","Grass Room",self.default_event)
            self.update_schedule("Saturday","Morning","Grass Room",self.default_event)
            #day
            #self.update_schedule("Sunday","Day","Cave Room",self.default_event)
            self.update_schedule("Monday","Day","Ruins Entrance",self.default_event)
            self.update_schedule("Tuesday","Day","Overlook",self.default_event)
            self.update_schedule("Wednesday","Day","Ruins Entrance",self.default_event)
            self.update_schedule("Thursday","Day","Overlook",self.default_event)
            self.update_schedule("Friday","Day","Ruins Entrance",self.default_event)
            self.update_schedule("Saturday","Day","Overlook",self.default_event)
            #afternoon
            self.update_schedule("Sunday","Afternoon","Grass Room",self.default_event)
            self.update_schedule("Monday","Afternoon","Grass Room",self.default_event)
            self.update_schedule("Tuesday","Afternoon","Grass Room",self.default_event)
            self.update_schedule("Wednesday","Afternoon","Cave Room",self.default_event)
            self.update_schedule("Thursday","Afternoon","Grass Room",self.default_event)
            self.update_schedule("Friday","Afternoon","Cave Room",self.default_event)
            self.update_schedule("Saturday","Afternoon","Cave Room",self.default_event)
            #evening
            #self.update_schedule("Sunday","Evening","Cave Room",self.default_event)
            self.update_schedule("Monday","Evening","Snail Hunting Room",self.default_event)
            #self.update_schedule("Tuesday","Evening","Cave Room",self.default_event)
            self.update_schedule("Wednesday","Evening","Snail Hunting Room",self.default_event)
            #self.update_schedule("Thursday","Evening","Cave Room",self.default_event)
            self.update_schedule("Friday","Evening","Snail Hunting Room",self.default_event)
            #self.update_schedule("Saturday","Evening","Cave Room",self.default_event)


label initialize_flowey:
    image flowey angry = "characters/Flowey/FloweyLineart-Angrycolor.png"
    image flowey annoyed = "characters/Flowey/FloweyLineart-Annoyedcolor.png"
    image flowey backside = "characters/Flowey/FloweyLineart-Backsidecolor.png"
    image flowey blush = "characters/Flowey/FloweyLineart-bashfulcolor.png"
    image flowey excited = "characters/Flowey/FloweyLineart-Excitedcolor.png"
    image flowey horror = "characters/Flowey/FloweyLineart-Horrorcolor.png"
    image flowey laugh = "characters/Flowey/FloweyLineart-LaughingColor.png"
    image flowey normal = "characters/Flowey/FloweyLineart-Normalcolor1.png"
    image flowey sad = "characters/Flowey/FloweyLineart-Sadcolor.png"
    image flowey sideglance = "characters/Flowey/FloweyLineart-SideGlarecolor.png"
    image flowey smug = "characters/Flowey/FloweyLineart-Smugcolor.png"
    image flowey surprised = "characters/Flowey/FloweyLineart-Surprisedcolorcorrected.png"
    image flowey suspicious = "characters/Flowey/FloweyLineart-Suspiciouscolor.png"
    image flowey wink = "characters/Flowey/FloweyLineart-Winkcolor.png"

    define flowey = ('Flowey')
    define floweyChar = Character('Flowey', color="#FFFFFF")
    
    python:
        def flowey(text, *args, **kwargs):
            floweyChar(text, *args, **kwargs)


    define flowey = Character('Flowey', color="#FFFFFF")
    define unknown = Character('?????', color = "#FFFFFF")
    
    return

#this is floweys default scene
label flowey_manager_default(owner = False,pause = True):
    
    if renpy.music.get_playing() != "audio/ruins/flowey.mp3":
        play music "audio/ruins/flowey.mp3" fadein 5
    call show_flowey_sprite(owner)

    call show_buttons

    while True:
        if pause:
            $ renpy.pause()
            
        call flowey_greeting(owner)

        if 'has_flowey_cell' not in player.variables:
            show flowey sideglance with Dissolve(.25)
            flowey "Oh look, you made it this far."
            play sound "audio/sfx/use_item.wav"
            "* You feel your phone vibrate a little."
            $ player.variables['has_flowey_cell'] = True
            flowey "I have a script I'm supposed to read here, but you aren't worth it."
            call show_flowey_sprite(owner)

        menu:
            "Chat":
                call Flowey_Interaction
                $ world.add_to_ac(2)
            
            "Give Gift" if len(inventory.items) > 0:
                call flowey_gift_menu_open(owner)
                $ result = renpy.call_screen("gift_item_menu",owner)
                if result == 'cancel':
                    call flowey_gift_menu_cancel(owner)
                else:
                    $ world.add_to_ac(10)
                call show_flowey_sprite(owner)
            "Leave":
                call flowey_goodbye(owner)
                return

    return

label flowey_gift_menu_open(owner):
    if owner.get_relationship() == "Hated":
        show flowey sideglance with Dissolve(.25)
        flowey "You have my attention..."
    elif owner.get_relationship() == "Disliked":
        show flowey suspicious with Dissolve(.25)
        flowey "Huh, what's that?"
    elif owner.get_relationship() == "Neutral":
        show flowey sideglance with Dissolve(.25)
        flowey "You... have something for me?"
    return

label flowey_gift_menu_cancel(owner):
    if owner.get_relationship() == "Hated":
        show flowey annoyed with Dissolve(.25)
        flowey "Ha ha, very funny."
    elif owner.get_relationship() == "Disliked":
        show flowey suspicious with Dissolve(.25)
        flowey "Ha ha, very funny."
    elif owner.get_relationship() == "Neutral":
        show flowey annoyed with Dissolve(.25)
        flowey "Ha ha, very funny."
    return

label show_flowey_sprite(owner):

    if owner.get_relationship() == "Hated":
        show flowey angry with Dissolve(.25)
    elif owner.get_relationship() == "Disliked":
        show flowey annoyed with Dissolve(.25)
    elif owner.get_relationship() == "Neutral":
        show flowey normal with Dissolve(.25)
    else:
        show flowey normal with Dissolve(.25)
        "relationship sprite not found"
    return

label flowey_greeting(owner):
    if owner.get_relationship() == "Hated":
        $ flowey_hated = True
        $ flowey_disliked = False
        $ flowey_neutral = False
        show flowey angry with Dissolve(.25)
        flowey "Go away. I'm busy right now."
    elif owner.get_relationship() == "Disliked":
        $ flowey_hated = False
        $ flowey_disliked = True
        $ flowey_neutral = False
        show flowey annoyed with Dissolve(.25)
        flowey "What do you want?"
    elif owner.get_relationship() == "Neutral":
        $ flowey_hated = False
        $ flowey_disliked = False
        $ flowey_neutral = True
        show flowey normal with Dissolve(.25)
        flowey "What?"
    else:
        flowey "GREETING NOT FOUND"
    return

label flowey_goodbye(owner):
    if owner.get_relationship() == "Hated":
        show flowey annoyed with Dissolve(.25)
        flowey "Good riddance."
    elif owner.get_relationship() == "Disliked":
        show flowey annoyed with Dissolve(.25)
        flowey "Finally."
    elif owner.get_relationship() == "Neutral":
        show flowey normal with Dissolve(.25)
        flowey "Bye."
    else:
        flowey "GREETING NOT FOUND"
    return