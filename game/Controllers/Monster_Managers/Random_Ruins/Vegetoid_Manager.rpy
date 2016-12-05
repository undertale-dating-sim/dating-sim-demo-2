

init -9 python:

    class Vegetoid(Monster):
        def __init__(self):
            Monster.__init__(self)
            self.default_event = Event("vegetoid_manager_default",True,self)
            self.name = 'Vegetoid'
            self.default_sprite = 'vegetoid normal'





#this is floweys default scene
label vegetoid_manager_default(owner=False,pause = True):
    
    show vegetoid normal
    call show_buttons from _call_show_buttons_5
    if pause:
        $ renpy.pause()

    if not owner.visited:
        vegetoid '...'
        "* Plants don't talk, silly."

    elif not owner.dialogue_toggle:
        vegetoid "..."
        "* Vegetoid smiled at you."
        "* It is genuine, but also a little creepy."
    else:
        vegetoid "...."
        "* Vegetoid is inviting you to eat some vegetables..."
        "* It is possible that they are the one providing supplies to Toriel, too."

    #swap to the other
    $ owner.dialogue_toggle = not owner.dialogue_toggle

    return