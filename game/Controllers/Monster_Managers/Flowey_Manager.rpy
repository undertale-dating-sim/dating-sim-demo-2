

init -9 python:

    class Flowey(Monster):
        def __init__(self):
            Monster.__init__(self)
            self.default_event = Event("flowey_manager_default",True,self)
            self.name = "Flowey"



label initialize_flowey:
    image flowey angry = "characters/Flowey/FloweyLineart-Angrycolor.png"
    image flowey annoyed = "characters/Flowey/FloweyLineart-Annoyedcolor.png"
    image flowey excited = "characters/Flowey/FloweyLineart-Excitedcolor.png"
    image flowey evil = "characters/Flowey/FloweyLineart-Horrorcolor.png"
    image flowey laugh = "characters/Flowey/FloweyLineart-LaughingColor.png"
    image flowey normal = "characters/Flowey/FloweyLineart-Normalcolor1.png"
    image flowey sad = "characters/Flowey/FloweyLineart-Sadcolor.png"
    image flowey sideglance = "characters/Flowey/FloweyLineart-SideGlarecolor.png"
    image flowey smug = "characters/Flowey/FloweyLineart-Smugcolor.png"
    image flowey wink = "characters/Flowey/FloweyLineart-Winkcolor.png"

    python:
        def flowey(text, *args, **kwargs):
            floweyChar(text, *args, **kwargs)

    define flowey = Character('Flowey', color="#FFFFFF")
    return

#this is floweys default scene
label flowey_manager_default(owner = False):

    call show_flowey_sprite(owner)

    call show_buttons
    $ renpy.pause()

    call flowey_greeting(owner)
    menu:
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









