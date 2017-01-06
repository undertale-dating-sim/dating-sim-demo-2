

label frisk_friendhsip_event_1:
    #"Do you want to go snail hunting with me?" should be added to Frisk’s 
        #general dialog if the player has not yet completed this event.
    #menu: "Do you want to go snail hunting with me?":
    
    show frisk smallsmile
    frisk "Yeah, that sounds fun!"
    frisk "It’s always a lot more interesting with friends."
    show frisk smallsmile
    frisk "I’m... uh..."
    frisk "Sorry, nevermind."
    show frisk normal
    frisk "Let’s just get going, okay?"
    #scene change snail hunting room
    frisk "Alright, we’re here!"
    frisk "Are you... uhm..."
    frisk "..."
    frisk "Oh, sorry."
    show frisk smallsmile
    frisk "Are you ready?"
    menu:
        "You seem distracted.":
            show frisk normal
            frisk "It’s nothing."
            frisk "Come on, let’s focus. Mom will be disappointed if we come back with nothing!"
            show frisk smallsmile
            frisk "I’m sure you’re ready, so here we go."
        "Let's start!":
            $world.get_monster ('Frisk').FP +=2
            frisk "Yeah... We’re both ready, so here we go."
    #call demo_undersnail
    
    #after game, regardless of performance
    show frisk distant
    frisk "..."
    frisk "..."
    menu:
        "Frisk...?":
            frisk "I..."
            show frisk sad
            frisk "I don’t feel so good."
            show frisk disgusted
            frisk "I’ll, uhh..."
            frisk "See you later."
            hide frisk
        "...":
            frisk "..."
            show frisk disgusted
            frisk "I can’t..."
            frisk "I’ll, uhh..."
            frisk "See you later."
            hide frisk


    #player is free to move around the Ruins. Once they go back to the tunnel divide...
    #scene tunnel divide
    show frisk distant
    "*Frisk is standing in the middle of the room, but they don’t appear to have noticed you."
    frisk "..."
    frisk "Please..."
    frisk "Please stop."
    frisk "Stop!"
    frisk "..."
    show frisk panicking
    frisk "Stop it! Stop!"
    menu:
        "What happened?":
            frisk "Y-you..."
            frisk "How did you find me?"
            frisk "You shouldn’t be here!"
            frisk "I-I can’t control..."
            frisk "It never stops!"
        "Are you okay?":
            frisk "Y-you..."
            frisk "Why are you here?"
            frisk "You need to leave!"
            frisk "I-it’s not safe f-for you!"
        "Have you gone crazy?":
            $world.get_monster ('Frisk').FP -=3
            frisk "No! I..."
            frisk "I..."
            frisk "I don’t know..."
            frisk "No! I’m not!"
            frisk "I just..."
    frisk "Argh..."
    frisk "I can’t..."
    show frisk panicking hands
    frisk "I can’t think!"
    frisk "I... I..."
    frisk "Help me!"
    frisk "No, don’t!"
    frisk "I..."
    menu:
        "*Give them space":
            frisk "No, don’t leave!"
            frisk "Please!"
            frisk "Not again!"
            frisk "Help me..."
        "*Reach out to help":
            frisk "No, you shouldn’t!"
            frisk "I just..."
            frisk "Since you’re here, I just..."
            frisk "I need to know you’re there."
    menu:
        "You're gonna be fine.":
            $world.get_monster ('Frisk').FP +=1
            frisk "I can’t..."
            frisk "I want to believe that, but..."
            frisk "It won’t g-go away!"
        "I'm not leaving.":
            $world.get_monster ('Frisk').FP +=3
            frisk "Thank y-you..."
            frisk "D-don’t go..."
            frisk "I said don’t go!"
        "I'll go get Toriel.":
            $world.get_monster ('Frisk').FP -=2
            frisk "No! Don’t!"
            frisk "She can’t help!"
            frisk "I-I can’t let her see me like this again!"
    
    frisk "It n-never stops!"
    frisk "Why won’t it j-just stop!?"
    show frisk disgusted
    frisk "Why?"
    frisk "Why...?"
    show frisk panicking
    frisk "Won’t it just l-leave me alone!?"
    show frisk disgusted
    frisk "But I won’t let it..."
    frisk "I can’t let it..."
    frisk "I can’t..."
    frisk "Never..."
    frisk "No more..."
    frisk "..."
    menu:
        "Are you okay?":
            $world.get_monster ('Frisk').FP +=2
            frisk "..."
            frisk "I..."
            show frisk distant
            frisk "Yeah..."
            frisk "I think so."
            frisk "..."
        "What is this all about?":
            frisk "..."
            frisk "It’s..."
            frisk "I don’t even..."
            frisk "..."
    show frisk distant
    frisk "I... I’m sorry..."
    frisk "I shouldn’t have asked you to help."
    frisk "You shouldn’t have seen that."
    frisk "..."
    show frisk sad
    frisk "Please, don’t tell Mom."
    frisk "I’m sorry..."
    #hide frisk
    
    #player is free to move around the Ruins. Once they go back to the black tree room:
    show frisk surprised
    frisk "What?"
    frisk "Why are you following me?!"
    show frisk sad
    frisk "Let’s just forget about this..."
    frisk "It would be best for both of us."
    menu:
        "Are you okay?":
            $world.get_monster ('Frisk').FP +=1
            frisk "Look, I’m fine."
            frisk "Thanks for your concern, but..."
            frisk "There’s nothing to say."
            show frisk smallsmile
            frisk "I’ll see you later, okay?"            
        "I think you owe me an explanation.":
            $world.get_monster ('Frisk').FP -=2
            show frisk annoyed
            frisk "Look, I told you already, it was just..."
            show frisk sad
            frisk "Do we really have to talk about this now?"
            menu:
                "Yes, we do.":
                    $world.get_monster ('Frisk').FP -=2
                    frisk "..."
                    frisk "I’d really rather not, okay?"
                    menu:
                        "Don't I deserve an explanation?":
                            $world.get_monster ('Frisk').FP -=2
                            frisk "..."
                            show frisk annoyed
                            frisk "You know what? No."
                            frisk "I’m not going to talk about this. In fact, I’ll just leave."
                            show frisk sad
                            frisk "...Goodbye."
                        "Alright, fine.":
                            $world.get_monster ('Frisk').FP +=1
                            frisk "Thank you."
                            frisk "Look, I’m gonna go now."
                            frisk "I’ll talk to you later."
                "Not if you aren't feeling up to it.":
                    $world.get_monster ('Frisk').FP +=1
                    frisk "Thank you."
                    frisk "I mean..."
                    frisk "You already think I’m crazy, don’t you?"
                    menu:
                        "I don't think you're crazy.":
                            $world.get_monster ('Frisk').FP +=3
                            show frisk smallsmile
                            frisk "Thanks."
                            frisk "But I don’t get it..."
                            frisk "I just met you, so why are you being so patient with me?"
                            menu:
                                "Because we're friends.":
                                    $world.get_monster ('Frisk').FP +=4
                                    frisk "Friends..."
                                    show frisk smile
                                    frisk "Yeah... I guess so."
                                    frisk "Well, if we’re really friends, then you’ll let this go. Right?"
                                    show frisk smallsmile
                                    frisk "..."
                                    frisk "Maybe I’ll tell you about it one day."
                                    frisk "But for now, I should go."
                                    show frisk smile
                                    frisk "Thanks again."
                                "I'm not sure.":
                                    frisk "Really?"
                                    frisk "Well, whatever it was for, thanks again."
                                    frisk "Maybe I’ll tell you about it someday."
                                    frisk "But, uhm... Not now."
                                    frisk "I should get going."
                                    frisk "See you later."
                                "That's just the way I am.": #if patience >0
                                    $world.get_monster ('Frisk').FP +=2
                                    frisk "Huh, yeah, I guess that makes sense."
                                    frisk "Well, thanks again."
                                    frisk "Maybe I’ll tell you about it someday."
                                    frisk "But, uhm... Not now."
                                    frisk "I should get going."
                                    frisk "See you later."
                        "Yeah, a bit.":
                            $world.get_monster ('Frisk').FP -=1
                            show frisk sad
                            frisk "..."
                            frisk "I think I’ll just go now."
                            frisk "Please don’t bring this up again."
                            frisk "See you later."
            
    #frisk is now back to wherever they should be at this time of day according to their schedule
    
    
    #the next time the player encounters Frisk normally, play the following before the player can talk to them:
    frisk "Hey, about last time we talked..."
    frisk "Sorry I was acting so weird!"
    frisk "It’s just a really complicated situation, and I’d rather not think about it."
    frisk "So, let’s just pretend that never happened!"
    frisk "Anyway, did you need something?"
    
    return
    