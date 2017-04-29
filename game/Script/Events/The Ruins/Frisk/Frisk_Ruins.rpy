

label frisk_start:
    $ frisk_fp = 0
    #Frisk seems disturbed, absentmindedly fingering a toy knife
    #Frisk turns to see player
    #Frisk stands up
    #Frisk Sprite Change: surprised
    #Frisk Sprite Change: expression softens
    xxxfrisk "Oh! Um, hi. I wasn't expecting another human."
    xxxfrisk "How... how did you get here?"
    
    menu:
        "I could ask the same to you.":
            #frisk_fp stays the same
            #Frisk Sprite Change: contemplative
            xxxfrisk "Oh, well, you know... I guess I was hiking and I just... sort of..."
            #Frisk Sprite Change: Surprise
            xxxfrisk "Oh! I'm sorry, I forgot my manners."
            #Frisk Sprite Change: somewhat happy
            frisk "I'm Frisk. It's nice to meet you!"
            frisk "In case you're wondering, I'm actually a human too - not a shapeshifter or anything."
            menu:
                "Whoa, are shapeshifters real?":
                    $ frisk_fp += 3
                    #Frisk Sprite Change: neutral
                    frisk "Actually, I don't know. Maybe!"
                    #Frisk Sprite Change: friendly smile
                    frisk "Monsters are pretty cool, you never know what to expect!"
                    #Frisk Sprite Change: neutral
                    frisk "But um, yeah, I'm an actual human."
                    frisk "I live with Mom- I mean, you probably know her as Toriel. She takes really good care of me."
                    #Frisk Sprite Change: slightly happy
                    frisk "She’s taken care of me ever since I fell down here, actually."
                    jump selection3
                "And you live with a monster?":
                    #frisk_fp stays the same
                    frisk "Yeah. When I came to the Underground, she found me and took me in ever since."
                    jump selection3
        "I tripped.":
            $ frisk_fp +=3
            #Frisk Sprite Change: giggly
            xxxfrisk "Ha ha! You're funny.  No one just 'trips' and ends up down here."
            #Frisk Sprite Change: contemplative
            xxxfrisk "..."
            xxxfrisk "At least, no one that I know."
            #Frisk Sprite Change: somewhat happy
            frisk "Oh, where are my manners, my name is Frisk!"
            jump selection3w6
        "You're not Toriel's kid, are you?":
            $ frisk_fp -= 3
            #Frisk Sprite Change: sad
            xxxfrisk "No, I'm not..."
            xxxfrisk "Oh, right. You were probably expecting me to be a monster, too."
            #Frisk Sprite Change: somewhat happy
            frisk "My name is Frisk, I’m a human. Mom- well, you know her as Toriel..."
            frisk "She’s really nice, and I live with her."
            jump selection3
        "Hi, nice to meet you!":
            $ frisk_fp += 4
            #Frisk Sprite Change: surprise
            xxxfrisk "Oh! Right, where are my manners?"
            #Frisk Sprite Change: friendly smile
            frisk "It’s nice to meet you, too. I, uh… hope you get to like the underground."
            frisk "It's pretty great once you get used to it."
            jump selection3w6

#this includes a third dialogue option only available after having made certain decisions
label selection3w6:
    menu:
        "Say, I can't help but notice you're a human.":
            #frisk_fp stays the same
            frisk "Yeah, I am. Mom- I mean, I live with the caretaker of the Ruins."
            frisk "She’s really kind. Have you met her?"
            jump selection3
        "I've recently met Toriel. She seems nice.":
            jump choice7
        "How's life here in the ruins?":
            jump choice8
    
label selection3:
    menu:
        "I've recently met Toriel. She seems nice.":
            jump choice7
        "How's life here in the ruins?":
            jump choice8
    
    
label choice7:
    $ frisk_fp += 3
    #Frisk Sprite Change: somewhat happy
    frisk "Yeah! Out of all the people that could have found me, I’m glad it was her."
    menu:
        "Are you saying the other monsters are bad?":
            $ frisk_fp -=5
            #Frisk Sprite Change: surprised
            frisk "What? No!"
            #Frisk Sprite Change: slightly sad
            frisk "I mean, other monsters are great too. I shouldn't have said that; it was mean."
            frisk "But she’s the only one who can really take care of me, ya know?"
            jump selection5
            
        "I can relate; she helped me too.":
            $ frisk_fp +=2
            #Frisk Sprite Change: friendly smile
            frisk "That's great! She can handle anything!"
            #Frisk Sprite Change: slightly sad
            frisk "..."
            #Frisk Sprite Change: slightly happy
            frisk "Well, most things."
            jump selection5
    
    
label choice8:
    $ frisk_fp +=2
    #Frisk Sprite Change: slightly happy
    frisk "Well, we don’t have much, but it’s nice. It’s just that sometimes Mom makes food with snails in it and it’s..."
    #Frisk Sprite Change: slightly sad
    frisk "...not amazing... but don’t worry about it."
    #Frisk Sprite Change: slightly happy
    frisk "Other than that, things are pretty great."
    jump selection5
    
    
