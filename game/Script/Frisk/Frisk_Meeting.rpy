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
        chose_frisk_meeting_option72 = False
    python:
        chose_frisk_meeting_option6 = False
        accepted_toriel_invitation = True
        met_frisk_before_toriel = True
        toriel_fp = 0 #temp var
    #looked_around_before_toriel = True
    #red numbers indicates HB points
    show frisk surprised with Dissolve(.25)
    
    unknown "Oh! Um, hi. I wasn’t expecting to see another human. How... how did you get here?" 
    jump frisk_meeting_menu
label frisk_meeting_menu:
    menu:
        "Meeting":
            jump frisk_meeting_selection1
        "Questions":
            jump frisk_meeting_questions
        "Snail Catching":
            jump frisk_meeting_snail_catching
        "Frisk Meeting Late":
            jump frisk_meeting_late

        "Look Around Before Meeting Toriel":
            jump looked_around_before_toriel
        "Ruins Intro Pass Out":
            jump ruins_intro_pass_out

        "Exit":
            jump statcheck
        "Change Past Events":
            jump frisk_meeting_change_vars

label frisk_meeting_change_vars:
    menu:
        "Accepted Toriel Invitation":
            $ accepted_toriel_invitation = True
            jump frisk_meeting_menu
        "Rejected Toriel Invitation/Haven't Met Toriel":
            $ accepted_toriel_invitation = False
            jump frisk_meeting_menu
        "Met Frisk Before Toriel":
            $ met_frisk_before_toriel = True
            jump frisk_meeting_menu
        "Met Toriel Before Frisk":
            $ met_frisk_before_toriel = False
            jump frisk_meeting_menu

#########################
#  FRISK MEETING START  #
#########################

label frisk_meeting_selection1:
    menu:
        "I could ask you the same thing.":  
            jump frisk_meeting_choice1
        "I tripped.":
            $world.get_monster('Frisk').update_FP(3)
            jump frisk_meeting_choice2
        "You’re not Toriel’s kid, are you?" if met_frisk_before_toriel==False:
            $world.get_monster('Frisk').update_HB(2)
            jump frisk_meeting_choice3
        "Hi, nice to meet you!":
            $world.get_monster('Frisk').update_FP(4)
            jump frisk_meeting_choice4

label frisk_meeting_choice1:         
    show frisk smallsmile with Dissolve(.25)
    unknown "Oh, well, you know... I guess I was hiking, and I just... sort of..."
    show frisk surprised with Dissolve(.25)
    unknown "Oh! I’m sorry, I forgot my manners."
    show frisk somehappy with Dissolve(.25)
    unknown "I’m Frisk. It’s nice to meet you!"
    frisk "I’m a human, too!"
    frisk "But, um, I guess you could probably see that."
    jump frisk_meeting_selection2

label frisk_meeting_selection2:
    menu:
        "Are there more humans down here?":  
            $world.get_monster('Frisk').update_FP(1)
            jump frisk_meeting_choice5
        "And you live with a monster?":    
            jump frisk_meeting_choice6

label frisk_meeting_choice5:               
    show frisk normal with Dissolve(.25)
    frisk "Oh, no... not that I know of."
    frisk "You’re actually the first human I’ve seen since I fell down here."
    frisk "I’ve been living here with Mom- I mean, you probably know her as Toriel."
    show frisk somehappy with Dissolve(.25)
    frisk "She’s taken care of me since I was a kid!"
    jump frisk_meeting_questions

label frisk_meeting_choice6:     
    show frisk normal with Dissolve(.25)
    frisk "Yeah. When I came to the Underground, Mom... I mean, Toriel... found me and has been taking care of me ever since."
    jump frisk_meeting_questions

label frisk_meeting_choice2:     
    show frisk giggly with Dissolve(.25)
    unknown "Ha ha! You're funny.  No one just 'trips' and ends up down here."
    
    ######DOUBLE CHECK THIS
    "show frisk slightly happy << sprite check, currently using smallsmile -P"
    show frisk smallsmile with Dissolve(.25)
    unknown "..."
    unknown "At least, no one that I know."
    show frisk somehappy with Dissolve(.25)
    unknown "Oh, where are my manners... my name is Frisk!"
    jump frisk_meeting_questions

label frisk_meeting_choice3:
    show frisk annoyed with Dissolve(.25)
    unknown "Yes I am!"
    show frisk disappointed with Dissolve(.25)
    unknown "Oh, right. You were probably expecting me to be a monster, huh?"
    show frisk normal with Dissolve(.25)
    unknown "My name is Frisk."
    frisk "I’m a human. Mom- well, you know her as Toriel..."
    frisk "She’s really nice, and she takes care of me."
    jump frisk_meeting_questions

label frisk_meeting_choice4:
    show frisk surprised with Dissolve(.25)
    unknown "Oh! Right, where are my manners... my name is Frisk!"
    show frisk smallsmile with Dissolve(.25)
    frisk "It’s nice to meet you, too. I, uh... hope you grow to like the Underground."
    frisk "It's pretty great once you get used to it."
    jump frisk_meeting_questions
    

