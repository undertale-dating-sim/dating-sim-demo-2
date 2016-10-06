

init -9 python:

    class Moldsmol(Monster):
        def __init__(self):
            Monster.__init__(self)
            self.default_event = Event("moldsmol_manager_default",True,self)
            self.name = "Moldsmol"
            self.default_sprite = 'moldsmol normal'




#this is floweys default scene
label moldsmol_manager_default(owner=False,pause=True):
    
    show moldsmol normal
    call show_buttons from _call_show_buttons_4
    if pause:
        $ renpy.pause()

    if not owner.visited:
        moldsmol "Blurp"
        "It seems like that slime looking monster is trying to greet you."


    elif not owner.dialogue_toggle:
        moldsmol "Squorch"
        "You aren't sure, but it seems like they trid to wiggle or..."
        "flirt with you?!"

    else:
        moldsmol "..."
        "They seem pensive, but you aren't sure that they actually have a brain."


    #swap to the other
    $ owner.dialogue_toggle = not owner.dialogue_toggle

    return
