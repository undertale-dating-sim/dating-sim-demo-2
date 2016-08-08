

init -9 python:

    class Loox(Monster):
        def __init__(self):
            Monster.__init__(self)
            self.default_event = Event("flowey_manager_default",True)





#this is floweys default scene
label loox_manager_default:
    
    show flowey normal

    while True:
        pause

    return
