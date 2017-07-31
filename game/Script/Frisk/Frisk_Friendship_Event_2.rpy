
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
    
label frisk_friendship_hangout2(owner=get_frisk()):
    

    $ player.variables['frisk_friend_hangout2_day'] = world.day

    show frisk tinysmile with Dissolve(.25)
    frisk "Hey, I’m glad you’re here."
    frisk "Could you help me with the dishes, please?"
    menu:
        "No way.":
            $get_monster('Frisk').update_FP(-1)
            frisk "Aw, okay... I get it."
            frisk "You’re probably busy, so I guess I’ll see you later."
            hide frisk with Dissolve(.25)
            $ move_to_room("Living Room")
            return
        "Yeah, sure.":
            $ get_monster('Frisk').update_FP(2)
            show frisk tinysmile with Dissolve(.25)
            frisk "Great! There’s a stack of plates over there. If you could scrub those, that’d be super helpful!"
            show frisk normal with Dissolve(.25)
            "* Frisk turns and gets back to work."
            "* You grab a few plates and start scrubbing."
            "* ..."
            frisk "So... How’ve you been doing?"
            menu:
                "Can we talk about what happened the other day?":
                    $get_monster('Frisk').update_FP(-1)
                    frisk "..."
                    frisk "Do we have to?"
                    frisk "Look, I-"
                    frisk "..."
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
                            frisk "I keep telling her not to be concerned..."
                            frisk "I really don’t like to worry her."
                        "Alright, I’ll stop asking.": 
                            $get_monster('Frisk').update_FP(2)
                            frisk "Thanks..."
                            frisk "It’s just something I have to deal with on my own."
                        "(Say nothing)": 
                            $get_monster('Frisk').update_FP(1)
                            frisk "..."
                            frisk "Just don’t worry about me."
                            frisk "I guess it can be a little much, and there’s something about this thing that feels really personal."
                            frisk "Like I’m not supposed to talk about it."
                "Fine. You?":##//(+1)
                    $get_monster('Frisk').update_FP(1)
                    frisk "That’s good. I’ve been fine, too."
                    frisk "But, uhm..."
                    frisk "Well, you know."
                    frisk "I was certain you were going to try and get me to talk about it..."
                    frisk "Thanks for understanding."
                    frisk "It’s just one of those things I need to work out on my own, y’know?"
                    frisk "Whatever it is. I’m still not sure myself."
                    show frisk disappointed with Dissolve(.25)
                    frisk "..."
                    frisk "And it can be a little overwhelming."
                    frisk "But it’s something I can handle, really it is."
            
    show frisk normal with Dissolve(.25)
    "* Frisk picks up a knife and starts cleaning it."
    frisk "I’ll figure it out, just like I always do..."
    show frisk distant with Dissolve(.25)
    frisk "..."
    "* They’re staring at the knife in their hands."
    frisk "..."
    frisk "I don’t feel so good."
    menu:
        "Are you okay?":                    
            frisk "I uh..."
            frisk "I’m fine. Really."
        "Is it happening again?":          
            frisk "W-what? No, it’s just..."
        "Put down the knife!":              
            frisk "Oh... I-I’m sorry..."
            frisk "I just..."
            frisk "I can’t."

    frisk "..."
    menu:
        "Should I get Toriel?":             
            frisk "N-no, I can handle this."
            frisk "..."
            frisk "It’s going away."
            frisk "..."
            #sound of a metal clang as the knife falls to the floor
            show frisk disgusted with Dissolve(.25)
            frisk "Oh no... I’m so sorry!"
            show frisk disappointed with Dissolve(.25)
            frisk "But it’s fine... It’s fine. I’m feeling better now."
            frisk "I’m sorry you had to see that..."

        "(Back away)":                    
            $get_monster('Frisk').update_FP(3)
            frisk "I’m so sorry..."
            show frisk panicking with Dissolve(.25)
            frisk "I’m not like this, I swear!"
            frisk "It’s going away, honest!"
            frisk "I just- I can’t-"
            frisk "..."
            #sound of a metal clang as the knife falls to the floor
            show frisk disgusted with Dissolve(.25)
            frisk "Oh no... I’m so sorry!"
            show frisk disappointed with Dissolve(.25)
            frisk "But it’s fine... It’s fine. I’m feeling better now."
            frisk "I’m so sorry... I scared you, didn’t I?"

        "(Try to grab the knife away from Frisk)":# if bravery>=2:      
            frisk "...!"
            "* You pry the knife from their hands, and it falls to the floor."
            #sound of a metal clang as the knife falls to the floor
            frisk "Huh?"
            show frisk disgusted with Dissolve(.25)
            frisk "Oh no... I’m so sorry!"
            show frisk disappointed with Dissolve(.25)
            frisk "But it’s fine... It’s fine. I’m feeling better now."
            frisk "If you hadn’t grabbed the knife from me, I..."
            frisk "I don’t know what would’ve happened."

        "It’s okay, let’s just wait it out.":# if patience>=2:       
            $get_monster('Frisk').update_FP(4)
            frisk "Yeah... Okay..."
            frisk "..."
            frisk "I think it’s going away..."
            #sound of a metal clang as the knife falls to the floor
            show frisk disgusted with Dissolve(.25)
            frisk "Oh no... I’m so sorry!"
            show frisk disappointed with Dissolve(.25)
            frisk "But it’s fine... It’s fine. I’m feeling better now."
            frisk "Thank you for waiting with me... That was exactly what I needed."
        

    menu:
        "Are you sure you’re alright?":         
            $get_monster('Frisk').update_FP(2)
            frisk "Yeah, I’m fine... Really."
            show frisk sad with Dissolve(.25)
            frisk "Look..."
        "You need to tell me what’s going on.":     
            show frisk sad with Dissolve(.25)
            frisk "...You’re right."        

    frisk "I could’ve hurt you, and I’d never forgive myself if I did that."
    frisk "I really shouldn’t have tried to act like this was nothing."
    frisk "I just don’t want other people to be burdened with my own problems."
    frisk "We can talk more about this, but..."
    frisk "Tomorrow. Please."
    frisk "I need some time to think. Come and find me in my room tomorrow."
    hide frisk
    $ player.variables['frisk_friendship_2_Complete'] = True
    $ move_to_room("Living Room")
    return

