

init -9 python:

    class Migosp(Monster):
        def __init__(self):
            Monster.__init__(self)
            self.default_event = Event("migosp_manager_default",True)
            self.name = "Migosp"




#this is floweys default scene
label migosp_manager_default(owner = False):
    
    show migosp normal
    call show_buttons
    $ renpy.pause()

    return
