#character-settings
define blooky = Character('Napstablook')

#default-font
init python:
    style.default.font = "font/DTM-Mono.otf"
       
label blooky_ruins:
    
    $ issinger = False
    $ isdancer = False
    $ likedmusic = False
    $ dislikedmusic = False
    
    menu:
        "Like Karaoke, but Without the Lyrics on the Screen":
            jump blooky_event1
        "Snail Hunting is an Art":
            jump blooky_event2
        "One Man's Trash...":
            jump blooky_event3
        "Blooky's Date":
            jump blooky_questions_date
        "Exit":
            jump start
            
            
##################################################################      HANGOUT 1       ##################################################################
       
       
    label blooky_event1:
        
        #Event Name: Like Karaoke, but Without the Lyrics on the Screen
        #Event Trigger: Returning to Napstablook's room after all rooms in the Ruins have been explored
        #Synopsis: Napstablook offers to let you listen to a new song he made. How will you respond?
        
        blooky "oh...... hi. i didn’t think you’d come back here...."
        blooky "i’m glad you did, though....... i mean, i’ve been working on a new song and i was wondering if..... maybe....... you’d want to listen to it?"
        blooky "you don’t have to, if you don’t want......"
        
        menu:
            "Sure, I’d love to!": #(+3 FP)
                blooky "wow, i didn’t think you’d......"
                blooky "okay, i’ll put it on.... just a minute...."
                jump nq1a
            "I can’t, I’m busy.": #(-2 FP)
                #Bad end, hangout does not occur
                blooky "that’s okay.... i understand......."
                jump blooky_ruins
                
    label nq1a:
    #Path: "Sure, I’d love to!"
    #If the player decided to listen to Napstablook's music in the first hangout
        blooky "um...... okay.... this isn’t even that good, and it’s not done.... i mean, i think it’s done, but i always end up changing things later so it’s probably not done...."
        blooky "and... i know it doesn’t have lyrics...... and some people don’t like that.... but i’m not a very good singer, so...."
        
        menu:
            "Just turn it on, the anticipation is killing me!": #(-2 FP)
                blooky "oh.... okay...... sorry......."
            "I’m sure it’s fine.": #(+1 FP)
                blooky "maybe..... um, i’ll turn it on now......."
            "Maybe I could sing along?": #(+3 FP)
                blooky "o-oh.... uh...."
                #Small smile
                blooky "ha.... okay.... if you want...."
                $ issinger = True
                
        ######     MUSIC BEGINS PLAYING     ######
        
        blooky "so.... this is it......."
        jump nq2a

    label nq2a:
    #Path: Q1 Any
    #How will you respond to Blooky's music?
        menu:
            "I like it!": #(+1 FP)
                blooky "really?"
                blooky "oh....... i wasn’t expecting that...."
                blooky "thank you......"
                $ likedmusic = True
                jump nq3a
            "It’s not really my style…": #(-2 FP)
                blooky "sorry....... i’ll turn it off now...."
                $ dislikedmusic = True
                jump end_blook_hangout1
            "Dance": #(+3 FP)
                blooky "what are you... doing?"
                $ isdancer = True
                jump nq5a
            "Sing along" if issinger:
                #Smiling
                blooky "ha...... haha...."
                blooky "oh, sorry, you have a good voice, it’s just.... i guess the song wasn’t really meant to have lyrics... "
                blooky "not that yours aren’t.... creative.... haha... "
                jump nq6a
                
    label nq3a:
    #Path: "I like it!"
    #Give a followup comment to Blooky
        menu:
            "Yeah! You should make an album.": #(+2)
                blooky "oh..... i don’t know.... that sounds kind of daunting......."
                blooky "but maybe.... i’ll think about it......."
                jump end_blook_hangout1
            "Have you showed this to anyone else?": #(+0)
                blooky "um, no.... just you so far...."
                jump nq4a
            "It’s actually starting to get a little repetitive...": #(-2)
                blooky "sorry....... i’ll turn it off now...."
                # jump end_blook_hangout1
                
    label nq4a:
    #Path: "I like it!" -> "Have you showed this to anyone else?"
    #Reassure Blooky
        menu:
            "That’s probably for the best.": #(-4 FP)
                blooky "oh....... if you say so......."
            "You should, I bet people would love it!": #(+2 FP)
                blooky "oh....... you think so?"
                blooky "maybe.... i could show it to Frisk.... they always like my music, even when it’s bad......"
                
    label nq5a:
    #Path: "Dance"
    #Explain or deny what you're doing to Blooky
        menu:
            "I’m dancing, obviously!": #(+1 FP)
                blooky "oh... i couldn’t tell......"
                blooky "oh, um.. don’t take that the wrong way... i was trying to be funny.... you’re, uh.... a really good dancer..........."
                jump nq9a
            "“Oh, nothing…": #(+0 FP)
                "You stop dancing."
                blooky "oh... okay......"
                blooky "you, uh.... didn’t have to stop.."
                jump end_blook_hangout1
                
    label nq6a:
    #Path: Sing along
    #Napstablook challenges your singing.
        menu:
            "Hey, my lyrics are genius! A true masterpiece!": #(+2 FP)
                #Smiling
                blooky "ha.... yeah.... definitely......."
                jump end_blook_hangout1
            "Haha… yeah I guess you’re right. I shouldn’t have ruined your song with my crappy singing.": #(+0 FP)
                #Frowning
                blooky "oh.... no...... it’s okay.... you don’t have to stop.... i don’t mind......."
                jump end_blook_hangout1
            "You try singing, I bet you can’t do better!": #(-1 FP)
                #Neutral
                blooky "oh..... you’re right.... i can’t...."
                jump nq7a
                
    label nq7a:
    #Path: Sing along -> "You try singing, I bet you can’t do better!"
    #Encourage Napstablook to sing.
        menu:
            "So you’re saying I win?": #(-1 FP)
                blooky "oh.... yeah, i guess......."
                jump end_blook_hangout1
            "C’mon… just try? I promise I won’t laugh, or anything.": #(+1 FP)
                blooky "um... well.... i suppose i could try....."
                "Napstablook starts singing so quietly that you can’t even understand them."
                jump nq8a

    label nq8a:
    #Path: Sing along -> "You try singing, I bet you can’t do better!" -> "C’mon… just try? I promise I won’t laugh, or anything."
    #Napstablook looks uncomfortable. What will you do?
        menu:
            "Come on… belt it out!": #(-2 FP)
                blooky "um... i’d rather not.... sorry to disappoint you...."
                jump end_blook_hangout1
            "If it makes you uncomfortable, you don’t have to.": #(+2 FP)
                blooky "okay.... that’s a relief...... thanks........"
                jump end_blook_hangout1
            "That’s nice… you should incorporate some vocals into your next song. Maybe we could sing a duet?": #(+4 DP)
                #Blushing
                blooky "ha... ha... you would really do that?"
                blooky "that might be fun....."
                jump end_blook_hangout1
                
    label nq9a:
    #Path: "Dance" -> "I’m dancing, obviously!"
    #Napstablook compliments you. What will you do?
        menu:
            "That’s okay, I know I suck.": #(-1 FP)
                blooky "oh........"
                blooky "...."
                blooky "can i ask, um.... why do you do it, then?"
                jump nq10a
            "Damn right I am!": #(-2 FP)
                blooky "um....... yeah........"
                jump end_blook_hangout1
            "Dance with me?": #(+2 DP)
                #Blushing
                blooky "oh.... i don’t know.... i’m not very good......."
                jump nq11a
                
    label nq10a:
    #Why do you dance?
    #Path: "Dance" -> "I’m dancing, obviously!" -> "That’s okay, I know I suck."
        menu:
            "Because it’s fun… I don’t have to be good at something to enjoy it.": #(+4 FP)
                blooky "oh... i see......."
                blooky "that’s nice.... sounds like a pretty good outlook to have on things......"
            "Because I like to make people laugh, even if it’s at my own expense.": #(+2 FP)
                blooky "that’s nice of you.... but you didn’t have to do that...."
                blooky "oh, no.... and i didn’t even laugh.... i’m sorry......."
            "I don’t know… because I can?": #(-1 FP)
                blooky "oh, um.... okay then......."
        jump end_blook_hangout1
        
    label nq11a:
    #Path: "Dance" -> "I’m dancing, obviously!" -> "Dance with me?"
    #Convince Blooky to dance with you.
        menu:
            "That’s okay, I’m not either.": #(+1 FP)
                #Frowning
                blooky "oh, no.... you’re...... okay... "
            "You don’t know until you try!": #(-1 FP)
                #Neutral
                blooky "i have tried, though... that’s how i know........"
        blooky "um.... i think i’ll pass this time.... sorry....."
        jump end_blook_hangout1

    label end_blook_hangout1:
    #Napstablook is leaving.
        ######     MUSIC STOPS PLAYING     ######
        blooky "well.... that’s all i have...."
        blooky "i should go now.... thanks for listening........"
        jump blooky_ruins
        
        
    ##################################################################      HANGOUT 2       ##################################################################


    label blooky_event2:
        #Event Name: "Snail Hunting is an Art"
        #Event Trigger:  Having at least +10 FP with Napstablook
        #                Having played the snail minigame at least 3 times
        #                Finding Napstablook in Toriel’s garden
        #Synopsis: Napstablook notices you've been catching a lot of snails recently, and offers to help.

        $ ruinsnails_asked = False
        $ net_asked = False
        $ extrasnails_asked = False
        
        $ torielsnails_asked = True
        $ blookyfavsnail_asked = True
        $ boughtsnails_asked = True

        blooky "hi.... i see you’ve been catching a lot of snails lately and, um...."
        blooky "i was wondering if... maybe... you wanted some advice? n-not that you’re not doing well on your own........."
        
        menu:
            "Sure!": #(+3 FP)
                blooky "okay... i’m glad...."
                blooky "so, um..... what do you want to know?"
                jump snail_advice
            "Sorry, not now.": #(-1 FP)
                blooky "oh..... okay......."
                blooky "well, see you later, then. or not. whatever you want...."
                jump end_blook_hangout2
            "I don’t need advice, I’m a snail hunting expert!": #(-3 FP)
                blooky "oh, well.... if you’re sure......."
                blooky "i guess i’ll just leave, then. sorry to bother you....."
                jump end_blook_hangout2

    label snail_advice:
    #Napstablook is giving you snail-hunting advice.

        menu:
            "What types of snails are there in the Ruins?" if ruinsnails_asked is False: #(+1 FP)
                blooky "oh, there’s a lot..."
                blooky "there’s the common house snail... which actually isn’t all that common. they’re pretty rare. i guess  not everyone can afford to own their own home in this economy......."
                blooky "then there’s the book snail.... not to be confused with a book worm.... they really like to read, and don’t always pay attention to where they’re going..."
                blooky "there are some snails that are addicted to coffee... their movements are so random, i sometimes have a hard time catching them..."
                blooky "lastly, there’s the rocket snails. they like to consider themselves daredevils.... i don’t know how to tell them that they’re only flying a few inches in the air, and aren’t actually in any danger. maybe it’s better that way......"
                
                $ ruinsnails_asked = True
                $ torielsnails_asked = False
                $ blookyfavsnail_asked = False
                
                jump snail_advice
                
            "My net is too slow and big… is there anywhere I can get a better one?" if net_asked is False: #(+2 FP)
                blooky "um.... Toriel probably has better nets.... but they can get kind of expensive, so she might not trust you with them right away...."
                blooky "but, uh.... i just prefer the slower nets, anyway. i like to take my time."
                blooky "i actually have a net that i’m not using... do you want it?"
                $ net_asked = True
                jump snailnet_q
                
            "How can I get rid of my extra snails?" if extrasnails_asked is False: #(+1 FP)
                blooky "oh, i’ll take them.... if you don’t want them...."
                blooky "or you could sell them to Toriel.... i think she’ll give you 1G per snail."
                blooky "but, um.... if you happened to find me in the ruins.... i’ll give you a better deal...."
                
                $ extrasnails_asked = True
                $ boughtsnails_asked = False
                
                jump snail_advice
                
            "Why are there so many snails in Toriel’s garden?" if torielsnails_asked is False: #(+1 FP)
                blooky "i don’t actually know.... they all just seem to prefer her house, for some reason."
                blooky "i thought i saw her spreading something on the ground once..... but i didn’t ask her what it was.... i didn’t want to bother her...."
                
                $ torielsnails_asked = True
                
                jump snail_advice
                
            "What’s your favorite kind of snail?" if blookyfavsnail_asked is False: #(+2 FP)
                blooky "oh...... that’s a difficult question......."
                blooky "i don’t think i have a favorite kind. i like all snails.... especially the ones that live on my farm."
                $ blookyfavsnail_asked = True
                jump snail_advice
                
            "What do you do with the snails you buy?" if boughtsnails_asked is False: #(+1 FP)
                blooky "i just bring them back to my farm.... it’s in waterfall..."
                blooky "people will pay more for snails there than they will in the ruins. that’s how we stay in business."
                
                $ boughtsnails_asked = True
                
                jump snail_advice
                
            "That’s all I wanted to know.": #(+0 FP)
                blooky "oh, okay... i hope that was helpful......"
                blooky "did you, um.... want to try catching snails again? i could watch and tell you how you did after..."
                
                menu: 
                    "Sure!": #(+1 FP)
                        blooky "i’ll wait here.... good luck....."
                        
                        ####### SNAIL GAME CODE #######
                        
                        jump snail_judgement
                    
                    "I’ll pass.": #(-1 FP)
                        blooky "oh, okay.... i understand. i wouldn’t want anyone to watch me, either..."
                        blooky "um, well... in that case... i’ll see you around...... i guess......"
                        jump end_blook_hangout2

    label snailnet_q:
        menu:
            "Yes, please!": #(+2 FP)
                blooky "okay, here you go.... i hope that’s helpful..."
                
                ###### GET INTERMEDIATE NET ITEM ######
                
                jump snail_advice
                
            "No, thanks!": #(+0 FP)
                blooky "oh, okay.... just thought i’d offer...."
                jump snail_advice
                
    label snail_judgement:
        #if snail_score < 5 and snail_score > 0 #Adjust as needed
        blooky "oh.... um... you did......... fine........"
        blooky "i’m sure you’ll do better next time, now that you’ve practiced."
        
        #if snail_score > 5 #Adjust as needed
        #Smiles
        blooky "i guess my advice really helped..... i’m glad...."
        
        #if snail_score < 0
        #blook "um...... i'm not a snail......... i'm sorry....."
        
        jump end_blook_hangout2

    label end_blook_hangout2:
        #neutral
        blooky "well, that’s all i have to say...."
        blooky "if you have any more questions about snails, you can always find me..... i’ll be around...."
        jump blooky_ruins
        
        
    ##################################################################      HANGOUT 3       ##################################################################



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
            "Hey… Napstablook?": #(+1 FP)
                blooky "huh? oh, hi........."
                jump somethings_wrong
                
            "Sneak up on Napstablook and frighten them.": #(-3 FP)
                blooky "..........."
                #Surprised
                blooky "oh! oh....... it’s just you...."
                jump somethings_wrong
                
            "Leave before they notice you.": #(+0 FP)
                blooky "..........."
                "You ditched Napstablook."
                jump end_blook_hangout3
                
    label somethings_wrong:
        blooky "..........."
        
        menu:
            "What are you doing?": #(+1 FP)
                blooky "oh.... nothing... it doesn’t matter..."
            "You seem distracted.": #(+0 FP)
                blooky "..........."
                blooky "what? oh, sorry....."
                
        menu:
            "Tell me what’s wrong.": #(-1 FP)
                blooky "oh, um... i guess... if you say so......."
            "If something happened, you can tell me.": #(+2 FP)
                blooky "well....... it’s not that big of a deal, really... but i guess, if you want to know...."
                
        blooky "my headphones.... they broke yesterday. they’re pretty old, so it’s not that surprising, but....... i really liked them......"
        blooky "so i’m looking for new ones. none of the shops sell them.... or not good ones, anyway. i have to find them in the garbage......"
        
        menu:
            "I’ll help you look!": #(+3 FP)
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
            "Give it to Napstablook.": #(+1 FP)
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
            "Give it to Napstablook.": #(+1 FP)
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
            "Give it to Napstablook.": #(+2 FP)
                blooky "oh, wow.... that’s pretty. thanks......"
            "Keep it for yourself.": #(+0 FP)
                "It’s too pretty to just leave it in the trash. You give it a little shake before putting it in your pocket."
                ###### ITEM GET SNOW GLOBE ######
            "Put it back.": #(+0 FP)
                "This isn’t what you’re looking for, anyways."
            "Break it.": #(-2 FP)
                "The glass makes a satisfying sound as it shatters."
                blooky "did... something break?"
                
                $ broke_snowglobe = True
                jump snowglobe_q
        
        $ smltrash_searched += 1
        jump search_trash
    
    label snowglobe_q:
        menu:
            "No.": #(-2 FP)
                blooky "oh.... because it sounded like....."
                blooky "nevermind......."
            "Yeah. Don’t worry about it.": #(-1 FP)
                blooky "um.... why......"
                blooky "okay........."
            "It was an accident.": #(+0 FP)
                blooky "oh, that’s sad......."
        $ smltrash_searched += 1
        jump search_trash
    
    label headphones_found:
        menu:
            "Give it to Napstablook.": #(+5 FP)
                #Smiling
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
            "Break them.": #(-5 FP)
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
            "Nothing…": #(-4 FP)
                blooky "are those... headphones?"
            "Show them the broken headphones.": #(-4 FP)
                blooky "oh....... you broke them......"
            "I didn’t mean to…": #(-2 FP)
                blooky "oh....... um, sure... that’s okay, i guess......."
        jump sad_ending
                
    label sneak_headphones_q:
        menu:
            "Oh no… I think that was a pair of headphones, sorry!": #(+0 FP)
                blooky "oh...... that’s bad luck.... i guess i should’ve expected something like this to happen…"
            "Gosh… I’m so clumsy, I’m sorry.": #(+0 FP)
                #Frowning
                blooky "those were headphones, weren’t they? And they probably won’t work now that they’re all wet...."
        
        blooky "that’s okay........ we can keep looking, i guess...."
        jump search_trash
                
                
    label whats_next:
        menu:
            "No problem! I’m happy to help.": #(+3 DP)
                blooky "i’m going to go try them out right away. thanks again....."
                jump end_blook_hangout3
            "I’d like to keep looking around, if that’s okay.": #(+1 FP)
                blooky "oh, sure.... i’ll just be here if you need me......"
                jump search_trash
            
    label end_blook_hangout3:
        if headphones_given is False:
            blooky "oh, is that all you could find?"
        
        if headphones_found is True:
            blooky "thanks again for your help... i’m really glad you found me here. see you around......."
        if sneak_broke_headphones is True:
            #Frowning
            blooky "don’t worry about it... it was an accident. i can just look for headphones...... somewhere else....... i’ll go do that... bye........"
        if headphones_given is False:
            blooky "we didn’t find the headphones, but that’s okay... i can just look somewhere else...... i’ll see you later... "
        jump blooky_ruins
    
    label sad_ending:
        #Sadly
        blooky "you know... um....... i think i’ll just... go look somewhere else......."
        jump blooky_ruins


    ##################################################################        DATE          ##################################################################
                
                
                
    label blooky_questions_date:
        #Event Name: "Blooky's Date"
        #Event Trigger:
        
        
        "Hey!"
        "It's a small white dog, chewing on the remnants of a script."
        "The Annoying Dog has fled."
        jump blooky_ruins