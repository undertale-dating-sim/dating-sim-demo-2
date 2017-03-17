screen cell:
    frame pos(0.3,0.05):
        background Frame("UI/text-box3.png",21, 21)
        vbox:
            textbutton "Flowey":
                action [ui.callsinnewcontext("call_Monster","Flowey")] background "#000000"
            textbutton "Frisk":
                action [ui.callsinnewcontext("call_Monster","Frisk")] background "#000000"
            textbutton "Toriel":
                action [ui.callsinnewcontext("call_Monster","Toriel")] background "#000000"
            textbutton "Napstablook":
                action [ui.callsinnewcontext("call_Monster","Napstablook")] background "#000000"
            
label call_Monster(monster = "Frisk"):

    $ location = world.current_area.current_room
    $ loc_name = "call_"+monster+"_"+location.name.replace(" ","_")

    if renpy.has_label(loc_name):
        call expression loc_name pass (world.get_monster(monster))
    elif renpy.has_label("call_[monster]_Unknown"):
        call expression "call_[monster]_Unknown"
    else:
        call unknown_Call
    return

label unknown_Call:
    "But nobody answered."
    "Rude."
    return