label selection5:
    menu:
        "Hey, are you feeling okay? You look a little under the weather.":
            $ frisk_fp += 3
            frisk "Oh, uhm. I’m… I’m fine."
            frisk "Tiring day, ya know?"
            frisk "But... I appreciate your concern."
            menu:
                "Are you sure you're okay? Do you want to talk about something?":
                    $ frisk_fp += 1
                    frisk "No, really it’s fine. I appreciate the help. I really do, but honestly, it’s nothing."
                    menu: 
                        "Oh come on, tell me!":
                            $ frisk_fp -= 2
                            #Frisk Sprite Change: slightly irritated
                            frisk "Please, you're making this more than it needs to be."
                            menu:
                                "You have to tell me!":
                                    $ frisk_fp -= 5
                                    #Frisk Sprite Change: more annoyed
                                    frisk "No, I don’t have to tell you anything! I’m not talking about this anymore!"
                                    #Frisk Sprite Change: neutral
                                    frisk "Sorry, I don’t like people getting on my back about things."
                                "Alright. I'm sorry.":
                                    #frisk_fp stays the same
                                    Frisk "..."
                                    Frisk "... Thank you."
                        "Just making sure.":
                            $ frisk_fp += 2
                            frisk "Thanks. You remind me a lot of Mom, actually."
                            #Frisk Sprite Change: friendly smile
                            frisk "But... don’t think you can actually outdo her in the mothering department!"
                "*Say nothing*":
                    #Skips to the next lines of dialogue
                    #frisk_fp stays the same, but I added the code below so that ren'py thinks this option does something
                    $ frisk_fp += 0
        "I'm sure everything must be great for you then!":
            #frisk_fp stays the same
            frisk "Yup... pretty much."
    
    #Frisk Sprite Change: neutral
    frisk "You know what...?"
    #Frisk Sprite Change: surprise
    frisk "Oh wait, I forgot!"
    #Frisk Sprite Change: somewhat happy
    frisk "Hey, I’m actually supposed to be doing something important."
    frisk "I need your help. It won’t take long, I promise."
    frisk "Just follow me!"
    #Background changes to snail catching background
    #Frisk Sprite Change: neutral
    frisk "Okay, here we are."
    frisk "I know this is going to sound a bit weird, but I need to catch snails."
    frisk "Mom makes food with them and she needs a lot!"
    menu:
        "You're right, that is weird.":
            $ frisk_fp -= 2
            frisk "Well, what can I say?"
            frisk "But seriously, this is important, I will need your help."
            frisk "Snails are actually hard to catch."
        "That sounds completely reasonable.":
            $ frisk_fp += 3
            frisk "Really, you think so?"
            menu:
                "Yeah, I do it all the time!":
                    $ frisk_fp += 5
                    #Frisk Sprite Change: friendly smile
                    frisk "That's great! This will be easy!"
                "I lied. That makes no sense whatsoever.":
                    $ frisk_fp -= 5
                    #Frisk Sprite Change: slightly sad
                    frisk "Oh... Okay."
                    frisk "Well- please, I really do need your help."
                    
    #Frisk Sprite Change: neutral
    frisk "Here’s what I want you to do."
    frisk "First, here, take this net."
    "You got the Butterfly Net."
    ##################################################INSERT ITEM GAINING CODE##################################################
    frisk "Okay, when the game starts, you will want to catch as many snails as you can before the timer runs out."
    frisk "Just click on the snail to catch it! It’s easy."
    frisk "Just be careful, more and more will appear as the game goes on."
    frisk "Also, some of the snails are surprisingly fast, so watch out."
    frisk "Ready? Here we go!"
    ##################################################INSERT UNDERSNAIL MINIGAME CODE##################################################
    $ frisk_fp += 5
    $ undersnail_score = 0
    if undersnail_score == 100:
        #Frisk Sprite Change: neutral with Chara alterations
        frisk "..."
        frisk "... Good."
        frisk "Very good."
        #Frisk Sprite Change: neutral (without Chara alteration)
        frisk "You're a natural!"
    elif frisk_fp > 20:
        #Frisk Sprite Change: friendly smile
        frisk "Wow, you did great! Thanks again for helping, Toriel will be so happy!"
    elif frisk_fp < 10:
        frisk "Um, good job. You... uhm, did pretty well."
    else:
        #frisk_fp is between 10 and 20
        frisk "That was good! Thanks for helping me out."
        
    frisk "Ya know, I’m actually feeling a bit better right now."
    frisk "I should mention, Mom really likes snails."
    frisk "If you give her some, maybe she’ll appreciate it. Maybe even pay you back somehow."
    frisk "Also, you may want to check with her, since she wants different types of snails on different days."
    #Frisk Sprite Change: surprise
    frisk "Oh!"
    #Frisk Sprite Change: friendly smile
    frisk "And if you want to do this again sometime, just tell me. This was fun!"
    frisk "Or you could do it on your own, whatever works! Help in any form is appreciated!"
    #Frisk Sprite Change: neutral
    frisk "I, uh, I should get going now, Mom is probably wondering why I’m out so late."
    frisk "I’m guessing you know where home is? Do you want to come with me?"
    menu:
        "Yeah, I'm in!":
            $ explored = False
            #frisk_fp stays the same
            #Frisk Sprite Change: friendly smile
            frisk "Alright, let’s go!"
            jump home
        "Actually, I'm going to look around the Ruins for a little while longer.":
            $ explored = True
            #frisk_fp stays the same
            frisk "Alright, that’s fine. I’ll see ya there!"
            #Frisk Sprite Change: friendly smile
            frisk "Just be sure not to stay out too late. If your stamina gets too low, you could get sick."
            frisk "I’m sounding like Mom right now... Oh well, see ya!"
            #frisk sprite leaves the screen
            #MC is free to roam the map
            ##################################################INSERT MAP CODE##################################################
            jump home
    
            
