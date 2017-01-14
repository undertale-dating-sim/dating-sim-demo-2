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

    $ location = world.currentArea.current_room
    $ loc_name = "call_"+monster+"_"+location.name.replace(" ","_")

    if renpy.has_label(loc_name):
        call expression loc_name pass (cell_convo_count) from _call_expression_1
        $ cell_convo_count += 1
    elif renpy.has_label("call_[monster]_Unknown"):
        call expression "call_[monster]_Unknown" from _call_expression_2
    else:
        call unknown_Call from _call_unknown_Call
    return

label unknown_Call:
    "But nobody answered."
    "Rude."
    return