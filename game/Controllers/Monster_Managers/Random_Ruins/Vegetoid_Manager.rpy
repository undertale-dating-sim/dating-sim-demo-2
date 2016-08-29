

init -9 python:

    class Vegetoid(Monster):
        def __init__(self):
            Monster.__init__(self)
            self.default_event = Event("vegetoid_manager_default",True)
            self.name = 'Vegetoid'





#this is floweys default scene
label vegetoid_manager_default(owner=False):
    
    show vegetoid normal
    call show_buttons
    $ renpy.pause()

    if not owner.visited:
        vegetoid "..."
        "You are kind of surprised it isn't capable of speech."
        "Especially since other plants here seem to be able to talk."
        "Maybe talking only applies to flowers..."

    elif not owner.dialogue_toggle:
        vegetoid "..."
        "Vegetoid seems to smile at you."
        "It is genuine, but also a little creepy."
    else:
        vegetoid "...."
        "Vegetoid is inviting you to eat some vegetables..."

    #swap to the other
    owner.dialogue_toggle = not owner.dialogue_toggle

    return