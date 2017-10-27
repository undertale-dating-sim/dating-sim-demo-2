label frisk_meeting_start:
    python:
        chose_frisk_meeting_option40_5 = False
        chose_frisk_meeting_option39=False
        chose_frisk_meeting_option27=False
        chose_frisk_meeting_option30=False
        chose_frisk_meeting_option65_count = 0
        chose_frisk_meeting_option66_count = 0
        chose_frisk_meeting_option67_count = 0
        chose_frisk_meeting_option68_count = 0
        chose_frisk_meeting_option69_count = 0
        chose_frisk_meeting_option70_count = 0
        chose_frisk_meeting_option71_count = 0
        chose_frisk_meeting_option65 = False
        chose_frisk_meeting_option66 = False
        chose_frisk_meeting_option67 = False
        chose_frisk_meeting_option68 = False
        chose_frisk_meeting_option69 = False
        chose_frisk_meeting_option70 = False
        chose_frisk_meeting_option71 = False
        fm_checked_toriel_room = False
        chose_frisk_meeting_option6 = False
        chose_frisk_meeting_option37 = False
        chose_frisk_meeting_option72 = False

    $ renpy.transition(fade)
    $ renpy.show(world.get_room("Overlook").bg)
    $ set_lock_room("Snail Hunting Room",False)
    $ player.variables['met_frisk'] = True
    show frisk normal
    stop music
    $renpy.pause()
    show frisk surprised with Dissolve(.25)
    play music "audio/ruins/frisk.mp3"
    unknown "Oh! Um, hi. I wasn't expecting to see another human. How... how did you get here?" 

    menu:
        "I could ask you the same thing.":  
            show frisk smallsmile with Dissolve(.25)
            unknown "Oh, well, you know... I guess I was hiking, and I just... sort of..."
            show frisk surprised with Dissolve(.25)
            unknown "Oh! I'm sorry, I forgot my manners."
            show frisk somehappy with Dissolve(.25)
            unknown "I'm Frisk. It's nice to meet you!"
            frisk "I'm a human, too!"
            frisk "But, um, I guess you could probably see that."

            menu:
                "Are there more humans down here?":  
                    $world.get_monster('Frisk').update_FP(1)
                    show frisk normal with Dissolve(.25)
                    frisk "Oh, no... not that I know of."
                    frisk "You're actually the first human I've seen since I fell down here."
                    frisk "I've been living here with Mom- I mean, you probably know her as Toriel."
                    show frisk somehappy with Dissolve(.25)
                    frisk "She's taken care of me since I was a kid!"

                "And you live with a monster?":    
                    show frisk normal with Dissolve(.25)
                    frisk "Yeah. When I came to the Underground, Mom... I mean, Toriel... found me and has been taking care of me ever since."

        "I tripped.":
            $world.get_monster('Frisk').update_FP(3)
            show frisk giggly with Dissolve(.25)
            unknown "Ha ha! You're funny.  No one just 'trips' and ends up down here."
            show frisk smallsmile with Dissolve(.25)
            unknown "..."
            unknown "At least, no one that I know."
            show frisk somehappy with Dissolve(.25)
            unknown "Oh, where are my manners... my name is Frisk!"

        "You're not Toriel's kid, are you?":
            $world.get_monster('Frisk').update_HP(2)
            show frisk annoyed with Dissolve(.25)
            unknown "Yes I am!"
            show frisk disappointed with Dissolve(.25)
            unknown "Oh, right. You were probably expecting me to be a monster, huh?"
            show frisk normal with Dissolve(.25)
            unknown "My name is Frisk."
            frisk "I'm a human. Mom- well, you know her as Toriel..."
            frisk "She's really nice, and she takes care of me."

        "Hi, nice to meet you!":
            $world.get_monster('Frisk').update_FP(4)
            show frisk surprised with Dissolve(.25)
            unknown "Oh! Right, where are my manners... my name is Frisk!"
            show frisk smallsmile with Dissolve(.25)
            frisk "It's nice to meet you, too. I, uh... hope you grow to like the Underground."
            frisk "It's pretty great once you get used to it."

