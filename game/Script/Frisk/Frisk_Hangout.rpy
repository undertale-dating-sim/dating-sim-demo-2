#---- In Order To Keep From Confusing Coders, All Dialogue Templates Should Attempt to Follow This Pattern  ----

#KEY:
#sans "__"      = character dialog
#*Asterisks*     = Sprite changes
#("Parenthesis") = dialogue options
##//(+0)           = Response’s Increase/Decrease to Date Meter
##/// If >  <   = The order of player answers that lead up to that            dialogue
#[n/a #]        = Dialogue option not available if previous option
#has been used (all options assigned a number)
#+ Or -         = amount of points
#jump ___    = tells the game to skip to a different part of the script
#label ___:    = marks a part of the script so it can be jumped to
#blah blah     = message for all coders and editors. used for all other communication that cannot be indicated otherwise
#Edited Dialogue After coders have already put it into the game
#Striked out means text has been deleted
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Event Name: Arts n’ Crafts with Frisk
#Event Trigger: 1. Enter Frisk’s room in the afternoon

#You go into Frisk’s room and walk in on them looking at a blank canvas. This can be set later in the day via the use of the game’s internal clock.


#Expressions
#frisk: normal, disappointed, upset, distant, annoyed, tiny smile, teary eyes, surprised, soulless, big smile, angry, giggling, blush, sad, disgusted, somewhat happy, both panicking sprites

#Requested Artwork:
#Frisk’s painting


#+FP in green

label frisk_friendship_hangout1_main:
    stop music
    play music "audio/music/music-home.mp3"
    show background frisk_room
    python:
        red = False
        yellow = False
        blue = False
        orange = False
        green = False
        purple = False
        aqua = False
        swirls = False
        stripes = False
        randompaintsplatter = False
    #scene frisk’s room
    show frisk surprised
    frisk "Oh!"
    show frisk normal
    frisk "I didn’t see you there."
    frisk "Actually, since you're here, would you like to join me?"
    show frisk tinysmile
    frisk "I like painting things, but..."
    frisk "...I don’t know what to paint."
    frisk "If you make something, maybe it’ll inspire me."
    frisk "It could be fun!"
    frisk "So, what do you say?"
    jump frisk_friendship_hangout1_selection1
label frisk_friendship_hangout1_selection1:
    menu:
        "Sorry, I’m busy.": ##//(-2)
            $ world.get_monster('Frisk').update_FP(-2)

            jump frisk_friendship_hangout1_choice1
        "Yeah!":    ##//(+2)
            $world.get_monster('Frisk').update_FP(2)
            jump frisk_friendship_hangout1_choice2

label frisk_friendship_hangout1_choice1:
    show frisk sad
    frisk "Aww..."
    show frisk normal
    frisk "Okay, I understand."
    frisk "See you around."
    #scene change hallway
label frisk_friendship_return_to_frisk:
    #if the player re-enters Frisk’s room anytime before dinner:
    show frisk normal
    frisk "Oh, did you change your mind?"
    jump frisk_friendship_hangout1_selection2
label frisk_friendship_hangout1_selection2:
    menu:
        "I hate to break it to you, but no.":    #//(+0)
            jump frisk_friendship_hangout1_choice3
        "Yes, it actually sounds fun.":        #//(+2)
            $ world.get_monster('Frisk').update_FP(2)
            jump frisk_friendship_hangout1_choice4

label frisk_friendship_hangout1_choice3:
    #/// If >3("I hate to break it to you, but no.")<
    frisk "Okay... I’ll see you later."
    #scene change hallway
    #####################
    #Change below code to hallway code
    jump statcheck

label frisk_friendship_hangout1_choice4:
    #/// If >4("Yes, it actually sounds fun.")<
    jump frisk_friendship_hangout1_start
label frisk_friendship_hangout1_choice2:
    #/// If >2("Yeah!")<
    jump frisk_friendship_hangout1_start


