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


#default-font
init python:
    style.default.font = "font/DTM-Mono.otf"

#default-text-speed
#config.default_text_cps=20
label start:
    jump flowey_hangout1

label flowey_hangout1:
    label flowey_Q1:
        #Surprised
        flowey "Wha-?! You snuck up on me. "
        #Suspicious side glance
        flowey "What do you want? I’m not gonna give you any tips, and I’m not here to talk. Buzz off."
        menu:
            
            "Exit":  #Neutral 0
                jump flowey_end
            "...I’d just like to chat.": #Neutral 0
                $ neutral+=0
            "I’d like to talk to you, flower.": #Neutral 0 +HB
                $ neutral+=0
            
    label flowey_Q2:
        #evil
        flowey "I d i o t . You’re in the wrong place. Get out before you piss me off. I’m busy."
        menu:
            "Alright, bye":
                jump flowey_end
            "Busy? Busy doing what?": #neutral 0
                flowey "That’s none of your business."
            "What does a flower have to do?":#neutral0 + hb
                #angry
                flowey "Seriously? More than you do obviously."

    label flowey_Q3:
        flowey "Why don't you go and find someone to play with?"
        menu:
            "I'm just interested in what life is like down here.": #increase +fp
                flowey "Then go ask someone else. I have better things to do than to talk to some human, and you’re not going to find your happy ending here. Stop trolling and wasting both of our time."
            "I just thought we could play a game.": #Increase +HB
                #surprised
                flowey "A game...?"
                #angry
                flowey "I'm not interested in playing games with you right now."
            "Sorry, my bad.":
                jump flowey_end
    label flowey_Q4:
        flowey "Stop trolling and wasting both of our time."
        menu:
            "Ya got me, I'm a big troll.": #Decrease - FP
                #Evil
                flowey "That's pretty funny, troll. Now go before I kill ya."
                jump flowey_end
            "I'm not interested in them right now. Maybe I could help you.": #increase + FP
                #surprised
                flowey "Help me?"
                #suspicious side glance
                flowey "Idiot. You can’t help me. Go bother someone else."
                jump flowey_end

label flowey_nopie:
    "You don't have the pie yet, and I'm still trying to figure out how to put all the text."

label flowey_hangout2:
    #Second dialogue set takes place as soon as listed prerequisites haven been met.
    label flowey_Q1:
    flowey "To be continued"

label flowey_end:

    system "It's a wonderful idea!!"
