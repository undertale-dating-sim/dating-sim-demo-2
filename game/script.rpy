init python:



    # config.empty_window = renpy.curry(extend)("", interact=False)
    # _last_say_what = ""

    def beepy_voice(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show":
            renpy.sound.play("audio/sfx/voice_sans.wav",channel="audio")
        #if event == "slow_done":
            #renpy.sound.stop()



    def telemetry(string):
        dummy = list(string)
        dummy2 = "{cps=100}"
        for d in dummy:
            if d != ' ':
                dummy2 += "{w=0}"+d
            else:
                dummy2 += d
        dummy2 += "{/cps}"
        return dummy2

define test = Character("Sans", callback=beepy_voice)

###################

#    Our basic start label.  Will usually g to start the game.

###################


label start:
    
    scene black
    jump the_fall
    return


label skip_to_day_1:
    scene black
    $ player.variables['tf_scream_count'] = 1
    $ player.variables['satchel_found'] = True
    $ player.variables['satchel_refused'] = False
    $ player.variables['accepted_toriel'] = True
    $ inventory.max_items = 5
    $ player.variables['clicked_toriel'] = 1
    $ player.variables['met_toriel'] = True
    $ player.variables['met_frisk'] = True
    $ player.variables['has_frisk_cell'] = True
    $ player.variables['has_cellphone'] = True
    $ player.variables['accepted_frisk'] = True

    
    call player_sleeping_th
    $ move_to_room("Your Room")
    return



label splashscreen:

    scene black
    "Welcome to the UDS Demo!"
    "Be warned.  While we did test as much as possible, there are still some spots that get kind of sketchy."
    "At the moment, Saving and Loading, as well as Back and other Renpy functions are pretty much broken."
    scene black
    with Pause(1)

    show text "Team UDS Presents..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return


label Snail_Hunter_Random_Event:

    call show_buttons

    if player.last_snail_day == False or player.last_snail_day != world.day:

        "* You notice the flowers are moving a little."

        menu:

            "What do you do?"
            "Check under the flowers":
                if get_timezone() == "Night":
                    "It looks like they all went home to sleep."
                    "..."
                    "Wait..."
                else:
                    call UnderSnail

            "Ignore it. Too scary.":
                return

    else:
        "* A very quiet, peaceful room.  It looks new.  The flowers are still."
    return

label day_transition:
    stop music
    call hide_buttons
    scene black
    $ renpy.pause(2)
    $world.day += 1
    show image Text("{size=80}Day %s" % world.day, text_align = 0.5) at center with Fade(1, 0, 1)
    play sound "audio/new_day.wav"
    $ renpy.pause(2)
    $ world.start_the_day()
    call player_waking_up
    return


###################

    # This label is mainly for dev purposes.  It goes off after we hit Shift + R.
    # It currently just resets the multiple monster code, but it isn't perfect.  Needs more tweaking.

###################

label after_load:

    # stop music
    
    # $ player.variables['tf_scream_count'] = 1
    # $ player.variables['satchel_found'] = True
    # $ player.variables['satchel_refused'] = False
    # $ player.variables['accepted_toriel'] = True
    # $ inventory.max_items = 5
    # $ player.variables['clicked_toriel'] = 1
    # $ player.variables['met_toriel'] = True
    # $ player.variables['met_frisk'] = True
    # $ player.variables['has_frisk_cell'] = True
    # $ player.variables['has_cellphone'] = True
    # $ player.variables['accepted_frisk'] = True

    # $ move_to_room("Your Room")
    return



###################
    # This label shows all of the UI Buttons.  Needs to be called at the start of each room for the player to be able to see the UI since
    # we are creating new contexts in each room.
###################

label show_buttons:
    
    show screen show_menu_button
    show screen show_nav_button
    #show screen show_map_button
    show screen show_information_overlay
    show screen show_testing_button
    return



###################
    # Same as the above function, except that it hides the buttons.
###################

label hide_buttons:

    hide screen show_menu_button
    hide screen show_nav_button
    #hide screen show_map_button
    hide screen show_information_overlay
    hide screen multiple_monster_click_screen
    hide screen show_testing_button
    return



###################
    # Label to call the updater.  Aims at my own personal site, which means I have to FTP the update files there for it to work.
    # Look at the documentation for it.
###################

label updater:
    $ updater.update(url='http://www.apartmentgaming.com/update/updates.json')
    return
