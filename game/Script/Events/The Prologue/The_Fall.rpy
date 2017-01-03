label the_beginning:
    #play thud
    stop music
    play sound "audio/sfx/Hitting_the_ground.wav"
    scene

    with vpunch
    "Thud"

    $ renpy.show(world.get_room("Cave Room").bg)
    with fade

    "* Ow."
    #this looks dirty, but I need to make the variables unique to this screen
    $ tf_loop = True
    $ tf_scream_count = 0
    $ tf_look_around_count = 0
    $ tf_show_exit = 0

    while tf_loop:
        menu:
            "Scream for help":
                call tf_scream
            "Lie down and hope for the best":
                call tf_lie_down
            "Look around" if not tf_show_exit:
                call tf_look_around


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
    return
        


label unlock_movement_engine:
    $ world.get_room("Grass Room").add_event("tf_item_room")
    $ world.move_to_room("Cave Room")
    return

#if the player refuses all offers by Toriel and Frisk to stay at their house, they will eventually run out of stamina. In this case, the following scene will play:
label ruins_intro_pass_out:
    #can we have some kind of transition showing the MC’s eyes slowly opening?
    $ world.move_to_room('Your Room')
    show toriel normal
    toriel "Oh, thank goodness you are awake…"
    toriel "I apologize, this must be very disorienting for you."
    show toriel awkward
    toriel "I found you lying on the ground outside, and thought it would be best to bring you into my home. You would not wake up, I was afraid that…"
    show toriel normal
    toriel "Well, you should be more careful. You mustn’t keep running yourself into the ground… You need to allow yourself time to rest."
    show toriel small_smile
    toriel "You are more than welcome to return here whenever you are tired. I promise, my child and I do not bite!"

    menu:
        toriel "You are more than welcome to return here whenever you are tired. I promise, my child and I do not bite!"
        "Alright, I’ll stay here with you.":
            $ world.get_monster('Toriel').FP += 1
            call accept
        "No way, I’m leaving!":
            $ world.get_monster('Toriel').FP -= 2
            call reject


# ///If >81("Alright, I’ll stay here with you.")<
# #show toriel smile
# toriel "I am glad to hear it."


# #if the player has already met Frisk:
# toriel "While you were gone, I made a meal with the snails you and Frisk caught. I am sure there is enough to go around, if you would like to join us for dinner."
# Frisk "Mom? Are they awake yet?"
# #show Frisk big smile
# Frisk "Oh, hey! I’m glad you’re okay… Mom and I were really worried about you!"
# Frisk "If you’re staying for dinner, you should hurry up! The food’s getting cold!"
# #show Frisk normal
# Frisk "C’mon, I’ll show you to the living room…"
# jump frisk_meeting_eat


# #if the player has not met Frisk, jump ruins_intro_find_Frisk


label reject:
    show toriel annoyed
    toriel "Well, if that is how you feel..."
    toriel "Just do not expect me to find you the next time you pass out."
    show toriel sad
    toriel "I cannot keep chasing after someone who does not want my help."
    toriel "You are always welcome to return if you change your mind. Just remember that."
    $ move_to_room("Black Tree Room")
    $ player.safe_room = 'Black Tree Room'


    #player is now free to wander the Ruins. If they pass out again, they’ll just wake up in the same spot with the following narration:
    

    #*You wake up, sore from laying on the ground. You must’ve passed out again.
    #the game cannot progress until the player returns to toriel’s house and accepts her offer





    