label frisk_friendship_hangout1_start:
    show frisk tinysmile
    frisk "Great!"
    show frisk normal
    frisk "Okay, here, take these."
    "*Frisk gives you paper, a brush, and various colors of paint."
    frisk "Just make whatever you feel like."
    show frisk tinysmile
    frisk "Don’t worry, I won’t judge."
    frisk "I don’t even consider myself that great, but it’s all in good fun."
    frisk "Oh! I just had an idea... I’ll show it to you when we’re both finished."
    frisk "Have fun!"

    "*What color will you use first?"
    jump frisk_friendship_hangout1_selection3
label frisk_friendship_hangout1_selection3:
    menu:
        "Red":          #//(+0)
            $ red = True
        "Yellow":      #//(+0)
            $ yellow = True
        "Blue":          #//(+2)
            $world.get_monster('Frisk').update_FP(2)
            $ blue = True
    frisk "You know, I’m really glad you decided to do this with me."
    frisk "You can probably tell, but I don’t really have many chances to paint with other people."
    show frisk sad
    frisk "I tried to get Mom to paint with me, but..."
    frisk "She said it wasn’t really for her."

    "*What color will you use next?"
    jump frisk_friendship_hangout1_selection4

label frisk_friendship_hangout1_selection4:
    menu:
        "Orange":                                #//(+0)
            $  orange = True
        "Green":                                #//(+0)
            $ green = True
        "Purple":                                #//(+0)
            $ purple = True
        "Aqua":                        #//(+0)
            $ aqua = True
    frisk "It can sometimes get a bit..."
    frisk "...Lonely."
    show frisk disappointed
    frisk "Don’t get me wrong, I love Mom and the other monsters here. But..."
    frisk "A lot of them aren’t exactly..."
    show frisk upset
    frisk "Oh, what am I saying?"
    frisk "I’m sorry, my mind tends to wander when I’m painting."
    jump frisk_friendship_hangout1_selection5

label frisk_friendship_hangout1_selection5:
    menu:
        "No, it’s okay. I understand how you feel.":    #//(+3)
            $ world.get_monster('Frisk').update_FP(3)
            jump frisk_friendship_hangout1_choice12
        "Mine, too.":                            #//(+1)
            $ world.get_monster('Frisk').update_FP(1)
            jump frisk_friendship_hangout1_choice13
        "...":                            #//(-2)
            $ world.get_monster('Frisk').update_FP(-1)
            jump frisk_friendship_hangout1_choice14
label frisk_friendship_hangout1_choice12:
    #/// If >12("No, it’s okay. I understand how you feel.")<
    show frisk normal
    frisk "You do?"
    show frisk disappointed
    frisk "It’s just that... I like everyone here, but I want to do more than just live in the Ruins the rest of my life."
    show frisk normal
    frisk "I don’t know exactly what I want to do, but I know it’s not hunting snails!"
    jump frisk_friendship_hangout1_finished
label frisk_friendship_hangout1_choice13:
    #/// If >13("Mine, too.")<
    show frisk normal
    frisk "Yeah? What do you think about?"
    jump frisk_friendship_hangout1_selection6
label frisk_friendship_hangout1_selection6:
    menu:
        "Nothing in particular.":            #//(+0)
            jump frisk_friendship_hangout1_choice15
        "Stuff I have to do later.":            #//(+1)
            $ world.get_monster('Frisk').update_FP(1)
            jump frisk_friendship_hangout1_choice16
        "People I miss on the surface.":        #//(+3)
            $ world.get_monster('Frisk').update_FP(3)
            jump frisk_friendship_hangout1_choice17
        "I’d rather not share.":                #//(+0)
            jump frisk_friendship_hangout1_choice18
label frisk_friendship_hangout1_choice15:

    #/// If >13("Mine, too.")< AND >15("Nothing in particular.")<
    show frisk tinysmile
    frisk "Zoning out can be pretty relaxing. I wish I could do that, but sometimes I can’t seem to switch off."
    jump frisk_friendship_hangout1_finished
