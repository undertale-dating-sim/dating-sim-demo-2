#Mealtimes in the Ruins

#temp manager for backgrounds because I can't find them in the managers
#Never mind, found it, but the temp black background needs declaring >_<
image background black_room = ("backgrounds/UI/blackScreen.png")

label ruins_first_breakfast:
    $frisk_first_breakfast_conv_count = 0
    $frisk_first_breakfast_conv_future = False  
    $frisk_first_breakfast_conv_fun = False  
    $frisk_first_breakfast_conv_surface = False  
    
    $ruins_want_to_leave = False
    
    #black screen, then knocking noise
    show bg black_room with dissolve
    frisk "Hey, wake up! Breakfast should be ready soon."
    #black screen fades out to reveal MC room-
    show bg toriel_house_your_room with dissolve
    #$world.move_to_room("Your Room")
    frisk "Hurry up! We don’t want the food to get cold!"
    #the player can check the room, but the normal room description just plays. The only thing they can do is exit to the hallway
    label examineYourRoomUponWakeup:
        menu:
            "Look around":
                "It's a nice room."
                jump examineYourRoomUponWakeup
            "Examine item [x]":
                "...placeholder text."
                jump examineYourRoomUponWakeup
            "Leave your room":
                pass
    show bg toriel_house_corridor with dissolve
    show frisk normal at left with Dissolve(.25)
    frisk "Oh good, you’re up. Let’s go eat!"
    
    
    #scene change living room
    #$world.move_to_room("Living Room")
    show bg toriel_house_livingroom with dissolve
    show frisk normal at left with Dissolve(.25)
    show toriel smallsmile at right with Dissolve(.25)
    frisk "Morning!"
    toriel "Good morning, my dear."
    toriel "I am glad you decided to join us for breakfast. It is the most important meal of the day, after all. I would hate for you to miss it. It is nearly as important as getting enough rest!"
    toriel "Speaking of which, how did you sleep?"
    menu:
        "Great!":
            $world.get_monster('Frisk').update_FP(2)
            $world.get_monster('Toriel').update_FP(2)
            toriel "I am glad."
        "I slept alright.":
            toriel "I understand... It can be strange sleeping somewhere new for the first time."
        "Could've been better.":
            toriel "I am sorry to hear that. Is there anything I can do to better accommodate you?"
            menu:
                "No, it’s nothing that you’re doing wrong. It’s just different here.":
                    toriel "I understand... it can be strange sleeping somewhere new for the first time."
                "Really? That’s very kind of you to ask.":
                    #toriel.DP +=3
                    show frisk bigsmile at left with Dissolve(.25)
                    frisk "Mom’s the best!"
                    show toriel blushing at right with Dissolve(.25)
                    toriel "Aw, you are both too sweet."

    show toriel smile at right with Dissolve(.25)
    toriel "But, still... I do hope you take my advice, dear. It is important to watch your stamina. It will decrease throughout the day when you complete certain tasks."
    show frisk normal at left with Dissolve(.25)
    frisk "Yeah, be careful. If you run out of stamina while outside, you could pass out and..."
    show frisk smallsmile at left with Dissolve(.25)
    frisk "Uh..."
    toriel "Yes. But that is easily prevented with food and rest."
    toriel "So, just be mindful while you are out and about, dear."
    frisk "Once you get used to an area, it becomes easier to manage your stamina. So I’m sure you won’t have that much trouble once you get to know the Ruins better!"
    menu:
        "Thanks for the advice.":
            $world.get_monster('Frisk').update_FP(3)
            show frisk bigsmile at left with Dissolve(.25)
            frisk "You’re welcome!"
        "Are you saying I don’t know what I’m doing?":
            $world.get_monster('Frisk').update_FP(-3)
            show frisk surprised at left with Dissolve(.25)
            frisk "What? Oh, of course not, I just thought..." 
            show frisk dissapointed at left with Dissolve(.25)
            frisk "I just wanted to help."
            frisk "But... um..."
    
    show frisk smallsmile at left with Dissolve(.25)
    frisk "I’m really happy you’re staying with us! It’s been so long since I’ve met anyone new, let alone another human!"
    show toriel normal at right with Dissolve(.25)
    toriel "Oh... My child, we do not know if it is their wish to stay with us permanently." 
    toriel "We have not asked what their plans were. We should try not to assume."
    show frisk disappointed at left with Dissolve(.25)
    frisk "Oh..."
    show frisk smallsmile at left with Dissolve(.25)
    frisk "Well, uh, what do you plan on doing?"
    menu:
        "I want to leave the Ruins as soon as possible":
            $world.get_monster('Frisk').update_FP(-3)
            $world.get_monster('Toriel').update_FP(-4)
            $ruins_want_to_leave = True
            show frisk sad at left with Dissolve(.25)
            show toriel normal at right with Dissolve(.25)
            frisk "Oh..."
            toriel "I thought you might say that."
            toriel "You are an adult, and if you would like to leave, I will not try to stop you."
            toriel "However, please know that the rest of the Underground may not be as friendly as we are in the Ruins. If you wish to leave, then it will be at your own risk."
            #if toriel.FP >= ???:
                #show toriel sad at right with Dissolve(.25)
                #toriel "I did hope that you might stay for a little while longer, but..."
            show toriel normal at right with Dissolve(.25)
            toriel "Should you choose to leave, the gateway to the rest of the Underground can be found in the basement."
            toriel "Please be careful, and come back to visit when you can. You are welcome here whenever you need a safe place to rest."
        "I want to stay here with you guys.":
            $world.get_monster ('Frisk').update_FP(3)
            $world.get_monster ('Toriel').update_FP(3)
            show frisk bigsmile at left with Dissolve(.25)
            show toriel smile at right with Dissolve(.25)
            toriel "Oh! That is wonderful, dear. Of course, we would love for you to stay here with us."
            toriel "I only ask that you help gather snails every day for your meal here. I am not sure if Frisk could find enough for all of us."
            menu:
                "I'd love to help.":
                    $world.get_monster ('Toriel').update_FP(4)
                    show toriel smile at right with Dissolve(.25)
                    toriel "I am glad. Frisk could really use the help."
                "Seems like a chore...":
                    $world.get_monster ('Toriel').update_FP(-4)
                    show frisk smallsmile at left with Dissolve(.25)
                    show toriel awkward at right with Dissolve(.25)
                    toriel "I suppose it may seem like that at first..."
                    frisk "But you can just treat it like a game. That’s what I do!"
            show toriel normal at right with Dissolve(.25)
            toriel "But I must also warn you... should you ever change your mind and decide to leave, the rest of the Underground may not be as friendly as we are in the Ruins. It could be dangerous out there."
            show toriel smile at right with Dissolve(.25)
            toriel "But, if you plan on staying, then you needn’t worry about that."
        "I don't know, honestly.":
            toriel "That is quite alright. Of course, you may leave if you wish, but I would advise against it."
            toriel "The rest of the Underground may not be as friendly as we are in the Ruins. It could be dangerous to leave."
            toriel "However, if you decide to explore, the gateway to the Underground can be found in the basement."
            frisk "But... if you do leave... make sure you come back to visit!"
            show toriel smile at right with Dissolve(.25)
            toriel "Yes, you are always welcome here."
    
    show frisk smallsmile at left with Dissolve(.25)
    frisk "So... what do you want to do now?"
    menu:
        "I’m done with breakfast, so I think I’ll go for a walk.":
            $world.get_monster ('Frisk').update_FP(-1)
            show frisk normal at left with Dissolve(.25)
            show toriel normal at right with Dissolve(.25)
            frisk "Oh, wait, you're going already?"
            frisk "Well, have fun."
            frisk "I guess we can talk later."
            toriel "Be careful... Remember to eat and drink enough, rest when you are tired, and-"
            frisk "Mom, I think they know how to take care of themselves."
            show toriel smallsmile with Dissolve(.25)
            toriel "I suppose so. I just like to make sure."
            toriel "Oh! And dinner is served every day at six if you would like to join us, dear. Otherwise, I will leave the leftovers in the fridge for you."
            toriel "Enjoy your walk."
            #player is free to explore the Ruins or go down to the basement door and exit the Ruins
        "Let's talk for a little while longer.":
            $world.get_monster ('Frisk').update_FP(3)
            toriel "You two have fun. I am going to get a head start on the dishes."
            hide toriel with Dissolve(.25)
            show frisk smallsmile at center with Dissolve(.25)
            frisk "Okay, so what should we talk about?"
            while True:
                menu:
                    "What are your plans for the future?" if frisk_first_breakfast_conv_future == False:
                        $world.get_monster ('Frisk').update_FP(1)
                        $frisk_first_breakfast_conv_future = True
                        $frisk_first_breakfast_conv_count +=1
                        show frisk distant with Dissolve(.25)
                        frisk "Hm..."
                        frisk "I haven’t really thought about it."
                        show frisk normal with Dissolve(.25)
                        frisk "I guess I’d like to explore more of the Underground..." 
                        show frisk surprised with Dissolve(.25)
                        frisk "Er, I mean..."
                        show frisk normal with Dissolve(.25)
                        frisk "When I’m older."
                        frisk "But other than that... I’m not really sure."
                        frisk "I mean, I guess snail gathering isn’t that bad for now."
                    "What do you do for fun?" if frisk_first_breakfast_conv_fun == False:
                        $world.get_monster ('Frisk').update_FP(2)
                        $frisk_first_breakfast_conv_fun = True
                        $frisk_first_breakfast_conv_count +=1
                        frisk "Well, I like to draw and read."
                        show frisk smallsmile with Dissolve(.25)
                        frisk "Just walking around the Ruins is fun, too. I like hanging out with all the Froggits and Whimsuns!"
                    "What was life like on the surface?" if frisk_first_breakfast_conv_surface == False:
                        $world.get_monster ('Frisk').updatee_FP(1)
                        $frisk_first_breakfast_conv_surface = True
                        $frisk_first_breakfast_conv_count +=1
                        show frisk upset with Dissolve(.25)
                        frisk "I... would rather not talk about that."
                        show frisk smallsmile with Dissolve(.25)
                        frisk "Sorry."
                    "May I be excused? I'm leaving now.":
                        if frisk_first_breakfast_conv_count == 0:
                            show frisk smallsmile with Dissolve(.25)
                            frisk "Okay... We didn’t really talk about anything, though."
                        elif frisk_first_breakfast_conv_count == 1:
                            show frisk sad with Dissolve(.25)
                            frisk "Aw, already?"
                        else:
                            show frisk normal with Dissolve(.25)
                            frisk "Alright!"
                        return
                    
    show frisk normal with Dissolve(.25)
    frisk "I’ll see you later, then."
    frisk "Have fun!"
    $world.move_to_room("Corridor")
    #"Breakfast is over, you're free to explore the Ruins or leave through the basement"
