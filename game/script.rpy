label splashscreen:


    return

label after_load:
    jump start
    return

label show_buttons:
    show screen show_menu_button
    show screen show_nav_button
    show screen show_map_button
    show screen show_information_overlay
    return

label hide_buttons:
    hide screen show_menu_button
    hide screen show_nav_button
    hide screen show_map_button
    hide screen show_information_overlay
    return


#This takes place after the MC has heard about Frisk from Toriel.
label start:
    stop music
    #play music "audio/music/music-home.mp3"
    #call super_secret_console
    #call show_buttons
    $ talking = False
    jump scrolling_credits
    #$ world.get_monster("Toriel").move_to_room("Basement Door")
    #jump start_the_game
    #jump load_room
    #jump dev_label
    #jump frisk_start

screen talking_text():
    text "Talk to [talking]?" xpos .5 ypos .2

screen multiple_monster_click_screen:
    $ count = 1
    $ width = (1.0/(len(world.currentArea.currentRoom.monsters)))
    for monster in world.currentArea.currentRoom.monsters:
        $ x = count * width
        mousearea:
            area ((count-1)* width, .4, width, .6)
            hovered [SetVariable('talking',monster.name),Notify(monster.name)]

        $ count+= 1

        #unhovered SetVariable('talking',False)
    # mousearea:
    #     area (.33, 0, .33, 1.0)
    #     hovered [SetVariable('talking',world.currentArea.currentRoom.monsters[1].name),Notify(world.currentArea.currentRoom.monsters[1].name)]
    #     #unhovered SetVariable('talking',False)

    # mousearea:
    #     area (.66, 0, .33, 1.0)
    #     hovered [SetVariable('talking',world.currentArea.currentRoom.monsters[2].name),Notify(world.currentArea.currentRoom.monsters[2].name)]
    #     #unhovered SetVariable('talking',False)


    #     #hovered Show("buttons", transition=dissolve)
    #     #unhovered Hide("buttons", transition=dissolve)

label multiple_monster:
    
    #show the background
    call show_buttons
    show screen multiple_monster_click_screen
    python:
        renpy.scene()
        if world.currentArea.currentRoom.bg:
            renpy.show(world.currentArea.currentRoom.bg)
    #for each monster, we need to figure out where to put them
    while True:
        python:
            count = 1
            
            for monster in world.currentArea.currentRoom.monsters:
                width = (1.0/(len(world.currentArea.currentRoom.monsters)+1))
                x = count * width
                
                if monster.name != talking:
                    renpy.show(monster.default_sprite,[Position(xpos = x, xanchor = 'center')])

                count += 1  
        
        pause
        if talking:
            call expression world.get_monster(talking).default_event.label pass(world.get_monster(talking))
    return

label dev_label:
    show screen show_menu_button
    #show screen show_map_button
    while True:
        menu:
            "Where would you like to go? Warning, you will probably have to completely restart to get back. Nothing is done."
            "The Ruins":
                jump load_room
            "Undersnail":
                jump demo_undersnail
            "Name Select":
                jump name_select
            "Random Encounters":
                menu:
                    "Vegetoid":
                        jump vegetoid_start
                    "Whimsun":
                        jump whimsun_start



label demo_end:
    "This demo ends here. Thanks for playing!"
    "Stay determined..."