label frisk_meeting_questions:
    menu:
        "You're actually a human? Not some monster?" if chose_frisk_meeting_option6 == False:
            show frisk somehappy with Dissolve(.25)
            frisk "Yeah! I live with my mom- I mean, Toriel, the caretaker of the Ruins."
            frisk "She's really kind. Have you met her?"
            $ chose_frisk_meeting_option6 = True
            jump frisk_meeting_questions
        
        "I've recently met Toriel. She seems nice.":
            $world.get_monster('Frisk').update_FP(3)
            show frisk bigsmile with Dissolve(.25)
            frisk "Yeah! Out of all the people that could've found me, I'm glad it was her."

            menu:
                "Are you saying the other monsters are bad?":
                    $world.get_monster('Frisk').update_HP(1)            
                    show frisk surprised with Dissolve(.25)
                    frisk "What? No!"
                    show frisk upset with Dissolve(.25)
                    frisk "I mean, other monsters are great, too."
                    frisk "I shouldn't have said that... it was mean."
                    frisk "But she's the only one who's really taken care of me, y'know?"

                "I can relate. She helped me, too.":
                    $world.get_monster('Frisk').update_FP(2)
                    show frisk smallsmile with Dissolve(.25)
                    frisk "That's great! She can handle anything!"
                    show frisk upset with Dissolve(.25)
                    frisk "..."
                    show frisk somehappy with Dissolve(.25)
                    frisk "Well, most things."

        "How's life here in the Ruins?":
            $world.get_monster('Frisk').update_FP(3)  
            show frisk somehappy with Dissolve(.25)
            frisk "Well, we don't have much, but it's nice. It's just that sometimes Mom makes food with snails in it, and it's..."
            show frisk upset with Dissolve(.25)
            frisk "...not amazing... but don't worry about it."
            show frisk somehappy with Dissolve(.25)
            frisk "Other than that, things are pretty great."
            menu:
                "Are you feeling okay? You look a little under the weather.":
                    $world.get_monster('Frisk').update_FP(3)
                    frisk "Oh, um. I'm... I'm fine."
                    frisk "Tiring day, ya know?"
                    frisk "But... I appreciate your concern."
                    menu:
                        "Are you sure you're okay? Do you want to talk about something?":
                            $world.get_monster('Frisk').update_FP(1)
                            frisk "No, really... it's fine. I appreciate the help... I really do. But, honestly, it's nothing."
                            menu:
                                "Oh, come on, tell me!":
                                    $world.get_monster('Frisk').update_HP(2)
                                    show frisk annoyed with Dissolve(.25)
                                    frisk "Please, you're making this more than what it is."
                                    menu:
                                        "You have to tell me!":
                                            $world.get_monster('Frisk').update_FP(-3)
                                            #+1 Determination
                                            show frisk angry with Dissolve(.25)
                                            frisk "No, I don't have to tell you anything! I'm not talking about this anymore!"
                                            show frisk normal with Dissolve(.25)
                                            frisk "Sorry, I don't like people getting on my back about things."


                                        "Alright, I'm sorry.":
                                            show frisk annoyed with Dissolve(.25)
                                            frisk "..."
                                            frisk "...Thank you."


                                "Just making sure.":
                                    $world.get_monster('Frisk').update_FP(2)
                                    frisk "Thanks. You remind me a lot of Mom, actually." 
                                    show frisk bigsmile with Dissolve(.25)
                                    frisk "But... don't go thinking you can outdo her in the mothering department! She's the master!"

                        "...":
                            pass

                "I'm sure everything must be great for you then!":
                    frisk "Yup... pretty much."

##################################
#  FRISK MEETING SNAIL CATCHING  #
##################################

