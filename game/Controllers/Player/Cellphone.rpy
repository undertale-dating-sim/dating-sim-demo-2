screen cell:
    frame pos(0.3,0.05):
        vbox:
            textbutton "Frisk":
                action [ui.callsinnewcontext("call_Frisk")] background "#000000"
            textbutton "Toriel":
                action [ui.callsinnewcontext("call_Toriel")] background "#000000"

label call_Frisk:
    "ring"
    "ring"
    "ring"
    "Hello,This is Frisk"
    $ talking = True
    while talking:
        menu:
            "Hello!":
                "I don't really have anything to say to you."
            "Goodbye!":
                "click"
                return
    return

label call_Toriel:
    "This is Toriel"
    return