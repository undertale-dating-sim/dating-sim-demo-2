

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

    show flowey excited
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