label frisk_meeting_snail_catching:

    show frisk normal with Dissolve(.25)
    frisk "Oh, hey... is that a crack on your phone? It looks pretty banged up."
    show frisk smallsmile with Dissolve(.25)
    frisk "Here, you can take my old phone! My friend made me a new one, so I don't mind."

    play sound "audio/sfx/use_item.wav"

    "* You get The CELL!"
    "The CELL has been unlocked in the MENU."
    "You can use The CELL to view your relationship with the various citizens of the Underground."
    "If you call them, they can give you some info about the room you are in."
    "They can also let you know where they are!"

    frisk "And I've already transferred all of my old junk off of it, so it's just like new."
    frisk "Oh, and I'll add my number into it! That way, if you ever need to get in touch with me, I'll just be a phone call away!"

    ################################
    play sound "audio/sfx/use_item.wav"
    "* Frisk's number obtained."
    $player.variables['has_frisk_cell'] = True
    $player.variables['has_cellphone'] = True

    ###############################

    frisk "So..."
    show frisk surprised with Dissolve(.25)
    frisk "Oh wait, I almost forgot!"
    show frisk somehappy with Dissolve(.25)
    frisk "I'm actually supposed to be doing something important..."
    frisk "I need your help. It won't take long, I promise."
    frisk "Just follow me!"
     
    #-Transition to Snail Catching Room-
    #-Transition: Snail Catching Mini-game-
    show background ruins_monstercandy_room with Fade(0.5, 2, 0.5)
     
    show frisk normal with Dissolve(.25)
    frisk "Sorry for the hike."
    frisk "Check this out!"
    "* Frisk moves some of the vines out of the way behind the bowl of candy."
    "* There is a door there!"
    
    play sound "audio/sfx/use_item.wav"
    "You discover the Snail Hunting Room!"
    $ world.get_room("Snail Hunting Room").mappable = True

    frisk "Stuff like this is all over the place."
    frisk "There might even be some stuff I haven't found."

    show background ruins_snailhunting_room with Fade(0.5, 0, 0.5)
    frisk "Okay, here we are."
    frisk "I know this is going to sound a bit weird, but I need to catch snails."
    frisk "Mom makes food with them, and she needs a lot!"

    menu:
        "You're right, that is weird.":
            #-1 Patience
            $world.get_monster('Frisk').update_HP(1)
            show frisk somehappy with Dissolve(.25)
            frisk "Well, what can I say?" 
            show frisk annoyed with Dissolve(.25)
            frisk "But seriously, this is important. I'll need your help."
            show frisk bigsmile with Dissolve(.25)
            frisk "Catching snails is harder than you'd think."

        "That sounds completely reasonable.":
            $world.get_monster('Frisk').update_FP(3)
            frisk "Really, you think so?"
            menu:
                "Yeah, I do it all the time!":  
                    $world.get_monster('Frisk').update_FP(3)
                    show frisk bigsmile with Dissolve(.25)
                    frisk "That's great! This'll be easy!"

                "I lied. That makes no sense whatsoever.":
                    $world.get_monster('Frisk').update_FP(-5)
                    #-1 Integrity
                    show frisk upset with Dissolve(.25)
                    frisk "Oh... okay."
                    frisk "Well- please, I really do need your help. Even if it doesn't make sense to you."

        "Oh yeah, Toriel already told me." if 'clicked_toriel' in player.variables:
            $world.get_monster('Frisk').update_FP(4)
            show frisk bigsmile with Dissolve(.25)
            frisk "Nice!"
            frisk "Mom has a lot of different snail dishes. You wouldn't believe what she can do with them!"
            frisk "Anyway..."

    show frisk normal with Dissolve(.25)
    frisk "Here's what I need you to do..."
    frisk "First, here, take this net."
    
    play sound "audio/sfx/use_item.wav"
    "* You get the Butterfly Net!"
    "* It's a big butterfly net, good for catching snails."
     
    frisk "Basically, just try to catch as many snails as you can!"
    frisk "It's tricky, though, because you can only try to catch them for a certain amount of time per day. After that, they'll start to get suspicious and won't come out of their hiding places."
    frisk "Ready? Here we go!"
     
    #Snail Minigame happens
    call UnderSnail
     
    show frisk smallsmile with Dissolve(.25)
    frisk "Ya know, I'm actually feeling a bit better right now."
    frisk "Mom will be happy, too... She really likes snails!"
    frisk "If you give her some, she'll appreciate it. Maybe even pay you back somehow."
    #frisk "She might want different kinds of snails on different days, so you might want to check with her to find out."
    
    show frisk surprised with Dissolve(.25)
    frisk "Oh!"
    
    show frisk bigsmile with Dissolve(.25)
    frisk "And if you want to do this again sometime, just tell me. This was fun!"
    frisk "...Or you could do it on your own, whatever works! Help in any form is appreciated!"
    
    show frisk normal with Dissolve(.25)
    frisk "I, uh, I should get going now. Mom is probably wondering why I'm out so late..."
    frisk "Our house isn't too far from here. Do you want to come with me?"
    frisk "Mom and I would love it if you stayed for awhile..."
    
    menu:
        "Yeah, I'm in!":
            $player.variables['accepted_frisk'] = True
            $world.get_monster('Frisk').update_FP(3)
            show frisk bigsmile with Dissolve(.25)
            frisk "Alright, let's go!"
            $ renpy.transition(fade)
            play music "audio/ruins/toriels_house.mp3" fadein 5.0
            $ renpy.show(world.get_room("Staircase").bg)
            show frisk smallsmile with Dissolve(.25)
            frisk "Here we are!"
            show frisk normal with Dissolve(.25)
            frisk "Hold on... let me tell Mom we're back."
            hide frisk
            $ get_room("Staircase").events = {}
            jump frisk_meeting_home

        "I'll be there soon, but I think I'm gonna look around the Ruins for a little while longer.":
            $world.get_monster('Frisk').update_FP(3)
            frisk "Alright, that's fine. I'll see ya there!"
            frisk "Just be sure not to stay out too late. If you don't get enough sleep, you could get sick."
            show frisk bigsmile with Dissolve(.25)
            frisk "I'm starting to sound like Mom now. Oh well... see ya!"
            hide frisk with Dissolve(.25)
            $ get_room("Staircase").set_event("frisk_meeting_late",False)
            $ move_to_room('Snail Hunting Room')
            

        "I don't want to stay with you guys." if 'accepted_toriel' in player.variables and player.variables['accepted_toriel']==False:
            $world.get_monster('Frisk').update_FP(-4)
            show frisk disappointed with Dissolve(.25)
            frisk "Oh... okay. I just thought..."
            show frisk somehappy with Dissolve(.25)
            frisk "Well, if you ever change your mind, just stop on by our house! Mom and I love having guests."
            frisk "See ya later!"
            hide frisk with moveoutright
            $ move_to_room('Snail Hunting Room')
            
    return


