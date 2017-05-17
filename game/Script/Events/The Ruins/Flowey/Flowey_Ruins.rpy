

label flowey_hangout1:
    scene background floweyroomplaceholder
    #Hangout 1 
    #{After tutorial}
    #This initial "Hangout" dialogue will occur regardless if player has or has not yet met the prerequisites for a friendship with flowey
    show flowey surprised with dissolve
    flowey "Wha-?! You snuck up on me."

    label flowey_hangout1_Q1:
        show flowey suspicious
        flowey "What do you want? I’m not gonna give you any tips, and I’m not here to talk. Buzz off."
        menu:
            "Exit":
                jump flowey_ruins
            "...I’d just like to chat.": #Adds FP
                jump flowey_hangout1_Q2
            "I’d like to talk to you, flower.": 
                jump flowey_hangout1_Q2

    label flowey_hangout1_Q2:
        show flowey horror
        flowey "I d i o t . You’re in the wrong place. Get out before you piss me off. I’m busy."
        menu:
            "Alright, bye.":
                jump flowey_ruins
            "Busy? Busy doing what?":
                show flowey annoyed
                flowey "That’s none of your business." 
                jump flowey_hangout1_Q3
            "What does a flower have to do?": #+HB
                show flowey angry
                flowey "Seriously? More than you do {i}clearly{/i}."
                jump flowey_hangout1_Q3
    
    label flowey_hangout1_Q3:
        show flowey annoyed
        flowey "Why don't you go and find someone else to annoy?"
        menu:
            "I’m just interested in what life is like down here.": #+FP
                show flowey annoyed
                flowey "Then go ask someone else. I have better things to do than to talk to some human, and you’re not going to find your {i}happy ending{/i} here."
                flowey "Don't you have anything {i}better{/i} to do?"
                show flowey smug
                flowey "Silly me, of course you don't."
                jump flowey_hangout1_Q4
            "I thought we could play a game.": #+HB
                show flowey surprised
                flowey "A game...?"
                show flowey angry
                flowey "I’m not interested in playing games with you right now."
                flowey "Or ever, actually."
                jump flowey_hangout1_Q4
            "Sorry, my bad.":
                show flowey horror
                flowey "That's right, {i}you're{/i} bad--"
                show flowey surprised
                flowey "...wait"
                show flowey suspicious
                flowey "Your bad? That's it?"
                show flowey angry
                flowey "You wasted not just your time, but mine, for the sake of showing up to \"chat\" and now you have nothing better to say than \"my bad\"?!"
                flowey "This is pathetic."
                menu:
                    "Did... you want me to stay, FLowey?":
                    #if player has >5 FP:
                        show flowey surprised
                        flowey "..."
                        show flowey blush
                        flowey "I..."
                        show flowey sideglance
                        flowey "Don't be stupid."
                        show flowey normal
                        flowey "I mean, this encounter was actually kind of entertaining."
                        flowey "..."
                        flowey "But I couldn't care less if you chose to leave."
                        show flowey smug
                        flowey "So go. And I'll see you around~ Heehee~!"
                        jump flowey_ruins
                    #if player has <5 FP:
                        show flowey horror
                        flowey "..."
                        flowey "Are you kidding?"
                        show flowey laugh
                        flowey "Pff hahahaHAHAHA!!"
                        show flowey normal
                        flowey "..."
                        show flowey angry
                        flowey "Get out of my face, idiot."
                        jump flowey_ruins
                    "It sure is. So I'm leaving.":
                        show flowey normal
                        flowey "Of course you are."
                        show flowey wink
                        flowey "Get out of my face, idiot."
                        jump flowey_ruins
                    "What did you expect from me?":
                    #if player has >5 FP:
                        show flowey sideglance
                        flowey "..."
                        show flowey normal
                        flowey "Nothing, apparently."
                        show flowey surprised
                        flowey "Nothing at all."
                        show flowey normal
                        flowey "Well, get going, then. Stop wasting my time."
                        jump  flowey_ruins
                    #if player has >5 FP:
                        show flowey laugh
                        flowey "Heh, my expectations for you are very low."
                        show flowey normal
                        flowey "But you already failed them."
                        show flowey smug
                        flowey "Can't say I'm disappointed, however."
                        flowey "It's expected by now."
                        show flowey normal
                        flowey "..."
                        flowey "Get out of my face, idiot."
                        jump flowey_ruins
        label flowey_hangout1_Q4:
            show flowey annoyed
            flowey "I'm not the one wasting my time annoying someone who has no interest in talking to them."
            flowey "I have a lot more to do than you, apparently."
            menu:
                "I'm just interested in what life is like down here.":
                    show flowey sideglance
                    flowey "That's... a matter of perspective."
                    flowey "For obvious reasons."
                    show flowey normal
                    "........"
                    show flowey annoyed
                    flowey "Don't you have anything {i}better{/} to do?"
                    show flowey smug
                    flowey "Silly me, of course you don't."
                    jump flowey_hangout1_Q5
                "We're going to play a game.":
                    show flowey angry
                    flowey "I don't think so."
                    flowey "In fact, I think we're done here."
                    jump flowey_ruins
                    #HB route is now triggered, player moves onto Flowey HB 1 instead of the usual friendship route
                "Sorry, my bad.":
                    show flowey horror
                    flowey "That's right, {i}you're{/i} bad--"
                    show flowey surprised
                    flowey "...wait"
                    show flowey suspicious
                    flowey "Your bad? That's it?"
                    show flowey angry
                    flowey "You wasted not just your time, but mine, for the sake of showing up to \"chat\" and now you have nothing better to say than \"my bad\"?!"
                    flowey "This is pathetic."
                    menu:
                        "Did... you want me to stay, FLowey?":
                        #if player has >5 FP:
                            show flowey surprised
                            flowey "..."
                            show flowey blush
                            flowey "I..."
                            show flowey sideglance
                            flowey "Don't be stupid."
                            show flowey normal
                            flowey "I mean, this encounter was actually kind of entertaining."
                            flowey "..."
                            flowey "But I couldn't care less if you chose to leave."
                            show flowey smug
                            flowey "So go. And I'll see you around~ Heehee~!"
                            jump flowey_ruins
                        #if player has <5 FP:
                            show flowey horror
                            flowey "..."
                            flowey "Are you kidding?"
                            show flowey laugh
                            flowey "Pff hahahaHAHAHA!!"
                            show flowey normal
                            flowey "..."
                            show flowey angry
                            flowey "Get out of my face, idiot."
                            jump flowey_ruins
                        "It sure is. So I'm leaving.":
                            show flowey normal
                            flowey "Of course you are."
                            show flowey wink
                            flowey "Get out of my face, idiot."
                            jump flowey_ruins
                        "What did you expect from me?":
                        #if player has >5 FP:
                            show flowey sideglance
                            flowey "..."
                            show flowey normal
                            flowey "Nothing, apparently."
                            show flowey surprised
                            flowey "Nothing at all."
                            show flowey normal
                            flowey "Well, get going, then. Stop wasting my time."
                            jump  flowey_ruins
                        #if player has >5 FP:
                            show flowey laugh
                            flowey "Heh, my expectations for you are very low."
                            show flowey normal
                            flowey "But you already failed them."
                            show flowey smug
                            flowey "Can't say I'm disappointed, however."
                            flowey "It's expected by now."
                            show flowey normal
                            flowey "..."
                            flowey "Get out of my face, idiot."
                            jump flowey_ruins
        label flowey_hangout1_Q5:
            show flowey annoyed
            flowey "Stop trolling and wasting both of our time."
            menu:
                "You got me. I'm a big troll.":
                    show flowey horror
                    flowey "That's pretty funny, idiot."
                    flowey "Now go, before I kill you."
                    jump flowey_ruins
                "Maybe I could help you.":
                    show flowey surprised
                    flowey "Help me?"
                    show flowey sideglance
                    flowey "Idiot. You can't help me."
                    flowey "...Not that I need help, anyway."
                    flowey "..."
                    show flowey normal
                    flowey "I'm gonna go. Stay here by your lonesome as long as you'd like."
                    flowey "Or go bother someone else."
                    jump flowey_ruins
                    

