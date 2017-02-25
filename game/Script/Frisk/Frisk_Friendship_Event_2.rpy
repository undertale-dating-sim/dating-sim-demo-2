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
    #show frisk tiny smile
    show frisk tinysmile
    frisk "Hey, I’m glad you’re here."
    frisk "Could you help me with the dishes, please?"
    jump frisk_frienship_hangout2_selection1
label frisk_frienship_hangout2_selection1:
    menu:
        "No way.":
            $ frisk_fp -=1
            jump frisk_frienship_hangout2_choice1
        "Yeah, sure.":##//(+2)
            $ frisk_fp +=2
            jump frisk_frienship_hangout2_choice2
label frisk_frienship_hangout2_choice1:
    #/// If >1("No way.")<
    frisk "Aw, okay... I get it."
    frisk "You’re probably busy, so I guess I’ll see you later."
    "BAD END"
    jump frisk_friendship_hangout2_menu
    #Bad end
label frisk_frienship_hangout2_choice1_2:
    #if the player goes back into the kitchen within an hour:
    show frisk normal
    frisk "Hey! I’m still working on these dishes."
    frisk "See you around!"
    #two days after this, the player can find Frisk in the kitchen again. They cannot progress in Frisk’s friendship route without getting the good end to this event
label frisk_frienship_hangout2_choice2:
    #/// If >2("Yeah, Sure.")<
    show frisk tinysmile
    frisk "Great! There’s a stack of plates over there. If you could scrub those, that’d be super helpful!"
    #show frisk normal
    "*Frisk turns and gets back to work."
    "*You grab a few plates and start scrubbing."
    "*..."
    frisk "So… How’ve you been doing?"
label frisk_frienship_hangout2_selection2:
    menu:
        "Can we talk about what happened the other day?": #//(-1)
            $ frisk_fp -=1
            jump frisk_frienship_hangout2_choice5
        "Fine. You?":##//(+1)
            $ frisk_fp +=1
            jump frisk_frienship_hangout2_choice6
label frisk_frienship_hangout2_choice5:
    #/// If >5("Can we talk about what happened the other day?")<
    frisk "…"
    frisk "Do we have to?"
    frisk "Look, I-"
    frisk "…"
    show frisk disappointed
    frisk "What can I say?"
    frisk "I really think you should just let it go."
    frisk "It’s my own problem to handle."
    jump frisk_frienship_hangout2_selection3
label frisk_frienship_hangout2_selection3:
    menu:
        "What kind of problem?":            ##//(+0)

            jump frisk_frienship_hangout2_choice7
        "Does Toriel know?":            ##//(+0)
            jump frisk_frienship_hangout2_choice8
        "Alright, I’ll stop asking.":        ##//(+2)
            $ frisk_fp +=2
            jump frisk_frienship_hangout2_choice9
        "(Say nothing)":                ##//(+1)
            $ frisk_fp +=1
            jump frisk_frienship_hangout2_choice10
        "I’m not giving up until you let me help you." if determination>=2:                        ##//(-2)
        #frisk_frienship_hangout2_option 11 only available if the player has at least +2 Determination
            $ frisk_fp -=2
            jump frisk_frienship_hangout2_choice11
label frisk_frienship_hangout2_choice7:
    #/// If >7("What kind of problem?")<
    frisk "...It’s not important."
    frisk "It’s mine, and I should deal with it on my own."
    frisk "I can deal with it on my own."
    jump frisk_friendship_hangout2_knife
label frisk_frienship_hangout2_choice8:
    #/// If >8("Does Toriel know?")<
    frisk "...Yeah."
    frisk "I keep telling her not to be concerned…"
    frisk "I really don’t like to worry her."
    jump frisk_friendship_hangout2_knife
label frisk_frienship_hangout2_choice9:
    #/// If >9("Alright, I’ll stop asking.")<
    frisk "Thanks…"
    frisk "It’s just something I have to deal with on my own."
    jump frisk_friendship_hangout2_knife
