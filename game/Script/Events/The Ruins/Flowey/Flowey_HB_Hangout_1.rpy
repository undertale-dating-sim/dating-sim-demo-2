label flowey_HB_hangout_1:
    scene background floweyroomplaceholder
    # HB Hangout 1
    # End the first Flowey friendship hangout by choosing the option "We're going to play a game"
    
    show flowey sideglance
    flowey "What do {i}you{/i} want?"
    
    menu:
        "You're interesting.":
            $world.get_monster('Flowey').update_HB(2)
            show flowey annoyed
            flowey "Well, duh."
            show flowey smug
            flowey "In a world filled with this many idiots, anyone with sense has to seem pretty interesting, huh?"
            jump Flowey_HB_Hangout_1_Interesting
        "What, can't I chat with my favorite flower?":
            $world.get_monster('Flowey').update_HB(2)
            show flowey normal
            flowey "Not really, no."
            show flowey smug
            flowey "Did I look like I wanted to {i}chat{/i} with you?"
            flowey "I hope I didn't give you that impression..."
            flowey "...Considering I hate you and want nothing to do with you."
            flowey "And of course-"
            show flowey surprised
            flowey "...wait."
            show flowey suspicious
            flowey "Why the hell would I be your {i}favorite{/i}?"
            show flowey annoyed
            flowey "The last thing I want is to be put on any list of yours."
            jump Flowey_HB_Hangout_1_Flower
        "Nothing, I'm just bored.":
            jump Flowey_HB_Hangout_1_WastedTime
            
    label Flowey_HB_Hangout_1_Interesting:
        menu:
            "Well, are you ready to play that game now?":
                $world.get_monster('Flowey').update_HB(3)
                show flowey angry
                flowey "What is it with you?!?"
                flowey "I get it. This is all some game. Very funny."
                
                menu:
                    "Does it bother you?": #+3 HB
                        flowey "No!"
                        flowey "Nothing bothers me. I can't {i}be{/i} bothered."
                    "Now you're getting it.": #+2 HB
                        show flowey annoyed
                        flowey "Glad we're on the same page... Idiot."
                        
                jump Flowey_HB_Hangout_Bothered
            "This is why you don't have any friends.": #-1 FP
                $world.get_monster('Flowey').update_FP(-1)
                show flowey suspicious
                flowey "Wow, the 'no friends' comment. How original."
                show flowey horror
                flowey "If you think you're getting to me... You're not."
                
                menu:
                    "Don't you want friends?": #+2 HB
                        $world.get_monster('Flowey').update_HB(2)
                        show flowey suspicious
                        flowey "I don't need anybody, and nobody needs me. In short, things are just peachy the way they are."
                        jump Flowey_HB_Hangout_Bothered
                    "I didn't mean anything by it, sorry.": #-2 HB
                        $world.get_monster('Flowey').update_HB(-2)
                        jump Flowey_HB_Hangout_1_WastedTime
                    
            "You know what? Nevermind.":
                jump Flowey_HB_Hangout_1_WastedTime
    
    label Flowey_HB_Hangout_1_Flower:
        menu:
            "You may want to reconsider that...":
                show flowey smug
                flowey "Tch. Why should I?"
                flowey "Is this where you issue some sort of {i}threat{/i}?"
                show flowey normal
                flowey "You should know by now how little your threats mean to me."
                show flowey sideglance
                flowey "..."
                flowey "I don't want to talk to you. Your presence bores me to death."
                show flowey smug
                flowey "And I {i}wish{/i} I could say I was exaggerating."
                show flowey angry
                flowey "And for goodness' sake, don't {i}ever{/i} tell me I'm your {i}favorite{/i} anything {i}ever again{/i}."
                jump Flowey_HB_Hangout_1_Interesting
                
            "Come on, it wouldn't hurt to make friends.":
                show flowey annoyed
                flowey "First of all, I don't need friends."
                flowey "Second of all, this isn't some kids' TV show, so you can stop talking about stupid crap like \"making friends\"."
                flowey "Finally, I can't be your favorite if you know absolutely {i}nothing{/i} about me."
                show flowey smug
                flowey "And, feel free to take this personally, I don't want to learn anything about you."
                
                menu:
                    "You know what? Nevermind.":
                        jump Flowey_HB_Hangout_1_WastedTime
                    "My game, my rules.":
                        $world.get_monster('Flowey').update_HB(3)
                        jump Flowey_HB_Hangout_1_MyGame
            "I didn't mean anything by it, sorry.":
                jump Flowey_HB_Hangout_1_WastedTime
                
        label Flowey_HB_Hangout_1_MyGame:
            show flowey surprised
            flowey "..."
            show flowey suspicious
            flowey "..."
            flowey "Right... Whatever you say, idiot."
            
            menu:
                "You're powerless, and you know that.":
                    $world.get_monster('Flowey').update_HB(3)
                    show flowey sad
                    flowey "..."
                    flowey "See... you're failing to realize..."
                    show flowey horror
                    flowey "You're not in control, either."
                    show flowey normal
                    flowey "Heheh..."
                    show flowey sad
                    jump Flowey_HB_Hangout_Bothered
                "It's better to have me as a friend than an enemy, Flowey.":
                    $world.get_monster('Flowey').update_HB(-1)
                    show flowey suspicious
                    flowey "..."
                    flowey "I choose neither."
                    show flowey surprised
                    flowey "So go away. Your little hangout is over."
                    jump Flowey_HB_Hangout_Bothered
                "Just remember this is all a game. You're nothing more than an option.":
                    $world.get_monster('Flowey').update_HB(3)
                    show flowey angry
                    flowey "Don't you think I know that?"
                    flowey "The point of all this is for me to be left out of your stupid game."
                    show flowey sideglance
                    flowey "I wasn't supposed to be an option in the first place."
                    show flowey horror
                    flowey "I won't be a pawn. Not to you or anyone else."
                    show flowey angry
                    flowey "So back off."
                    
                    menu:
                        "Fine.": 
                            $world.get_monster('Flowey').update_HB(-1)
                            show flowey suspicious
                            flowey "Go away."
                            hide flowey
                            "Flowey left."
                            return
                        "Since when were you in control?":
                            $world.get_monster('Flowey').update_HB(3)
                            show flowey surprised
                            flowey "..."
                            show flowey sad
                            flowey "...Screw this."
                            show flowey angry
                            flowey "And {i}screw you too!{i}"
                            jump Flowey_HB_Hangout_Bothered
                            
    label Flowey_HB_Hangout_1_WastedTime:
        show flowey suspicious
        flowey "Whatever."
        flowey "Go waste someone else's time."
        hide flowey
        "Flowey left."
        return
        
    label Flowey_HB_Hangout_Bothered:
        if (owner.HB >= 5):
            flowey "..."
            show flowey angry
            flowey "What? Stop looking at me like that."
            flowey "You... you don't scare me!"
            flowey "Go away!"
            hide flowey
            "Flowey ran away."
        elif (owner.HB < 5):
            flowey "..."
            show flowey smug
            flowey "I see what you're trying to do here, and it's not going to work on me."
            flowey "Have fun with that, you freak."
        else:
            return
        return
        