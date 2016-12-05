

init -9 python:

    class Froggit(Monster):
        def __init__(self):
            Monster.__init__(self)
            self.name = "Froggit"
            self.default_event = Event("froggit_default_dialogue",True,self)
            self.default_sprite = 'froggit normal'





#this is floweys default scene
label froggit_default_dialogue(owner,pause = True):
    call show_buttons from _call_show_buttons_1
    show froggit normal

    if pause:
        $ renpy.pause()
    
    if not owner.visited:
        froggit "Oh, hello!"
        froggit "Try to watch out where you walk."
        froggit "Some of my friends are very tiny. It is easy to not see them." 
        froggit "Wait, where are they actually..."
        $ owner.visited = True
    
    elif not owner.dialogue_toggle:
        froggit "Is this the first time you've talked to a Froggit?"
        froggit "Sometimes people forget about us, so it feels nice..."
        show froggit happy
        froggit "I am glad we don't have to fight!"
        froggit "Hum?"
        show froggit normal
        froggit "Oh yes... monsters used to fight humans..."
        froggit "But that is in the past, we mostly just talk now!"
        $ owner.dialogue_toggle = True

    else:
        froggit "You know, even if it is sometimes tempting, it is quite rude to skip what someone is saying."
        froggit "But hey, if you want to, you just have to click!"
        $ owner.dialogue_toggle = False
    
    return

label froggit_advice_stats(owner):

    froggit "Hmm?"
    froggit "Oh sorry..."
    froggit "Just got turned down by another Froggit..."
    froggit "She said she wouldn’t date me because we didnt have enough skills in common."
    froggit "I think that’s just silly, but oh well."

    return