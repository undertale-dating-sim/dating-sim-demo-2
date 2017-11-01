label start_the_game:

#    $ world.move_to_room("Cave Room")

label prologue:
    
    #Notes from the video
    #Pause on commas
    #Elipses go slow
    #pictures fade out and in
    $ renpy.music.set_volume(.5)
    play music "audio/prologue.mp3"
    scene black
    show background prologue1 with Dissolve(2)
    "{cps=9}Long ago, two races ruled over Earth:{/cps}"
    "{cps=9}HUMANS and MONSTERS.{/cps}"
    hide background prologue1 with Dissolve(2)
    show background prologue2 with Dissolve(2)
    "{cps=9}One day, war broke out between the two races.{/cps}"
    "{cps=9}After a long battle, the humans were victorious.{/cps}"
    hide background prologue2 with Dissolve(2)
    show background prologue3 with Dissolve(2)
    "{cps=9}They sealed the monsters underground with a magic spell.{/cps}"
    scene black with Dissolve(2)
    "{cps=9}Many years later....{/cps}"
    hide background prologue3 with Dissolve(2)
    show background prologue4 with Dissolve(2)
    "{cps=9}MT. EBOTT 201X{/cps}"
    "{cps=9}A human fell down to the monsters.{/cps}"
    stop music fadeout 4
    scene black with Dissolve(4)
    "{cps=9}Their story, however, fell short.{/cps}"

    $ renpy.music.set_volume(1)
    pause 2.0
    wilson "..."
    wilson "We are out of cards?"
    wilson "What do you mean this is just the demo?"
    wilson "..."
    "* Scribbling noises..."
    play music "audio/main_menu.mp3"
    show background prologue5 with Dissolve(5)
    "{cps=9}...Not so many years after that...{/cps}"
    "{cps=9}MT. EBOTT 202X...{/cps}"
    hide background prologue1 with Dissolve(2)
    show background prologue6 with Dissolve(3)
    "{cps=9}Another human has fallen...{/cps}"
    "{cps=9}Maybe your story will go a little better...{/cps}"
    scene black with Dissolve(5)
    return
    


label the_fall:
    $ renpy.music.set_volume(.5)
    scene black
    with fade
    stop music
    call prologue
    stop music
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


    