return



#if World.currentTime >= 1080 and World.currentTime <=1140:
    #call ruins_dinner
#elif World.currentTime >1140: 
    #call ruins_dinner_leftovers
label ruins_dinner:
    #There are three sets of days... with Friday missing in the script, so I determined it's most likely placement
    
    if World.days == "Monday" or World.days == "Thursday" or World.days == "Friday":
        $ruins_dinner_frisk_stays = True
        show toriel smile at right with Dissolve(.25)
        show frisk smallsmile at left with Dissolve(.25)
        "*You find Toriel and Frisk already at the table."
        "*They must’ve been waiting for you."
        toriel "Welcome home."
        frisk "Hey!"
        toriel "You are just in time. Take a seat and eat up."
        menu:
            "How was your day, Toriel?":
                jump ruins_dinner_talk_toriel
            "What did you do today, Frisk?":
                jump ruins_dinner_talk_frisk
            "Excuse me.":
                show toriel normal at right with Dissolve(.25)
                toriel "Not hungry?"
                toriel "Alright... have a good night."
                frisk "See you later!"
                $world.move_to_room("Corridor")
            "Well, I’m done. Thanks for dinner.":
                frisk "Wow, you ate quick!" 
                toriel "Have a good night, dear."
                $world.move_to_room("Corridor")
        return
        
    elif World.days == "Tuesday" or World.days == "Saturday":
        $ruins_dinner_frisk_stays = False
        show toriel smile at right with Dissolve(.25)
        show frisk normal at left with Dissolve(.25)
        "*You find Toriel and Frisk already at the table."
        "*They must have been waiting for you."
        toriel "Welcome home."
        frisk "Now, mom?"
        show toriel laughing at right with Dissolve(.25)
        toriel "Go ahead, Frisk."
        "*Frisk digs in ravenously."
        "*They sure have an appetite."
        "*It only takes them a few minutes to-"
        show frisk bigsmile at left with Dissolve(.25)
        frisk "Done!"
        show toriel awkward at right with Dissolve(.25)
        toriel "Already?"
        frisk "Yeah."
        show frisk smallsmile at left with Dissolve(.25)
        frisk "I’m beat, so I’m going to go to bed early, okay?"
        frisk "See you in the morning."
        toriel "Oh, alright. Goodnight, my child."
        hide frisk
        show toriel smallsmile with Dissolve(.25)
        toriel "Well, we can still chat, at least."
        menu:
            "How was your day, Toriel?":
                jump ruins_dinner_talk_toriel
            "Excuse me.":
                toriel "You are excused, dear."
                toriel "Rest well."
                $world.move_to_room("Corridor")
            "Well, I'm done. Thanks for dinner.":
                show toriel smile with Dissolve(.25)
                toriel "Oh, I am glad you liked it."
                toriel "Please let me know if you need anything else."
                toriel "Goodnight, dear."
                $world.move_to_room("Corridor")
        return
    else:
        $ruins_dinner_frisk_stays = False
        show toriel normal at right with Dissolve(.25)
        show frisk disappointed at left with Dissolve(.25)
        "*You find Toriel and Frisk already at the table."
        "*They must have been waiting for you."
        toriel "Welcome home."
        frisk "Hey."
        toriel "You are just in time. Take a seat and eat up."
        menu:
            "How was your day, Toriel?":
                toriel "It was fine, thank you for asking..."
                show toriel awkward at right with Dissolve(.25)
                toriel "Frisk, are you alright? You look ill..."
                show frisk smallsmile at left with Dissolve(.25)
                frisk "No, I’m good!"
                show frisk disappointed at left with Dissolve(.25)
                #yawning sound
                frisk "It’s been a long day... I think I’ll go to bed."
                show toriel awkward at right with Dissolve(.25)
                toriel "Are you sure? You have barely touched your dinner..."
                frisk "I’m fine, mom. Just need to catch some z’s, you know?"
                toriel "Well, alright. Rest well, both of you."
            "What did you do today, Frisk?":
                frisk "..."
                frisk "...Hmm?"
                frisk "Oh, sorry... I’m just kind of tired."
                show toriel awkward at right with Dissolve(.25)
                toriel "Are you okay, Frisk? You are not feeling ill, are you?"
                show frisk smallsmile at left with Dissolve(.25)
                frisk "No, I’m good!"
                show frisk disappointed at left with Dissolve(.25)
                #yawning sound
                frisk "It’s been a long day... I think I’ll go to bed."
                show toriel awkward at right with Dissolve(.25)
                toriel "Are you sure? You have barely touched your dinner..."
                frisk "I’m fine, mom. Just need to catch some z’s, you know?"
                toriel "Well, alright. Rest well, both of you."
            "Excuse me.":
                toriel "You are excused, dear."
                show frisk disappointed at left with Dissolve(.25)
                #yawning sound
                frisk "It’s been a long day... I think I’ll go to bed, too."
                show toriel awkward at right with Dissolve(.25)
                toriel "Are you sure? You two have barely touched your dinner..."
                frisk "I’m fine, mom. Just need to catch some z’s, you know?"
                toriel "Well, alright. Rest well, both of you."
            "Well, I'm done. Thanks for dinner.":
                show toriel smile at right with Dissolve(.25)
                toriel "Oh, I am glad you liked it."
                show frisk disappointed at left with Dissolve(.25)
                #yawning sound
                frisk "It’s been a long day... I think I’ll go to bed."
                show toriel awkward at right with Dissolve(.25)
                toriel "Are you sure? You have barely touched your dinner..."
                frisk "I’m fine, mom. Just need to catch some z’s, you know?"
                toriel "Well, alright. Rest well, both of you."                
        $world.move_to_room("Corridor")
        return
    return
    
