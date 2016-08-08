

init -9 python:

    class Whimsun(Monster):
        def __init__(self):
            Monster.__init__(self)
            self.default_event = Event("Whimsun_manager_default",True)





#this is floweys default scene
label Whimsun_manager_default:
    
    show whimsun normal
    $ renpy.pause()

    return