label home:
    if explored:
        #Frisk Sprite has not yet entered the screen
        frisk "Oh, I think they are here. I’ll be right back."
        #Frisk neutral sprite enters the screen
        frisk "Oh, hi. You’re a bit late, the food is a bit cold. I’m sure it’s fine."
        frisk "Hold on, let me tell Mom you're here."
    else:
        frisk "Here we are!"
        #Frisk Sprite Change: neutral
        frisk "Hold on. Let me tell Mom we’re back."
        
    #Frisk sprite leaves the screen
    "..."
    #Frisk neutral sprite enters the scene
    #Toriel neutral sprite enters the scene
    frisk "This is the person I told you about."
    toriel "Ah hello! It is very nice to see you come over for dinner."
    toriel "I do apologize for having to rush off so quickly before."
    toriel "Truthfully, I was a little worried about having to leave you on your own in the ruins."
    toriel "But, it is good to see that my fretting was nothing more than conjecture."
    if explored:
        toriel "Frisk has told me a lot about you while you were gone."
        if frisk_fp > 20:
            #$ toriel_fp += ???
            #Toriel Sprite Change: smile
            toriel "It makes me happy to see you and Frisk have made such fast friends."
            toriel "It gets a little lonely here in the ruins sometimes, and we do appreciate any well-meaning company."
            toriel "I am sure you know this by now, but I would like you to know that any friend of Frisk is welcome here."
        if frisk_fp < 15:
            #$ toriel_fp -= ???
            #Toriel Sprite Change: annoyed
            toriel "After all, it appears you made it here JUST FINE."
            #Frisk Sprite Change: curious
            frisk "Hey Mom, are you okay?"
            #Toriel Sprite Change: side glance
            toriel "Yes, of course."
        else:
            #frisk_fp is between 15 and 20
            #toriel_fp stays the same
            toriel "There’s not much to do here, but we are always looking for a helping hand, especially if you do not mind getting your hands dirty."
        
    #Frisk Sprite Change: friendly smile
    frisk "Alright, let’s eat!"
    #Toriel Sprite Change: neutral
    toriel "Yes, please join us at the table."
    #Background Change: dinner table
    frisk "I'm sure you'll love it! We're eating..."
    #Frisk Sprite Change: curious
    frisk "Mom, what are we having again?"
    toriel "We are having snail pie."
    #Frisk Sprite Change: slightly happy
    frisk "Oh good... I love snails."
    toriel "Is there something wrong?"
    frisk "Of course not. Hey, snail-catching friend, why don’t you try some?"
    "You take a bite."
    "..."
    "It tastes..."
    "...Interesting."
    frisk "So, how is it?"
    toriel "Please, do tell."
    menu:
        "It's great, I love it!":
            $ frisk_fp += 2
            #toriel_fp += 2
            $ dislike_snails = False
            $ like_snails = True
            $ love_snails = True
            #Frisk Sprite Change: Curious
            frisk "Really?"
            #Frisk Sprite Change: slightly happy
            frisk "I mean, of course! I knew you would."
            toriel "Frisk, is there a problem with my cooking?"
            frisk "Never. Snails are great!"
            toriel "Oh, naturally. Either way, I am glad our guest seems to be enjoying them."
        "It's not bad.":
            #frisk_fp and toriel_fp stay the same
            $ dislike_snails = False
            $ like_snails = True
            $ love_snails = False
            #Frisk Sprite Change: neutral
            frisk "See, I thought you would like it."
            toriel "Well, I try."
        "It's kinda... bad.":
            $ frisk_fp -= 2
            #toriel_fp -= 2
            $ dislike_snails = True
            $ like_snails = False
            $ love_snails = False
            #Frisk Sprite Change: annoyed
            #Toriel Sprite Change: disappointed
            frisk "Shh, don't say that."
            toriel "Ah, well I suppose snails are not everyone's cup of tea."
            toriel "Still, they are the only thing around here that will fill you up."
            toriel "If you decide to stay you will just have to get used to them..."
    
    
    #Frisk Sprite Change: slightly happy
    frisk "So, um... How have you been liking the Ruins so far?"
    menu:
        "I think I like it better than the surface!":
            $ hate_ruins = False
            #frisk_fp and toriel_fp stay the same
            #Frisk and Toriel Sprite Change: surprised
            if dislike_snails:
                toriel "Even though you did not like the cooking?"
            frisk "D-Do you really mean that?"
            menu:
                "Yeah!":
                    $ frisk_fp += 5
                    #toriel_fp += 5
                    #Frisk and Toriel Sprite Change: friendly smile
                    frisk "That's great!"
                    toriel "Oh, well, I am glad you are enjoying your stay!"
                "Actually, no. I just didn't want to be rude.":
                    $ frisk_fp -= 1
                    #toriel_fp -= 1
                    #Frisk and Toriel Sprite Change: disappointment
                    frisk "Oh... what?"
                    toriel "I guess I should not be too surprised."
                    #Toriel Sprite change: smile
                    toriel "Well... thank you for your consideration."
                    #Frisk Sprite Change: smile
                    frisk "Oh. come on. It isn't that bad, right?"
        "I don't think I like this place.":
            #frisk_fp and toriel_fp stay the same
            $ hate_ruins = False
            toriel "Oh, I know things may be difficult for you at first."
            toriel "This must be very different from what you were used to on the surface after all."
            toriel "Still, I do encourage you to give it a chance."
            #Frisk Sprite Change: smile
            frisk "Yeah! It’s actually pretty great once you get used to everything!"
        "I hate this place.":
            $ frisk_fp -= 5
            # toriel_fp -=5
            $ hate_ruins = True
            #Frisk Sprite Change: slightly sad
            #Toriel Sprite Change: slightly annoyed
            frisk "Aw, but… it’s not that bad, really."
            toriel "I understand that this place may not be to your liking."
            toriel "But I think that with a bit of time, you will learn to tolerate it."
            #Frisk and Toriel Sprite Change: smile
            frisk "R-Right! It's not so bad!"
        "It scares me...":
            $ frisk_fp += 3
            #toriel_fp += 3
            $ hate_ruins = False
            #Toriel Sprite Change: sympathetic smile
            toriel "Aww, poor thing. I had not realized until now that this must all seem very jarring."
            #Frisk Sprite Change: neutral
            frisk "Oh, yeah."
            #Frisk Sprite Change: slightly happy
            frisk "To be honest, when I first fell down here. I didn’t actually take it very well."
            #Frisk Sprite Change: slightly sad
            frisk "When monsters tried to help, I shoved them away and ran."
            frisk "I was being mean..."
            #Frisk Sprite Change: sad
            frisk "I even tried to trick Mom to get away. I thought she wanted to hurt me..."
            #Toriel Sprite Change: neutral
            toriel "Frisk, please - do remember I do not blame you for any of that."
            toriel "You were afraid, and I understand maybe I was being a bit... erm..."
            #Toriel Sprite Change: sheepish
            toriel "...clingy, which you could have easily found threatening."
            #Toriel Sprite Change: smile
            toriel "Besides, you are here now, and everything is okay."
            #Frisk Sprite Change: smile
            frisk "Yeah…"
            frisk "So friend, I know this may be scary for now, but if you give it a chance, I think you’ll find this place is actually pretty great."
            frisk "I mean it!"
            toriel "And we will be here to help you if you need anything."
    
    #Frisk Sprite Change: Neutral
    frisk "Well, whatever you think, you're always welcome here."
    toriel "Frisk."
    #Frisk Sprite Change: slightly happy
    frisk "Wait, um. Mom, is it okay if they stay here for a little bit?"
    toriel "Of course they can. It would be impolite to kick a guest out, especially if they have no-where else to go." 
    toriel "However, I must ask that you contribute to gathering food, specifically snails, everyday."
    if hate_ruins and dislike_snails:
        #Toriel Sprite Change: neutral
        toriel "As long as they work on their manners..."
        
    toriel "Now please, have some more food. It has many good nutrients."
    toriel "Even though some people... may not find it to their taste."
    if like_snails:
        #Frisk Sprite Change: slightly happy
        frisk "W-What are you looking at me for? I love all your cooking!"
        #Toriel Sprite Change: Giggle/Smirk/Smile
        frisk "Oh, it is alright my child, I know snails are not your favorite dish."
        #Frisk Sprite Change: contemplative
        frisk "..."
        frisk "How long have you known this?"
        #Toriel Sprite Change: wink
        toriel "A mother can always tell what her child is really thinking, but I do appreciate the sentiment."
        #Frisk Sprite Change: slightly happy
        frisk "Oh..."
        
    frisk "Actually, is it okay if I turn in early? I feel a bit tired."
    #Toriel Sprite Change: concerned
    toriel "But you have hardly eaten anything."
    toriel "..."
    #Toriel Sprite Change: neutral
    toriel "Oh, alright. After all, it is important that you get your rest."
    frisk "Thanks, Mom."
    #Frisk Sprite leaves the screen
    toriel "As for you, eat at least one more bite before you go."
    if love_snails:
        jump selection15good
    elif dislike_snails:
        jump selection15bad
    else:
        jump selection15all

