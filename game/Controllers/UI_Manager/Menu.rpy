
screen show_menu_button:
    
    textbutton "Show Menu(Q)" action [Play ("sound", "audio/sfx/click.wav"),Show("show_menu"),Hide("show_menu_button"),Show("stats"),Show("debug_monsters")] align(.95,.05) 
    key 'q' action [Play ("sound", "audio/sfx/click.wav") ,Show("show_menu"),Hide("show_menu_button"),Show("stats"),Show("debug_monsters")]
    key 'Q' action [Play ("sound", "audio/sfx/click.wav") ,Show("show_menu"),Hide("show_menu_button"),Show("stats"),Show("debug_monsters")]
screen show_menu:
    add "#0008"
    modal True
    #hide button
    textbutton "Hide Menu (Q)" action [Play ("sound", "audio/sfx/click.wav"),Hide("show_menu"),Show("show_menu_button"),Hide("items"),Hide("stats"),Hide("cell"),Hide("show_item_description"),Hide("debug_monsters")] align(.95,.05)  
    key 'q' action [Play ("sound", "audio/sfx/click.wav"),Hide("show_menu"),Show("show_menu_button"),Hide("items"),Hide("stats"),Hide("cell"),Hide("show_item_description"),Hide("debug_monsters")]
    key 'Q' action [Play ("sound", "audio/sfx/click.wav"),Hide("show_menu"),Show("show_menu_button"),Hide("items"),Hide("stats"),Hide("cell"),Hide("show_item_description"),Hide("debug_monsters")]
    vbox xalign 0.05 ypos 0.05:
        frame:
            background Frame("UI/text-box3.png",21, 21)
            hbox:    
                vbox:
                    text "[player.name]"
                    text "Day: "
                    text ""
                    text "Time: "
                    text world.get_current_timezone()
                    text "Health:"
                    text "SNAILS:"
                    text "Gold:"
                    if player.equipped_item:
                        text "Equip: "
                vbox:
                    text ""
                    text "[world.day]"
                    text world.get_current_day()
                    text world.get_current_time()
                    text ""
                    text "[player.current_health]/[player.total_health]"
                    text "[player.current_snails]/[player.max_snails]"
                    text "[player.gold]"
                    if player.equipped_item:
                        text player.equipped_item.name

        frame  ypos 0.5:
            background Frame("UI/text-box3.png",21, 21)
            vbox:
                textbutton "ITEM" action [Play ("sound", "audio/sfx/click.wav"),Show("items"),Hide("stats"),Hide("cell"),SetVariable("selected_caller",False)] background "#000000"
                textbutton "STAT" action [Play ("sound", "audio/sfx/click.wav"),Show("stats"),Hide("items"),Hide("cell"),SetVariable("selected_caller",False)] background "#000000"
                if 'has_cellphone' in player.variables:
                    textbutton "CELL" action [Play ("sound", "audio/sfx/click.wav"),Show("cell"),Hide("stats"),Hide("items"),SetVariable("selected_caller",False)] background "#000000"



label increment_hp:
    python:
        player.current_health += 10
        if player.current_health > player.total_health:
            player.current_health = player.total_health
        player.update_player()
    return

label decrement_hp:
    python:
        player.current_health -= 10
        if player.current_health < 0:
            player.current_health = 0
        player.update_player()
    return

screen debug_monsters:
    if 1 == 2:
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
                    textbutton "HP Down" action [Play ("sound", "audio/sfx/click.wav"), ui.callsinnewcontext("decrement_hp")]
                    textbutton "HP Up" action [Play ("sound", "audio/sfx/click.wav"), ui.callsinnewcontext("increment_hp")]
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
                    for a_name,a in world.areas.iteritems():
                        for r_name,r in a.rooms.iteritems():
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
    frame pos(0.4,0.05):
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
    
    if world.day > 0:
        vbox:
            hbox pos(0.1,0.01):
                text "%s" % world.get_current_timezone() outlines [ (1, "000000", 0, 0 ) ]
            hbox pos(0.1,0.03):
                text "AC : [world.timezone_action_count]/10" outlines [ (1, "000000", 0, 0 ) ]
        # hbox xpos .25:
        #     if world.current_area.current_room.current_monster and world.current_area.current_room.current_monster != False:
        #         vbox:
        #             text "[world.current_area.current_room.current_monster.name]"
        #             text "FP:[world.current_area.current_room.current_monster.FP]"
        #             text "DP:[world.current_area.current_room.current_monster.DP]"
        #             text "HP:[world.current_area.current_room.current_monster.HP]"