#############################
#  FRISK MEETING QUESTIONS  #
#############################

label frisk_meeting_questions:
    menu:
        "Continue":
            jump frisk_meeting_selection3
        "Beginning":
            jump frisk_meeting_start
        "Exit":
            jump statcheck

label frisk_meeting_selection3:
    menu:
        "You’re actually a human? Not some monster?" if chose_frisk_meeting_option6 == False:
            jump frisk_meeting_choice6_5
        
        "I’ve recently met Toriel. She seems nice." if met_frisk_before_toriel==False:
            $world.get_monster('Frisk').update_FP(3)
            jump frisk_meeting_choice7
        "How’s life here in the Ruins?":
            $world.get_monster('Frisk').update_FP(3)
            jump frisk_meeting_choice8       

label frisk_meeting_choice6_5:         
    show frisk somehappy
    frisk "Yeah! I live with my mom- I mean, Toriel, the caretaker of the Ruins. She’s really kind. Have you met her?"
    #remove option 6 from selection 3
    $ chose_frisk_meeting_option6 = True
    jump frisk_meeting_questions

label frisk_meeting_choice7:     
    show frisk bigsmile
    frisk "Yeah! Out of all the people that could’ve found me, I’m glad it was her."
    jump frisk_meeting_selection4 

label frisk_meeting_selection4:
    menu:
        "Are you saying the other monsters are bad?":
            $world.get_monster('Frisk').update_HB(1)            
            jump frisk_meeting_choice10
        "I can relate. She helped me, too." if met_frisk_before_toriel==False:
            $world.get_monster('Frisk').update_FP(2)
            jump frisk_meeting_choice11

label frisk_meeting_choice10:         
    show frisk surprised
    frisk "What? No!"
    show frisk upset
    frisk "I mean, other monsters are great, too. I shouldn't have said that... it was mean. But she’s the only one who’s really taken care of me, y’know?"
    jump frisk_meeting_snail_catching

label frisk_meeting_choice11:      
    show frisk smallsmile
    frisk "That’s great! She can handle anything!"
    show frisk upset
    frisk "..."
    show frisk somehappy
    frisk "Well, most things."
    jump frisk_meeting_snail_catching

label frisk_meeting_choice8:     
    show frisk somehappy
    frisk "Well, we don’t have much, but it’s nice. It’s just that sometimes Mom makes food with snails in it, and it’s..."
    show frisk upset
    frisk "...not amazing... but don’t worry about it."
    show frisk somehappy
    frisk "Other than that, things are pretty great."
    jump frisk_meeting_selection5 

label frisk_meeting_selection5:
    menu:
        "Are you feeling okay? You look a little under the weather.":
            $world.get_monster('Frisk').update_FP(3)
            jump frisk_meeting_choice12
        "I’m sure everything must be great for you then!":
            jump frisk_meeting_choice13

label frisk_meeting_choice12:         
    frisk "Oh, um. I’m... I’m fine."
    frisk "Tiring day, ya know?"
    frisk "But... I appreciate your concern."
    jump frisk_meeting_selection6 

label frisk_meeting_selection6:
    menu:
        "Are you sure you’re okay? Do you want to talk about something?":
            $world.get_monster('Frisk').update_FP(1)
            jump frisk_meeting_choice14
        "...":
            jump frisk_meeting_choice15

label frisk_meeting_choice14:         
    frisk "No, really... it’s fine. I appreciate the help... I really do. But, honestly, it’s nothing."
    jump frisk_meeting_selection7
     
label frisk_meeting_selection7:
    menu:
        "Oh, come on, tell me!":
            $world.get_monster('Frisk').update_HB(2)
            jump frisk_meeting_choice16
        "Just making sure.":
            $world.get_monster('Frisk').update_FP(2)
            jump frisk_meeting_choice17

label frisk_meeting_choice16:
    show frisk annoyed
    frisk "Please, you're making this more than what it is."
    jump frisk_meeting_selection8

label frisk_meeting_selection8:
    menu:
        "You have to tell me!":
            $world.get_monster('Frisk').update_FP(-3)
            jump frisk_meeting_choice18
        "Alright, I’m sorry.":
            jump frisk_meeting_choice19

label frisk_meeting_choice18:
    #+1 Determination
    show frisk angry
    frisk "No, I don’t have to tell you anything! I’m not talking about this anymore!"
    show frisk neutral
    frisk "Sorry, I don’t like people getting on my back about things."
    jump frisk_meeting_snail_catching

label frisk_meeting_choice19:
    show frisk annoyed
    frisk "..."
    frisk "...Thank you."
    jump frisk_meeting_snail_catching

label frisk_meeting_choice17:
    frisk "Thanks. You remind me a lot of Mom, actually." 
    show frisk bigsmile
    frisk "But... don’t go thinking you can outdo her in the mothering department! She’s the master!"
    jump frisk_meeting_snail_catching

label frisk_meeting_choice15:     
    jump frisk_meeting_snail_catching

