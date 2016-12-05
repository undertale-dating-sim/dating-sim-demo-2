

init -9 python:

    class Whimsun(Monster):
        def __init__(self):
            Monster.__init__(self)
            self.default_event = Event("Whimsun_manager_default",True,self)
            self.name = "Whimsun"
            self.default_sprite = 'whimsun normal'



#this is floweys default scene
label Whimsun_manager_default(owner = False,pause = True):
    
    show whimsun normal
    call show_buttons from _call_show_buttons_10
    if pause:
        $ renpy.pause()

    
    if not owner.visited:
        whimsun "Oh..."
        whimsun "I..."
        whimsun "I am sorry, I.....I didn't see you..."
        whimsun "I...I will try to .... not be a bother."
        
    elif not owner.dialogue_toggle:
        whimsun "Sometimes I try to hide in a corner so I don't....bother people...."
        whimsun "But I can't find a good spot....oh dear.."

    else:
        whimsun "You .... should talk to the other monsters."
        whimsun "I.....I'm sorry."

    #swap to the other
    $ owner.dialogue_toggle = not owner.dialogue_toggle

    return
