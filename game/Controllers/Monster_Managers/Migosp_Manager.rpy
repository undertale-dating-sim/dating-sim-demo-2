

init -9 python:

    class Migosp(Monster):
        def __init__(self):
            Monster.__init__(self)
            self.default_event = Event("migosp_manager_default",True)





#this is floweys default scene
label migosp_manager_default:
    
    show migosp normal
    $ renpy.pause()

    return
