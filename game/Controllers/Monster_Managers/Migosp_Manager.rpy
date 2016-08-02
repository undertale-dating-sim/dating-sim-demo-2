

init -9 python:

    class Migosp(Monster):
        def __init__(self):
            Monster.__init__(self)
            self.default_event = Event("flowey_manager_default",True)





#this is floweys default scene
label migosp_manager_default:
    
    show flowey normal
    $ ftalk = True
    while ftalk:
        menu:
            "FP   :   [flowey.FP]"
            "Raise FP +10":
                $ flowey.FP += 10
            "Leave":
                $ ftalk = False

    while True:
        pause

    return
