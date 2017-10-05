screen cell:
    frame pos(0.4,0.05):
        background Frame("UI/text-box3.png",21, 21)
        vbox:
            if 'has_flowey_cell' in player.variables:
                textbutton "Flowey":
                    action [ui.callsinnewcontext("call_Monster","Flowey")] background "#000000"
            if 'has_frisk_cell' in player.variables:
                textbutton "Frisk":
                    action [ui.callsinnewcontext("call_Monster","Frisk")] background "#000000"
            if 'has_toriel_cell' in player.variables:
                textbutton "Toriel":
                    action [SetVariable("selected_caller","Toriel")] background "#000000"
            if 'has_napstablook_cell' in player.variables:
                textbutton "Napstablook":
                    action [ui.callsinnewcontext("call_Monster","Napstablook")] background "#000000"
    if selected_caller and selected_caller == "Toriel":
        frame pos(.4,.3):
            background Frame("UI/text-box3.png",21, 21)
            
            hbox:            
                    vbox:
                        hbox:
                            image im.Scale(get_monster(selected_caller).cell_phone_pic,100,100)
                            text "    "
                            text "    "
                        text "FP : %s " % get_monster(selected_caller).FP
                        text "DP : %s " % get_monster(selected_caller).DP
                        text "HP : %s " % get_monster(selected_caller).HP
                        text "    "
                        textbutton "Call":
                            action [ui.callsinnewcontext("call_Monster","Toriel")] background "#000000"
                    vbox:
                        text "---------"
                        for x in get_monster(selected_caller).dating_requirements:
                            text "{size=-5}[x]{/size}"
                            for r in get_monster(selected_caller).dating_requirements[x]:
                                if get_monster(selected_caller).dating_requirements[x][r]:
                                    text "  {color=#00ff00}{size=-5}[r]{/size}{/color}"
                                else:
                                    text "  {color=#f00}{size=-5}[r]{/size}{/color}"
                            text "---------"

label call_Monster(monster):
    python:
        location = world.current_area.current_room
        loc_name = "call_"+monster+"_"+location.name.replace(" ","_")
        monster = world.get_monster(monster)

        call_location_variable = location.name.replace(" ","_") + "_call_count"

        if call_location_variable not in monster.variables:
            monster.variables[call_location_variable] = 1
        else:
            monster.variables[call_location_variable] += 1

        if monster.name+"_Cellphone_"+location.name.replace(" ","_")+"_Complete" not in player.variables:
            text_color = "#00ff00"
        else:
            text_color = "#ffffff"

    if monster.current_room.name == "Dead Room":
        "But nobody answered..."
    else:
        menu:
            "Hello?"
                    
            "{color=[text_color]}Chat about [world.current_area.current_room.name]{/color}":

                
                if renpy.has_label(loc_name):
                    call expression loc_name pass (monster,monster.variables[call_location_variable])
                elif renpy.has_label("call_[monster]_Unknown"):
                    call expression "call_[monster]_Unknown" pass (loc_name)
                else:
                    call unknown_Call
                $ player.variables[monster.name+"_Cellphone_"+location.name.replace(" ","_")+"_Complete"] = True

            "Where are you?":
                $ renpy.say(monster.name,"I'm at the [monster.current_room.name].")
                $ renpy.say(monster.name,"You should come say 'Hello!'.")
    return

label unknown_Call:
    "I'm not sure."
    "I don't think I'm supposed to be here."
    return