label frisk_meeting_choice13:     
    frisk "Yup... pretty much."
    jump frisk_meeting_snail_catching

##################################
#  FRISK MEETING SNAIL CATCHING  #
##################################

label frisk_meeting_snail_catching:
    menu:
        "Continue":
            pass
        "Beginning":
            jump frisk_meeting_start
        "Exit":
            jump statcheck
    show frisk normal
    frisk "Oh, hey... is that a crack on your phone? It looks pretty banged up."
    show frisk smallsmile
    frisk "Here, you can take my old phone! My friend made me a new one, so I don’t mind."
    frisk "And I’ve already transferred all of my old junk off of it, so it’s just like new."
    frisk "Oh, and I’ll add my number into it! That way, if you ever need to get in touch with me, I’ll just be a phone call away!"
    ################################
    "* Frisk’s number obtained."
    ###############################
    frisk "So..."
    show frisk surprised
    frisk "Oh wait, I almost forgot!"
    show frisk somehappy
    frisk "I’m actually supposed to be doing something important..."
    frisk "I need your help. It won’t take long, I promise."
    frisk "Just follow me!"
     
    #-Transition to Snail Catching Room-
    #-Transition: Snail Catching Mini-game-
     
    show frisk normal
    frisk "Okay, here we are."
    frisk "I know this is going to sound a bit weird, but I need to catch snails."
    frisk "Mom makes food with them, and she needs a lot!"
    jump frisk_meeting_selection9

label frisk_meeting_selection9:
    menu:
        "You’re right, that is weird.":
            $world.get_monster('Frisk').update_HB(1)
            jump frisk_meeting_choice20
        "That sounds completely reasonable.":
            $world.get_monster('Frisk').update_FP(3)
            jump frisk_meeting_choice21
        "Oh yeah, Toriel already told me." if accepted_toriel_invitation == True:
            $world.get_monster('Frisk').update_FP(4)
            jump frisk_meeting_choice61
        #option 61 only available if the player went to Toriel’s house before meeting frisk AND at some point accepted her invitation to stay at her house

label frisk_meeting_choice20:         
    #-1 Patience
    frisk "Well, what can I say?" 
    frisk "But seriously, this is important. I’ll need your help."
    frisk "Catching snails is harder than you’d think."
    jump frisk_meeting_selection10

label frisk_meeting_choice21:     
    frisk "Really, you think so?"
    jump frisk_meeting_selection10

label frisk_meeting_selection10:
    menu:
        "Yeah, I do it all the time!":  
            $world.get_monster('Frisk').update_FP(3)
            jump frisk_meeting_choice22
        "I lied. That makes no sense whatsoever.":
            $world.get_monster('Frisk').update_FP(-5)
            jump frisk_meeting_choice23

label frisk_meeting_choice22:     
    show frisk bigsmile
    frisk "That’s great! This’ll be easy!"
    jump frisk_snail_minigame

label frisk_meeting_choice23:     
    #-1 Integrity
    show frisk upset
    frisk "Oh... okay."
    frisk "Well- please, I really do need your help. Even if it doesn’t make sense to you."
    jump frisk_snail_minigame 

label frisk_meeting_choice61:     
    show frisk bigsmile
    frisk "Nice!"
    frisk "Mom has a lot of different snail dishes. You wouldn’t believe what she can do with them!"
    frisk "Anyway..."
    jump frisk_snail_minigame

label frisk_snail_minigame:
    show frisk normal
    frisk "Here’s what I need you to do..."
    frisk "First, here, take this net."
    #player acquires net, which cannot be removed or dropped yet
     
    #/// if Check Butterfly Net
    "*It’s a big butterfly net, good for catching snails. << if Check Butterfly Net"
     
    frisk "Basically, just try to catch as many snails as you can!"
    frisk "It’s tricky, though, because you can only try to catch them for a certain amount of time per day. After that, they’ll start to get suspicious and won’t come out of their hiding places."
    frisk "Ready? Here we go!"
     
    #Snail Minigame happens
     
    show frisk smallsmile
    frisk "Ya know, I’m actually feeling a bit better right now."
    frisk "Mom will be happy, too... She really likes snails!"
    frisk "If you give her some, she’ll appreciate it. Maybe even pay you back somehow."
    frisk "She might want different kinds of snails on different days, so you might want to check with her to find out."
    
    show frisk surprised
    frisk "Oh!"
    
    show frisk bigsmile
    frisk "And if you want to do this again sometime, just tell me. This was fun!"
    frisk "...Or you could do it on your own, whatever works! Help in any form is appreciated!"
    
    show frisk normal
    frisk "I, uh, I should get going now. Mom is probably wondering why I’m out so late..."
    frisk "Our house isn’t too far from here. Do you want to come with me?"
    frisk "Mom and I would love it if you stayed for awhile..."
    jump frisk_meeting_selection11

