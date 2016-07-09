screen cell:
    frame pos(0.3,0.05):
        background Frame("UI/text-box3.png",21, 21)
        vbox:
            textbutton "Frisk":
                action [ui.callsinnewcontext("call_Frisk")] background "#000000"
            

label call_Frisk:
    "ring..."
    ".ring..."
    "..ring..."
    "Hello? This is Frisk."
    $ talking = True
    while talking:
        menu:
            "Hello!":
                "I don't really have anything to say to you."
                "-click-"
                return
            "Goodbye!":
                "-click-"
                return
    return