label frisk_friendship_hangout1_choice16:
    #/// If >13("Mine, too.")< AND >16("Stuff I have to do later.")<
    frisk "Huh... You’re just like Mom."
    frisk "I think that’s why she didn’t like painting much. She was always thinking about other things she’d rather be doing, instead."
    jump frisk_friendship_hangout1_finished
label frisk_friendship_hangout1_choice17:
    #/// If >13("Mine, too.")< AND >17("People I miss on the surface.")<
    show frisk sad
    frisk "Oh..."
    frisk "Sometimes I forget that not everyone likes it down here..."
    frisk "I mean, I’d like to leave the Ruins, but I guess I’m not that gung-ho about the surface."
    show frisk normal
    frisk "All of my friends are here, so I wouldn’t want to leave them behind!"
    frisk "But I can understand why you’d miss the surface."
    jump frisk_friendship_hangout1_finished
label frisk_friendship_hangout1_choice18:
    #/// If >13("Mine, too.")< AND >18("I’d rather not share.")<
    frisk "Oh... okay."
    frisk "..."
    jump frisk_friendship_hangout1_finished
label frisk_friendship_hangout1_choice14:
    #/// If >14("...")<
    frisk "..."
    jump frisk_friendship_hangout1_finished


label frisk_friendship_hangout1_finished:
    show frisk normal
    frisk "Just curious, how far are you on your painting?"
    frisk "No pressure... I’m just wondering, is all."

    "*What are your finishing touches?"
    jump frisk_friendship_hangout1_selection7
label frisk_friendship_hangout1_selection7:
    menu:
        "Add some swirls":                        #//(+0)
            $ swirls = True
        "Add some stripes":                        #//(+0)
            $ stripes = True
        "Add some random paint splatter":            #//(+0)
            $ randompaintsplatter = True
    "*..."
    "*You made a thing."

    frisk "Done already?"
    show frisk tinysmile
    frisk "Let me see!"
    frisk "...Abstract. Cool."
    if (red and orange) or (yellow and orange):
        #/// If >([5(Red) + 8(Orange)] OR [6(Yellow) + 8(Orange)])<
        frisk "I like the warm colors."
        if swirls:
            #if 19(Add some swirls):
            frisk "It kinda looks like the sun."
        elif stripes:
            #if 20(Add some stripes):
            frisk "I’m not sure what it is, but that’s okay!"
            frisk "That’s the nice thing about abstract art... It doesn’t have to look like anything."
        else:
            #if 21(Add some random paint splatter):
            frisk "I think it looks a little like a face..."
            frisk "But maybe not."
    elif (blue and green) or (blue and purple) or (blue and aqua):
        #/// If > ([7(Blue) + 9(Green)] OR [7(Blue) + 10(Purple)] OR [7(Blue) + 11(Aqua)])<
        frisk "I love the cool colors!"
        #if 19(Add some swirls):
        if swirls:
            frisk "It sort of looks like a body of water, and the swirling in the middle is some kind of whirlpool."
            frisk "Does that make sense?"
            frisk "Anyway..."
        elif stripes:
            #if 20(Add some stripes):
            frisk "It reminds me of rain, with the cool colors and the stripes."
            frisk "...If that makes sense."
            frisk "Anyway..."
        else:
            #if 21(Add some random paint splatter):
            frisk "It definitely looks like water to me."
    elif (red and green) or (yellow and purple) or (blue and orange):
        #/// If > ([5(Red) + 9(Green)] OR [6(Yellow) + 10(Purple)] OR [7(Blue) + 8(Orange)])<
        frisk "Oh! Those are called complementary colors, right?"
        frisk "They look very striking together."
        if swirls:
            #if 19(Add some swirls):
            frisk "The swirls almost make it look hypnotizing."
        elif stripes:
            #if 20(Add some stripes):
            frisk "...Especially with those stripes!"
        #if 21(Add some random paint splatter):
        else:
            frisk "The paint splatter was a nice touch! It looks kind of wild, if that makes sense."
    elif (red and purple) or (red and aqua):

        #/// If > ([5(Red) + 10(Purple)] OR [5(Red) + 11(Aqua)])<
        frisk "Those colors are pretty together."

        if swirls:
            #if 19(Add some swirls):
            frisk "It’s especially fun-looking with those swirls!"
        elif stripes:

            #if 20(Add some stripes):
            frisk "The stripes almost make it look like a sunset, if you squint..."
        else:
            #if 21(Add some random paint splatter):
            frisk "You went pretty wild with that paint splatter! It looks good, though... Really bold."
    elif (yellow and green) or (yellow and aqua):
        #/// If > ([6(Yellow) + 9(Green)] OR [6(Yellow) + 11(Aqua)])<
        frisk "Such bright colors!"
        if swirls:

            #if 19(Add some swirls):
            frisk "The swirls almost make it look like a field of flowers..."
        elif stripes:

        #if 20(Add some stripes):
            frisk "It reminds me of lemons!"
            frisk "Mom doesn’t buy them often, but that’s alright. I never liked them much... Too sour."
            frisk "Anyway..."
        else:
            #if 21(Add some random paint splatter):
            frisk "It looks like a cupcake with sprinkles on top!"

    show frisk tinysmile
    frisk "It’s great!"
    show frisk normal
    frisk "I managed to come up with something, too."
    frisk "I don’t know if it’s very good, but..."
    frisk "Oh, well. I’ll just show you."
    #if the artists drew Frisk’s painting, show it now
    #if there is no drawing, play the following narration:
    "*Frisk holds up a drawing of a blue flower surrounded by water."

    frisk "So... what do you think?"
    jump frisk_friendship_hangout1_selection8