label frisk_meeting_selection11:
    menu:
        "Yeah, I’m in!":
            $world.get_monster('Frisk').update_FP(3)
            jump frisk_meeting_choice24
        "I’ll be there soon, but I think I’m gonna look around the Ruins for a little while longer.":
            $world.get_monster('Frisk').update_FP(3)
            jump frisk_meeting_choice25
        "I don’t want to stay with you guys." if accepted_toriel_invitation==False:
            $world.get_monster('Frisk').update_FP(-4)
            jump frisk_meeting_choice62

        #option 62 only available if the player has refused Toriel’s offers to stay (has NOT picked ruins outline option 56 OR ruins outline option 77)

label frisk_meeting_choice24:
    show frisk bigsmile
    frisk "Alright, let’s go!"
    #scene change to frisk and Toriel’s house
    show frisk smallsmile
    frisk "Here we are!"
    show frisk normal
    frisk "Hold on... let me tell Mom we’re back."
    hide frisk
    jump frisk_meeting_home

label frisk_meeting_choice25:
    frisk "Alright, that’s fine. I’ll see ya there!"
    frisk "Just be sure not to stay out too late. If you don’t get enough sleep, you could get sick."
    show frisk bigsmile
    frisk "I’m starting to sound like Mom now. Oh well... see ya!"
    #frisk leaves. Player is free to roam. 
    #If the player returns to Toriel’s house before running out of stamina, jump frisk_meeting_late
    #If the player does not return to Toriel’s house before running out of stamina, jump ruins_intro_pass_out
    jump frisk_meeting_start

label frisk_meeting_choice62:     
    show frisk disappointed
    frisk "Oh... okay. I just thought..."
    show frisk somehappy
    frisk "Well, if you ever change your mind, just stop on by our house! Mom and I love having guests."
    frisk "See ya later!"
    #frisk leaves. Player is free to roam.
    #If the player returns to Toriel’s house before running out of stamina, jump ruins_intro_toriel_house (located in the ruins outline)
    #If the player does not return to Toriel’s house and accept her offer before running out of stamina, jump ruins_intro_pass_out (located in the ruins outline)
    jump frisk_meeting_start 
     
label frisk_meeting_late:
    #frisk off-screen
    hide frisk
    frisk "Oh, I think they’re here. I’ll be right back!"
    show frisk normal
    frisk "Hi! You’re a bit late... the food is a little cold. But I’m sure it’s fine. Hold on, let me tell Mom you’re here."
    #frisk off-screen again
    hide frisk
    jump frisk_meeting_home

########################
#  FRISK MEETING HOME  #
########################

label frisk_meeting_home:
    menu:
        "Continue":
            pass
        "Beginning":
            jump frisk_meeting_start
        "Exit":
            jump statcheck
###################################
#### Doublecheck this part!!!!!!!
###################################
    show frisk normal at left
    show toriel normal at right
    frisk "This is the person I told you about."
    if met_frisk_before_toriel == True:
        #If the player found frisk BEFORE going to Toriel’s house:
        toriel "Ah, hello! It is very nice to have you over for dinner." 
        toriel "I do apologize for having to rush off so quickly before. Truthfully, I was a little worried about having to leave you on your own in the Ruins, but it is good to see that you are well."
        show frisk bigsmile
        frisk "Anyway, let’s eat!"
        toriel "Yes, please join us."
        jump frisk_meeting_eat
    elif met_frisk_before_toriel == False:
        #If the player went to Toriel’s house BEFORE finding frisk:
        toriel "Welcome back! I am glad you and Frisk managed to find each other."
        show frisk bigsmile
        frisk "Anyway, let’s eat!"
        toriel "Yes, please join us."
        jump frisk_meeting_eat

label looked_around_before_toriel:
        #If the player chose option 25 of selection 11 (look around the Ruins for a little while longer) (if not, just skip this part)
        toriel "Frisk has told me a lot about you while you were gone." 

        show toriel normal
        if toriel_fp<20:
            toriel "There is not much to do here, but we are always looking for a helping hand--especially if you do not mind getting your hands dirty."
            show frisk bigsmile
            frisk "Anyway, let’s eat!"
            toriel "Yes, please join us."
            jump frisk_meeting_eat
        else:
            #/// If >(FP >20) - good rating            Toriel#//(+3)
            $world.get_monster('Toriel').update_FP(3)
            show toriel smile
            toriel "It makes me happy to see you and frisk have become such fast friends. It gets a little lonely here in the Ruins sometimes, and we do appreciate any well-meaning company." 
            toriel "I am sure you know this by now, but I would like you to know that any friend of frisk is welcome here."
            show frisk bigsmile
            frisk "Anyway, let’s eat!"
            toriel "Yes, please join us."
            jump frisk_meeting_eat
             
#######################
#  FRISK MEETING EAT  #
#######################

label frisk_meeting_eat:
    #scene change living room
    show frisk normal with Dissolve(.25) at right
    show toriel normal with Dissolve(.25) at left
    frisk "I’m sure you’ll love it. We’re eating..."
    frisk "Mom, what’re we having again?"
    toriel "We are having snail casserole."
    show frisk somehappy
    frisk "Oh, good..."
    toriel "Is there something wrong?"
    frisk "Of course not. Hey, snail-catching friend, why don’t you try some?"
    "*You take a bite."
    "*..."
    "*It tastes..."
    "*...interesting."
    frisk "So, how is it?"
    toriel "Please, do tell."
     
