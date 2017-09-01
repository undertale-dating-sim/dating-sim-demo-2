#Event Name: Arts n’ Crafts with Frisk
#Event Trigger: 1. Enter Frisk’s room in the afternoon

#You go into Frisk’s room and walk in on them looking at a blank canvas. This can be set later in the day via the use of the game’s internal clock.


#Expressions
#frisk: normal, disappointed, upset, distant, annoyed, tiny smile, teary eyes, surprised, soulless, big smile, angry, giggling, blush, sad, disgusted, somewhat happy, both panicking sprites

#Requested Artwork:
#Frisk’s painting


#+FP in green

label frisk_friendship_hangout1_main(owner = get_frisk()):

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

    show frisk surprised
    frisk "Oh!"
    show frisk normal
    frisk "I didn’t see you there."
    frisk "Actually, since you're here, would you like to join me?"
    show frisk smallsmile
    frisk "I like painting things, but..."
    frisk "...I don’t know what to paint."
    frisk "If you make something, maybe it’ll inspire me."
    frisk "It could be fun!"
    frisk "So, what do you say?"

    menu:
        "Sorry, I’m busy.": ##//(-2)
            $ world.get_monster('Frisk').update_FP(-2)
            show frisk sad
            frisk "Aww..."
            show frisk normal
            frisk "Okay, I understand."
            frisk "See you around."
            $ get_monster("Frisk").set_special_event("frisk_friendship_return_to_frisk")
            $ move_to_room("Corridor")

        "Yeah!":    ##//(+2)
            $world.get_monster('Frisk').update_FP(2)
            jump frisk_friendship_hangout1_start

label frisk_friendship_return_to_frisk(owner=get_frisk()):
    #if the player re-enters Frisk’s room anytime before dinner:
    show frisk normal
    frisk "Oh, did you change your mind?"
    menu:
        "I hate to break it to you, but no.":    
            frisk "Okay... I’ll see you later."
            $ move_to_room("Corridor")
        "Yes, it actually sounds fun.":        
            $ world.get_monster('Frisk').update_FP(2)
            jump frisk_friendship_hangout1_start