label selection15good:
    menu:
        "No problem. I'll even eat two bites!":
            jump choice34
        "Fair enough.":
            jump choice35
    
label selection15bad:
    menu:
        "Fair enough.":
            jump choice35
        "But...":
            jump choice36

label selection15all:
    menu:
        "No problem. I'll even eat two bites!":
            jump choice34
        "Fair enough.":
            jump choice35
        "But...":
            jump choice36
            
label choice34:
    #Toriel Sprite Change: smile
    toriel "That's the spirit."
    "You take another bite."
    "..."
    "And another."
    "You feel a bit... weird?"
    jump home_hallway
    
label choice35:
    #Toriel Sprite Change: neutral
    "You take another bite."
    "..."
    if dislike_snails:
        "You bite off a bit too much and gag."
        "You force it down."
        "Ugh..."
    else:
        "Eh..."
    jump home_hallway
    
label choice36:
    #Toriel Sprite Change: stern
    toriel "No 'Buts'. Eat or you'll be hungry."
    "You take another bite."
    "Meh..."
    jump home_hallway
    
label home_hallway:
    $ toriel_room = False
    $ toriel_talk = False
    #Toriel Sprite Change: neutral
    toriel "Thank you. You may be excused."
    #Toriel Sprite leaves screen
    "You get up and leave."
    "What do you do now?"
    menu:
        "Go back and talk to Toriel a bit longer.":
            jump choice37a
        "Check Toriel's room.":
            jump choice37b
        "Go to bed.":
            jump choice38
        "Go talk to Frisk.":
            jump choice39
            
