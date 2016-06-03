#When Flowey is being creepy, I can change the text speed for that too



#character-images


#background-images


#character-settings
define narration = Character(kind=nvl)
define system = Character('', color="#FFFFFF")
define flowey = Character('Flowey')

#sprite positions
init:
    $ left = Position(xpos = 0.25, xanchor = 'left')
    $ center = Position(xpos = 0.5, xanchor = 'center')
    $ right = Position(xpos = 0.75, xanchor = 'right')

init:
    $ flowey_nopie_talked = 0
    $ nopie = True
    #expressions AFTER dialog
    $ nopie_dialog = ["I’m so sick of the dirt... And I’m so hungry...",
            "What? What are you doing here? Didn’t I tell you not to bother me?", #*Surprised* 
            "What do you want?", #*Suspicious side glance* 
            "I told you, I’m busy. Go talk to someone else.", # *Angry* 
            "I’m not going to talk to you. I don’t want to.",
            "I told you, I’m not giving any hints. Only nerds try to exhaust the dialogue for hints.",
            "...", #*Suspicious side glance* 
            "You’re a real creep, just standing there.",
            "If you’re gonna try to be a nerd, go make friends with Alphys. There’s no one nerdier than her.",
            "...",
            "...",
            "Listen, I’m not here to be your friend. I’m not going to be your friend, got it?", #*Evil* 
            "Idiot.", #*Angry* 
            "...",
            "...",
            "I told you, you can try all you want, I’m not going to be your friend.", # *Suspicious side glance* 
            "I don’t care what you know or don’t know about me. Get out of here, idiot.",
            "...",
            "...",
            "...",
            "...",#*Turns back away*
            "We can’t be friends. I told you.",
            "There are nicer people out there. There are people that will take care of you. Go be friends with them.",
            "Get out.",
            "..."]

#default-font
init python:
    style.default.font = "font/DTM-Mono.otf"

#default-text-speed
#config.default_text_cps=20
label flowey_start:
    menu:
        "Flowey Hangout1":
            jump flowey_hangout1
        "No Snail Pie in Inventory (After Finishing Hangout1)":
            jump flowey_overworld
        "With Snail Pie in Inventory (After Finishing Hangout1)":
            jump flowey_hangout2
        "Exit Game":
            return
#This works
label flowey_hangout1:
    label flowey_hangout1_Q1:
        #Surprised
        flowey "Wha-?! You snuck up on me. "
        #Suspicious side glance
        flowey "What do you want? I’m not gonna give you any tips, and I’m not here to talk. Buzz off."
        menu:
            flowey "What do you want? I’m not gonna give you any tips, and I’m not here to talk. Buzz off.{fast}"

            "Exit":  #Neutral 0
                jump flowey_end
            "...I’d just like to chat.": #Neutral 0
                jump flowey_hangout1_Q2
            "I’d like to talk to you, flower.": #Neutral 0 +HB
                jump flowey_hangout1_Q2
            
    label flowey_hangout1_Q2:
        #evil
        flowey "I d i o t . You’re in the wrong place. Get out before you piss me off. I’m busy."
        menu:
            flowey "I d i o t . You’re in the wrong place. Get out before you piss me off. I’m busy.{fast}"
            "Alright, bye":
                jump flowey_end
            "Busy? Busy doing what?": #neutral 0
                flowey "That’s none of your business."
                jump flowey_hangout1_Q3
            "What does a flower have to do?":#neutral0 + hb
                #angry
                flowey "Seriously? More than you do obviously."
                jump flowey_hangout1_Q3

    label flowey_hangout1_Q3:
        flowey "Why don't you go and find someone to play with?"
        menu:
            flowey "Why don't you go and find someone to play with?{fast}"
            "I'm just interested in what life is like down here.": #increase +fp
                flowey "Then go ask someone else. I have better things to do than to talk to some human, and you’re not going to find your happy ending here."
                jump flowey_hangout1_Q4
            "I just thought we could play a game.": #Increase +HB
                #surprised
                flowey "A game...?"
                #angry
                flowey "I'm not interested in playing games with you right now."
                jump flowey_hangout1_Q4
            "Sorry, my bad.":
                jump flowey_end
    label flowey_hangout1_Q4:
        flowey "Stop trolling and wasting both of our time."
        menu:
            flowey "Stop trolling and wasting both of our time.{fast}"
            "Ya got me, I'm a big troll.": #Decrease - FP
                #Evil
                flowey "That's pretty funny, troll. Now go before I kill ya."
                jump flowey_end
            "I'm not interested in them right now. Maybe I could help you.": #increase + FP
                #surprised
                flowey "Help me?"
                #suspicious side glance
                flowey "Idiot. You can’t help me. Go bother someone else."
                jump flowey_start

