

init -9 python:

    class Whimsun(Monster):
        def __init__(self):
            Monster.__init__(self)
            self.default_event = Event("Whimsun_manager_default",True)
            self.name = "Whimsun"




#this is floweys default scene
label Whimsun_manager_default(owner):
    
    show whimsun normal
    call show_buttons
    $ renpy.pause()

    return
