init python:
    basement_visit_count = 0



    
label toriel_return_from_basement:
    toriel "*surprised* Back already? "
    toriel "*smiles* Oh, I am not complaining, just surprised is all."
    toriel "I am glad to spend more time with you. I know Frisk appreciates having your company as well."
    return

label frisk_return_from_basement:
    frisk "Did you chicken out"
    frisk "That’s okay, leaving the ruins can be scary."
    frisk "But everyone is really friendly actually."
    frisk "Anyway, since you’re here, what do you want to do?"
    return


label flowey_basement_demo:
    
    if basement_visit_count == 1:
        flowey "Howdy!"
        flowey "You can’t exit the ruins just yet~"
        flowey "You see, the rest of this world is still being developed! You wouldn’t want to just fall into the void, would you?"
        flowey "*wink* Golly, that wouldn’t be fun."
        flowey "Good thing lil ol’ me was here to stop ya."
        flowey "*smug* Anyways, just turn around I guess. Have fun in the ruins while you wait! "

    elif basement_visit_count == 2:
        flowey "Howdy!"
        flowey "*smug* It’s still being developed, remember? So, I can’t let you go through just yet."

    elif basement_visit_count == 3:
        flowey "*smug* Ever heard of patience?"
        flowey "*smug* Go back and have your fun in the ruins."

    elif basement_visit_count == 4:
        flowey "*annoyed* They didn’t tell me I would have to put up with all of this when they assigned me here…"
        flowey "*sighs* Look, there’s nothing but 1’s and 0’s there, alright? We haven’t even begun creating the assets yet much less the modules for that part of the game. "
        flowey "So if you would be so kind, go back, unless you want to disturb the code monkeys hard at work. I’ve heard they’re too busy trying to keep this game from falling apart already. Memory leaks and all that."

    elif basement_visit_count == 5:
        flowey "*surprised* Object reference not set to an instance of an object"
        flowey "*surprised* ERROR Flag Raised. Memory Dump Log: ZVR117"
        flowey "*surprised* 50 6c 65 61 73 65 20 53 41 56 45 20 6d 65 2e"
        flowey "*angry* What? "
        flowey "*angry* What are you looking at?"

    elif basement_visit_count == 6:
        #FP GAIN NYI
        flowey "*annoyed* Is this some strange attempt to get close to me?"
        flowey "*annoyed* Well, it’s not working. Go away."

    else:
        flowey "*annoyed* Don’t you have anything better to do than pester me?"

        $ basement_visit_count += 1
    return


label the_first_breakfast_wakeup:
    #show black screen
    $ renpy.scene() 

    "Knock Knock"


    frisk "Hey, wake up! Breakfast should be ready soon."

    menu:
        "Get up":
            $ renpy.show(world.current_area.currentRoom.bg)
            #show frisk
            frisk "Hurry up! We don’t want breakfast to get cold!"
            #hide frisk

        "Ignore":

            frisk "Hmm. You're not a morning person, are you?"
            frisk "..."
            frisk "Well, don’t be too late for breakfast, okay?"
            "..."
            "..."
            $ world.move_to_room("Corridor")




# >>CHECK ROOM<<
# --------
# /// if closet
# *there’s nothing in here.
# *what did you expect?

# C2: *you really wish you had brought more clothes with you..

# /// if nightstand
# *it’s empty.

# C2: *it’s still empty.
# C3: *weird there’s no function to put items in here, huh?

# /// if bookshelf
# *you find lots of books about gardening.
# *maybe these could come in handy

# C1: *this may be obvious, but you should regularly water your plants to keep them healthy, and more importantly, alive.
# C2: *sunlight is also a thing.
# *but there isn’t any around here, though.
# C3: *luckily enough, flowers can be fed with magic instead.
# C4: *feeding them magic makes for the most luscious flowers.
# *but they can also suck some of the magic just drifting about in the air.

# /// if bed
# *do you really want to go to bed?
#     (yes)
#     (no)
# /// If (no)
# (player is brought back to the point and click bedroom bg)

# /// If (yes) + player has not had First Breakfast scene yet
# *but your tummy rumbles loudly.
# *maybe you should go have breakfast first.

# /// If (yes) + in the morning
# *but the day just started.
# *besides, don’t you have some snails to hunt?
# (player does not sleep)
# (by the time the player plays the snail hunting game and returns to the ruins ‘morning’ should have already passed)

# /// If (yes) + in the afternoon
# *you like your sleep, don’t you?
# (player sleeps)
# (maybe a small tune/lullaby plays?)

# /// If (yes) + in the evening
# *a bit early, but who cares.
# (player sleeps)
# (maybe a small tune/lullaby plays?)

# /// If (yes) + at night
# (player sleeps)
# (maybe a small tune/lullaby plays?)

# /// If player tries to leave the house
#     frisk "*neutral* You should eat something  before you go exploring!"
#     frisk "And don’t worry, mom isn’t cooking snail pancakes or anything."
#     frisk "*slightly happy* …"
#     frisk "… you shouldn’t mention that to her, she might start getting ideas..."
# /// If player tries to go downstairs
#     frisk "*slightly happy* I don’t think you should go there just yet. "
#     frisk "*Friendly smile* Come eat something first!"


# /// if a RESET has occurred 
# /// If >(player tries to leave the house)<
#     frisk "*neutral* Alright, if you really don’t want to eat, I get it."
#     frisk "You want to leave instead?"
#     (Yes.)
#     (No.)
#         /// If >(player tries to leave the house)< /// If >(yes)<
#             frisk "Okay, I guess I’ll see you later."
#             frisk "…"
#     frisk "And if you ever want to hangout, just tell me. It’ll be fun."
#         /// If >(player tries to leave the house)< /// If >(no)<
#             frisk "Well then, come on!"

# /// If >(player tries to go downstairs)<
#     frisk "You don’t have to leave so quickly, but I understand if you’re in a rush..."
#     (leave)
#     (stay)
# /// If >(player tries to go downstairs)< /// If >(leave)<
#     frisk "Oh… "
#     frisk "Okay, be careful!"
# /// If >(player tries to go downstairs)< /// If >(stay)<
#     frisk "Okay, well, come eat!"
#     frisk " … if you like!"