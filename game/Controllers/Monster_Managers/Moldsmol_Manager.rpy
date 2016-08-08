

init -9 python:

    class Moldsmol(Monster):
        def __init__(self):
            Monster.__init__(self)
            self.default_event = Event("moldsmol_manager_default",True)
            self.name = "Moldsmol"




#this is floweys default scene
label moldsmol_manager_default(owner):
    
    show moldsmol normal

    call show_buttons
    $ renpy.pause()
    return