label frisk_meeting_late:
    hide frisk
    $ world.set_current_time("Evening",False)
    frisk "Oh, I think they're here. I'll be right back!"
    show frisk normal with Dissolve(.25)
    frisk "Hi! You're a bit late... the food is a little cold. But I'm sure it's fine. Hold on, let me tell Mom you're here."
    hide frisk
    jump frisk_meeting_home

########################
#  FRISK MEETING HOME  #
########################

label frisk_meeting_home:
    show frisk normal at left with Dissolve(.25)
    show toriel normal at right with Dissolve(.25)
    frisk "This is the person I told you about."
    if 'met_toriel' in player.variables == True:
        toriel "Ah, hello! It is very nice to have you over for dinner." 
        toriel "I do apologize for having to rush off so quickly before."
        toriel "Truthfully, I was a little worried about having to leave you on your own in the Ruins, but it is good to see that you are well."
        show frisk bigsmile with Dissolve(.25)
        frisk "Anyway, let's eat!"
        show toriel smallsmile with Dissolve(.25)
        toriel "Yes, please join us."
        jump frisk_meeting_eat
    else:
        toriel "Welcome back! I am glad you and Frisk managed to find each other."
        show frisk bigsmile with Dissolve(.25)
        frisk "Anyway, let's eat!"
        toriel "Yes, please join us."
        jump frisk_meeting_eat

label looked_around_before_toriel:
        #If the player chose option 25 of selection 11 (look around the Ruins for a little while longer) (if not, just skip this part)
        toriel "Frisk has told me a lot about you while you were gone." 

        show toriel normal with Dissolve(.25)
        if world.get_monster('Toriel').FP < 20:
            toriel "There is not much to do here, but we are always looking for a helping hand--especially if you do not mind getting your hands dirty."
            show frisk bigsmile with Dissolve(.25)
            frisk "Anyway, let's eat!"
            toriel "Yes, please join us."
            jump frisk_meeting_eat
        else:
            $world.get_monster('Toriel').update_FP(3,"right")
            show toriel smile with Dissolve(.25)
            toriel "It makes me happy to see you and frisk have become such fast friends. It gets a little lonely here in the Ruins sometimes, and we do appreciate any well-meaning company." 
            toriel "I am sure you know this by now, but I would like you to know that any friend of frisk is welcome here."
            show frisk bigsmile with Dissolve(.25)
            frisk "Anyway, let's eat!"
            toriel "Yes, please join us."
            jump frisk_meeting_eat
             
#######################
#  FRISK MEETING EAT  #
#######################

