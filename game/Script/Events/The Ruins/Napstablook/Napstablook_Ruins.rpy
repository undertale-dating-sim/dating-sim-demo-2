
#default-font
#init python:
#    style.default.font = "font/DTM-Mono.otf"
        
        
##################################################################      HANGOUT 3 - UNUSED       ##################################################################



label blooky_event3:
    #Event Name: "One Man's Trash..."
    #Event Triggers: Returning to the trash pile room after having explored all of Waterfall
    #                Having at least +20 FP with Napstablook
    #Synopsis: Napstablook has broken his headphones. Help Napstablook hunt for a new pair of headphones at the Dump.
    
    $ broke_snowglobe = False
    $ broke_headphones = False
    $ sneak_broke_headphones = False
    $ headphones_found = False
    $ headphones_given = False
    
    blooky "..........."
    
    menu:
        "Hey… Napstablook?":
            $world.get_monster('Napstablook').update_FP(1)
            blooky "huh? oh, hi........."
            jump somethings_wrong
            
        "Sneak up on Napstablook and frighten them.":
            $world.get_monster('Napstablook').update_FP(-3)
            blooky "..........."
            show napstablook surprised
            blooky "oh! oh....... it’s just you...."
            jump somethings_wrong
            
        "Leave before they notice you.": #(+0 FP)
            blooky "..........."
            "You ditched Napstablook."
            jump blooky_ruins
                
    label somethings_wrong:
        blooky "..........."
        
        menu:
            "What are you doing?":
                $world.get_monster('Napstablook').update_FP(1)
                blooky "oh.... nothing... it doesn’t matter..."
            "You seem distracted.": #(+0 FP)
                blooky "..........."
                blooky "what? oh, sorry....."
                
        menu:
            "Tell me what’s wrong.":
                $world.get_monster('Napstablook').update_FP(-1)
                blooky "oh, um... i guess... if you say so......."
            "If something happened, you can tell me.":
                $world.get_monster('Napstablook').update_FP(2)
                blooky "well....... it’s not that big of a deal, really... but i guess, if you want to know...."
                
        blooky "my headphones.... they broke yesterday. they’re pretty old, so it’s not that surprising, but....... i really liked them......"
        blooky "so i’m looking for new ones. none of the shops sell them.... or not good ones, anyway. i have to find them in the garbage......"
        
        menu:
            "I’ll help you look!":
                $world.get_monster('Napstablook').update_FP(3)
                blooky "wow, really? that’d be nice.... thanks........"
                blooky "um, you can just start wherever, if you want... i’ll keep looking in this pile....."
                "Where will you look?"
                
                $ bigtrash_searched = 1
                $ medtrash_searched = 1
                $ smltrash_searched = 1
                
                jump search_trash
            "Good luck with that!": #(+0 FP)
                blooky "oh, thanks.... i should probably get back to looking... bye, i guess......."
                jump end_blook_hangout3

    label search_trash:
        menu:
            "Look in the big trash pile.":
                if bigtrash_searched is 1:
                    "There doesn't seem to be anything useful here."
                if bigtrash_searched is 2:
                    "There’s an action figure. What will you do with it?"
                    jump actionfigure_found
                if bigtrash_searched is 3:
                    "Seems there’s nothing but trash left in this trash pile."
                if bigtrash_searched >= 4:
                    "You really like this trash pile, huh? It’s served you well, but that doesn’t change the fact that there’s nothing here."
                    
                $ bigtrash_searched += 1
                jump search_trash
                
            "Look in the medium-sized trash pile.":
                if medtrash_searched is 1:
                    "You find a pair of running shoes tied together by the laces. What will you do with them?"
                    jump runshoes_found
                if medtrash_searched is 2:
                    "Seems there’s nothing but trash left in this trash pile."
                if medtrash_searched >= 3:
                    "Still nothing..."
                    
                $ medtrash_searched += 1
                jump search_trash
                    
            "Look in the small trash pile.":
                if smltrash_searched is 1:
                    "There’s a snow globe sitting right on top. Miraculously, it isn’t broken. What will you do with it?"
                    jump snowglobe_found
                if smltrash_searched is 2:
                    "There’s a pair of headphones in the middle of the pile. They look brand new, and the other trash surrounding them has kept them from touching the water. What will you do with them?"
                    $ headphones_found = True
                    jump headphones_found
                if smltrash_searched is 3:
                    "seems there’s nothing but trash left in this trash pile."
                if smltrash_searched >= 4:
                    "*there’s nothing else here… really."
            "Stop searching.":
                jump end_blook_hangout3
                
                
                
    label actionfigure_found:
        menu:
            "Give it to Napstablook.":
                $world.get_monster('Napstablook').update_FP(1)
                blooky "oh, thanks, but..... i don’t really need this... i don’t even know what show this is from......"
            "Keep it for yourself.": #(+0 FP)
                "Napstablook probably wouldn’t like it much, anyway."
                ###### ITEM GET ACTION FIGURE ######
            "Put it back.": #(+0 FP)
                "You don’t need it, and Napstablook probably wouldn’t like it much, anyway."
        
        $ bigtrash_searched += 1
        jump search_trash
        
    label runshoes_found:
        menu:
            "Give it to Napstablook.":
                $world.get_monster('Napstablook').update_FP(1)
                blooky "i actually can’t wear shoes.... awkward......."
                blooky "but... thanks anyway."
            "Keep it for yourself.": #(+0 FP)
                "Who knows when you might need to run from something…"
                ###### ITEM GET RUNNING SHOES ######
            "Put it back.": #(+0 FP)
                "you already have shoes, and you don’t think Napstablook can wear them, anyway. You put them back in the pile."
                
        $ medtrash_searched += 1
        jump search_trash
        
    label snowglobe_found:
        menu:
            "Give it to Napstablook.":
                $world.get_monster('Napstablook').update_FP(2)
                blooky "oh, wow.... that’s pretty. thanks......"
            "Keep it for yourself.": #(+0 FP)
                "It’s too pretty to just leave it in the trash. You give it a little shake before putting it in your pocket."
                ###### ITEM GET SNOW GLOBE ######
            "Put it back.": #(+0 FP)
                "This isn’t what you’re looking for, anyways."
            "Break it.":
                $world.get_monster('Napstablook').update_FP(-2)
                "The glass makes a satisfying sound as it shatters."
                blooky "did... something break?"
                
                $ broke_snowglobe = True
                jump snowglobe_q
        
        $ smltrash_searched += 1
        jump search_trash
    
    label snowglobe_q:
        menu:
            "No.":
                $world.get_monster('Napstablook').update_FP(-2)
                blooky "oh.... because it sounded like....."
                blooky "nevermind......."
            "Yeah. Don’t worry about it.":
                $world.get_monster('Napstablook').update_FP(-1)
                blooky "um.... why......"
                blooky "okay........."
            "It was an accident.": #(+0 FP)
                blooky "oh, that’s sad......."
        $ smltrash_searched += 1
        jump search_trash
    
    label headphones_found:
        menu:
            "Give it to Napstablook.":
                $world.get_monster('Napstablook').update_FP(5)
                show napstablook smile
                blooky "oh! you found some headphones.... and they look pretty new....."
                blooky "thank you for helping... this is really nice....."
                $ headphones_given = True
                jump whats_next
            "Keep it for yourself.": #(+0 FP)
                "You know Napstablook needs these, how selfish."
                ###### ITEM GET HEADPHONES ######
                jump search_trash
            "Put them back.": #(+0 FP)
                "But.. this is what you’re looking for."
                jump search_trash
            "Break them.":
                $world.get_monster('Napstablook').update_FP(-5)
                "They make a loud, snapping sound."
                "You vandal, you."
                blooky "what was that?"
                $ broke_headphones = True
                jump headphones_q
            "Break them discretely." if broke_snowglobe is True: #(+0 FP)
                "You check to make sure Napstablook isn’t looking, then carefully nudge the headphones until they fall off the pile. They splash in the water."
                blooky "..what was that?"
                $ sneak_broke_headphones = True
                jump sneak_headphones_q
                
    label headphones_q:
        menu:
            "Nothing…":
                $world.get_monster('Napstablook').update_FP(-4)
                blooky "are those... headphones?"
            "Show them the broken headphones.":
                $world.get_monster('Napstablook').update_FP(-4)
                blooky "oh....... you broke them......"
            "I didn’t mean to…":
                $world.get_monster('Napstablook').update_FP(-2)
                blooky "oh....... um, sure... that’s okay, i guess......."
        jump sad_ending
                
    label sneak_headphones_q:
        menu:
            "Oh no… I think that was a pair of headphones, sorry!": #(+0 FP)
                blooky "oh...... that’s bad luck.... i guess i should’ve expected something like this to happen…"
            "Gosh… I’m so clumsy, I’m sorry.": #(+0 FP)
                show napstablook sad
                blooky "those were headphones, weren’t they? And they probably won’t work now that they’re all wet...."
        
        blooky "that’s okay........ we can keep looking, i guess...."
        jump search_trash
                
                
    label whats_next:
        menu:
            "No problem! I’m happy to help.": #(+3 DP)
                blooky "i’m going to go try them out right away. thanks again....."
                jump end_blook_hangout3
            "I’d like to keep looking around, if that’s okay.":
                $world.get_monster('Napstablook').update_FP(1)
                blooky "oh, sure.... i’ll just be here if you need me......"
                jump search_trash
            
    label end_blook_hangout3:
        if headphones_given is False:
            blooky "oh, is that all you could find?"
        
        if headphones_found is True:
            blooky "thanks again for your help... i’m really glad you found me here. see you around......."
        if sneak_broke_headphones is True:
            show napstablook sad
            blooky "don’t worry about it... it was an accident. i can just look for headphones...... somewhere else....... i’ll go do that... bye........"
        if headphones_given is False:
            blooky "we didn’t find the headphones, but that’s okay... i can just look somewhere else...... i’ll see you later... "
        jump blooky_ruins
    
    label sad_ending:
        show napstablook sad
        blooky "you know... um....... i think i’ll just... go look somewhere else......."
        jump blooky_ruins