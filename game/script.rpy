'''
    Our basic start label.  Will usually go to start the game.
'''
label start:
    stop music
    #play music "audio/music/music-home.mp3"
    #jump choosemenu
    call show_buttons
    jump start_the_game

    return

'''
    This label is mainly for dev purposes.  It goes off after we hit Shift + R.

    It currently just resets the multiple monster code, but it isn't perfect.  Needs more tweaking.
'''
label after_load:
    $ talking = False
    hide screen multiple_monster_click_screen
    jump start
    return

'''
    This label shows all of the UI Buttons.  Needs to be called at the start of each room for the player to be able to see the UI since
    we are creating new contexts in each room.
'''
label show_buttons:
    show screen show_menu_button
    show screen show_nav_button
    show screen show_map_button
    show screen show_information_overlay
    return

'''
    Same as the above function, except that it hides the buttons.
'''
label hide_buttons:
    hide screen show_menu_button
    hide screen show_nav_button
    hide screen show_map_button
    hide screen show_information_overlay
    hide screen multiple_monster_click_screen
    return

'''
    Label to call the updater.  Aims at my own personal site, which means I have to FTP the update files there for it to work.
    Look at the documentation for it.
'''

label updater:
    $ updater.update(url='http://www.apartmentgaming.com/update/updates.json')
    return