label ruins_dinner_talk_toriel:
    $temp_random_num = renpy.random.randint(1, 5)

    if temp_random_num == 1:
        if ruins_dinner_frisk_stays == True:
            show toriel smile at right with Dissolve(.25)
        else:
            show toriel smile at center with Dissolve(.25)
        toriel "Oh, it was just fine. Thank you for asking."
        toriel "I took a nice walk through the Ruins..."
        toriel "I passed by the place where both you and Frisk fell, but, as usual, there was not a soul in sight."
        toriel "The flowers were blooming quite beautifully, however."
        toriel "...You look like you are done eating, dear. Feel free to head off to bed whenever you are ready!"
        toriel "There is no need to stick around and listen to an old lady yammer on about her day." 
        toriel "Have a good night."

    elif temp_random_num == 2:
        if ruins_dinner_frisk_stays == True:
            show toriel smile at right
        else:
            show toriel smile at center
        toriel "It was rather uneventful, but thank you for asking."
        toriel "I baked a batch of cookies for us all to enjoy, but I suspect Frisk may have scarfed them down already."
        if ruins_dinner_frisk_stays == True:
            show frisk annoyed at left with Dissolve(.25)
            frisk "Hey! I didn’t know they were for everyone!"
            show toriel laughing at right with Dissolve(.25)
            toriel "It is alright, my child."
        if ruins_dinner_frisk_stays == True:
            show toriel smile at right with Dissolve(.25)
        else:
            show toriel smile with Dissolve(.25)
        toriel "Sweets tend to disappear remarkably fast in this house!"
        toriel "But, regardless... You look like you are done eating, dear. Since I have no dessert to offer you, perhaps you should head off to bed."
        toriel "Have a good night."

    elif temp_random_num == 3:
        if ruins_dinner_frisk_stays == True:
            show toriel smile at right with Dissolve(.25)
        else:
            show toriel smile at center with Dissolve(.25)
        toriel "My day was nice. Thank you for asking."
        toriel "I took a walk through the Ruins and saw a group of Froggit children playing in the leaves."
        if ruins_dinner_frisk_stays == True:
            toriel "I remember when Frisk used to play in the leaves like that... What ever happened to those days, my child?"
            show frisk blush at left with Dissolve(.25)
            frisk "Mom... I’m not a little kid anymore."
            show toriel laughing at right with Dissolve(.25)
            toriel "Of course not."
        else:
            toriel "I remember when Frisk used to play in the leaves like that... A part of me longs for those days again."
            show toriel awkward with Dissolve(.25)
            toriel "They seem to grow more and more distant from me as they get older. I often look back on the times when they would run around the Ruins, playing pretend."
            toriel "It made me feel younger, myself."
        if ruins_dinner_frisk_stays == True:
            show toriel normal at right with Dissolve(.25)
        else:
            show toriel normal with Dissolve(.25)
        toriel "Pay me no mind... I am just a silly old woman wishing that time would not pass so quickly."
        toriel "...You look like you are done eating, dear. Feel free to head off to bed whenever you are ready!"
        toriel "There is no need to stick around and listen to an old lady yammer on about her day." 
        toriel "Have a good night."

    elif temp_random_num == 4:
        if ruins_dinner_frisk_stays == True:
            show toriel smallsmile at right with Dissolve(.25)
        else:
            show toriel smallsmile at center with Dissolve(.25)
        toriel "It was alright, thank you." 
        toriel "On my walk, I found a Whimsun crying about something or another..."
        if ruins_dinner_frisk_stays == True:
            show toriel awkward at right with Dissolve(.25)
        else:
            show toriel awkward
        toriel "I tried to console the poor thing, but I am afraid I only made matters worse."
        toriel "I do not know why I try..."
        if ruins_dinner_frisk_stays == True:
            show toriel smallsmile at right with Dissolve(.25)
        else:
            show toriel smallsmile with Dissolve(.25)
        toriel "But I suppose it is better to make an attempt than to not do anything at all."
        toriel "Regardless... You look like you are done eating, dear. Since I have no dessert to offer you, perhaps you should head off to bed."
        toriel "Have a good night."
        
    else:
        if ruins_dinner_frisk_stays == True:
            show toriel smile at right with Dissolve(.25)
        else:
             show toriel smile at center with Dissolve(.25)
        toriel "It was good. Thank you for asking."
        toriel "I purchased a fresh bucket of snails from the ghost, Napstablook, today."
        if ruins_dinner_frisk_stays == True:
            show frisk normal at left with Dissolve(.25)
            frisk "You saw Blooky? How’re they doing?"
            toriel "As well as can be. It seems their business has slowed down as of late. Poor thing is running the entire farm by themselves, now."
        toriel "Their snails are the best in the Underground, and we are lucky that they are willing to travel to the Ruins to sell them to us."
        toriel "But, regardless... You look like you are done eating, dear. Since I have no dessert to offer you, perhaps you should head off to bed."
        toriel "Have a good night."

    $temp_random_num = 0
    $world.move_to_room("Corridor")
    return
    