#if you look, I have added the multiple monster screen here.  It was causing a divide by zero error and I'm not sure how to fix it
screen show_nav_button:
    textbutton "Show Nav (E)" action [Play ("sound", "audio/sfx/click.wav"), Show("navigation_buttons"), Hide("show_nav_button")] align(.95,.11) 
    key 'e' action [Play ("sound", "audio/sfx/click.wav"), Show("navigation_buttons"), Hide("show_nav_button"),Hide("multiple_monster_click_screen")]
    key 'E' action [Play ("sound", "audio/sfx/click.wav"), Show("navigation_buttons"), Hide("show_nav_button"),Hide("multiple_monster_click_screen")]
screen navigation_buttons:
    add "#0008"
    modal True

    # vbox pos(.2,.1):
    #     for area_name,area in world.areas.iteritems():
    #         for r_name,r in area.rooms.iteritems():
    #             textbutton "[r.name]" action [Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Function(world.move_to_room,r.name)]
    $dirs = world.current_area.cr_get_neighbors()

    textbutton "Hide Nav (E)" action [Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button'),Hide("multiple_monster_click_screen")] align(.95,.1) 
    key 'e' action [Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button')]
    key 'E' action [Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button')]
    if "north" in dirs:
        text '[dirs[north]]' outlines [ (1, "000000", 0, 0 ) ] align(0.5,0.1)
        imagebutton auto "UI/button_north_%s.gif"  align(0.5,0.0) action[Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button'),Function(world.current_area.move_dir,'north')]
        key 'w' action[Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button'),Function(world.current_area.move_dir,'north')]
        key 'W' action[Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button'),Function(world.current_area.move_dir,'north')]

    if "south" in dirs:
        text '[dirs[south]]' outlines [ (1, "000000", 0, 0 ) ] align(0.5,.9)
        imagebutton auto "UI/button_south_%s.gif"  align(0.5,1.0) action[Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button'),Function(world.current_area.move_dir,'south')]
        key 's' action[Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button'),Function(world.current_area.move_dir,'south')]
        key 'S' action[Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button'),Function(world.current_area.move_dir,'south')]

    if "east" in dirs:
        text '[dirs[east]]' outlines [ (1, "000000", 0, 0 ) ] align(1.0,.6)
        imagebutton auto "UI/button_east_%s.gif"  align(1.0,0.5)  action[Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button'),Function(world.current_area.move_dir,'east')]
        key 'd' action[Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button'),Function(world.current_area.move_dir,'east')]
        key 'D' action[Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button'),Function(world.current_area.move_dir,'east')]

    if "west" in dirs:
        text '[dirs[west]]' outlines [ (1, "000000", 0, 0 ) ] align(0.0,.6)
        imagebutton auto "UI/button_west_%s.gif"  align(0.00,0.5) action[Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button'),Function(world.current_area.move_dir,'west')]
        key 'a' action[Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button'),Function(world.current_area.move_dir,'west')]
        key 'A' action[Play ("sound", "audio/sfx/click.wav"),Hide("navigation_buttons"),Show('show_nav_button'),Function(world.current_area.move_dir,'west')]

    text '[world.current_area.current_room.name]' outlines [ (1, "000000", 0, 0 ) ] pos(0.015,0.09)
    vbox xalign 0.5 ypos 0.12:
        vbox:
            add Minimap():
                xalign 0.6
                yalign 0.5                  