label frisk_meeting_eat:
    call hide_buttons
    $ player.variables['accepted_toriel'] = True
    if world.current_timezone == "Afternoon":
        $ world.set_current_time("Evening")
    else:
        $ world.set_current_time("Afternoon")
    hide frisk with moveoutleft
    hide toriel with moveoutleft
    "* You follow Toriel and Frisk to the Living Room."
    $ renpy.show(world.get_room("Living Room").bg)

    show frisk normal at left with Dissolve(.25) 
    show toriel normal at right with Dissolve(.25)
    frisk "I'm sure you'll love it. We're eating..."
    frisk "Mom, what're we having again?"
    toriel "We are having snail casserole."
    show frisk somehappy with Dissolve(.25)
    frisk "Oh, good..."
    toriel "Is there something wrong?"
    frisk "Of course not. Hey, snail-catching friend, why don't you try some?"
    "* You take a bite."
    "* ..."
    "* It tastes..."
    "* ...interesting."
    frisk "So, how is it?"
    toriel "Please, do tell."
     
    menu:
        "It's great, I love it!":           

            $world.get_monster('Toriel').update_FP(2)
            $world.get_monster('Frisk').update_FP(2,"right")
            #+1 Kindness
            show frisk surprised with Dissolve(.25)
            frisk "Really?"
            show frisk somehappy with Dissolve(.25)
            frisk "I mean, of course! I knew you would."
            toriel "Frisk, is there a problem with my cooking?"
            frisk "Never. Snails are great!"
            toriel "Oh, naturally. Either way, I am glad our guest seems to be enjoying them."

        "It's not bad.":                       
            show frisk normal with Dissolve(.25)
            frisk "See, I knew you would like it."
            toriel "Well, I try."

        "It's kinda... bad.":               
                                       
            $chose_frisk_meeting_option27=True
            $world.get_monster('Toriel').update_FP(-2,"right")
            $world.get_monster('Frisk').update_FP(-2)
            #-1 Kindness
            show frisk disappointed with Dissolve(.25)
            frisk "Shhh, don't say that."
            show toriel annoyed with Dissolve(.25)
            toriel "Ah, well I suppose snails are not everyone's cup of tea. Still, they are the only thing around here that will fill you up. So, if you decide to stay, you will just have to get used to them."     
    show frisk somehappy with Dissolve(.25)
    frisk "...So, um... how have you been liking the Ruins so far?"

    menu:
        "I think I like it better here than the surface!":
            show frisk surprised with Dissolve(.25)
            show toriel surprised with Dissolve(.25)
            frisk "D-do you really mean that?"
            if chose_frisk_meeting_option27==True:
                toriel "Even though you did not like the cooking?"
            menu:
                "Yeah!":                   
                    $world.get_monster('Toriel').update_FP(4,"right")
                    $world.get_monster('Frisk').update_FP(4)
                    #+1 Integrity
                    show frisk bigsmile with Dissolve(.25)
                    show toriel smile with Dissolve(.25)
                    frisk "That's great!"
                    toriel "Oh, well I'm glad you are enjoying your stay!"

                "Actually no, I just didn't want to be rude.":
                    $ get_toriel().update_FP(-2,"right")
                    $ get_frisk().update_FP(-3)
                    #-1 Integrity   
                    show toriel sad with Dissolve(.25)
                    show frisk sad with Dissolve(.25)
                    frisk "Oh... what?"
                    toriel "I guess I should not be too surprised."
                    show toriel smallsmile with Dissolve(.25)
                    toriel "Well... erm... thank you for your consideration."
                    show frisk somehappy with Dissolve(.25)
                    frisk "Oh come on. It isn't that bad, right?"      


        "I don't think I like this place.":           #//(+0)
            show toriel normal with Dissolve(.25)
            toriel "Oh, I know things may be difficult for you at first. This must be very different from what you were used to on the surface, after all. Still, I do encourage you to give it a chance."
            show frisk bigsmile with Dissolve(.25)
            frisk "Yeah! It's actually pretty great once you get used to everything!"
        "I hate this place.":           
            $ chose_frisk_meeting_option30=True
            $world.get_monster('Toriel').update_FP(-2,"right")
            $world.get_monster('Frisk').update_FP(-4)
            show frisk sad with Dissolve(.25)
            frisk "Aw, but... it's not that bad, really."
            show toriel awkward with Dissolve(.25)
            toriel "I understand that this place may not be to your liking." 
            show toriel smallsmile with Dissolve(.25)
            toriel "But I think that, with a bit of time, you will learn to tolerate it."
            show frisk smallsmile with Dissolve(.25)
            frisk "R-right! It's not so bad!"
        "It scares me...":                 
            $world.get_monster('Toriel').update_FP(2,"right")
            $world.get_monster('Frisk').update_FP(2)                                        
            show toriel sad with Dissolve(.25)
            toriel "Aww, poor thing. I had not realized until now that this must all seem very jarring."
            frisk "Oh, yeah."
            frisk "To be honest, when I first fell down here, I didn't take it very well."
            show frisk sad with Dissolve(.25)
            frisk "When people tried to help, I shoved them away and ran..."
            show frisk tearyeyes with Dissolve(.25)
            frisk "I even tried to run away from Mom. I thought she wanted to hurt me..."
            show toriel normal with Dissolve(.25)
            toriel "Frisk, please. Remember, I do not blame you for any of that. You were afraid, and I understand maybe I was being a bit... erm..."
            show toriel awkward with Dissolve(.25)
            toriel "...clingy, which you could have easily found threatening."
            show toriel smallsmile with Dissolve(.25)
            toriel "Besides, you are here now, and everything turned out alright."
            show frisk somehappy with Dissolve(.25)
            frisk "Yeah..."
            show frisk smallsmile with Dissolve(.25)
            frisk "So, the point is... I know this might be scary for now."
            frisk "But, if you give it a chance, I think you'll find this place is actually pretty great."
            show frisk bigsmile with Dissolve(.25)
            frisk "I mean it!"
            show toriel smile with Dissolve(.25)
            toriel "And we will be here to help you if you need anything."

    show frisk normal with Dissolve(.25)
    frisk "Well, whatever you think, you're always welcome here."
    show toriel smallsmile with Dissolve(.25)
    toriel "Of course. It would be impolite to kick a guest out, especially if they have nowhere else to go. However, I must ask that you contribute to gathering food--specifically, snails--everyday."
    if chose_frisk_meeting_option27==True or chose_frisk_meeting_option30==True:
        toriel "And as long as you work on your manners..."
     
    toriel "Now please, have some more food. It is good for you." 
    toriel "Even though some people... may not find it to their taste."
    show frisk somehappy with Dissolve(.25)
    frisk "W-what are you looking at me for? I love all of your cooking!"
    show toriel laughing with Dissolve(.25)
    toriel "Oh, it is alright, my child. I know snails are not your favorite dish."
    show frisk surprised with Dissolve(.25)
    frisk "..."
    frisk "How long have you known?"
    toriel "A mother can always tell what her child is really thinking, but I do appreciate the sentiment."
    show frisk somehappy with Dissolve(.25)
    frisk "Oh..."
    show frisk disappointed with Dissolve(.25)
    frisk "Actually, is it okay if I turn in early? I feel a little tired."
    show toriel sad with Dissolve(.25)
    toriel "But you have hardly eaten anything."
    toriel "..."
    show toriel normal with Dissolve(.25)
    toriel "Oh, alright. After all, it is important that you get your rest."
    show frisk smallsmile with Dissolve(.25)
    frisk "Thanks, Mom."
    hide frisk with Dissolve(.25)
    show toriel normal at center with Dissolve(.25)
    toriel "As for you, eat at least one more bite before you go."

    menu:
        "No problem. I'll even eat two bites!":       #//(+3)
            $world.get_monster('Toriel').update_FP(3)
            #+1 Perseverance
            show toriel smile with Dissolve(.25)
            toriel "That's the spirit."
            "* You take another bite."
            "* ..."
            "* And another."
            "* You feel a bit... weird?"

        "Fair enough.":                       #//(+0)
            show toriel normal with Dissolve(.25)
            toriel "Thank you."
            "* You take another bite"
            "* ..."
            #if the player chose option 27 earlier:
            if chose_frisk_meeting_option27:
                "* You bite off a bit too much. You gag, but you force it down."
                "* Uhg... "
                toriel "See, was that so hard?"
                "* Eh..."


        "But...":                           #//(+1)
            $world.get_monster('Toriel').update_FP(1)     
            #-1 Perseverance
            show toriel annoyed with Dissolve(.25)
            toriel "No buts. Eat, or you'll be hungry later."
            "* You take another bite."
            "* ..."
            "* Meh..."
             
            show toriel normal with Dissolve(.25)
            toriel "Thank you. You may be excused."
    
    toriel "Oh! Is that a CELL?"
    toriel "Can I see it for a second?"
    "* Toriel fumbles around with the buttons for a little longer than is comfortable."
    toriel "There!"
    play sound "audio/sfx/use_item.wav"
    "You got Toriel's Number!"
    $ player.variables['has_toriel_cell'] = True
    toriel "Do not hesitate to call me if you need me!"
    toriel "Have a good night!"

    #Add Talking to toriel to the living room
    $ get_room("Staircase").clear_events()
    $ set_lock_room("Living Room",False)
    $ set_lock_room("Basement Door",True)
    $ set_lock_room("Corridor",False)
    $ get_room("Living Room").set_event('frisk_meeting_toriel_after_dinner',False)
    #$ get_monster("Toriel").move_to_room("Living Room")
    $ get_room("Corridor").set_event('frisk_meeting_corridor_after_dinner',True)
    $ move_to_room('Staircase')
    return
 
