

init -9 python:

    class Moldsmal(Monster):
        def __init__(self):
            Monster.__init__(self)
            self.default_event = Event("moldsmal_manager_default",True)





#this is floweys default scene
label moldsmal_manager_default:
    
    show moldsmal normal
    $ renpy.pause()
    return
