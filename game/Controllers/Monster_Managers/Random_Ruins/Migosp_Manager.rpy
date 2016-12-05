

init -9 python:

    class Migosp(Monster):
        def __init__(self):
            Monster.__init__(self)
            self.default_event = Event("migosp_manager_default",True,self)
            self.name = "Migosp"
            self.default_sprite = 'migosp normal'




#this is floweys default scene
label migosp_manager_default(owner = False,pause = True):
    
    show migosp normal
    call show_buttons from _call_show_buttons_2
    if pause:
        $ renpy.pause()

    if not owner.visited:
        migosp "La la la....Hey!"
        migosp "You should dance with me, nothing like having some time alone!"
        migosp "Well, with you, it isn't really alone... but that's okay!"

    elif not owner.dialogue_toggle:
        migosp "There's not much happening around here, so people always hang out together."
        migosp "But I would rather be alone sometimes..."
    else:
        migosp "People say I change when my friends are with me, I don't really see why."
        migosp "I'm always myself when the human is here."

    #swap to the other
    $ owner.dialogue_toggle = not owner.dialogue_toggle

    return