################################
#  FRISK MEETING AFTER DINNER  #
################################

#going to change this to be the corridor
label frisk_meeting_corridor_after_dinner:
    if 'checked_your_door' not in player.variables:
        $ door_text = "Check Unmarked Door"
    else:
        $ door_text = "Check Your Door"
    call show_buttons
    "* You notice that there are three doors here."
    while True:
        menu:
            "Check Toriel's room" :
                "* Toriel's room strikes you as the type to be clean, orderly, and cozy."
                "* Going inside would be a huge invasion of privacy."
                "* You should know better."
                menu:
                    "Go inside anyway" if not chose_frisk_meeting_option72:
                        #-1 Justice
                        $ renpy.transition(fade)
                        $ renpy.show(world.get_room("Toriel's Room").bg)
                        "* There are a plethora of items to snoop through."
                        #see questions at top of doc
                        jump frisk_meeting_choice21
                        $ fm_checked_toriel_room = True
                    "Do not":
                        #+1 Justice
                        "* You are above that."


            "[door_text]":
                if 'checked_your_door' not in player.variables:
                    "* You hear Toriel calling from the kitchen."
                    toriel "I forgot to mention, there is a room you can use at the far end of the hall."
                    toriel "Goodnight, and sleep well!"
                    $ player.variables['checked_your_door'] = True
                menu:
                    "Go in?"
                    "Yes (End the Day)":
                        $ renpy.transition(fade)
                        $ renpy.show(world.get_room("Your Room").bg)
                        "* This is a very cozy room."
                        "* When did your eyes get so heavy?"
                        "* You plop down on the bed."
                        scene black with Dissolve(4)
                        stop music fadeout 4
                        "* ..."
                        "* .."
                        "* This is a weird place."
                        "* ..."
                        call day_transition
                        $ move_to_room('Your Room')
                    "No":
                        return
      

            "Check Frisk's Room":
                if chose_frisk_meeting_option39:
                    "* The light is off and the door is locked."
                else:
                    jump frisk_meeting_choice39
            "Do nothing":
                return
    return

