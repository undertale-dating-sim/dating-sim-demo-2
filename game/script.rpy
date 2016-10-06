label splashscreen:


    return

label after_load:
    $ talking = False
    hide screen multiple_monster_click_screen
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
    hide screen multiple_monster_click_screen
    return
label updater:
    $ updater.update(url='http://www.apartmentgaming.com/update/updates.json')
    return

#This takes place after the MC has heard about Frisk from Toriel.
label start:
    stop music
    #play music "audio/music/music-home.mp3"
    
    #call super_secret_console
    call show_buttons from _call_show_buttons_11
    #jump scrolling_credits
    #$ world.get_monster("Toriel").move_to_room("Basement Door")
    jump start_the_game
    #jump load_room
    #jump dev_label
    #jump frisk_start
    return

screen talking_text():
    text "Talk to [talking]?" xpos .5 ypos .2



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