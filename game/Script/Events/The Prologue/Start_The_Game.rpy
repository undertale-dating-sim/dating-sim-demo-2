label start_the_game:

#    $ world.move_to_room("Cave Room")

label prologue:
    
    #Notes from the video
    #Pause on commas
    #Elipses go slow
    #pictures fade out and in
    scene
    "Long ago, two races ruled over Earth:"
    "HUMANS and MONSTERS."
    "One day, war broke out between the two races."
    "After a long battle, the humans were victorious."
    "They sealed the monsters underground with a magic spell."
    "Many years later...."
    "MT. Ebott"
    "Legends say that those who climb the mountain never return."
    


label the_fall:
    
    scene
    with fade

    #play wind sfx
    #play music "audio/sfx/Falling_down_wind.wav"

    #pause for a few seconds
    $ renpy.pause(delay=3,hard=True)
    
    "..."
    "* Falling."
    "* ....You're falling."
    "* How did this happen?"
    "* ..."
    "* In the distance,you hear someone calling your name."
    
    $ temp_loop = True
    while temp_loop:
        call Name_Select
        "* [player.name]"
        "* ...Is that what they called you?"
        menu:
            "Yes":
                "* ...Right. That was it."
                "* ..."
                "* That's what the voice said."
                $ temp_loop = False
            "No":
                "* Well, what is it, then?"

    # wait a couple of seconds
    $ renpy.pause(delay=3,hard=True)

    jump the_beginning


    