label frisk_meeting_toriel_after_dinner:
    show toriel surprised with Dissolve(.25)
    toriel "Oh, hello again. Did you want to talk about something?"
    menu:
        "What can I do?":
            show toriel normal with Dissolve(.25)
            toriel "Oh, good question!"
            show toriel awkward with Dissolve(.25)
            toriel "Hmm... There is not really any work to be done for the rest of the day--at least, not that I can think of at the moment."
            show toriel smile with Dissolve(.25)
            toriel "It appears you are off the hook. Personally, I would use this chance to rest. After all, you must be very tired by now. I know I would be! The ruins are not usually this lively."
            toriel "I will see you again in the morning... sleep well!"
            #remove option 37 from selection 16
            $ chose_frisk_meeting_option37 = True

        "Nothing in particular.":
            #+1 Patience
            toriel "Hm, that is alright. Although..."
            show toriel awkward with Dissolve(.25)
            toriel "I cannot think of anything to talk about quite yet, either. I suppose sitting in silence can be nice, too--if you would like to do that."    
            show toriel normal with Dissolve(.25)
            "* You and Toriel sit in silence for a little while."
            "* It is nice."
            toriel "As much as I enjoy your company, I think it would be wise if you went to bed. We can always talk in the morning, if you wish."
            toriel "Sleep well!"
            #remove option 37 from selection 16
            $ chose_frisk_meeting_option37 = True
    $ move_to_room('Staircase')
    return

