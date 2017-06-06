# ---- In Order To Keep From Confusing Coders, All Dialogue Templates Should Attempt to Follow This Pattern  ----
#
# KEY:
# sans "__"      = character dialog
# *Asterisks*     = Sprite changes
# ("Parenthesis") = dialogue frisk_frienship_hangout2_options
# ##//(+0)           = Response’s Increase/Decrease to Date Meter
# #/// If >  <   = The order of player answers that lead up to that            dialogue
# [n/a #]        = Dialogue frisk_frienship_hangout2_option not available if previous frisk_frienship_hangout2_option
# has been used (all frisk_frienship_hangout2_options assigned a number)
# + Or -         = amount of points
# jump ___    = tells the game to skip to a different part of the script
# label ___:    = marks a part of the script so it can be jumped to
# #blah blah     = message for all coders and editors. used for all other communication that cannot be indicated otherwise
# Edited Dialogue After coders have already put it into the game
# Striked out means text has been deleted
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Event Name: What Could Go Wrong?
# Event Trigger: 1. Must have completed friendship event 1
# 2. Any day after event 1, enter the kitchen after breakfast but before dinner
#
# Frisk says they are doing fine, but they freak out again, not realizing they have a knife in their hands.
#
#
# Expressions
# frisk normal, disappointed, upset, distant, annoyed, tiny smile, teary eyes, surprised, soulless, big smile, angry, giggling, blush, sad, disgusted, somewhat happy, both panicking sprites
#
# Sound Effects Needed
# Sound of a knife clanging as it’s dropped on tile floor
#
# +FP in green
label frisk_friendship_hangout2_menu:
    $ visited_frisk = 0
    menu:
        "Start":
            jump frisk_friendship_hangout2_start
        "Visit Frisk After Hangout":
            jump frisk_friendship_hangout2_visit_frisk_same_day
        "Exit":
            jump testing_area
label frisk_friendship_hangout2_start:
    python:
        frisk_fp = 0
        determination = 2
        bravery = 2
        patience = 2

        frisk_frienship_hangout2_option = []
        for i in range(0,20):
            frisk_frienship_hangout2_option.append(False)
    show background toriel_kitchen
    stop music
    play music "audio/music/music-home.mp3"

    #scene kitchen
    show frisk tinysmile with Dissolve(.25)
    frisk "Hey, I’m glad you’re here."
    frisk "Could you help me with the dishes, please?"
    menu:
        "No way.":
            $ frisk_fp -=1
            frisk "Aw, okay... I get it."
            frisk "You’re probably busy, so I guess I’ll see you later."
            hide frisk with Dissolve(.25)
            "BAD END"
            #if the player goes back into the kitchen within an hour:
            show frisk normal with Dissolve(.25)
            frisk "Hey! I'm still working on these dishes."
            frisk "See you around!"
            hide frisk with Dissolve(.25)
            #two days after this, the player can find Frisk in the kitchen again. They cannot progress in Frisk’s 
            #friendship route without getting the good end to this event
            return
        "Yeah, sure.":
            $ frisk_fp +=2
            show frisk tinysmile with Dissolve(.25)
            frisk "Great! There’s a stack of plates over there. If you could scrub those, that’d be super helpful!"
            show frisk normal with Dissolve(.25)
            "*Frisk turns and gets back to work."
            "*You grab a few plates and start scrubbing."
            "*..."
            frisk "So… How’ve you been doing?"
            menu:
                "Can we talk about what happened the other day?":
                    $ frisk_fp -=1
                    jump frisk_fe2_otherday
                "Fine. You?":##//(+1)
                    $ frisk_fp +=1
                    frisk "That’s good. I’ve been fine, too."
                    frisk "But, uhm…"
                    frisk "Well, you know."
                    frisk "I was certain you were going to try and get me to talk about it…"
                    frisk "Thanks for understanding."
                    frisk "It’s just one of those things I need to work out on my own, y’know?"
                    frisk "Whatever it is. I’m still not sure myself."
                    show frisk disappointed with Dissolve(.25)
                    frisk "…"
                    frisk "And it can be a little overwhelming."
                    frisk "But it’s something I can handle, really it is."
            
