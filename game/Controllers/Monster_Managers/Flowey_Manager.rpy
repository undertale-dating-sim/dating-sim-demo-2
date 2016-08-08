

init -9 python:

    class Flowey(Monster):
        def __init__(self):
            Monster.__init__(self)
            self.default_event = Event("flowey_manager_default",True)





#this is floweys default scene
label flowey_manager_default:
    
    show flowey normal
    $ renpy.pause()
    $ ftalk = True
    while ftalk:
        menu:
            "FP   :   [flowey.FP]"
            "Raise FP +10":
                $ flowey.FP += 10
            "Leave":
                $ ftalk = False

    return
