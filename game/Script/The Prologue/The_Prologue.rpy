label start_the_game:

    #$ world.get_monster("toriel").move_to_room("Dead Room")
    #$ world.get_monster("toriel").reset_schedule()
   # $ world.get_monster("napstablook").move_to_room("Dead Room")
    #$ world.get_monster("napstablook").reset_schedule()
    #$ world.get_monster("frisk").move_to_room("Overlook")
    #$ world.get_monster("frisk").reset_schedule()
   # $ world.get_monster("flowey").move_to_room("Dead Room")
    #$ world.get_monster("flowey").reset_schedule()

    $ world.move_to_room("Dead Room")
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


    jump the_beginning


    