label frisk_fe2_otherday:
    frisk "…"
    frisk "Do we have to?"
    frisk "Look, I-"
    frisk "…"
    show frisk disappointed with Dissolve(.25)
    frisk "What can I say?"
    frisk "I really think you should just let it go."
    frisk "It’s my own problem to handle."
    menu:
        "What kind of problem?":
            frisk "...It’s not important."
            frisk "It’s mine, and I should deal with it on my own."
            frisk "I {i}can{/i} deal with it on my own."
        "Does Toriel know?": 
            frisk "...Yeah."
            frisk "I keep telling her not to be concerned…"
            frisk "I really don’t like to worry her."
        "Alright, I’ll stop asking.": 
            $ frisk_fp +=2
            frisk "Thanks…"
            frisk "It’s just something I have to deal with on my own."
        "(Say nothing)": 
            $ frisk_fp +=1
            frisk "…"
            frisk "Just don’t worry about me."
            frisk "I guess it can be a little much, and there’s something about this thing that feels really personal."
            frisk "Like I’m not supposed to talk about it."

    show frisk normal with Dissolve(.25)
    "*Frisk picks up a knife and starts cleaning it."
    frisk "I’ll figure it out, just like I always do..."
    show frisk distant with Dissolve(.25)
    frisk "..."
    "*They’re staring at the knife in their hands."
    frisk "..."
    frisk "I don’t feel so good."
    menu:
        "Are you okay?":                    
            frisk "I uh…"
            frisk "I’m fine. Really."
        "Is it happening again?":          
            frisk "W-what? No, it’s just…"
        "Put down the knife!":              
            frisk "Oh… I-I’m sorry…"
            frisk "I just…"
            frisk "I can’t."

    frisk "..."
    menu:
        "Should I get Toriel?":             
            $ frisk_frienship_hangout2_option[13] = True
            frisk "N-no, I can handle this."
            frisk "…"
            frisk "It’s going away."
            frisk "..."
            #sound of a metal clang as the knife falls to the floor
        "(Back away)":                    
            $ frisk_fp -=3
            $ frisk_frienship_hangout2_option[14] = True
            frisk "I’m so sorry…"
            show frisk panicking with Dissolve(.25)
            frisk "I’m not like this, I swear!"
            frisk "It’s going away, honest!"
            frisk "I just- I can’t-"
            frisk "..."
            #sound of a metal clang as the knife falls to the floor
        "(Try to grab the knife away from Frisk)" if bravery>=2:      
            $ frisk_frienship_hangout2_option[15] = True
            frisk "...!"
            "*You pry the knife from their hands, and it falls to the floor."
            #sound of a metal clang as the knife falls to the floor
            frisk "Huh?"
        "It’s okay, let’s just wait it out." if patience>=2:       
            $ frisk_fp +=4
            $ frisk_frienship_hangout2_option[16] = True
            frisk "Yeah… Okay…"
            frisk "..."
            frisk "I think it’s going away…"
            #sound of a metal clang as the knife falls to the floor
            
    stop music
    play music "audio/music/music-home.mp3"
    show frisk disgusted with Dissolve(.25)
    frisk "Oh no… I’m so sorry!"
    show frisk disappointed with Dissolve(.25)
    frisk "But it’s fine… It’s fine. I’m feeling better now."
    if frisk_frienship_hangout2_option[13]:
        frisk "I’m sorry you had to see that…"
    elif frisk_frienship_hangout2_option[14]:
        frisk "I’m so sorry… I scared you, didn’t I?"
    elif frisk_frienship_hangout2_option[15]:
        frisk "If you hadn’t grabbed the knife from me, I…"
        frisk "I don’t know what would’ve happened."
    elif frisk_frienship_hangout2_option[16]:
        frisk "Thank you for waiting with me… That was exactly what I needed."

    menu:
        "Are you sure you’re alright?":         
            $ frisk_fp+=2
            $ frisk_frienship_hangout2_option[17]=True
            frisk "Yeah, I’m fine… Really."
            show frisk sad with Dissolve(.25)
            frisk "Look…"
        "You need to tell me what’s going on.":     
            $ frisk_frienship_hangout2_option[18] = True
            show frisk sad with Dissolve(.25)
            frisk "...You’re right."        

    frisk "I could’ve hurt you, and I’d never forgive myself if I did that."
    frisk "I really shouldn’t have tried to act like this was nothing."
    frisk "I just don’t want other people to be burdened with my own problems."
    frisk "We can talk more about this, but…"
    frisk "Tomorrow. Please."
    frisk "I need some time to think. Come and find me in my room tomorrow."
    hide frisk
    "Good End."
    return

label frisk_friendship_hangout2_visit_frisk_same_day:
    show background frisk_room
    #if the player goes to Frisk’s room later the same day
    if visited_frisk==0:
        #1st time:
        show frisk sad with Dissolve(.25)
        frisk "I know this is probably all so strange to you…"
        frisk "But, please… I need some time to myself."
    elif visited_frisk==1:
        #2nd time
        show frisk sad with Dissolve(.25)
        frisk "I know you wanna help, but I need some space."
        frisk "We can talk tomorrow."
    elif visited_frisk==2:
        #3rd time
        show frisk sad with Dissolve(.25)
        frisk "I’m being sincere. Please, just go."
    elif visited_frisk==3:
        #4th time
        show frisk sad with Dissolve(.25)
        frisk "…"
        frisk "Don’t you have anything better to do?"
    elif visited_frisk==4:
        #5th time
        show frisk sad with Dissolve(.25)
        frisk "…"
    elif visited_frisk==5:
        #6th time
        show frisk annoyed with Dissolve(.25)
        frisk "…"
    elif visited_frisk==6:
        #7th time
        $ frisk_fp -=4
        show frisk angry with Dissolve(.25)
        frisk "I said go away!"
    else:
        hide frisk with Dissolve(.25)
        #Frisk’s room is now locked if the player tries to enter again before the next day
    $ visited_frisk+=1
    return
