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

#standings
init:
    $ neutral = 0
    $ flowey_nopie_talked = 0
    $ nopie = True
    $ nopie_dialog = ["I’m so sick of the dirt... And I’m so hungry...",
            "*Surprised* What? What are you doing here? Didn’t I tell you not to bother me?",
            "*Suspicious side glance* What do you want?",
            "*Angry* I told you, I’m busy. Go talk to someone else.",
            "I’m not going to talk to you. I don’t want to.",
            "I told you, I’m not giving any hints. Only nerds try to exhaust the dialogue for hints.",
            "*Suspicious side glance* ...",
            "You’re a real creep, just standing there.",
            "If you’re gonna try to be a nerd, go make friends with Alphys. There’s no one nerdier than her.",
            "...",
            "...",
            "*Evil* Listen, I’m not here to be your friend. I’m not going to be your friend, got it?",
            "*Angry* Idiot.",
            "...",
            "...",
            " *Suspicious side glance* I told you, you can try all you want, I’m not going to be your friend.",
            "I don’t care what you know or don’t know about me. Get out of here, idiot.",
            "...",
            "...",
            "...",
            "*Turns back away*",
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
        "With Snail Pie in Inventory":
            jump flowey_hangout2
        "Exit Game":
            return
label flowey_hangout1:
    label flowey_hangout1_Q1:
        #Surprised
        flowey "Wha-?! You snuck up on me. "
        #Suspicious side glance
        flowey "What do you want? I’m not gonna give you any tips, and I’m not here to talk. Buzz off."
        menu:
            flowey "What do you want? I’m not gonna give you any tips, and I’m not here to talk. Buzz off."

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
            flowey "I d i o t . You’re in the wrong place. Get out before you piss me off. I’m busy."
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
            flowey "Why don't you go and find someone to play with?"
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
            flowey "Stop trolling and wasting both of our time."
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
    #Second dialogue set takes place as soon as listed prerequisites haven been met.
    label flowey_hangout2_Q1:
        flowey "*Suspicious side glance* What do you want?"
        menu:
            "I was bored. Let's chat.":
                #*Evil* 
                flowey "I’m not your entertainment. Scram."
            "I'd still like to talk.":
                #angry
                flowey "I told you, I’m not interested in talking. Get out of here."
            "These people aren't fun. Let's talk.":
                flowey "I don’t want to talk to you. Leave me alone."
        jump flowey_hangout2_Q2
    label flowey_hangout2_Q2:
        flowey "Wait... What's that smell?"

        "PayneGray" "To be continued~"
        jump flowey_start

label flowey_end:
    menu:
        "Start Over":
            jump flowey_start
        "Return to Main Menu":
            jump start
