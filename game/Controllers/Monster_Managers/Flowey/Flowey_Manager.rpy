

init -9 python:

    class Flowey(Monster):
        def __init__(self):
            Monster.__init__(self)
            self.default_event = Event("flowey_manager_default",True,self)
            self.name = "Flowey"
            self.handle_schedule()
            self.default_sprite = 'flowey normal'
            self.hover_sprite = "flowey annoyed"

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
            #self.update_schedule("Monday","Morning","Cave Room",self.default_event)
            self.update_schedule("Monday","Morning","Basement Door",self.default_event)
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

    call show_flowey_sprite(owner)

    call show_buttons

    while True:
        if pause:
            $ renpy.pause()
            
        call flowey_greeting(owner)
        menu:
            "convo":
                call flowey_default_conversation(owner)
            "remember test":
                $r = renpy.show_screen("remember",owner)
            "Raise FP 20":
                $ owner.FP += 20
            "Lower FP 20":
                $ owner.FP -= 20
            "Give Gift" if len(inventory.items) > 0:
                call flowey_gift_menu_open(owner)
                $ result = renpy.call_screen("gift_item_menu",owner)
                if result == 'cancel':
                    call flowey_gift_menu_cancel(owner)
                
            "Leave":
                call flowey_goodbye(owner)

    return

label flowey_gift_menu_open(owner):
    if owner.get_relationship() == "Hated":
        show flowey sideglance
        flowey "You have my attention..."
    elif owner.get_relationship() == "Disliked":
        show flowey suspicious
        flowey "Huh, what's that?"
    elif owner.get_relationship() == "Neutral":
        show flowey sideglance
        flowey "You... have something for me?"
    return



label flowey_gift_menu_cancel(owner):
    if owner.get_relationship() == "Hated":
        show flowey annoyed
        flowey "Ha ha, very funny."
    elif owner.get_relationship() == "Disliked":
        show flowey suspicious
        flowey "Ha ha, very funny."
    elif owner.get_relationship() == "Neutral":
        show flowey annoyed
        flowey "Ha ha, very funny."

    return

label show_flowey_sprite(owner):

    if owner.get_relationship() == "Hated":
        show flowey angry
    elif owner.get_relationship() == "Disliked":
        show flowey annoyed
    elif owner.get_relationship() == "Neutral":
        show flowey normal
    else:
        show flowey normal
        "relationship sprite not found"
    return

label flowey_greeting(owner):
    
    if owner.get_relationship() == "Hated":
        show flowey angry
        flowey "Go away. I'm busy right now."
    elif owner.get_relationship() == "Disliked":
        show flowey annoyed
        flowey "What do you want?"
    elif owner.get_relationship() == "Neutral":
        show flowey normal
        flowey "What?"
    else:
        flowey "GREETING NOT FOUND"
    return

label flowey_goodbye(owner):

    if owner.get_relationship() == "Hated":
        show flowey annoyed
        flowey "Good riddance."
    elif owner.get_relationship() == "Disliked":
        show flowey annoyed
        flowey "Finally."
    elif owner.get_relationship() == "Neutral":
        show flowey normal
        flowey "Bye."
    else:
        flowey "GREETING NOT FOUND"
    return