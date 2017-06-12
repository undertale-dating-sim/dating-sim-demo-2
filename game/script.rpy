init python:



    

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

label demo_values:
    $player.variables['has_toriel_cell'] = True
    $player.variables['has_frisk_cell'] = True
    $player.variables['has_napstablook_cell'] = True
    $player.variables['has_flowey_cell'] = True
    return

label start:
    
    call demo_values
    # $ world.update_world(True)
    $ get_monster("Flowey").move_to_room("Cave Room")
    $ get_monster("Toriel").move_to_room("Grass Room")
    $ get_monster("Napstablook").move_to_room("Tunnels")
    $ get_monster("Napstablook").move_to_room("Tunnels")
    $ get_monster("Frisk").move_to_room("Ruins Entrance")
    $ move_to_room("Cave Room")
    #jump the_beginning
    return







label Snail_Hunter_Random_Event:

    call show_buttons
    $ renpy.pause()

    if player.last_snail_day == False or player.last_snail_day != world.day:

        "* You notice the flowers are moving a little."
        menu:

            "What do you do?"
            "Check under the flowers":
                $snail_count = renpy.random.randint(3,10)
                "You found some snails!"
                if player.current_snails >= player.max_snails:
                    "Your pockets are full though. Bummer."
                elif player.current_snails + snail_count <= player.max_snails:
                    "[snail_count] added to inventory."
                else:
                    $ snail_count = (player.current_snails + snail_count) - player.max_snails
                    "[snail_count] added to inventory."

                $ player.current_snails += snail_count
                $ player.last_snail_day = world.day

            "Ignore it. Too scary.":
                return

    else:
        "* A very quiet, peaceful room.  It looks new.  The flowers are still."
    return

###################

    # This label is mainly for dev purposes.  It goes off after we hit Shift + R.
    # It currently just resets the multiple monster code, but it isn't perfect.  Needs more tweaking.

###################

label after_load:

    stop music
    $ talking = False
    hide screen multiple_monster_click_screen
    #jump start
    jump start
    return



###################
    # This label shows all of the UI Buttons.  Needs to be called at the start of each room for the player to be able to see the UI since
    # we are creating new contexts in each room.
###################

label show_buttons:
    
    show screen show_menu_button
    show screen show_nav_button
    show screen show_map_button
    show screen show_information_overlay
    show screen show_testing_button
    return



###################
    # Same as the above function, except that it hides the buttons.
###################

label hide_buttons:

    hide screen show_menu_button
    hide screen show_nav_button
    hide screen show_map_button
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