label frisk_frienship_hangout2_choice10:
    #/// If >10(Say nothing)<
    frisk "…"
    frisk "Just don’t worry about me."
    frisk "I guess it can be a little much, and there’s something about this thing that feels really personal."
    frisk "Like I’m not supposed to talk about it."
    jump frisk_friendship_hangout2_knife
label frisk_frienship_hangout2_choice6:
    #/// If >6("Fine. You?")<
    frisk "That’s good. I’ve been fine, too."
    frisk "But, uhm…"
    frisk "Well, you know."
    frisk "I was certain you were going to try and get me to talk about it…"
    frisk "Thanks for understanding."
    frisk "It’s just one of those things I need to work out on my own, y’know?"
    frisk "Whatever it is. I’m still not sure myself."
    show frisk disappointed
    frisk "…"
    frisk "And it can be a little overwhelming."
    frisk "But it’s something I can handle, really it is."
    jump frisk_friendship_hangout2_knife


label frisk_friendship_hangout2_knife:

    show frisk normal
    "*Frisk picks up a knife and starts cleaning it."
    frisk "I’ll figure it out, just like I always do..."
    show frisk distant
    frisk "..."
    "*They’re staring at the knife in their hands."
    frisk "..."
    frisk "I don’t feel so good."
    jump frisk_frienship_hangout2_selection4
label frisk_frienship_hangout2_selection4:
    menu:
        "Are you okay?":                        ##//(+0)
            jump frisk_frienship_hangout2_choice10_2
        "Is it happening again?":                ##//(+0)
            jump frisk_frienship_hangout2_choice11_2
        "Put down the knife!":                    ##//(+0)
            jump frisk_frienship_hangout2_choice12
label frisk_frienship_hangout2_choice10_2:
    #/// If >10("Are you okay?")<
    frisk "I uh…"
    frisk "I’m fine. Really."
    jump frisk_frienship_hangout2_selection5
label frisk_frienship_hangout2_choice11_2:
    #/// If >11("Is it happening again?")<
    frisk "W-what? No, it’s just…"
    jump frisk_frienship_hangout2_selection5
label frisk_frienship_hangout2_choice12:
    #/// If >12("Put down the knife!")<
    frisk "Oh… I-I’m sorry…"
    frisk "I just…"
    frisk "I can’t."

    frisk "..."
    jump frisk_frienship_hangout2_selection5
label frisk_frienship_hangout2_selection5:
    menu:
        "Should I get Toriel?":                    ##//(+0)
            $ frisk_frienship_hangout2_option[13]=True
            jump frisk_frienship_hangout2_choice13
        "(Back away)":                            ##//(-3)
            $ frisk_fp -=3
            $ frisk_frienship_hangout2_option[14] = True
            jump frisk_frienship_hangout2_choice14
        "(Try to grab the knife away from Frisk)" if bravery>=2:        ##//(+0)
            $ frisk_frienship_hangout2_option[15] = True
            jump frisk_frienship_hangout2_choice15
        #frisk_frienship_hangout2_option 15 only available if the player has at least +2 Bravery
        "It’s okay, let’s just wait it out." if patience>=2:        ##//(+4)
            $ frisk_fp +=4
            $ frisk_frienship_hangout2_option[16] = True
            #frisk_frienship_hangout2_option 16 only available if the player has at least +2 Patience
            jump frisk_frienship_hangout2_choice16
label frisk_frienship_hangout2_choice13:
    #/// If >13("Should I get Toriel?")<
    frisk "N-no, I can handle this."
    frisk "…"
    frisk "It’s going away."
    frisk "..."
    #sound of a metal clang as the knife falls to the floor
    jump frisk_friendship_hangout2_knife_aftermath
label frisk_frienship_hangout2_choice14:
    #/// If >14(Back away)<
    frisk "I’m so sorry…"
    #####show frisk panicking
    show frisk sad
    frisk "I’m not like this, I swear!"
    frisk "It’s going away, honest!"
    frisk "I just- I can’t-"
    frisk "..."
    #sound of a metal clang as the knife falls to the floor
    jump frisk_friendship_hangout2_knife_aftermath
