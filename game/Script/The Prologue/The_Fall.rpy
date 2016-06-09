label the_fall:
    
    scene
    with fade

    #play wind sfx
    play music "audio/sfx/Falling_down_wind.wav"

    #pause for a few seconds
    $ renpy.pause(delay=3,hard=True)
    
    "..."
    "falling."
    "....you're falling."
    "How did this happen?"
    "In the distance...you hear someone calling your name..."
    
    $ temp_loop = True
    while temp_loop:
        call Name_Select
        "[player.name]"
        "...was that your name?"
        menu:
            "yes":
                "...right. That was it."
                "How could you have forgotten?"
                $ temp_loop = False
            "no":
                "Well, what is it then?"

    $ renpy.pause(delay=3,hard=True)

    #play thud
    stop music
    play sound "audio/sfx/Hitting_the_ground.wav"



    scene
    with vpunch
    "thud"

    scene background flowerfall
    with fade

    "Ow"
    #this looks dirty, but I need to make the variables unique to this screen
    $ tf_loop = True
    $ tf_scream_count = 0
    $ tf_look_around_count = 0
    $ tf_show_exit = 0

    while tf_loop:
        menu:
            "Scream for help":
                call tf_scream from _call_tf_scream
            "Lie down and hope for the best":
                call tf_lie_down from _call_tf_lie_down
            "Look around" if not tf_show_exit:
                call tf_look_around from _call_tf_look_around
            "Approach the door" if tf_show_exit:
                $ tf_loop = False
                jump tf_item_room


label tf_scream:
    $ tf_scream_count += 1

    if tf_look_around_count > 0:
        "you start to scream but quickly notices that the room you’re in has some sound absorbing qualities."
        "Seems like screaming is useless."
    elif tf_scream_count == 1:
        "You scream."
        "..."
        "But nobody came."
    elif tf_scream_count == 2:
        "You scream with all your might."
        "Your ears start ringing."
    elif tf_scream_count == 3:
        "You scream until your throat goes sore."
        "Great, now you are deaf and mute."
    else:
        "You try to scream but all that comes out is a sound not dissimilar to a strangled frog."
        "It may be better to keep your voice down for a while."
    return

label tf_lie_down:

    if tf_scream_count >= 3:
        "Giving a rest to your voice seems like a good idea."
        "..."
        "..."
        "..."
        "You are starting to get thirsty."

    elif tf_look_around_count > 0:
        "You lie down on the flower patch."
        "There are shapes in the shadow.  That one is shaped like an iron maiden."
        "..."
        "..."
        "..."
        "What now?"
    else:
        "You lie down on the flower patch."
        "It's sticky, but otherwise quite soft."
        "..."
        "..."
        "..."
        "What now?"
    return

label tf_look_around:
    $ tf_look_around_count += 1

    if tf_look_around_count == 1:
        "You see dark shadows moving along the cave walls."
        "Your eyes must have not gotten used to the darkness yet."
        "...the concussion you probably have can't be helping any either."
    elif tf_look_around_count == 2:
        "You move your hand over the walls. They are surprisingly clean and dust free."
        "Your nail gets stuck in a crevice.  When you try to pull it out, it breaks."
        "<curse>"
    elif tf_look_around_count == 3:
        "You think one side of the cave is actually brighter so you decide to investigate."
        "Huh?!?"
        "There is a door here.  A fancy door."
        $ tf_show_exit = True
    return


label tf_item_room:
    
    "This room reeks of being a placeholder..."
    
    #for each item, add it to the inventory and then clean up the variable
    while True:
        menu:   
            "There are some items on the floor."
            "Heart Locket":
                call pickup_item(Heart_Locket())
            # "Pocket Mirror":
            # "Stick":
            # "Flower":
