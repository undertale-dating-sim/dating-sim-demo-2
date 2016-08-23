
screen show_menu_button:
    
    textbutton "Show Menu" action [Play ("sound", "audio/sfx/click.wav"),Show("show_menu"),Hide("show_menu_button"),Show("stats"),Show("debug_monsters")] align(.95,.05) 

screen show_menu:
    add "#0008"
    modal True
    #hide button
    textbutton "Hide Menu" action [Play ("sound", "audio/sfx/click.wav"),Hide("show_menu"),Show("show_menu_button"),Hide("items"),Hide("stats"),Hide("cell"),Hide("show_item_description"),Hide("debug_monsters")] align(.95,.05)  
    vbox xalign 0.05 ypos 0.05:
        frame:
            background Frame("UI/text-box3.png",21, 21)       
            vbox:
                text "[player.name]"
                text "Day: "+world.get_current_day()
                text "Time: "+world.get_current_time()
                text world.get_current_timezone()
                text "HP:  [player.current_health]/[player.total_health]"
                text "STAM:  [player.current_stamina]/[player.max_stamina]"
                text "G:   [player.gold]"

        frame  ypos 0.5:
            background Frame("UI/text-box3.png",21, 21)
            vbox:
                textbutton "ITEM" action [Play ("sound", "audio/sfx/click.wav"),Show("items"),Hide("stats"),Hide("cell")] background "#000000"
                textbutton "STAT" action [Play ("sound", "audio/sfx/click.wav"),Show("stats"),Hide("items"),Hide("cell")] background "#000000"
                textbutton "CELL" action [Play ("sound", "audio/sfx/click.wav"),Show("cell"),Hide("stats"),Hide("items")] background "#000000"

label increment_time(arg = 'day'):
    python:
        if arg == 'day':
            world.day += 1
        else:
            world.currentTime += 200
        world.update_world()
        renpy.jump("load_room")
    return

label decrement_time(arg = 'day'):
    python:
        if arg == 'day':
            world.day -= 1
        else:
            world.currentTime += 200
        world.update_world()
        renpy.jump("load_room")
    return

label increment_stamina:
    python:
        player.current_stamina += 10
        if player.current_stamina > player.max_stamina:
            player.current_stamina = player.max_stamina
    return

label decrement_stamina:
    python:
        player.current_stamina -= 10
        if player.current_stamina < 0:
            player.current_stamina = 0
    return

screen debug_monsters:
    frame pos(.3,.5):
        background Frame("UI/text-box3.png",21,21)
        ymaximum 300
        vbox:
            hbox:
                textbutton "Day Back" action [Play ("sound", "audio/sfx/click.wav"), ui.callsinnewcontext("decrement_time","day")]
                textbutton "Day Forward" action [Play ("sound", "audio/sfx/click.wav"), ui.callsinnewcontext("increment_time","day")]
            hbox:
                textbutton "Time Back" action [Play ("sound", "audio/sfx/click.wav"), ui.callsinnewcontext("decrement_time","hour")]
                textbutton "Time Forward" action [Play ("sound", "audio/sfx/click.wav"), ui.callsinnewcontext("increment_time","hour")]

            hbox:
                textbutton "Stam Down" action [Play ("sound", "audio/sfx/click.wav"), ui.callsinnewcontext("decrement_stamina")]
                textbutton "Stam Up" action [Play ("sound", "audio/sfx/click.wav"), ui.callsinnewcontext("increment_stamina")]
            vpgrid:
                draggable True
                mousewheel True
                scrollbars "vertical,horizontal"
                side_xalign 0.5
                cols 1
                spacing 30
                hbox:
                    text "Name"
                    text "      "
                    text "Location"
                for a in world.areas:
                    for r in a.rooms:
                        for m in r.monsters:
                            hbox:
                                text "[m.name]"
                                text "      "
                                text "[r.name]"
                            # text "Schedule"
                            # for s,t in m.schedule.iteritems():
                            #     for x in t:
                            #         hbox:
                            #             text "[s]"
                            #             text "  "
                            #             text "[x]"
                            #             text "  "
                            #             text t[x].label

screen stats:
    frame pos(0.3,0.05):
        background Frame("UI/text-box3.png",21, 21)
        hbox:
            vbox:
                text "Patience:"
                text "Integrity:"
                text "Bravery:"
                text "Perseverance:"
                text "Kindness:"    
                text "Justice:"
            vbox:
                text "[player.patience_impulsiveness]"
                text "[player.integrity_deceit]"
                text "[player.bravery_cowardice]"
                text "[player.perseverance_surrender]"
                text "[player.kindness_cruelty]"
                text "[player.justice_apathy]"  

screen show_information_overlay:
    vbox:
        hbox pos(0.25,0.01):
            if player.current_stamina < 25:
                text 'Stamina : {color=#f00}[player.current_stamina]'
            elif player.current_stamina < 50:
                text 'Stamina : {color=#FF0}[player.current_stamina]'
            elif player.current_stamina < 75:
                text 'Stamina : {color=#00FF00}[player.current_stamina]'
            else:
                text 'Stamina : {color=#008000}[player.current_stamina]'    
            text '              '
            text world.get_current_time()
        hbox xpos .25:
            if world.currentArea.currentRoom.current_monster and world.currentArea.currentRoom.current_monster != False:
                text "[world.currentArea.currentRoom.current_monster.name]         FP:[world.currentArea.currentRoom.current_monster.FP]"


screen show_nav_button:
    textbutton "Show Nav (E)" action [Play ("sound", "audio/sfx/click.wav"), Show("navigation_buttons"), Hide("show_nav_button")] align(.95,.1) 
    key 'e' action [Play ("sound", "audio/sfx/click.wav"), Show("navigation_buttons"), Hide("show_nav_button")]
screen navigation_buttons:
    add "#0008"
    modal True

    vbox pos(.2,.1):
        for area in world.areas:
            for r in area.rooms:
                textbutton "[r.name]" action [Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Function(world.move_to_room,r.name)]
    $dirs = world.currentArea.cr_get_neighbors()

    textbutton "Hide Nav (E)" action [Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button')] align(.95,.1) 
    key 'e' action [Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button')]
    if dirs.count('north') > 0:
        imagebutton auto "UI/button_north_%s.gif"  align(0.5,0.0) action[Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button'),Function(world.currentArea.move_dir,'north')]
        key 'w' action[Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button'),Function(world.currentArea.move_dir,'north')]

    if dirs.count('south') > 0:
        imagebutton auto "UI/button_south_%s.gif"  align(0.5,1.0) action[Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button'),Function(world.currentArea.move_dir,'south')]
        key 's' action[Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button'),Function(world.currentArea.move_dir,'south')]

    if dirs.count('east') > 0:
        imagebutton auto "UI/button_east_%s.gif"  align(1.0,0.5)  action[Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button'),Function(world.currentArea.move_dir,'east')]
        key 'd' action[Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button'),Function(world.currentArea.move_dir,'east')]

    if dirs.count('west') > 0:
        imagebutton auto "UI/button_west_%s.gif"  align(0.00,0.5) action[Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button'),Function(world.currentArea.move_dir,'west')]
        key 'a' action[Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button'),Function(world.currentArea.move_dir,'west')]

    text '[world.currentArea.currentRoom.name]' align(0.5,0.5)                  