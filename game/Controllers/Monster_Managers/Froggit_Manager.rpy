

init -9 python:

    class Froggit(Monster):
        def __init__(self):
            Monster.__init__(self)
            self.name = "Froggit"
            self.default_event = Event("froggit_default_dialogue",True)





#this is floweys default scene
label froggit_default_dialogue:
    
    show flowey normal

    if not froggit_actor.visited:
        froggit "Oh, hello!"
        froggit "Try to watch out where you walk."
        froggit "Some of my friends are very tiny, so it is easy to not see them." 
        froggit "Wait, where are they...actually..."
        $ froggit_actor.visited = True
    
    elif not froggit_actor.dialogue_toggle:
        froggit "Is this the first time for you to talk to a Froggit?"
        froggit "Sometimes people forget about us so it feels nice..."
        froggit "I am glad we don't have to fight!"
        froggit "Hum?"
        froggit "Oh yes, monsters used to fight humans..."
        froggit "But that is in the past, we mostly talk now!"
        $ froggit_actor.dialogue_toggle = True

    else:
        froggit "You know, even if it is sometimes tempting, it is quite rude to skip what someone is saying you know."
        froggit "But hey, if you want to, you just have to click!"
        $ froggit_actor.dialogue_toggle = False
    
    while True:
        pause
    return

