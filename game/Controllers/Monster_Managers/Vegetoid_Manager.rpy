

init -9 python:

    class Vegetoid(Monster):
        def __init__(self):
            Monster.__init__(self)
            self.default_event = Event("vegetoid_manager_default",True)





#this is floweys default scene
label vegetoid_manager_default:
    
    show vegetoid normal
    $ renpy.pause()

    return