label frisk_friendship_hangout2_visit_frisk_same_day:
    #added this logic to the room select for Corridor 'toriel_rooms.rpy'
    #if the player goes to Frisk’s room later the same day
    if 'frisk_f2_visit_count' not in player.variables or ('frisk_f2_visit_day' not in player.variables or world.day != player.variables['frisk_f2_visit_day']):
        $ player.variables['frisk_f2_visit_count'] = 0
        $ player.variables['frisk_f2_visit_day'] = world.day
    if player.variables['frisk_f2_visit_count']==0:
        #1st time:
        show frisk sad with Dissolve(.25)
        frisk "I know this is probably all so strange to you..."
        frisk "But, please... I need some time to myself."
    elif player.variables['frisk_f2_visit_count']==1:
        #2nd time
        show frisk sad with Dissolve(.25)
        frisk "I know you wanna help, but I need some space."
        frisk "We can talk tomorrow."
    elif player.variables['frisk_f2_visit_count']==2:
        #3rd time
        show frisk sad with Dissolve(.25)
        frisk "I’m being sincere. Please, just go."
    elif player.variables['frisk_f2_visit_count']==3:
        #4th time
        show frisk sad with Dissolve(.25)
        frisk "..."
        frisk "Don’t you have anything better to do?"
    elif player.variables['frisk_f2_visit_count']==4:
        #5th time
        show frisk sad with Dissolve(.25)
        frisk "..."
    elif player.variables['frisk_f2_visit_count']==5:
        #6th time
        show frisk annoyed with Dissolve(.25)
        frisk "..."
    elif player.variables['frisk_f2_visit_count']==6:
        #7th time
        $get_monster('Frisk').update_FP(-4)
        show frisk angry with Dissolve(.25)
        frisk "I said go away!"
    else:
        pass
        #Frisk’s room is now locked if the player tries to enter again before the next day
    $ player.variables['frisk_f2_visit_count']+=1
    $ move_to_room("Corridor",transition=None)
    return