#label flowey_overworld:
#    scene background floweyroomplaceholder
    

label flowey_nopie:
    scene background floweyroomplaceholder
#    Hangout 2 
#    Two options for this, depending on prerequisites. 
#    - snail pie
#    - friends with Toriel (how they get the pie)
#    First set are if the initial prerequisites haven’t been met. Player should have option to continue talking or leave at each line .
#
#    **requires snail pie - Flowey will always be facing away from player and not interactable until player gets the pie
#    ((if player approaches him and clicks the gift option ))

    $ nopie_dialog = ["I’m so sick of the dirt... And I’m so hungry...", #0
                "What? What are you doing here? Didn’t I tell you not to bother me?", #*Surprised* 1
                "What do you want?", #*Suspicious side glance* 2
                "I told you, I’m busy. Go talk to someone else.", # *Angry* 3 
                "I’m not going to talk to you. I don’t want to.", #4
                "I told you, I’m not giving any hints. Only nerds try to exhaust the dialogue for hints.", #5
                "...", #*Suspicious side glance* 6
                "You’re a real creep, just standing there.", #7
                "If you’re gonna try to be a nerd, go make friends with Alphys. There’s no one nerdier than her.", #8
                "...", #9
                "...", #10
                "Listen, I’m not here to be your friend. I’m not going to be your friend, got it?", #*Evil* 11
                "Idiot.", #*Angry* 12
                "...", #13
                "...", #14
                "I told you, you can try all you want, I’m not going to be your friend.", # *Suspicious side glance* 15
                "I don’t care what you know or don’t know about me. Get out of here, idiot.", #16
                "...", #17
                "...", #18
                "...", #19
                "...",#*Turns back away* 20
                "We can’t be friends. I told you.",#21
                "There are nicer people out there. There are people that will take care of you. Go be friends with them.",#22
                "Get out."] #24
    if flowey_nopie_talked==0:
        show flowey back with dissolve
    elif flowey_nopie_talked==1:
        show flowey surprised
    elif flowey_nopie_talked>=2 and flowey_nopie_talked<6:
        show flowey angry
    elif flowey_nopie_talked>=6 and flowey_nopie_talked<11:
        show flowey suspicious
    elif flowey_nopie_talked==11:
        show flowey evil
    elif flowey_nopie_talked>=12 and flowey_nopie_talked<15:
        show flowey angry
    elif flowey_nopie_talked>=15 and flowey_nopie_talked<20:
        show flowey suspicious
    else:
        show flowey back

    if flowey_nopie_talked>=24:
        flowey "..."
        "PayneGray" "That's all he's gonna say from now on."

    else:
        
        $ renpy.say(flowey,nopie_dialog[flowey_nopie_talked])
        $ flowey_nopie_talked += 1
    menu:
        "Talk to flowey":
            if nopie:
                jump flowey_nopie
            else:
                jump flowey_hangout2
        "Back to menu":
            $ flowey_nopie_talked = 0
            jump flowey_ruins