label frisk_meeting_selection12:
    menu:
        "It’s great, I love it!":           #Toriel#//(+2)
                                        #frisk#//(+2)
            $world.get_monster('Frisk').update_FP(2)
            $world.get_monster('Frisk').update_FP(2)
            jump frisk_meeting_choice25_5
        "It’s not bad.":                       #//(+0)
            jump frisk_meeting_choice26
        "It’s kinda... bad.":               #Toriel#//(-2)
                                        #frisk#//(-2)
            $chose_frisk_meeting_option27=True
            $world.get_monster('Frisk').update_FP(-2)
            $world.get_monster('Frisk').update_FP(-2)
            jump frisk_meeting_choice27

label frisk_meeting_choice25_5:         
    #+1 Kindness
    show frisk surprised
    frisk "Really?"
    show frisk somehappy
    frisk "I mean, of course! I knew you would."
    toriel "Frisk, is there a problem with my cooking?"
    frisk "Never. Snails are great!"
    toriel "Oh, naturally. Either way, I am glad our guest seems to be enjoying them."

label frisk_meeting_choice26:     
    show frisk normal
    frisk "See, I knew you would like it."
    toriel "Well, I try."

label frisk_meeting_choice27:     
    #-1 Kindness
    show frisk disappointed
    frisk "Shhh, don’t say that."
    show toriel annoyed
    toriel "Ah, well I suppose snails are not everyone's cup of tea. Still, they are the only thing around here that will fill you up. So, if you decide to stay, you will just have to get used to them."     
    show frisk somehappy
    frisk "...So, um... how have you been liking the Ruins so far?"

label frisk_meeting_selection13:
    menu:
        "I think I like it better here than the surface!":   #//(+0)
            jump frisk_meeting_choice28
        "I don’t think I like this place.":           #//(+0)
            jump frisk_meeting_choice29
        "I hate this place.":               #Toriel#//(+2)
                                       # frisk#//(+4)
            $ chose_frisk_meeting_option30=True
            $world.get_monster('Toriel').update_FP(-2)
            $world.get_monster('Frisk').update_FP(-4)
            jump frisk_meeting_choice30
        "It scares me...":                   #Toriel#//(+2)
                                        #frisk#//(+2)
            $world.get_monster('Toriel').update_FP(2)
            $world.get_monster('Frisk').update_FP(2)                                        
            jump frisk_meeting_choice31

label frisk_meeting_choice28:         
    #/// If >28("I think I like it better than the surface!":<
    show frisk surprised
    show toriel surprised
    frisk "D-do you really mean that?"
    #if the player chose option 27 of selection 12 (if not, skip this line and go right to selection 14)
    if chose_frisk_meeting_option27==True:
        toriel "Even though you did not like the cooking?"
    jump frisk_meeting_selection14        
label frisk_meeting_selection14:
    menu:
        "Yeah!":                   #Toriel#//(+4)
                                    #frisk#//(+4)
            $world.get_monster('Toriel').update_FP(4)
            $world.get_monster('Frisk').update_FP(4)
            jump frisk_meeting_choice32
        "Actually no, I just didn’t want to be rude.":
                                    #Toriel#//(-2)
                                    #frisk#//(-3)
            $world.get_monster('Toriel').update_FP(-2)
            $world.get_monster('Frisk').update_FP(-3)
            jump frisk_meeting_choice33

label frisk_meeting_choice32:         
    #+1 Integrity
    show frisk bigsmile
    show toriel smile
    frisk "That’s great!"
    toriel "Oh, well I’m glad you are enjoying your stay!"
label frisk_meeting_choice33:      
    #-1 Integrity
    show toriel sad
    show frisk sad
    frisk "Oh... what?"
    toriel "I guess I should not be too surprised."
    show Toriel smallsmile
    toriel "Well... erm... thank you for your consideration."
    show frisk somehappy
    frisk "Oh come on. It isn’t that bad, right?"

label frisk_meeting_choice29:      
    show toriel normal
    toriel "Oh, I know things may be difficult for you at first. This must be very different from what you were used to on the surface, after all. Still, I do encourage you to give it a chance."
    show frisk bigsmile
    frisk "Yeah! It’s actually pretty great once you get used to everything!"

label frisk_meeting_choice30:      
    show frisk sad
    frisk "Aw, but... it’s not that bad, really."
    show toriel awkward
    toriel "I understand that this place may not be to your liking." 
    show toriel smallsmile
    toriel "But I think that, with a bit of time, you will learn to tolerate it."
    show frisk smallsmile
    frisk "R-right! It’s not so bad!"

