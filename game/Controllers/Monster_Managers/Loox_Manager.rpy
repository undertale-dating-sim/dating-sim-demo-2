

init -9 python:

    class Loox(Monster):
        def __init__(self):
            Monster.__init__(self)
            self.default_event = Event("loox_manager_default",True)
            self.name = "Loox"




#this is floweys default scene
label loox_manager_default(owner = False):
    
    show loox normal


    call show_buttons
    $ renpy.pause()

    return