label choice37a:
    $ toriel_talk = True
    #Toriel Surprise Sprite Enters Screen
    toriel "Oh, hello again. Did you want to talk about anything?"
    menu:
        "What can I do?":
            toriel "Oh, good question!"
            #Toriel Sprite Change: thoughtful
            toriel "Hmm… There’s not really any work to be done for the rest of the day… At least from what I can remember at the moment."
            #Toriel Sprite Change: smile
            toriel "It appears you’re off the hook."
            toriel "Personally, I would use this chance to rest. After all, you must be very tired by now. I know I would be!"
            toriel "The ruins are not usually this lively."
        "Nothing in particular.":
            toriel "Hm, that’s alright. Although..."
            #Toriel Sprite Change: sheepish
            toriel "I can’t think of anything to talk about quite yet either."
            toriel "I suppose sitting in silence can be quite nice too - if you’d like to do that."
            "You and Toriel sit in silence for a little while."
            "It was quite nice."
            
    if toriel_room:
        menu:
            "Go to bed.":
                jump choice38
            "Go talk to Frisk.":
                jump choice39
    else:
        menu:
            "Check Toriel's room.":
                jump choice37b
            "Go to bed.":
                jump choice38
            "Go talk to Frisk.":
                jump choice39

label choice37b:
    $ toriel_room = True
    "Toriel’s room strikes you as the type to be clean, orderly, and cozy."
    "Going inside would be a huge invasion of privacy. You should know better."
    menu:
        "Go inside anyway.":
            #toriel_fp -= 10
            "There are a plethora of items to snoop through."
            $ snooping_looping = True
            while snooping_looping:
                menu:
                    "Diary":
                        "There are several entries about Humans, but most of the diary is filled with bad puns about anything that exists."
                        diary "The man who invented knock knock jokes must have won the No-Bell prize."
                        diary "Toucan do jokes as good as good as mine only if you dove in. No need to swallow your pride to make one."
                        "Oh! In the midst of bad puns, you find a rather serious entry. It seems personal..."
                        menu:
                            "Read it.":
                                diary "Frisk is late... They have never stayed out this long and I cannot begin to express my worry for them."
                                diary "I know they leave the ruins at night to explore, I honestly cannot blame them. The ruins are small and they are growing up." 
                                diary "Exploring makes them happy."
                                diary "I noticed after a few months passed when Frisk first arrived in the underground that they was growing less interested in everything the ruins had to offer."
                                diary "They were losing that excitement and joy they always seemed to carry."
                                diary "But then they started sneaking out at night, thinking that I would not put two and two together."
                                diary "I was going to confront them. To destroy the gate that was their only exit from the ruins."
                                diary "But it was during this time I also noticed my old Frisk returning to me. The bright and happy child they were before came back."
                                diary "Maybe they were even happier than before they began sneaking out. So, how could I destroy the only thing that is making my child happy?"
                                diary "They have been safe so far at least... But each time I worry."
                                diary "Frisk is so kind and innocent, surely there could be unfriendly monsters beyond the gate."
                                diary "I can only hope that the man I talk to beyond the door is doing a good job keeping my Frisk safe."
                                "..."
                            "Do not.":
                                "You feel bad for peeking."
                                "Every person is entitled to their privacy."
                        "Are you done snooping yet?"
                        menu:
                            "Yes.":
                                $ snooping_looping = False
                                "You sneak back out of Toriel’s room and feel guilty about what you’ve done."
                            "No.":
                                $snooping_looping = True
                                "You decide to continue invading her privacy."
                    "Chair":
                        "The chair’s soft pillow adapts to the one who sits on it."
                        "You have absolutely no idea how Toriel can fit in this."
                        "Are you done snooping yet?"
                        menu:
                            "Yes.":
                                $ snooping_looping = False
                                "You sneak back out of Toriel’s room and feel guilty about what you’ve done."
                            "No.":
                                $snooping_looping = True
                                "You decide to continue invading her privacy."
                    "Cactus":
                        "Ah, truly stunning, a plant that can survive in such extreme heat."
                        "This plant looks like it roots for you."
                        "Maybe you should cacti up with Toriel and Frisk."
                        "Are you done snooping yet?"
                        menu:
                            "Yes.":
                                $ snooping_looping = False
                                "You sneak back out of Toriel’s room and feel guilty about what you’ve done."
                            "No.":
                                $snooping_looping = True
                                "You decide to continue invading her privacy."
                    "Shelf":
                        "There are several books about cooking and gardening and a book about bug hunting."
                        "There is a special book called “101 Snail Facts.” It looks well-thumbed."
                        "They are neatly organized based on their color and type."
                        "Are you done snooping yet?"
                        menu:
                            "Yes.":
                                $ snooping_looping = False
                                "You sneak back out of Toriel’s room and feel guilty about what you’ve done."
                            "No.":
                                $snooping_looping = True
                                "You decide to continue invading her privacy."
                    "Drawer":
                        "You shouldn’t really peek through someone’s drawer."
                        "Are you really sure?"
                        menu:
                            "Yes.":
                                "There are a lot of socks for someone who doesn’t need them... s-scandalous."
                            "No.":
                                "You step away from the drawer."
                        "Are you done snooping yet?"
                        menu:
                            "Yes.":
                                $ snooping_looping = False
                                "You sneak back out of Toriel’s room and feel guilty about what you’ve done."
                            "No.":
                                $snooping_looping = True
                                "You decide to continue invading her privacy."
                    "Bed":
                        "It’s way more comfortable than it looks. The color of the aqua sheets reminds you of a stormy sea."
                        "Are you done snooping yet?"
                        menu:
                            "Yes.":
                                $ snooping_looping = False
                                "You sneak back out of Toriel’s room and feel guilty about what you’ve done."
                            "No.":
                                $snooping_looping = True
                                "You decide to continue invading her privacy."
                    "Bucket":
                        "This bucket is filled entirely with a slimy mass of live snails. Looks delicious."
                        "Are you done snooping yet?"
                        menu:
                            "Yes.":
                                $ snooping_looping = False
                                "You sneak back out of Toriel’s room and feel guilty about what you’ve done."
                            "No.":
                                $snooping_looping = True
                                "You decide to continue invading her privacy."
        "Do not.":
            "You are a better person than that."
            
    if toriel_talk:
        menu:
            "Go to bed.":
                jump choice38
            "Go talk to Frisk.":
                jump choice39
    else:
        menu:
            "Go back and talk to Toriel a bit longer.":
                jump choice37a
            "Go to bed.":
                jump choice38
            "Go talk to Frisk.":
                jump choice39