label frisk_meeting_choice21:

    menu:
        "Look in the diary" if chose_frisk_meeting_option65==False:
            $ chose_frisk_meeting_option65_count+=1
            if chose_frisk_meeting_option65_count ==1:
                "* There are several entries about humans, but most of the diary is filled with random, bad puns."

            elif chose_frisk_meeting_option65_count ==2:
                "* The man who invented knock-knock jokes must have won the No-Bell prize."

            elif chose_frisk_meeting_option65_count ==3:
                "* Toucan do jokes as good as mine only if you dove in. No need to swallow your pride to make one."
            else:
                $chose_frisk_meeting_option65 = True
                "* In the midst of bad puns, you find a rather serious entry. It seems personal..."
                menu:
                    "Read it":
                        "* Frisk has been acting strange recently."
                        "* Some days, they seem exhausted despite going to bed at a decent hour."
                        "* I am uncertain as to why this is, but I have my ideas."
                        "* I am not sure if I should confront them about it, though."
                        "* They might not be as energetic as they were when they first came here, but they seem happier now more than ever."
                        "* I must think on this."
                    "Do not":
                        "* You shouldn't peek..."

        "Examine the chair" if chose_frisk_meeting_option66==False:
            $ chose_frisk_meeting_option66 = True
            "* The chair seems really cozy. Anyone could spend hours writing while sitting in this beauty."
        "Examine the cactus" if chose_frisk_meeting_option67==False:
            $ chose_frisk_meeting_option67_count+=1
            if chose_frisk_meeting_option67_count ==1:
                "* Ah, truly stunning, a plant that can survive in such extreme heat."
                "* It looks like it's rooting for you."
            else:
                $chose_frisk_meeting_option67 = True
                "* Truly the most tsundere of plants."
        "Examine the shelf" if chose_frisk_meeting_option68==False:
            $chose_frisk_meeting_option68 = True
            "* There are several books about cooking, gardening, and bug hunting."
            "* There is even one called \"101 Snail Facts.\" It looks well-thumbed."
        "Look in the drawer" if chose_frisk_meeting_option69==False:
            $chose_frisk_meeting_option69 = True
            "* There are a lot of socks for someone who doesn't need them... s-scandalous."
        "Examine the bed" if chose_frisk_meeting_option70==False:
            $chose_frisk_meeting_option70 = True
            "* It's way more comfortable than it looks."
        "Examine the bucket" if chose_frisk_meeting_option71==False:
            $chose_frisk_meeting_option71 = True
            "* This bucket is filled entirely with a slimy mass of live snails."
            "* Looks delicious."
        "Leave Toriel's room" if chose_frisk_meeting_option72==False:
            $ chose_frisk_meeting_option72= True
            "* Finally, you're done snooping."
            "* Don't you feel even a little guilty about what you've done?"
            $ renpy.transition(fade)
            $ renpy.show(world.get_room("Corridor").bg)
            jump frisk_meeting_corridor_after_dinner
    jump frisk_meeting_choice21



label frisk_meeting_choice39:      
    "* There is a light shining under the door."
    "* You knock on the door."
    frisk "Come in!"
    "* You open the door and enter the room."
    $ renpy.transition(fade)
    $ renpy.show(world.get_room("Frisk's Room").bg)
    show frisk bigsmile with Dissolve(.25)
    frisk "Oh, hi again!"
    show frisk normal with Dissolve(.25)
    frisk "Something on your mind?"
     
label frisk_meeting_selection19:
    $ chose_frisk_meeting_option39=True
    menu:
        "How are you?" if chose_frisk_meeting_option40_5 == False:                       #//(+1)    
            $world.get_monster('Frisk').update_FP(1)
            $ chose_frisk_meeting_option40_5=True
            frisk "I'm doing fine, thank you." 
            jump frisk_meeting_selection19
            
        "I was just stopping by to say 'hey'. I'm heading off to bed. Goodnight!":                       #//(+1)
            $world.get_monster('Frisk').update_FP(1)
            show frisk smallsmile with Dissolve(.25)
            frisk "Oh, alright. That was nice of you!"
            frisk "Goodnight!"
            #remove option 39 from selection 16
            $ renpy.transition(fade)
            $ move_to_room('Corridor')
        "What's all that stuff you have on your shelves?":
            show frisk normal with Dissolve(.25)
            frisk "Oh, just a couple of things from the Underground."
            menu:
                "Just wondering. I think I'll be heading off to bed now.":
                    show frisk normal with Dissolve(.25)
                    frisk "Oh, okay. It was nice seeing you."
                    frisk "Goodnight!"
                    $ move_to_room('Corridor')

                "But how did you actually get all of this?":       
                    show frisk blushing with Dissolve(.25)
                    frisk "Oh, you know..." 
                    frisk "I just found it laying around..."
                    show frisk normal with Dissolve(.25)
                    frisk "Actually, I'm pretty tired. I think I'm gonna go to bed, sorry."
                    frisk "Goodnight!"
                    $ move_to_room('Corridor')
    return
     
    
  
    