label frisk_meeting_choice31:      
    #-1 Bravery
    show toriel smallsmile
    toriel "Aww, poor thing. I had not realized until now that this must all seem very jarring."
    show frisk sad
    frisk "Oh, yeah."
    frisk "To be honest, when I first fell down here, I didn’t take it very well."
    show frisk sad
    frisk "When people tried to help, I shoved them away and ran..."
    show frisk tearyeyes
    frisk "I even tried to run away from Mom. I thought she wanted to hurt me..."
    show toriel normal
    toriel "frisk, please. Remember, I do not blame you for any of that. You were afraid, and I understand maybe I was being a bit... erm..."
    show toriel awkward
    toriel "...clingy, which you could have easily found threatening."
    show toriel smallsmile
    toriel "Besides, you are here now, and everything turned out alright."
    show frisk somehappy
    frisk "Yeah..."
    show frisk friendly smile
    frisk "So, the point is... I know this might be scary for now. But, if you give it a chance, I think you’ll find this place is actually pretty great."
    frisk "I mean it!"
    toriel "And we will be here to help you if you need anything."
     
    show frisk normal
    frisk "Well, whatever you think, you're always welcome here."
    show toriel smallsmile
    toriel "Of course. It would be impolite to kick a guest out, especially if they have nowhere else to go. However, I must ask that you contribute to gathering food--specifically, snails--everyday."
    if chose_frisk_meeting_option27==True or chose_frisk_meeting_option30==True:
        #if the player has chosen option 27 or option 30 (if not, skip this line):
        toriel "And as long as you work on your manners..."
     
    toriel "Now please, have some more food. It is good for you." 
    toriel "Even though some people... may not find it to their taste."
    show frisk somehappy with Dissolve(.25)
    frisk "W-what are you looking at me for? I love all of your cooking!"
    show toriel laughing with Dissolve(.25)
    toriel "Oh, it is alright, my child. I know snails are not your favorite dish."
    show frisk  with Dissolve(.25)
    frisk "..."
    frisk "How long have you known?"
    toriel "A mother can always tell what her child is really thinking, but I do appreciate the sentiment."
    show frisk somehappy with Dissolve(.25)
    frisk "Oh..."
    frisk "Actually, is it okay if I turn in early? I feel a little tired."
    show toriel sad with Dissolve(.25)
    toriel "But you have hardly eaten anything."
    toriel "..."
    show toriel normal with Dissolve(.25)
    toriel "Oh, alright. After all, it is important that you get your rest."
    show frisk smallsmile with Dissolve(.25)
    frisk "Thanks, Mom."
    #frisk exits the scene
    hide frisk with Dissolve(.25)
    hide toriel with Dissolve(.25)
    show toriel normal with Dissolve(.25)
    toriel "As for you, eat at least one more bite before you go."
    jump frisk_meeting_selection15
     
label frisk_meeting_selection15:
    menu:
        "No problem. I’ll even eat two bites!":       #//(+3)
            $world.get_monster('Toriel').update_FP(3)

            jump frisk_meeting_choice34 

        "Fair enough.":                       #//(+0)
            jump frisk_meeting_choice35 
        "But...":                           #//(+1)
            $world.get_monster('Toriel').update_FP(1)
            jump frisk_meeting_choice36 
label frisk_meeting_choice34:          
    #+1 Perseverance
    show toriel smile with Dissolve(.25)
    toriel "That’s the spirit."
    "*You take another bite."
    "*..."
    "*And another."
    "*You feel a bit... weird?"
    jump frisk_meeting_after_dinner

label frisk_meeting_choice35:      
    show toriel normal with Dissolve(.25)
    toriel "Thank you."
    "*You take another bite"
    "*..."
    #if the player chose option 27 earlier:
    if chose_frisk_meeting_option27==True:
        "*You bite off a bit too much. You gag, but you force it down."
        "*Uhg... "
        toriel "See, was that so hard?"
    if chose_frisk_meeting_option25==True or chose_frisk_meeting_option26:
        #if the player chose option 25 or 26 earlier:
        "*Eh..."
    jump frisk_meeting_after_dinner

label frisk_meeting_choice36:      
    #-1 Perseverance
    show toriel annoyed with Dissolve(.25)
    toriel "No buts. Eat, or you’ll be hungry later."
    "*You take another bite."
    "*..."
    "*Meh..."
     
    show toriel normal with Dissolve(.25)
    toriel "Thank you. You may be excused."
     
    #scene change to hallway
    "*What will you do now?"
    jump frisk_meeting_after_dinner
     
################################
#  FRISK MEETING AFTER DINNER  #
################################

label frisk_meeting_after_dinner:

    jump frisk_meeting_selection16
label frisk_meeting_selection16:
    menu:
        "Go back and talk to Toriel a bit longer" if chose_frisk_meeting_option37==False:
            jump frisk_meeting_choice37 
        "Check Toriel’s room" if chose_frisk_meeting_option72==True:
            jump frisk_meeting_choice37_5 
        "Go to bed":
            jump frisk_meeting_choice38 
        "Go talk to Frisk" if chose_frisk_meeting_option39 == False:
            jump frisk_meeting_choice39 