label ruins_dinner_talk_frisk:
    $temp_random_num = renpy.random.randint(1, 3)
    if temp_random_num == 1:
        show frisk smallsmile at left with Dissolve(.25)
        frisk "Oh, not much."
        frisk "I was drawing all day... kind of lost track of time."
        show toriel smile at right with Dissolve(.25)
        toriel "I have noticed! I had to call your name five times before you answered me. Sometimes, it is like you are in a whole other world."
        frisk "Yeah. It feels that way to me, too."
        frisk "Oh, hey, are you done eating? So am I... I think I’m gonna head off to bed."
        toriel "Goodnight, both of you."
    elif temp_random_num == 2:
        show frisk bigsmile at left with Dissolve(.25)
        frisk "I ran into Napstablook today! They spend a lot of time at their snail farm, so I don’t get to see them much..."
        #!!!#if the player has gone on a date with Blooky (HB or TL), play the following:
        #if napstablook_tl_date == True or napstablook_hpdate == True???
        show frisk normal at left with Dissolve(.25)
        frisk "They asked about you... I didn’t know you guys were so close."
        "*Frisk waggles their eyebrows suggestively."
        show frisk smallsmile at left with Dissolve(.25)
        frisk "Anyway, Blooky showed me the latest song they’re working on. It was a lot of fun!"
        frisk "Oh, hey, are you done eating? So am I... I think I’m gonna head off to bed."
        toriel "Goodnight, both of you."
    else:
        show frisk smallsmile at left with Dissolve(.25)
        frisk "I used my allowance to buy something from the spider bakery. They make great donuts!"
        show toriel smallsmile at right with Dissolve(.25)
        toriel "Better than my desserts?"
        show frisk surprised at left with Dissolve(.25)
        frisk "Er, no! I didn’t mean-"
        show toriel laughing at right with Dissolve(.25)
        toriel "Relax, my child. I am only teasing you."
        show frisk smallsmile at left with Dissolve(.25)
        frisk "Heh... I knew that."
        frisk "Oh, hey, are you done eating? So am I... I think I’m gonna head off to bed."
        show toriel smile at right with Dissolve(.25)
        toriel "Goodnight, both of you."
    $temp_random_num = 0
    $world.move_to_room("Corridor")
    return
    