label flowey_overworld:
    menu:
        "Talk to Flowey":
            if nopie:
                jump flowey_nopie
            else:
                jump flowey_hangout2
        "Back to menu":
            jump flowey_start


label flowey_nopie:

    if flowey_nopie_talked>=25:
        flowey "..."
        "PayneGray" "That's all he's gonna say from now on."

    else:
        $ renpy.say(flowey,nopie_dialog[flowey_nopie_talked])
        $ flowey_nopie_talked += 1
    
    jump flowey_overworld




label flowey_hangout2:
    #Second dialogue set takes place as soon as listed prerequisites haven been met. (If you have the snail pie.)
    label flowey_hangout2_Q1:

        flowey "What do you want?"
        menu:
            #*Suspicious side glance* 
            flowey "What do you want?{fast}"
            "I was bored. Let's chat.": #Neutral 0
                #*Evil* 
                flowey "I’m not your entertainment. Scram."
            "I'd still like to talk.": #Increase + FP
                #angry
                flowey "I told you, I’m not interested in talking. Get out of here."
            "These people aren't fun. Let's talk.": #Increase + + HB
                flowey "I don’t want to talk to you. Leave me alone."
        jump flowey_hangout2_Q2








    label flowey_hangout2_Q2:
        flowey "Wait... What's that smell?"
        menu:
            flowey "Wait... What's that smell?{fast}"
            "I thought you told me to leave?": #Neutral 0
                #*Angry* 
                flowey "You said you wanted to chat, so let’s chat. What is it?"
            "I have something for you.": #Increase + FP
                #Surprised
                flowey "What is it?"
            "Hungry, little flower?": # Increase + +HB
                #Angry
                flowey "Flowers can't eat, you idiot. I was just curious. What is it?"
        jump flowey_hangout2_Q3


    label flowey_hangout2_Q3:
        #Suspicious side glance
        flowey "Well?"
        menu:
            flowey "Well?{fast}"
            "I’ll be back later to show you.":#Neutral 0
                flowey "Thanks for wasting my time."
                jump flowey_end
            "Show him what’s in your bag":#Increase + FP
                #Suprised
                flowey "Is that... pie?"
                jump flowey_hangout2_Q7
            "It’s a gift~":
                jump flowey_hangout2_Q4

    label flowey_hangout2_Q4:#
        #Suspicious side glance
        flowey "Why give me anything?"
        menu:
            flowey "Why give me anything?{fast}"
            "Because I think you will like it.":#Increase + FP
                flowey "What is it, exactly? It smells... Familiar."
                jump flowey_hangout2_Q6_Nice

            "Suddenly interested, huh?": #Decrease - FP
                #*Angry* 
                flowey "So what? Shove a bag in my face and of course I’d be interested, Idiot."
                #Anger
                flowey "You think you can just bribe someone into friendship? That’s not how it works. That’s not how I work. You might have the others fooled, but never forget:"
                #evil
                flowey "I  s e e  r i g h t  t h r o u g h  y o u ." 
                menu:
                    flowey "I  s e e  r i g h t  t h r o u g h  y o u .{fast}"
                    "That's not it.I just thought you might like it.":
                        #*Suspicious* 
                        flowey "Like what?"
                        jump flowey_hangout2_Q6_Nice
                    "Oh, do you? Well... I know a little about you too. You’d like this, Flower.":
                        #Suspicious
                        flowey "Why’s that?"
                        jump flowey_hangout2_Q6_Nice
                    "I was just trying to help, jeeze...":
                        #Surprised
                        flowey "Oh? You were just trying to help?"
                        #Friendly smile
                        flowey "You know, a lot of those idiots have tried to help me in the past."
                        #Wink
                        flowey "I’ll give you some advice on trying to help me."
                        #Evil
                        flowey "D o n ’ t ." 
                        flowey "Now get out of here, i d i o t."
                        flowey "But you can at least leave whatever you were going to give me to make up for wasting my time."
                        flowey "..."
                        flowey "What even is it, anyway? It better be good."


                        jump flowey_hangout2_Q6_Mean
            "Someone made it, just for me. I didn’t want it. Take it as a gift.": #Increase + +HB
                #flowey "Well, what is it? It smells... Familiar."
                jump flowey_hangout2_Q5
            "It’s a gift. You can take it or leave it.":
                jump flowey_hangout2_Q5







    #There was another bit of dialog in the doc. I didn't know where to put, "It’s a gift. You can take it or leave it." 
    label flowey_hangout2_Q5:#
        flowey "Wait, gifts? I don’t need any gifts."
        flowey "I told you,  I’m not going to be your friend. I’m not like those other idiots—I don’t become friends because of some trinkets. We can’t be friends."
        menu:
            #suspicious
            flowey "I told you,  I’m not going to be your friend. I’m not like those other idiots—I don’t become friends because of some trinkets. We can’t be friends.{fast}"
            "It’s not to be friends. I just thought you might like it.":#Increase + FP
                flowey "Hmph. Alright. What is it?"
                jump flowey_hangout2_Q6_Nice
            "C’mon, even flowers can accept a little gift.": #Increase + +HB
                flowey "Hmph. Alright. What is it?"
                jump flowey_hangout2_Q6_Nice

            "You don’t know that yet.": #Neutral 0
                #*Evil* 
                flowey "Oh, trust me, I do know. I know more than you ever could... You Idiot."
                jump flowey_hangout2_Q6_Mean
            "Everyone needs a friend. And since no one else is offering, it looks like I’m your only option.": #+ HB
                flowey "What?"
                flowey "Who said I even wanted a friend?" 
                flowey "Just leave whatever you brought me over there. It’s the least you could do for wasting my time."
                flowey "What even is it? It better be great."
                jump flowey_hangout2_Q6_Mean


    label flowey_hangout2_Q6_Nice:
        menu:
            "Tell him it’s snail pie.":#Increase + FP
                jump flowey_hangout2_Q7
            "Wouldn’t you like to know~":#//Increase + +HB
                #smug
                flowey "Hehe, that’s fine. I’ll remember this."
                jump flowey_end
    label flowey_hangout2_Q6_Mean:
        menu:
            "Well… Here you go, jerk. It’s snail pie.":#”)  // Increase + HB
                jump flowey_hangout2_Q7
            "Ask him \"Wouldn’t you like to know~\" and leave":#            //Increase + +HB
                jump flowey_end

    label flowey_hangout2_Q7:#
        flowey "What? A snail pie? What do you expect me to do with this disgusting thing?!"
        menu:
            #Surprise
            flowey "What? A snail pie? What do you expect me to do with this disgusting thing?!{fast}"
            "Oh, um, sorry, I’ll get rid of it for you..":#Increase +FP
                #fear or shock
                flowey "No!"
                #bashful
                flowey "I mean, it’s not doing any harm just sitting here."
                #slightly annoyed
                flowey "Just leave, already."
                #slightly annoyed
                flowey "You’re getting annoying."
            "Wow, so ungrateful, aren’t you?":#Decrease - FP           
                flowey "Well, I never asked for your stupid gift, did I?"
                flowey "Get lost already."
                narration "*You see several large vines, sprouting up from the ground, taking the pie from your hands."
                flowey "Not that I actually want it, but this is the least you owe me for wasting my time."
        jump flowey_end

label flowey_end:
    menu:
        "Start Over":
            jump flowey_start
        "Return to Main Menu":
            jump start