label frisk_meeting_choice37:          
    #scene change living room
    show toriel surprised with Dissolve(.25)
    toriel "Oh, hello again. Did you want to talk about something?"
    jump frisk_meeting_selection17

label frisk_meeting_selection17:
    menu:
        "What can I do?":
            jump frisk_meeting_choice40
        "Nothing in particular.":
            jump frisk_meeting_choice41

label frisk_meeting_choice40:
    show toriel normal with Dissolve(.25)
    toriel "Oh, good question!"
    show toriel awkward with Dissolve(.25)
    toriel "Hmm... There is not really any work to be done for the rest of the day--at least, not that I can think of at the moment."
    show toriel smile with Dissolve(.25)
    toriel "It appears you are off the hook. Personally, I would use this chance to rest. After all, you must be very tired by now. I know I would be! The ruins are not usually this lively."
    toriel "I will see you again in the morning... sleep well!"
    #remove option 37 from selection 16
    $ chose_frisk_meeting_option37 = True
    #scene change hallway
    jump frisk_meeting_after_dinner

label frisk_meeting_choice41:      
    #+1 Patience
    toriel "Hm, that is alright. Although..."
    show toriel awkward with Dissolve(.25)
    toriel "I cannot think of anything to talk about quite yet, either. I suppose sitting in silence can be nice, too--if you would like to do that."    
    show toriel normal with Dissolve(.25)
    "*You and toriel sit in silence for a little while."
    "*It is nice."
    toriel "As much as I enjoy your company, I think it would be wise if you went to bed. We can always talk in the morning, if you wish."
    toriel "Sleep well!"
    #remove option 37 from selection 16
    $ chose_frisk_meeting_option37 = True
    #scene change hallway
    jump frisk_meeting_after_dinner

label frisk_meeting_choice37_5:     
    #/// If >37.5(Check Toriel’s room)< 
    "*Toriel’s room strikes you as the type to be clean, orderly, and cozy."
    "*Going inside would be a huge invasion of privacy. You should know better."
    jump frisk_meeting_selection8

label frisk_meeting_selection18:
    menu:
        "Go inside anyway":
            jump frisk_meeting_choice63
        "Do not":
            jump frisk_meeting_choice64_5

label frisk_meeting_choice63:
    #-1 Justice
    "*There are a plethora of items to snoop through."
    #see questions at top of doc
    jump frisk_meeting_choice21     

label frisk_meeting_selection21:

    menu:
        "Look in the diary" if chose_frisk_meeting_option65==False:
            $ chose_frisk_meeting_option65_count+=1
            if chose_frisk_meeting_option65_count ==1:
                jump frisk_meeting_choice65
            elif chose_frisk_meeting_option65_count ==2:
                jump frisk_meeting_choice65_2
            elif chose_frisk_meeting_option65_count ==3:
                jump frisk_meeting_choice65_3
            else:
                $chose_frisk_meeting_option65 = True
                jump frisk_meeting_choice65_4
        "Examine the chair" if chose_frisk_meeting_option66==False:
            $ chose_frisk_meeting_option66 = True
            jump frisk_meeting_choice66
        "Examine the cactus" if chose_frisk_meeting_option67==False:
            $ chose_frisk_meeting_option67_count+=1
            if chose_frisk_meeting_option67_count ==1:
                jump frisk_meeting_choice67
            else:
                
                $chose_frisk_meeting_option67 = True
                jump frisk_meeting_choice67_5
        "Examine the shelf" if chose_frisk_meeting_option68==False:
            $chose_frisk_meeting_option68 = True
            jump frisk_meeting_choice68
        "Look in the drawer" if chose_frisk_meeting_option69==False:
            $chose_frisk_meeting_option69 = True
            jump frisk_meeting_choice69
        "Examine the bed" if chose_frisk_meeting_option70==False:
            $chose_frisk_meeting_option70 = True
            jump frisk_meeting_choice70
        "Examine the bucket" if chose_frisk_meeting_option71==False:
            $chose_frisk_meeting_option71 = True
            jump frisk_meeting_choice71
        "Leave Toriel’s room" if chose_frisk_meeting_option72==False:
            $ chose_frisk_meeting_option72= True
            jump frisk_meeting_choice72

label frisk_meeting_choice65:
    "*There are several entries about humans, but most of the diary is filled with random, bad puns."
    jump frisk_meeting_selection21

label frisk_meeting_choice65_2:      
    "*The man who invented knock-knock jokes must have won the No-Bell prize."
    jump frisk_meeting_selection21
label frisk_meeting_choice65_3:      
    "*Toucan do jokes as good as mine only if you dove in. No need to swallow your pride to make one."
    jump frisk_meeting_selection21
label frisk_meeting_choice65_4:      
    "*In the midst of bad puns, you find a rather serious entry. It seems personal..."
    jump frisk_meeting_selection22
     
label frisk_meeting_selection22:
    menu:
        "Read it":
            jump frisk_meeting_choice73
        "Do not":
            jump frisk_meeting_choice74