label flowey_hangout2:
    scene background floweyroomplaceholder
        #Second dialogue set takes place as soon as listed prerequisites haven been met. 
    label flowey_hangout2_Q1:
        #*Suspicious side glance*
        show flowey suspicious 
        flowey "What do you want?"
        menu:
            flowey "What do you want?{fast}"
            "I was bored. Let’s chat.": #//Neutral 0
                #*Evil* 
                show flowey horror
                flowey "I’m not your entertainment. Scram."
            "I’d still like to talk.": #//Increase + FP
                #*Angry* 
                show flowey angry
                flowey "I told you, I’m not interested in talking. Get out of here."
            "These people aren’t fun. Let’s talk.": #//Increase + +HB
                flowey "I don’t want to talk to you. Leave me alone."
        jump flowey_hangout2_Q2

    label flowey_hangout2_Q2:
        #*Suspicious side glance*
        show flowey suspicious 
        flowey "Wait... What’s that smell?"
        menu:
            flowey "Wait... What’s that smell?{fast}"
            "I thought you told me to leave?": #//Neutral 0
                #*Angry*
                show flowey angry
                flowey "You said you wanted to chat, so let’s chat. What is it?"
            "I have something for you.": #//Increase + FP
                #*Surprised*
                show flowey surprised 
                flowey "What is it?"
            "Hungry, little flower?": #//Increase + +HB
                #*Angry* 
                show flowey angry
                flowey "Flowers can’t eat, you idiot. I was just curious. What is it?"
        jump flowey_hangout2_Q3

    label flowey_hangout2_Q3:
        #*Suspicious side glance* 
        show flowey suspicious
        flowey "Well?"
        menu:
            flowey "Well?{fast}"
            "I’ll be back later to show you.":     #//Neutral 0
                flowey "Thanks for wasting my time."
                #-Player exits the encounter-
                jump flowey_ruins
            "Show him what’s in your bag":   #//Increase + FP
                #*Surprised* 
                show flowey surprised
                flowey "Is that... pie? "
                jump flowey_hangout2_Q7
            "It’s a gift~":
                jump flowey_hangout2_Q4

    label flowey_hangout2_Q4:
        #*Suspicious side glance* 
        show flowey suspicious
        flowey "Why give me anything?"
        menu:
            flowey "Why give me anything?{fast}"
            "Because I think you will like it.": #//Increase + FP
                flowey "What is it, exactly? It smells... Familiar."
            "Suddenly interested, huh?": #//Decrease - FP
                #*Angry* 
                show flowey angry
                flowey "So what? Shove a bag in my face and of course I’d be interested, Idiot."
                jump flowey_hangout2_Q5_choice2
            "Someone made it, just for me. I didn’t want it. Take it as a gift.": #//Increase + +HB
                flowey "Well, what is it? It smells... Familiar."
                jump flowey_hangout2_Q5_choice1
            "It’s a gift. You can take it or leave it.": #//Increase + +HB
                flowey "Well, what is it? It smells... Familiar."
                jump flowey_hangout2_Q5_choice1

    label flowey_hangout2_Q5:
        label flowey_hangout2_Q5_choice1:
            #F Q5: #/// If >(It’s a gift. You can take it or leave it.)< OR #/// If >(Someone made it, just for me. I didn’t want it. Take it as a gift.)< 
            flowey "Wait, gifts? I don’t need any gifts."
            #*Suspicious* 
            show flowey suspicious
            flowey "I told you,  I’m not going to be your friend. I’m not like those other idiots—I don’t become friends because of some trinkets. We can’t be friends."
            menu:
                flowey "I told you,  I’m not going to be your friend. I’m not like those other idiots—I don’t become friends because of some trinkets. We can’t be friends.{fast}"
                "It’s not to be friends. I just thought you might like it.": #//Increase + FP
                    flowey "Hmph. All right. What is it?"
                    jump flowey_hangout2_Q6_choice1
                "C’mon, even flowers can accept a little gift.": #//Increase + +HB
                    flowey "Hmph. All right. What is it?"
                    jump flowey_hangout2_Q6_choice1
                "You don’t know that yet.": #//Neutral 0
                    #*Evil* 
                    show flowey horror
                    flowey "Oh, trust me, I do know. I know more than you ever could... You Idiot."
                    jump flowey_hangout2_Q6_choice2
                "Everyone needs a friend. And since no one else is offering, it looks like I’m your only option.": #+ HB
                    flowey "What?"
                    flowey "Who said I even wanted a friend?" 
                    flowey "Just leave whatever you brought me over there. It’s the least you could do for wasting my time."
                    flowey "What even is it? It better be great."
                    jump flowey_hangout2_Q6_choice2
        label flowey_hangout2_Q5_choice2:
            #flowey *Anger* 
            show flowey angry
            flowey "You think you can just bribe someone into friendship? That’s not how it works. That’s not how I work. You might have the others fooled, but never forget:"
            #*Evil* 
            show flowey horror
            flowey "I  s e e  r i g h t  t h r o u g h  y o u ." 
            menu:
                "I was just trying to help, jeeze...": #//Decrease - FP
                    #Surprised
                    show flowey surprised
                    flowey "Oh? You were just trying to help?"
                    #Friendly smile
                    show flowey normal
                    flowey "You know, a lot of those idiots have tried to help me in the past."
                    #Wink
                    show flowey wink
                    flowey "I’ll give you some advice on trying to help me."
                    #Evil
                    show flowey horror
                    flowey "D o n ’ t ." 
                    flowey "Now get out of here, i d i o t."
                    flowey "But you can at least leave whatever you were going to give me to make up for wasting my time."
                    flowey "..."
                    flowey "What even is it, anyway? It better be good."
                    jump flowey_hangout2_Q6_choice2
                "That’s not it. I just thought you might like it.": #//Increase + FP
                    #*Suspicious* 
                    show flowey suspicious
                    flowey "Like what?"
                    jump flowey_hangout2_Q6_choice1
                "Oh, do you? Well... I know a little about you too. You’d like this, Flower.": #//Increase+ +HB
                    #*Suspicious*
                    show flowey suspicious 
                    flowey "Why’s that?"
                    jump flowey_hangout2_Q6_choice1
    label flowey_hangout2_Q6:
        label flowey_hangout2_Q6_choice1:
            menu:
                "Tell him it’s snail pie.": #//Increase + FP
                    jump flowey_hangout2_Q7
                "Wouldn’t you like to know~": #//Increase + +HB
                    #*smug* 
                    show flowey smug
                    flowey "Hehe, that’s fine. I’ll remember this."
                    #-player exits encounter-
                    jump flowey_ruins

    #F Q6: #/// If >(It’s a gift. You can take it or leave it.)< #/// If >(You don’t know that yet.)< 
    #OR  #/// If >(Suddenly interested, huh?)< #/// If >(I was just trying to help, jeeze...)<
    #OR #/// If >("Everyone needs a friend. And since no one else is offering, it looks like I’m your only option.")<
        
        
        label flowey_hangout2_Q6_choice2:
            menu:
                "Well... Here you go, jerk. It’s snail pie.": #// Increase + HB
                    jump flowey_hangout2_Q7
                "Ask him \"Wouldn’t you like to know~\" and leave": #//Increase + +HB
                    #-player exits encounter-
                    jump flowey_ruins


    label flowey_hangout2_Q7:
        show flowey surprised
        flowey "What? A snail pie? What do you expect me to do with this disgusting thing?!"
        menu:
            #Surprise
            flowey "What? A snail pie? What do you expect me to do with this disgusting thing?!{fast}"
            "Oh, um, sorry, I’ll get rid of it for you..":#Increase +FP
                #fear or shock
                show flowey surprised
                flowey "No!"
                #bashful
                show flowey bashful
                flowey "I mean, it’s not doing any harm just sitting here."
                #slightly annoyed
                show flowey annoyed
                flowey "Just leave, already."
                #slightly annoyed
                flowey "You’re getting annoying."
            "Wow, so ungrateful, aren’t you?":#Decrease - FP 
                show flowey angry          
                flowey "Well, I never asked for your stupid gift, did I?"
                flowey "Get lost already."
                "*You see several large vines, sprouting up from the ground, taking the pie from your hands."
                show flowey annoyed
                flowey "Not that I actually want it, but this is the least you owe me for wasting my time."
        #-Player exits encounter-
        jump flowey_ruins