label choice38:
    "You hear Toriel calling from the kitchen."
    toriel "I forgot to mention, there is a room you can use at the far end of the hall. Goodnight, sleep well."
    #Screen goes black
    "You go to the room, plop down on the bed and go to sleep..."
    "..."

label choice39:
    "You check a few rooms and eventually find Frisk’s."
    #Background change: Frisk's room
    #Frisk Smile Sprite enters screen
    frisk "Oh, hi, you again!"
    #Frisk Sprite Change: neutral
    frisk "Something on your mind?"
    "You notice Frisk’s shelves are covered in various Items that don’t seem to belong to anything in the Ruins."

label selection19:
    menu: 
        "How are you?":
            jump choice40
        "Just stopping by to say 'hey.'":
            jump choice41
        "What is all that stuff you have on your shelves?":
            jump choice42

label choice40:
    $ frisk_fp += 1
    frisk "I'm doing fine, thank you."
    menu:
        "Just stopping by to say 'hey.'":
            jump choice41
        "What is all that stuff you have on your shelves?":
            jump choice42
    
label choice41:
    $ frisk_fp += 1
    #Frisk Sprite Change: Smile
    frisk "Oh, alright. That was nice of you!"
    #Frisk Sprite Change: Neutral
    frisk "There is a room at the far end of the hall. You can sleep there."
    frisk "Goodnight!"
    jump day1end
    
    
label choice42:
    #frisk_fp stays the same
    frisk "Oh, just a couple things from the Underground."
    menu:
        "Just wondering. Actually, I think I'll be heading off to bed.":
            #frisk_fp stays the same
            frisk "Oh, okay. It was nice seeing you."
            #Frisk Sprite Change: Neutral
            frisk "There is a room at the far end of the hall. You can sleep there."
            frisk "Goodnight!"
            jump day1end
        "But, how did you actually get all these?":
            #frisk_fp stays the same
            #Frisk Sprite Change: contemplative
            frisk "Hm..."
            frisk "Alright, but you have to promise not to tell Mom, okay?"
            #Frisk Sprite Change: neutral
            frisk "So, what do you say?"
            menu:
                "I don't make promises.":
                    $ frisk_fp -= 3
                    #Frisk Sprite Change: slightly annoyed
                    frisk "Well… fine. I guess I won’t tell you then."
                    menu:
                        "Well, then goodnight.":
                            $ frisk_fp -= 3
                            #Frisk Sprite Change: contemplative
                            frisk "..."
                            #Frisk Sprite Change: friendly smile
                            frisk "Alright then, guess you’ll never know."
                            #Frisk Sprite Change: Neutral
                            frisk "There is a room at the far end of the hall. You can sleep there."
                            frisk "Goodnight!"
                            jump day1end
                        "Alright, alright, I promise.":
                            #frisk_fp stays the same
                            #Frisk Sprite Change: contemplative
                            frisk "..."
                            #Frisk Sprite Change: neutral
                            frisk "Do you swear? Cross your heart and hope to die?"
                            menu:
                                "Nah, just kidding.":
                                    $ frisk_fp -= 5
                                    #Frisk Sprite Change: annoyed
                                    frisk "What, really?"
                                    frisk "You know what?"
                                    #Frisk Sprite Change: Neutral
                                    frisk "That's fine."
                                    frisk "There is a room at the far end of the hall. You can sleep there."
                                    frisk "Bye."
                                    jump day1end
                                "I swear.":
                                    #frisk_fp stays the same
                                    #Frisk Sprite Change: friendly smile
                                    frisk "Great!"
                                    jump frisk_drawer_secret
                                
                "I promise.":
                    $ frisk_fp += 1
                    #Frisk Sprite Change: friendly smile
                    frisk "Great! Thank you!"
                    jump frisk_drawer_secret

