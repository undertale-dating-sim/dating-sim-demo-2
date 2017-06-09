

init -9 python:

    class Loox(Monster):
        def __init__(self):
            Monster.__init__(self)
            self.default_event = Event("loox_manager_default",True,self)
            self.name = "Loox"
            self.default_sprite = 'loox normal'




#this is floweys default scene
label loox_manager_default(owner = False,pause = True):
    
    show loox normal


    call show_buttons from _call_show_buttons_8
    if pause:
        $ renpy.pause()


    if not owner.visited:
        loox "Hey!"
        loox "Don't look at me like that, it's rude."
        loox "Especially with two eyes..."
        loox "Do I do that to you? Huh?"

    elif not owner.dialogue_toggle:
        
        loox "It is always calm here, which is why we try to hang out so we don't get bored."
        loox "Sometimes, the human even joins us, but I feel like their mother doesn't like that too much." 

    else:
        loox "Some of my friends seem to pick on Whimsun..."
        loox "The human told them to stop but I don't think it did any good."


    #swap to the other
    $ owner.dialogue_toggle = not owner.dialogue_toggle

    return