label frisk_friendship_hangout1_start:
    show frisk smallsmile
    frisk "Great!"
    show frisk normal
    frisk "Okay, here, take these."
    "* Frisk gives you paper, a brush, and various colors of paint."
    frisk "Just make whatever you feel like."
    show frisk smallsmile
    frisk "Don’t worry, I won’t judge."
    frisk "I don’t even consider myself that great, but it’s all in good fun."
    frisk "Oh! I just had an idea... I’ll show it to you when we’re both finished."
    frisk "Have fun!"

    "* What color will you use first?"
    menu:
        "Red":          
            $ red = True
        "Yellow":      
            $ yellow = True
        "Blue":         
            $world.get_monster('Frisk').update_FP(2)
            $ blue = True
    frisk "You know, I’m really glad you decided to do this with me."
    frisk "You can probably tell, but I don’t really have many chances to paint with other people."
    show frisk sad
    frisk "I tried to get Mom to paint with me, but..."
    frisk "She said it wasn’t really for her."

    "* What color will you use next?"
    menu:
        "Orange":                                
            $  orange = True
        "Green":                                
            $ green = True
        "Purple":                                
            $ purple = True
        "Aqua":                        
            $ aqua = True
    frisk "It can sometimes get a bit..."
    frisk "...Lonely."
    show frisk disappointed
    frisk "Don’t get me wrong, I love Mom and the other monsters here. But..."
    frisk "A lot of them aren’t exactly..."
    show frisk upset
    frisk "Oh, what am I saying?"
    frisk "I’m sorry, my mind tends to wander when I’m painting."
    menu:
        "No, it’s okay. I understand how you feel.":    
            $ world.get_monster('Frisk').update_FP(3)
            show frisk normal
            frisk "You do?"
            show frisk disappointed
            frisk "It’s just that... I like everyone here, but I want to do more than just live in the Ruins the rest of my life."
            show frisk normal
            frisk "I don’t know exactly what I want to do, but I know it’s not hunting snails!"
        "Mine, too.":                            
            $ world.get_monster('Frisk').update_FP(1)
            show frisk normal
            frisk "Yeah? What do you think about?"
            menu:
                "Nothing in particular.":            #//(+0)
                    show frisk smallsmile
                    frisk "Zoning out can be pretty relaxing. I wish I could do that, but sometimes I can’t seem to switch off."
                "Stuff I have to do later.":            #//(+1)
                    $ world.get_monster('Frisk').update_FP(1)
                    frisk "Huh... You’re just like Mom."
                    frisk "I think that’s why she didn’t like painting much. She was always thinking about other things she’d rather be doing, instead."
                "People I miss on the surface.":        #//(+3)
                    $ world.get_monster('Frisk').update_FP(3)
                    show frisk sad
                    frisk "Oh..."
                    frisk "Sometimes I forget that not everyone likes it down here..."
                    frisk "I mean, I’d like to leave the Ruins, but I guess I’m not that gung-ho about the surface."
                    show frisk normal
                    frisk "All of my friends are here, so I wouldn’t want to leave them behind!"
                    frisk "But I can understand why you’d miss the surface."
                "I’d rather not share.":                #//(+0)
                    frisk "Oh... okay."
                    frisk "..."
        "...":                            
            $ world.get_monster('Frisk').update_FP(-1)
            frisk "..."

    show frisk normal
    frisk "Just curious, how far are you on your painting?"
    frisk "No pressure... I’m just wondering, is all."

    "* What are your finishing touches?"
    menu:
        "Add some swirls":                        #//(+0)
            $ swirls = True
        "Add some stripes":                        #//(+0)
            $ stripes = True
        "Add some random paint splatter":            #//(+0)
            $ randompaintsplatter = True
    "* ..."
    "* You made a thing."

    frisk "Done already?"
    show frisk smallsmile
    frisk "Let me see!"
    frisk "...Abstract. Cool."
    if (red and orange) or (yellow and orange):
        frisk "I like the warm colors."
        if swirls:
            frisk "It kinda looks like the sun."
        elif stripes:
            frisk "I’m not sure what it is, but that’s okay!"
            frisk "That’s the nice thing about abstract art... It doesn’t have to look like anything."
        else:
            frisk "I think it looks a little like a face..."
            frisk "But maybe not."
    elif (blue and green) or (blue and purple) or (blue and aqua):
        frisk "I love the cool colors!"
        if swirls:
            frisk "It sort of looks like a body of water, and the swirling in the middle is some kind of whirlpool."
            frisk "Does that make sense?"
            frisk "Anyway..."
        elif stripes:
            frisk "It reminds me of rain, with the cool colors and the stripes."
            frisk "...If that makes sense."
            frisk "Anyway..."
        else:
            frisk "It definitely looks like water to me."
    elif (red and green) or (yellow and purple) or (blue and orange):
        frisk "Oh! Those are called complementary colors, right?"
        frisk "They look very striking together."
        if swirls:
            frisk "The swirls almost make it look hypnotizing."
        elif stripes:
            frisk "...Especially with those stripes!"
        else:
            frisk "The paint splatter was a nice touch! It looks kind of wild, if that makes sense."
    elif (red and purple) or (red and aqua):

        frisk "Those colors are pretty together."

        if swirls:
            frisk "It’s especially fun-looking with those swirls!"
        elif stripes:

            frisk "The stripes almost make it look like a sunset, if you squint..."
        else:
            frisk "You went pretty wild with that paint splatter! It looks good, though... Really bold."
    elif (yellow and green) or (yellow and aqua):
        frisk "Such bright colors!"
        if swirls:

            frisk "The swirls almost make it look like a field of flowers..."
        elif stripes:

            frisk "It reminds me of lemons!"
            frisk "Mom doesn’t buy them often, but that’s alright. I never liked them much... Too sour."
            frisk "Anyway..."
        else:
            frisk "It looks like a cupcake with sprinkles on top!"

    show frisk smallsmile
    frisk "It’s great!"
    show frisk normal
    frisk "I managed to come up with something, too."
    frisk "I don’t know if it’s very good, but..."
    frisk "Oh, well. I’ll just show you."
    #if the artists drew Frisk’s painting, show it now
    #if there is no drawing, play the following narration:
    "* Frisk holds up a drawing of a blue flower surrounded by water."

    frisk "So... what do you think?"
    menu:
        "I’ve seen better.":                    #//(-3)
            $ world.get_monster('Frisk').update_FP(-3)
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
            $ player.variables['frisk_friendship_1_Complete'] = True
            $ move_to_room("Corridor")
        "Not bad.":                       #//(+0)
            show frisk normal
            frisk "Thanks."
            frisk "We both didn’t really have a lot of time, so I guess it turned out okay."
            frisk "We should do this again sometime. It was fun!"
            frisk "Dinner will probably be ready soon, so I’ll see you around."
            show frisk smallsmile
            frisk "Bye!"
            $ player.variables['frisk_friendship_1_Complete'] = True
            $ move_to_room("Corridor")

        "I love it!":                            #//(+3)
            $ world.get_monster('Frisk').update_FP(3)
            show frisk normal
            frisk "Really?"
            show frisk bigsmile
            frisk "Wow, thanks!"
            frisk "I had a lot of fun doing this. It sounds like you did, too."
            show frisk smallsmile
            frisk "I wish we could do more right now, but it’s getting late. Dinner will probably be ready soon."
            frisk "I’ll see you around!"
            $ player.variables['frisk_friendship_1_Complete'] = True
            $ move_to_room("Corridor")