label ruins_dinner_leftovers:
    "*You find some leftovers in the fridge, just as Toriel had promised."
    menu:
        "(Eat them)":
            "*It would have been better fresh..."
            "*But it still fills you up."
        "(Leave them)":
            "*You can always eat them later..."
    return

label ruins_breakfast:
    $World.currentTime = 480
    #Waking up scene???
    
    #black screen, knocking sound
    show bg black_room with dissolve
    frisk "Come on, sleepy head! Breakfast is almost ready!"
    #scene change MC room
    show bg toriel_house_your_room with dissolve
    #if they go to the living room, continue to breakfast
    #else, if they try to leave the house...
    call examineYourRoomUponWakeup
    show bg toriel_house_corridor with dissolve
    show frisk normal with Dissolve(.25)
    frisk "Hey, are you leaving? Aren’t you going to eat first?"
    menu:
        "No, I’m skipping breakfast.":
            frisk "Oh, alright! Have a good day..."
            #scene change black tree room
            show bg ruins_outside_house with dissolve
            jump breakfast_time_flowey
        "Yeah, I’ll eat.":
            show frisk smallsmile with Dissolve(.25)
            frisk "Well, what’re you doing over here, then? Food’s in the living room, silly!"
            #scene change living room
            show bg toriel_house_livingroom with dissolve
    show toriel normal at right with Dissolve(.25)
    show frisk normal at left with Dissolve(.25)
    "*You share a delicious breakfast with Frisk and Toriel."
    if World.days == "Friday" or World.days == "Sunday":
        "*Frisk looks exhausted."
    toriel "So, what are your plans for the day?"
    menu:
        "I’m going to catch some snails.":
            show toriel smile with Dissolve(.25)
            toriel "That sounds like a good plan. I wish you luck!"
            frisk "Save some for me to catch!"
        "I’m going to see if I can find Napstablook.":
            #NYI Fix this!!!
            #if the MC is not friends with Blooky and is not dating them:
            toriel "Oh? Do you have business with them?"
            #if the MC has more than 7 FP with Blooky, but has not gone on a date with them:
            show toriel smile with Dissolve(.25)
            toriel "I am glad you have been able to make friends down here... It can get rather lonely otherwise."
            #if the MC has gone on a date with Blooky:
            show toriel smile with Dissolve(.25)
            show frisk smallsmile with Dissolve(.25)
            toriel "That is good... I am sure they will appreciate the company."
            "*Frisk winks at you when Toriel isn’t looking."
            toriel "Have a good day, dear."
        "I’m going to explore the Ruins.":
            show toriel smile with Dissolve(.25)
            toriel "That sounds exciting... Have a good time, and stay safe."
            frisk "I’d go with you, but I think I’ve seen everything there is to see in the Ruins. You have fun, though!"
        "I’m leaving the Ruins today.":
            $ruins_want_to_leave = True
            #if the player has never left the Ruins before:
            if True:
                show toriel awkward with Dissolve(.25)
                show frisk distant with Dissolve(.25)
                toriel "Oh, I see..."
                toriel "Well, I will not try to stop you, but please stay safe."
                #if the player has 5 or more FP with Frisk:
                if True:
                    show frisk normal with Dissolve(.25)
                    frisk "And come back to visit soon!"
                    toriel "Yes, don’t be a stranger."
                #if the player has less than 5 FP with Frisk:
                else:
                    frisk "..."
                toriel "The gateway to the rest of the Underground is in the basement, if you really want to leave."
                toriel "I wish you all the best."
            #if the player has left the ruins before
            else:
                toriel "Ah, I see."
                toriel "Please take care of yourself, and come back whenever you would like."
                frisk "See you later!"             
        "I’ll probably hang out around the house.":
            show toriel smallsmile with Dissolve(.25)
            toriel "That will be relaxing, I am sure."
            toriel "Have a good day, dear."
        "I don’t know yet.":
            frisk "If you’re bored, how about you go hunt for some snails? It saves me from having to catch as many!"
            show toriel smallsmile with Dissolve(.25)
            toriel "Frisk, are you trying to making our guest do your chores for you?"
            #show frisk blush <- no blush image or equivalent
            show frisk bigsmile  with Dissolve(.25)
            frisk "Haha, what? ‘Course not!"
            show toriel laughing with Dissolve(.25)
            toriel "Well, whatever you decide to do, I hope you have a good day."
    $world.move_to_room("Corridor")
    return
    