label frisk_meeting_choice73:          
    "*Frisk has been acting strange recently. Some days, they seem exhausted despite going to bed at a decent hour. I am uncertain as to why this is, but I have my ideas. I am not sure if I should confront them about it, though. They might not be as energetic as they were when they first came here, but they seem happier now more than ever. I must think on this."
    jump frisk_meeting_selection21


label frisk_meeting_choice74:      
    "*You shouldn’t peek..."
    jump frisk_meeting_selection21


label frisk_meeting_choice66:      
    "*The chair seems really cozy. Anyone could spend hours writing while sitting in this beauty."
    jump frisk_meeting_selection21

label frisk_meeting_choice67:      
    "*Ah, truly stunning, a plant that can survive in such extreme heat."
    "*It looks like it’s rooting for you."
    jump frisk_meeting_selection21

label frisk_meeting_choice67_5:      
    "*Truly the most tsundere of plants."
    jump frisk_meeting_selection21

label frisk_meeting_choice68:      
    "*There are several books about cooking, gardening, and bug hunting. There is even one called \"101 Snail Facts.\" It looks well-thumbed."
    jump frisk_meeting_selection21

label frisk_meeting_choice69:      
    "*There are a lot of socks for someone who doesn’t need them... s-scandalous."
    jump frisk_meeting_selection21

label frisk_meeting_choice70:      
    "*It’s way more comfortable than it looks."
    jump frisk_meeting_selection21

label frisk_meeting_choice71:      
    "*This bucket is filled entirely with a slimy mass of live snails."
    "*Looks delicious."
    jump frisk_meeting_selection21

label frisk_meeting_choice72:      
    "*Finally, you’re done snooping."
    "*Don’t you feel even a little guilty about what you’ve done?"
    jump frisk_meeting_after_dinner

label frisk_meeting_choice64_5:      
    #+1 Justice
    "*You are above that."
    jump frisk_meeting_after_dinner
     



label frisk_meeting_choice38:      
    #/// If >38(Go to bed)
    "*You hear Toriel calling from the kitchen."
    toriel "I forgot to mention, there is a room you can use at the far end of the hall. Goodnight, and sleep well!"
    #scene change MC’s room
    "*You enter the room, plop down on the bed, and fall asleep..."
    "*..."
    #END DAY 1


label frisk_meeting_choice39:      
    "*You see a light on in one of the rooms."
    #scene change frisk’s room
    show frisk bigsmile with Dissolve(.25)
    frisk "Oh, hi again!"
    show frisk normal with Dissolve(.25)
    frisk "Something on your mind?"
     
label frisk_meeting_selection19:
        
    menu:
        "How are you?" if chose_frisk_meeting_option40_5 == False:                       #//(+1)    
            $world.get_monster('Frisk').update_FP(1)
            $ chose_frisk_meeting_option40_5=True
            jump frisk_meeting_choice40_5
        "I was just stopping by to say ‘hey’. I’m heading off to bed. Goodnight!":                       #//(+1)
            $world.get_monster('Frisk').update_FP(1)
            $ chose_frisk_meeting_option39=True
            jump frisk_meeting_choice41_5
        "What’s all that stuff you have on your shelves?":
                                            #//(+0)
            jump frisk_meeting_choice42
label frisk_meeting_choice40_5:          
    #/// If >40("How are you?":<
    frisk "I’m doing fine, thank you." 
    #remove option 40 from selection 19
    #go back to selection 19
    jump frisk_meeting_selection19
label frisk_meeting_choice41_5:      
    #/// If >41("I was just stopping by to say ‘hey’. I’m heading off to bed. Goodnight!":<
    show frisk smallsmile with Dissolve(.25)
    frisk "Oh, alright. That was nice of you!"
    frisk "Goodnight!"
    #remove option 39 from selection 16
    
    #scene change hallway
    jump frisk_meeting_after_dinner

label frisk_meeting_choice42:      
    #/// If > 42(What’s all that stuff you have on your shelves?)
    show frisk normal with Dissolve(.25)
    frisk "Oh, just a couple of things from the Underground."
    jump frisk_meeting_selection20

label frisk_meeting_selection20:
    menu:
        "Just wondering. I think I’ll be heading off to bed now.":
            jump frisk_meeting_choice43
        "But how did you actually get all of this?":  
            jump frisk_meeting_choice44
label frisk_meeting_choice43:          
    show frisk normal with Dissolve(.25)
    frisk "Oh, okay. It was nice seeing you."
    frisk "Goodnight!"
    $ chose_frisk_meeting_option39=True
    #scene change hallway
    jump frisk_meeting_after_dinner
label frisk_meeting_choice44:      
    #/// If > 44("But how did you actually get all of this?":
    show frisk blush with Dissolve(.25)
    frisk "Oh, you know..." 
    frisk "I just found it laying around..."
    show frisk normal with Dissolve(.25)
    frisk "Actually, I’m pretty tired. I think I’m gonna go to bed, sorry."
    frisk "Goodnight!"
    #scene change hallway
    jump frisk_meeting_after_dinner

label frisk_meeting_after_dinner:
    jump frisk_meeting_start