label frisk_frienship_hangout2_choice15:
    #/// If >15(Try to grab the knife away from Frisk)<
    frisk "...!"
    "*You pry the knife from their hands, and it falls to the floor."
    #sound of a metal clang as the knife falls to the floor
    frisk "Huh?"
    jump frisk_friendship_hangout2_knife_aftermath
label frisk_frienship_hangout2_choice16:
    #/// If >16("It’s okay, let’s just wait it out.")<
    frisk "Yeah… Okay…"
    frisk "..."
    frisk "I think it’s going away…"
    #sound of a metal clang as the knife falls to the floor
    jump frisk_friendship_hangout2_knife_aftermath
label frisk_friendship_hangout2_knife_aftermath:
    stop music
    play music "audio/music/music-home.mp3"
    #####show frisk disgusted
    show frisk annoyed
    frisk "Oh no… I’m so sorry!"
    show frisk disappointed
    frisk "But it’s fine… It’s fine. I’m feeling better now."
    if frisk_frienship_hangout2_option[13]:
        #if frisk_frienship_hangout2_option 13 was chosen:
        frisk "I’m sorry you had to see that…"
    elif frisk_frienship_hangout2_option[14]:
        #if frisk_frienship_hangout2_option 14 was chosen:
        frisk "I’m so sorry… I scared you, didn’t I?"
    elif frisk_frienship_hangout2_option[15]:
        #if frisk_frienship_hangout2_option 15 was chosen:
        frisk "If you hadn’t grabbed the knife from me, I…"
        frisk "I don’t know what would’ve happened."
    elif frisk_frienship_hangout2_option[16]:
        #if frisk_frienship_hangout2_option 16 was chosen:
        frisk "Thank you for waiting with me… That was exactly what I needed."
        #All branches converge at frisk_frienship_hangout2_selection 6
    jump frisk_frienship_hangout2_selection6
label frisk_frienship_hangout2_selection6:
    menu:
        "Are you sure you’re alright?":            ##//(+2)
            $ frisk_fp+=2
            $ frisk_frienship_hangout2_option[17]=True
        "You need to tell me what’s going on.":        ##//(+0)
            $ frisk_frienship_hangout2_option[18] = True
    if frisk_frienship_hangout2_option[17]:
        #/// If >17("Are you sure you’re alright?")<
        frisk "Yeah, I’m fine… Really."
        show frisk sad
        frisk "Look…"
    elif frisk_frienship_hangout2_option[18]:
        #/// If >18("You need to tell me what’s going on.")<
        show frisk sad
        frisk "...You’re right."

    frisk "I could’ve hurt you, and I’d never forgive myself if I did that."
    frisk "I really shouldn’t have tried to act like this was nothing."
    frisk "I just don’t want other people to be burdened with my own problems."
    frisk "We can talk more about this, but…"
    frisk "Tomorrow. Please."
    frisk "I need some time to think. Come and find me in my room tomorrow."
    hide frisk
    #Good end

label frisk_friendship_hangout2_visit_frisk_same_day:
    show background frisk_room
    #if the player goes to Frisk’s room later the same day
    if visited_frisk==0:
        #1st time:
        show frisk sad
        frisk "I know this is probably all so strange to you…"
        frisk "But, please… I need some time to myself."
    elif visited_frisk==1:
        #2nd time
        show frisk sad
        frisk "I know you wanna help, but I need some space."
        frisk "We can talk tomorrow."
    elif visited_frisk==2:
        #3rd time
        show frisk sad
        frisk "I’m being sincere. Please, just go."
    elif visited_frisk==3:
        #4th time
        show frisk sad
        frisk "…"
        frisk "Don’t you have anything better to do?"
    elif visited_frisk==4:
        #5th time
        show frisk sad
        frisk "…"
    elif visited_frisk==5:
        #6th time
        show frisk annoyed
        frisk "…"
    elif visited_frisk==6:
        #7th time
        ##//(-4)
        show frisk angry
        frisk "I said go away!"
    else:
        hide frisk
        "#Frisk’s room is now locked if the player tries to enter again before the next day"
    $ visited_frisk+=1
    jump frisk_friendship_hangout2_menu
