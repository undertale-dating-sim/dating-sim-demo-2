

init -9 python:

    class Whimsun(Monster):
        def __init__(self):
            Monster.__init__(self)
            self.default_event = Event("Whimsun_manager_default",True)
            self.name = "Whimsun"



#this is floweys default scene
label Whimsun_manager_default(owner = False):
    
    show whimsun normal
    call show_buttons
    $ renpy.pause()

    
    if not owner.visited:
        whimsun "O..."
        whimsun "I..."
        whimsun "..I am sorry, I.....I didn't see you..."
        whimsun "I...I will try to .... not be a bother."
        
    elif not owner.dialogue_toggle:
        whimsun "Sometimes I try to hide in a corner so I don't....bother people...."
        whimsun "But I can't find a good one....oh no.."

    else:
        whimsun "You .... should talk to the other monsters."
        whimsun "I.....I am sorry."

    #swap to the other
    owner.dialogue_toggle = not owner.dialogue_toggle

    return
