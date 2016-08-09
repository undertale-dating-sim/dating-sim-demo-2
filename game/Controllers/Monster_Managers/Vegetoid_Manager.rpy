

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

    return