label frisk_drawer_secret:
    #Frisk Sprite Change: neutral
    frisk "Okay, so here it is..."
    frisk "When Mom is asleep sometimes I sneak out to other parts of the Underground."
    #Frisk Sprite Change: friendly smile
    frisk "I’ve met some really nice monsters!"
    #Frisk Sprite Change: slightly happy
    frisk "And some... not so nice..."
    frisk "But even they can be okay once you get to know them."
    frisk "A few of the monsters even gave me gifts!"
    frisk "That’s what most of the stuff is at least."
    #Frisk Sprite Change: friendly smile
    frisk "I want to tell you about all of them!"
    #Frisk Sprite Change: contemplative
    frisk "Let’s see, uhm, where to start..."
    #Frisk Sprite Change: neutral
    frisk "Hey, how about you decide."
    frisk "Just tell me what, and I’ll share the story behind it!"
    $ seen_bone = False
    $ seen_bottle = False
    $ looking_looping = True
    while looking_looping:
        if frisk_fp < 32:
            menu:
                "Actually, I think I should be going to bed":
                    #Frisk Sprite Change: slightly sad
                    frisk "Aw, what? But I wanted to..."
                    #Frisk Sprite Change: slightly happy
                    frisk "Nevermind, I understand. Get some rest, we can talk about stuff tomorrow."
                    frisk "There is a room at the far end of the hall. You can sleep there."
                    #Frisk Sprite Change: neutral
                    frisk "Goodnight."
                    jump day1end
                "Bone with Red Bowtie":
                    jump frisk_bone
                "An Empty Bottle of Ketchup":
                    jump frisk_bottle
                "A DVD":
                    jump frisk_dvd
                "A Wrapped Present":
                    jump frisk_present
                "An Empty Space on the Shelf":
                    jump frisk_space
                "A Jagged Piece of Metal":
                    jump frisk_metal
                "A Pocket-Sized Book":
                    jump frisk_book
                "Give Frisk an Item":
                    jump give_frisk_item
        else:
            #frisk_fp is 32 or higher
            menu:
                "Cool stuff! I need to be going to bed, but we can talk later.":
                    #Frisk Sprite Change: friendly smile
                    frisk "Alright, nice talking with you!"
                    frisk "There is a room at the far end of the hall. You can sleep there."
                    #Frisk Sprite Change: neutral
                    frisk "Goodnight."
                    jump day1end
                "Bone with Red Bowtie":
                    jump frisk_bone
                "An Empty Bottle of Ketchup":
                    jump frisk_bottle
                "A DVD":
                    jump frisk_dvd
                "A Wrapped Present":
                    jump frisk_present
                "An Empty Space on the Shelf":
                    jump frisk_space
                "A Jagged Piece of Metal":
                    jump frisk_metal
                "A Pocket-Sized Book":
                    jump frisk_book
                #"Give Frisk an Item":
                    #jump give_frisk_item
          
        label frisk_bone:
            $ seen_bone = True
            if seen_bottle:
                frisk "Oh, that was a gift from Sans's brother, Papyrus."
                #Frisk Sprite Change: slightly happy
                frisk "He's really nice, but a little bit..."
                frisk "Eccentric?"
                frisk "He tried to give me more of this same thing on many occasions."
                #Frisk Sprite Change: neutral
                frisk "I wouldn’t be surprised if he keeps drawers and drawers filled with the stuff."
            else:
                #Frisk Sprite Change: slightly happy
                frisk "Oh, right… that."
                frisk "I met this skeleton monster named Papyrus."
                frisk "He's really nice, but a little bit..."
                frisk "Eccentric?"
                frisk "He tried to give me more of the same thing on many occasions."
                #Frisk Sprite Change: neutral
                frisk "I wouldn’t be surprised if he keeps drawers and drawers filled with the stuff."
                #Frisk Sprite Change: slightly happy
                frisk "But I really appreciate the gesture. I hope you meet him someday too."
                frisk "I think you two would become great friends."
                
            jump continue_looking

        label frisk_bottle:
            $ seen_bottle = True
            if seen_bone:
                #Frisk Sprite Change: Surprise
                frisk "Oh, I forgot, Papyrus actually has a brother named Sans."
                #Frisk Sprite Change: neutral
                frisk "He’s pretty laid back."
                #Frisk Sprite Change: Slightly happy
                frisk "Really laid back..."
                frisk "We were talking at one point and then he drank the whole bottle in one gulp."
                frisk "Then he said {font=font/comic.ttf}{size=20}'here, you can have this...'{/size}{/font} and just handed it to me without another word."
                frisk "So I guess I should be thankful that he wanted to give me a gift...?"
            else:
                #Frisk Sprite Change: Slightly happy
                frisk "Uh."
                frisk "Well I’m not sure if that was really a 'gift.'"
                frisk "I met a skeleton monster outside the ruins named Sans."
                frisk "We were talking at one point and then he drank the whole bottle in one gulp."
                frisk "Then he said {font=font/comic.ttf}{size=20}'here, you can have this...'{/size}{/font} and just handed it to me without another word."
                frisk "So I guess I should be thankful that he wanted to give me a gift…?"
                
            jump continue_looking
    
        label frisk_dvd:
            #Frisk Sprite Change: Slightly happy
            frisk "Oh, I met the Royal Scientist of the monsters. Her name is Alphys!"
            frisk "That means she is really important for..."
            #Frisk Sprite Change: Contemplative
            frisk "...I don’t really know. Just... science stuff."
            frisk "I’m sure she knows what she is doing."
            frisk "Even though she seemed a bit nervous when we first met..."
            #Frisk Sprite Change: Slightly Happy
            frisk "...like, really nervous."
            frisk "Anyway, she gave me this."
            #Frisk Sprite Change: Contemplative
            frisk "She called it... am-in-ay?"
            frisk "Well the only problem is that we don’t exactly have a TV here so..."
            #Frisk Sprite Change: Neutral
            frisk "Still, it was nice of her."
            
            jump continue_looking
    
        label frisk_present:
            #Frisk Sprite Change: Friendly Smile
            frisk "Did you know monsters also have holidays where they give each other things?"
            #Frisk Sprite Change: Neutral
            frisk "However, I’m not allowed to open it until that day."
            frisk "Which is in..."
            #Frisk Sprite Change: Contemplative
            frisk "..."
            frisk "Seven months?"
            frisk "I wonder why that monster gave it to me so early."
            #Frisk Sprite Change: Neutral
            frisk "Oh well, I can’t complain. It’s the thought that counts."
            
            jump continue_looking
    
        label frisk_space:
            #Frisk Sprite Change: Slightly Happy
            frisk "So uh..."
            frisk "An invisible monster actually gave me that."
            frisk "...I don’t exactly know what it is."
            #Frisk Sprite Change: Neutral
            frisk "But at least they were nice about it."
            
            jump continue_looking
    
        label frisk_metal:
            #Frisk Sprite Change: Neutral
            frisk "Okay, so this is a bit of a complicated story."
            frisk "I've never actually met this person."
            frisk "Her name is 'Undyne', and she is the captain of the Royal Guard."
            frisk "That means she is the best a guarding..."
            #Frisk Sprite Change: Contemplative
            frisk "...royalty."
            #Frisk Sprite Change: Slightly happy
            frisk "Some of the monsters I have become friends with talked to her on my behalf."
            frisk "Because, from what I heard, for a time she wanted to..."
            #Frisk Sprite Change: Slightly sad
            frisk "To..."
            #Frisk Sprite Change: sad
            frisk "... kill me."
            frisk "But..."
            #Frisk Sprite Change: slightly happy
            frisk "My friends talked with her."
            frisk "And I hear she doesn’t want to hurt me anymore."
            #Frisk Sprite Change: slightly sad
            frisk "Still I’m a bit... hesitant to meet her."
            frisk "..."
            #Frisk Sprite Change: friendly smile
            frisk "You know what, if my friends say she is okay..."
            frisk "Then I bet she is a good person!"
            #Frisk Sprite Change: Neutral
            frisk "She even gave me a gift..."
            frisk "... that I have no idea what to do with."
            #Frisk Sprite Change: Contemplative
            frisk "I think it’s a piece of some kind of armor, but..."
            frisk "It’s a few hundred sizes too large for me."
            #Frisk Sprite Change: Neutral
            frisk "Still, I’ll thank Undyne when I get the chance."
            
            jump continue_looking
    
        label frisk_book:
            #Frisk Sprite Change: slightly happy
            frisk "This is actually something I brought with me from the surface."
            frisk "It’s my favorite story."
            frisk "...from a very small list."
            frisk "I wasn’t given much up there, so I had to cherish whatever I got."
            frisk "Maybe I’ll tell you more about what is like some time."
            frisk "Just not now..."
            frisk "..."
            frisk "I’m glad I have friends."
            #Frisk Sprite Change: neutral
            frisk "Is there anything else you want to talk about?"
            
            jump continue_looking

        
        label continue_looking:
            "Would you like to continue looking?"
            menu:
                "Yes.":
                    $ looking_looping = True
                "No.":
                    $ looking_looping = False
                    frisk "There is a room at the far end of the hall. You can sleep there."
                    #Frisk Sprite Change: neutral
                    frisk "Goodnight."
                    jump day1end
        

label day1end:
    #Frisk Sprite Leaves the Screen
    #background transitions to black
    "You find your way to the spare room."
    "You lay down on the bed... and go to sleep."
    "..."
    jump day2start
    
label day2start:
    "You wake up feeling refreshed."
    "HP restored."
    "You had your clothes on from yesterday, so you're ready to go."
    #Transition to Hallway Background
    "Smells like breakfast is being cooked."
    "It has a distinct non-snail odor."
    
    jump demo_end
    

    