label frisk_friendship_hangout1_selection8:
    menu:
        "I’ve seen better.":                    #//(-3)
            $ world.get_monster('Frisk').update_FP(-3)
            jump frisk_friendship_hangout1_choice22
        "Not bad.":                       #//(+0)
            jump frisk_friendship_hangout1_choice23

        "I love it!":                            #//(+3)
            $ world.get_monster('Frisk').update_FP(3)
            jump frisk_friendship_hangout1_choice24
label frisk_friendship_hangout1_choice22:
    #/// If > 22("I’ve seen better.")<
    show frisk sad
    frisk "Oh..."
    frisk "I thought it was alright..."
    frisk "Well, uh..."
    show frisk somehappy
    show frisk bigsmile
    frisk "I appreciate your honesty."
    frisk "I’ll try again next time...?"
    frisk "Well... if you wanna do this again another time..."
    frisk "Let me know, okay?"
    frisk "I’ll see you later."
    #End of scene, time should be dinnertime
    jump statcheck
label frisk_friendship_hangout1_choice23:
    #/// If >23("Not bad.")<
    show frisk normal
    frisk "Thanks."
    frisk "We both didn’t really have a lot of time, so I guess it turned out okay."
    frisk "We should do this again sometime. It was fun!"
    frisk "Dinner will probably be ready soon, so I’ll see you around."
    show frisk tinysmile
    frisk "Bye!"
    #End of scene, time should be dinnertime
    jump statcheck
label frisk_friendship_hangout1_choice24:

    #/// If >24("I love it!")<
    show frisk normal
    frisk "Really?"
    show frisk bigsmile
    frisk "Wow, thanks!"
    frisk "I had a lot of fun doing this. It sounds like you did, too."
    show frisk tinysmile
    frisk "I wish we could do more right now, but it’s getting late. Dinner will probably be ready soon."
    frisk "I’ll see you around!"
    #End of scene, time should be dinnertime
    jump statcheck
label statcheck:
    #$ renpy.say("Frisk FP: ",str(frisk_fp))
    jump testing_area