label breakfast_time_flowey:
    if world.get_monster ('Flowey').FP < 0:
        show Flowey surprised with Dissolve(.25)
        flowey "...!"
        show Flowey angry with Dissolve(.25)
        flowey "What’re you looking at?"
        hide Flowey sprite
    elif world.get_monster ('Flowey').FP <= 5:
        show Flowey annoyed with Dissolve(.25)
        flowey "...What?"
        hide Flowey sprite with Dissolve(.25)
    elif world.get_monster ('Flowey').FP <=10:
        show Flowey surprised with Dissolve(.25)
        flowey "I..."
        show Flowey annoyed with Dissolve(.25)
        flowey "I wasn’t doing anything!"
        hide Flowey sprite
    else:
        show Flowey backside with Dissolve(.25)
        flowey "..."
        hide Flowey sprite
    
    return
    
label ruins_basement_door_first_visit:
    frisk "Hey."
    show frisk distant with Dissolve(.25)
    if ruins_want_to_leave == True:
        frisk "So, you’re really leaving, huh?"
    else:
        frisk "Behind that door lies the end of the Ruins..."
        frisk "But I think you already knew that, didn’t you?"
    frisk "..."
    if world.get_monster ('Toriel').FP > 3:
        frisk "You know, Mom says she’s fine with you leaving... but I can tell she’s really not."
        frisk "She still thinks it’s dangerous out there, in the rest of the Underground..."
    else:
        frisk "You know, I think Mom’ll be glad you’re leaving."
        frisk "Sometimes, I kind of wish she felt the same way about me..."

    show frisk upset with Dissolve(.25)
    frisk "It’s not fair. She won’t let me go outside of the Ruins. She says it’s too risky, but she won’t tell me what she’s afraid of."
    frisk "..."
    show frisk distant with Dissolve(.25)
    frisk "Can I tell you a secret?"
    frisk "I sneak out at night a lot. I’ve been out there, and I still don’t get why she’s so scared of it."
    show frisk upset with Dissolve(.25)
    frisk "Everyone in the Underground is so nice! If Mom would only try to talk to some of them, maybe she wouldn’t be so bent on keeping me locked up in the Ruins my whole life."
    show frisk distant with Dissolve(.25)
    frisk "So, I guess what I’m trying to say is... I understand why you want to leave."
    frisk "Just... don’t be a stranger, alright? Come back and visit every now and then."
    
    menu:
        "I will.":
            $world.get_monster ('Frisk').update_FP(4)
            show frisk smallsmile with Dissolve(.25)
            frisk "Thanks."
            frisk "Have fun out there, and tell Sans and Papyrus I said ‘hi’." 
            frisk "See you later."
            hide frisk
        "Not likely.":
            $world.get_monster ('Frisk').update_FP(-5)
            frisk "...I guess I get it. This place can be a little..."
            frisk "...Stifling."
            frisk "Maybe I’ll see you on the other side sometime."
            frisk "But, if I don’t... Goodbye, and good luck out there."
            hide frisk
    
    #wait a second before having the screen fade to black, play the sound of a heavy door opening
    #end of demo
    jump end_of_demo
    return



label end_of_demo:

    "Will try to remember to put something here."

    jump main_menu