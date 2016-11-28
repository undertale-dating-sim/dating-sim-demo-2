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
    $ listened_music = False
    
    menu:
        "Like Karaoke, but Without the Lyrics on the Screen":
            jump blooky_event1
        "Snail Hunting is an Art":
            jump blooky_event2
        "One Man's Trash...":
            jump blooky_event3
        "Blooky's Date":
            jump blooky_hb_date
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
                $ listened_music = True
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
                $ likedmusic = True
                
                blooky "really?"
                blooky "oh....... i wasn’t expecting that...."
                blooky "thank you......"
                menu:
                    "Yeah! You should make an album.": #(+2)
                        blooky "oh..... i don’t know.... that sounds kind of daunting......."
                        blooky "but maybe.... i’ll think about it......."
                        jump end_blook_hangout1
                    "Have you showed this to anyone else?": #(+0)
                        blooky "um, no.... just you so far...."
                        menu:
                            "That’s probably for the best.": #(-4 FP)
                                blooky "oh....... if you say so......."
                            "You should, I bet people would love it!": #(+2 FP)
                                blooky "oh....... you think so?"
                                blooky "maybe.... i could show it to Frisk.... they always like my music, even when it’s bad......"
                    "It’s actually starting to get a little repetitive...": #(-2)
                        blooky "sorry....... i’ll turn it off now...."
                        $ likedmusic = False
                        $ dislikedmusic = True
                        # jump end_blook_hangout1
                
            "It’s not really my style…": #(-2 FP)
                blooky "sorry....... i’ll turn it off now...."
                $ dislikedmusic = True
                jump end_blook_hangout1
                
            "Dance": #(+3 FP)
                blooky "what are you... doing?"
                $ isdancer = True
                $ likedmusic = True
                menu:
                    "I’m dancing, obviously!": #(+1 FP)
                        blooky "oh... i couldn’t tell......"
                        blooky "oh, um.. don’t take that the wrong way... i was trying to be funny.... you’re, uh.... a really good dancer..........."
                        menu:
                            "That’s okay, I know I suck.": #(-1 FP)
                                blooky "oh........"
                                blooky "...."
                                blooky "can i ask, um.... why do you do it, then?"
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
                            "Damn right I am!": #(-2 FP)
                                blooky "um....... yeah........"
                                jump end_blook_hangout1
                            "Dance with me?": #(+2 DP)
                                #Blushing
                                blooky "oh.... i don’t know.... i’m not very good......."
                                menu:
                                    "That’s okay, I’m not either.": #(+1 FP)
                                        #Frowning
                                        blooky "oh, no.... you’re...... okay... "
                                    "You don’t know until you try!": #(-1 FP)
                                        #Neutral
                                        blooky "i have tried, though... that’s how i know........"
                                blooky "um.... i think i’ll pass this time.... sorry....."
                                jump end_blook_hangout1
                
                    "“Oh, nothing…": #(+0 FP)
                        "You stop dancing."
                        blooky "oh... okay......"
                        blooky "you, uh.... didn’t have to stop.."
                        jump end_blook_hangout1
                        
            "Sing along" if issinger:
                #Smiling
                $ likedmusic = True
                blooky "ha...... haha...."
                blooky "oh, sorry, you have a good voice, it’s just.... i guess the song wasn’t really meant to have lyrics... "
                blooky "not that yours aren’t.... creative.... haha... "
                
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
                        
                        menu:
                            "So you’re saying I win?": #(-1 FP)
                                blooky "oh.... yeah, i guess......."
                                jump end_blook_hangout1
                            "C’mon… just try? I promise I won’t laugh, or anything.": #(+1 FP)
                                blooky "um... well.... i suppose i could try....."
                                "Napstablook starts singing so quietly that you can’t even understand them."

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
                
                
                
    label blooky_hb_date:
        #Event Name: "Blooky's Date"
        #Event Trigger: A meddling small white dog
        
        ####### TEMP TESTING!!!! #######
        $ isdancer = True
        
        python:
            question_num = 0
            prev_qs = [0]
            
            likesart = False
            likesreading = False
            likesguns = False
            likescooking = False
            likesexercise = False
            
            didnothing = False
            asked_ghostfood = False
            feelliketrash = False
            dislikedmusic = False
            
            asked_1 = False
            asked_2 = False
            asked_3 = False
            asked_4 = False
            asked_5 = False
            asked_6 = False
            asked_7 = False
            asked_8 = False
            asked_9 = False
            asked_10 = False
            hobbies_asked = False
        
        #Surprised
        blooky "really?"
        blooky "hangout........with me? that’d be nice..."
        #Normal/Happy
        blooky "sure.....if it’s not too much of a bother..."
        blooky "..... ...well i know a place nearby we can go..."
        blooky "follow me...."
        
        #Fade black
        
        blooky "..."
        
        #Scene chage: Front of Ruins
        
        blooky "oh good"
        blooky "it’s empty"
        
        menu:
            "Just the two of us, then.": #(+ DP)
                #Normal/Happy
                blooky "yeah..."
                blooky "just you and me..."
                blooky "i hope that’s okay.... ...i come to the ruins to usually be alone so..."
                blooky "usually my music is good company"
                
                #tiny smile
                
                blooky ".... ....but so are you"
            "Is that okay?": #(+ FP, +Kindness)
                blooky "i think so yeah..."
                blooky "i usually like being alone with my music..."
                blooky "i don’t mind it at all..."
            
            "Are people avoiding you?": #(+ HB)
                #Sad
                blooky "i don’t know......"
                blooky "i really wouldn’t be surprised if they did....."
                blooky "i can understand that i’m a downer"
                blooky "i learned to accept it......"
                
                jump downer_response
        jump date_start
                
        label downer_response:
            menu:
                "Well I don’t think you’re a downer.": #(+ HB)
                    #Happy/ Tiny smile
                    blooky "oh.... good..."
                    blooky "im glad.... ... at least there’s still you"
                "Quietly smile.": 
                    #(+0 HB FP DP)    
                    $ bump = 0
            jump date_start
                    
        label date_start:
            
            blooky "so"
            blooky "how do we start this?"
            
            #Blushing deeply
            
            blooky "to be honest... ...it’s been awhile since i last got to hang out with someone....."
            blooky "....."
            blooky "..........."
            blooky "maybe we could... ask each other questions? that’s how people get to know each other.... right?"
            
            menu:
                "The cliche approach. How original.": #(+ HB)
                    blooky "oh...thanks... it’s no big deal...."
                    blooky "well... i guess...... we can take turns..... or something..."
                "I guess, if that’s what you want to do…": #(+ FP)
                    blooky "oh..... um........ okay...."
                    blooky "i  guess i’ll start...... we can take turns....."
            jump blooky_date_questions
        
        label blooky_date_questions:
            python:
                blooky_asking = True
                while blooky_asking is True:
                    randnum = renpy.random.randint(1, 11)
                    if randnum in prev_qs:
                        continue
                    else:
                        prev_qs.append(randnum)
                        blooky_asking = False
                        question_num += 1
                        
            #$ randnum = 1
            "%(randnum)d" 
            
            if (randnum is 1) and (asked_1 is False):
                $ asked_1 = True
                # Normal
                blooky "um......."
                blooky "if you don’t...... mind me asking......."
                blooky "how did.... you end up down here...?"
                blooky "i know you fell but..... how did you..... manage to fall into.... such a big hole?"
                blooky "how did you wind up down here?"
                
                menu:
                    "I mean, it was a {i}really big hole.{/i}": #(+HB)
                        blooky "well....... i can understand that......."
                        blooky "i didn’t mean to sound...... offensive or......."
                        blooky "to come off in such a way...... sorry...."
                        blooky "i was just wondering........"
                        blooky "because........... well........"
                        blooky "i’ve heard some people don’t actually...... fall down here for good reasons...."
                        blooky "....but...."
                        blooky "..........."
                        #Sad
                        blooky "i’m sorry..... maybe this is a touchy subject........."
                    "I wasn’t really paying attention too much where I was going.": #(+FP)
                        blooky "i get it... sometimes i’m not paying too much attention either..."
                        blooky "though...i never run into anything or fall really..."
                        blooky "since you know….i’m a ghost..."
                        blooky "........"
                        #Sad
                        blooky "i...hope you didn’t hurt yourself too much..."
                        blooky "...when you fell down here"
                        #Normal
                        blooky "just...be careful, okay?"
                    "...": #(+0 FP DP)
                        blooky "it’s ok...."
                        blooky "......you don’t have to answer"
                        blooky "..........."
                        #Sad
                        blooky "i’m sorry..... maybe this is a touchy subject........."
                    "I’m not really comfortable… answering.": #(+FP)
                        #Sad
                        blooky "oh......"
                        blooky "i understand... it’s ok it’s....."
                        blooky "it was wrong of me to ask........ i understand, i’m sorry"
                        #Normal
                        blooky "but..... for whatever reason it might be......."
                        #Smile
                        blooky "i’m.....glad you’re here"
            if (randnum is 2) and (asked_2 is False):
                $ asked_2 = True
                #Normal
                blooky "i really find this place.... well......"
                #Smile
                blooky "peaceful"
                blooky "...... what do you think about this part of the ruins?"
                
                menu:
                    "It’s not the best place for a first date...": #(+HB)
                        #Surprised
                        blooky "oh..... date.......?"
                        #Normal
                        blooky "i just... figured maybe this would be better than....... .....a busy place...."
                        blooky "i don’t really like crowded places and this is the most quiet...... um....."
                        blooky ".....sorry, maybe i should have asked you where you wanted to go"
                        
                        menu:
                            "Maybe next time I’ll tell you where to go, it’ll be fine.": #(+HB)
                                #Surprised
                                blooky "n-next time.....?"
                                blooky "......."
                                #Blushing
                                blooky "i....... okay..... i’d like that......."
                            "Yeah you should’ve.": #(+HB)
                                #Sad
                                blooky "i-i’m sorry......"
                                blooky "....... really.... really sorry........."
                                blooky "um......"
                                blooky "lets just... keep going......."                            
                            "No, this is fine, don’t worry!": #(+FP)
                                #Normal
                                blooky "oh..... are you sure?"
                                blooky "well....... thanks..... "
                                #Smile
                                blooky "......i’m glad you like this place...."
                                blooky "even if it’s only a little bit"
                    "It’s kind of eerily quiet.": #(+FP)
                        blooky ".....is it?"
                        blooky "i like it quiet sometimes....."
                        blooky "don’t be worried… we’re here together, so....."
                        blooky "maybe it won’t be as scary as you think....."
                    "I don’t really like it here.": #(-HB)
                        #Sad
                        blooky "o-oh.........."
                        blooky "...sorry, i guess i should’ve picked more carefully..."
                        blooky "........"
                        blooky "sorry..."
                    "I couldn’t really care less about this place.": #(+HB)
                        #Sad
                        blooky "oh"
                        blooky "........you don't like it?"
                        
                        menu:
                            "I like you, but not this place.": #(+HB)
                                #Blushing
                                blooky "o-oh..... really?"
                                blooky "well........"
                                #Smile
                                blooky "i guess that means... so long as we’re together... we’ll be alright"
                            "Well maybe a little bit.": #(+FP)
                                #Smile
                                blooky "oh, good....."
                                #Normal
                                blooky "i was worried that..... I chose a bad spot..."
                                #Smile
                                blooky "i'm glad you like it though..."
                                blooky "even just a little"
                            "Nah.": #(-FP)
                                #Sad
                                blooky "oh..... i'm sorry....."
                                blooky "maybe....... next time i’ll try to find someplace else.........."
                                blooky ".....i'm sorry....."
                        
            if (randnum is 3) and (asked_3 is False):
                $ asked_3 = True
                blooky "i know you haven’t been underground that long, but..."
                blooky ".....i hope you’re enjoying yourself"
                blooky "........"
                #Sad
                blooky "“i hope i’m not boring you too much either........ i'm sorry........"
                
                menu:
                    "This could be worse, but at least you’re trying.": #(+HB)
                        blooky "yeah...sorry... i wanted to pick something you’d like..."
                        blooky "sorry...if i’m getting on your nerves..."
                        blooky "..."
                    "I’m just a little tired, but I’m having fun.": #(+FP)
                        blooky ".......oh..... do you need to rest?"
                        blooky "i’m happy you’re having fun..... but......"
                        blooky "if you’re tired you should really get some rest......."
                        blooky "i don’t want to be....... taking up your time"
                        
                        menu:
                            "You're not.": #(+FP)
                                blooky "are you sure?"
                                blooky "well..... ok then....."
                                blooky "so long as you’re okay....."
                            "I'll get over it.": #(+0)
                                blooky "ah........... alright..."
                                blooky "if you're sure......."
                                blooky "hm........."
                    "It gets pretty dull around here, I won't lie.": #(-FP)
                        blooky "you think so?"
                        blooky "i’m sorry....... i wish i was better at entertaining people......."
                        blooky "i don’t go out much..... and i’m usually alone so......"
                        blooky "this is all new to me...... too......"
                        #Sad
                        blooky "i'm sorry......."
            if (randnum is 4) and (asked_4 is False):
                $ asked_4 = True
                blooky "actually......"
                blooky "i think you’d get along with my cousin......"
                blooky "for some reason..... you two seem alike......"
                blooky "........"
                blooky "what do you think of robots?"
                
                menu:
                    "Robots are cool.": #(+HB)
                        $temp = 0
                        jump coolrobot
                    "They’re pretty neat, I guess.": #(+FP)
                        label coolrobot:
                            #Smile
                            blooky "yeah?"
                            blooky ".....my cousin is a robot....."
                            blooky "and if you like robots....... then you two will get along really well....."
                            blooky "that...... makes me happy."
                    "Depends on the robot...": #(+0)
                        blooky "well....."
                        blooky "the kind that cook...dance..... sing......."
                        blooky "star in their own movies and shows"
                        blooky "......the kind that can do anything i guess?"
                        blooky "do you like those kind of robots?"
                        
                        menu:
                            "Oh, definitely!": #(+FP)
                                #Smile
                                blooky "yeah?"
                                blooky ".....my cousin is a robot....."
                                blooky "and if you like robots....... then you two will get along really well....."
                                blooky "that...... makes me happy."
                            "They're alright, I guess.": #(+HB)
                                blooky "......."
                                blooky "i’m sorry if the conversation is boring......."
                                blooky "we can talk about something else......."
                            "Not really.":
                                blooky ".....oh......"
                                blooky "well..... ok..."
                                
                                menu:
                                    "I hope that didn’t come out wrong!": #(+FP)
                                        blooky "no... no it's ok..."
                                        blooky "i just..... wish you'd give robots a chance....."
                                        blooky "......but oh well..."
                                    "But I do like ghosts.": #(+HB)
                                        blooky "a-ah....."
                                        #Blushing
                                        blooky "well........"
                                        blooky "that’s good........ i think"
                                    "Shrug.":
                                        blooky "........."
            if (randnum is 5) and (asked_5 is False):
                $ asked_5 = True
                blooky "well....... i only really ever come here to relax..."
                blooky "sometimes, i’m just not in the mood to talk or do anything"
                blooky "........not all the time..."
                blooky "but most of the time"
                blooky "..."
                blooky "do....... you ever feel like escaping sometimes?"
                
                menu:
                    "Yeah, for the most part.": #(+HB)
                        blooky "really? i can relate....."
                        blooky "that...... makes me relieved."
                        blooky "i always thought i was the only one"
                        #Smile
                        blooky ".........this is nice"
                    "Not really, no.": #(+FP)
                        blooky "..........must be nice"
                        blooky "to not have to worry about....... running away....."
                        blooky "........."
                    "Only from people with an emotional crisis.": #(-FP)
                        blooky "........"
                        blooky "......oh"
                        #Sad
                        blooky "i’m sorry i....... i didn’t realize......."
                        #Normal
                        
                        menu:
                            "That’s not what I meant, I’m sorry...": #(+FP)
                                blooky "oh.....?"
                                blooky "it's ok....."
                                blooky "i was just worried that..... i was annoying you....."
                                blooky "i wouldn't be surprised..... but it's fine......"
                            "It’s okay, I’ll be around to cheer you up.": #(+HB)
                                blooky "...really?"
                                blooky "oh..... good."
                                blooky "i know that i..... get sad a lot..... it can make people uncomfortable and upset....."
                                blooky "maybe with you around i can cheer up more"
                            "Don’t worry about it.": #(+0)
                                blooky ".........."
                                blooky "alright....... i won't..."
            if (randnum is 6) and (asked_6 is False):
                $ asked_6 = False
                blooky "i wouldn’t call myself a hermit but"
                blooky "i like to be alone a lot..."
                blooky "....."
                blooky "if i want company i usually just go to work on the family snail farm..."
                blooky "or sometimes i even turn on the tv to watch something"
                blooky "it’s nice to go out now and again, though"
                blooky "..."
                #Contemplative
                blooky "while you were on the surface,"
                blooky "were there places you wanted to go to meet new people?"
                
                menu:
                    "Yes.": #(+HB)
                        blooky "you..... don’t sound very happy about that..."
                        blooky "but i guess any chance you could get was a good one..... right?"
                        blooky "that must feel nice though..... to meet new people..."
                    "A few places.": #(+FP)
                        blooky ".....well, even a few places is better than no place, right?"
                        blooky "that's good......"
                    "I don’t socialize much.":
                        blooky "oh..... really?"
                        blooky "well..... i don’t either... if that makes it any better..."
                        
                        menu:
                            "I’d rather just talk to you.": #(+HB)
                                #Blush
                                blooky "that's........."
                                blooky "......."
                                #Smile
                                blooky "you're really nice....."
                            "That’s why we get along so well.": #(+FP)
                                blooky "yeah?"
                                blooky "we do..... don't we....."
                                blooky "hehe....."
                            "I just don’t see a point in it.": #(-FP)
                                blooky "i understand..."
                                blooky "i’m the same way sometimes, but......"
                                blooky "some days it’s really nice to go to a friend..... or just..... let go....."
                                blooky ".....well for me at least"
            if (randnum is 7) and (asked_7 is False):
                $ asked_7 = True
                blooky "i actually come here to cry sometimes..."
                blooky ".....not a lot, but enough i guess to not want others to see what i’m doing"
                blooky ".....and i like to lay down in my house and feel like trash..."
                blooky "i could stay home where no one can see me, but....."
                blooky "some days i wind up here anyway..."
                blooky "......."
                blooky ".....do you ever feel like trash?"
                
                label trash_q:
                    menu:
                        "Excuse me?!" if feelliketrash is False: #(-FP)
                            blooky "huh?"
                            blooky "n-no..... not..... bad..... but-"
                            blooky "i don’t know how to....... explain myself..."
                            blooky "just laying around....... not caring what happens?"
                            blooky "just..... laying around... like trash........"
                            blooky "......."
                            
                            menu:
                                "Oh... well, in that case...":
                                    $ feelliketrash = True
                                    jump trash_q
                                "I am NOT trash!": #(+HB)
                                    blooky "i-i didn’t mean for it to sound like....."
                                    blooky "that’s not......."
                                    #Sad
                                    blooky "i’m so sorry....... i’m sorry............"
                                    blooky "........ah........  i’m really bad at this..... forgive me......."
                                        
                                    menu:
                                        "It’s okay, I’ll forgive you this time.": #(+HB)
                                            #Smile
                                            blooky "oh... thank you..."
                                        "Oh, no, it’s okay. Sorry I overreacted.": #(+FP)
                                            blooky "really... are you sure?"
                                            #Smile
                                            blooky "...thank you..."
                            #Normal
                        "Yes, I do sometimes.": #(+FP)
                            blooky "maybe..... then....."
                            blooky "we could feel like trash together?"
                            blooky "sometime?"
                        "Not really.": #(+FP)
                            blooky "oh....."
                            blooky "well..... maybe you should try it sometime..."
                            blooky "it’s not so bad..... it’s kinda relaxing....."
                        "Only trash should feel like trash.": #(+HB)
                            blooky "i... well......"
                            blooky "i am trash..."
                            
                            menu:
                                "Then I guess you’re cute and classy trash.": #(+HB)
                                    blooky "heheheh........."
                                    #Smile
                                    blooky ".....do you really think i’m classy?"
                                    blooky "........maybe some other time..... i can show you my....."
                                    blooky "{i}dapperblook{/i}"
                                "No you aren’t!":#()
                                    blooky "i just..... feel like it sometimes......."
                                    blooky "but..... i know i shouldn’t talk that way around people......."
                                    blooky "i’m sorry..."
            if (randnum is 8) and (asked_8 is False):
                $ asked_8 = True
                blooky "......."
                blooky "did i mention that i own a snail farm?"
                blooky "probably but my memory isn’t great....."
                blooky "it’s been in the blook family for generations"
                blooky "there’s racing and show snails for everyone to see......."
                blooky "there aren’t many of us left... just me....... so i’m taking care of it..."
                blooky "do you like snails?"
                
                menu:
                    "Yes.": #(+HB)
                        blooky "oh, cool..."
                        blooky "maybe you can stop by the farm sometime..."
                        blooky "i think you’ll like it"
                    "I don’t ‘dislike’ them?": #(+FP)
                        blooky "well..... that's good..."
                        blooky "maybe you can stop by the farm sometime..."
                        blooky "you might like it..."
                    "Ew, no!": #(+FP)
                        blooky "........oh"
                        blooky "well....... that's ok..."
                        blooky "we can always go somewhere else...... so..... i'm not worried about that..."
                        
            if (randnum is 9) and (asked_9 is False):
                $ asked_9 = True
                blooky "what type of music do you like listening to?"
                blooky "if it’s okay to ask....... you probably haven’t heard anything in awhile since you fell..."
                blooky "but....... did you like anything when you used to be on the surface?"
            
                label musicq:
                    menu:
                        "Pop":
                            blooky "pop?"
                            blooky "isn’t that a drink...?"
                            blooky "well....... i guess that would sound cool..."
                            blooky "i think i like pop, too"
                        "Hip Hop and R&B":
                            blooky "hip..... hop.....?"
                            blooky "i don’t think i’ve heard of that before..."
                            blooky "it must be hip"
                            blooky "does it get humans to hop?"
                        "Trap and Trance":
                            blooky "trap?"
                            blooky "there are a lot of old puzzles and tests through the ruins..."
                            blooky "i’m sure if you get a few wrong, you’ll find plenty of traps..."
                            blooky "........."
                            blooky "though i don’t think they sound all that great, to be honest"
                        "Dance and Techno":
                            blooky "dance and techno... huh..."
                            blooky "technology types of things sound like something the royal scientist would know about..."
                            blooky "and i can’t dance..."
                            blooky "at least........ not well..."
                        "Classical and Instrumental":
                            blooky "i don’t know what classical is... but..."
                            blooky "instrumental i do."
                            blooky "i think..... i like instrumental, too..."
                            blooky "i don’t have a lot of instruments, though....."
                            blooky "......."
                            blooky ".......sometimes, i hear someone playing a trombone..."
                        "Kpop and Jpop":
                            blooky "what do the k and j stand for?"
                            blooky "is it different from the regular pop?"
                            blooky "........"
                            blooky "sounds unique..."
                        "Oldies music":
                            blooky "oldies?"
                            blooky "old music?"
                            blooky "........"
                            blooky "i do have a few records in my room..."
                            blooky "...maybe you’ll like to hear them sometime..."
                        "Jazz and Swing.":
                            blooky "i’ve heard of jazz and swing before..."
                            blooky "i can’t say i listen to it all the time...... but it’s nice every now and then"
                            blooky "we have similar tastes"
                            blooky "......."
                            #Smile
                            blooky "that's cool"
                        "I don't like music." if dislikedmusic is False: #(-FP)
                            blooky "really?"
                            blooky "well......"
                            blooky "what do you like?"
                            
                            menu:
                                "I messed up, I actually do like music.": #(+FP)
                                    $ dislikedmusic = True
                                    blooky "oh, that’s ok."
                                    blooky "so... what kind of music do you like?"
                                    jump musicq
                                "Well, it's not music.":
                                    #Sad
                                    blooky "........"
                                    blooky "well..... that's ok"
                                    blooky "..................."
                                    blooky "i guess....."
                                "You.": #(+HB)
                                    blooky ".....o-oh.....?"
                                    blooky "well..... well....."
                                    blooky "i like you too..."
                                    blooky "......"
                                    #Smile
                                    blooky "...but i also like music."
            if (randnum is 10) and (asked_10 is False):
                $ asked_10 = True
                blooky "um....."
                blooky "sorry..... i’m not very talkative"
                blooky "it's hard to get to know people... or talk to people..... or purposefully approach people......."
                blooky "you know?"
                
                menu:
                    "Yeah, I understand how you feel.": #(+FP)
                        blooky "yeah"
                        blooky "it feels..... like it takes up a lot of energy"
                        blooky ".....i get tired easily and i start to feel..... small....."
                        blooky "it’s easier to just avoid it altogether"
                    "Don't worry, you never have to feel that way with me.": #(+HB)
                        blooky "oh........ well, that's nice........"
                        blooky "i'm glad......"
                        blooky ".....you make me feel very..... relaxed"
                        #Smile
                        blooky "it's really..... nice"
                    "Um... no? I don't know.": #(-FP)
                        blooky "oh..... well....."
                        blooky "that's fine..... i guess"
                        blooky "we don’t have to have everything in common to be friends"





        label ask_blooky:
            # Normal
            if question_num is 1:
                blooky "okay.... um..... i think it’s your turn to.... ask a question. if you want to, i mean..."
            if question_num is 2:
                blooky "um.... it’s your turn... again....."
            if question_num is 3:
                blooky "i’m sorry..... is this boring? maybe this question thing was a bad idea....."
                menu:
                    "I'm having fun! Let's keep going!": #(+FP)
                        #Happy
                        "really? okay, it's your turn then..."
                    "It's never boring hanging out with you.": #(+DP)
                        #Blushing
                        blooky "o-oh..... ha..... that's nice of you to say......"
                        blooky "let's keep going, then, if you're having fun...... it's your turn, then....."
                    "Yeah, I'm bored. Let's stop.": #(-DP)
                        jump end_blook_date
            if question_num is 4:
                blooky "okay, you go... i think i like it better when it's your turn to ask the questions..... it's less pressure......"
            if question_num is 5:
                blooky "i think i'm out of questions.... i can't think of any more...."
                blooky "sorry, i guess we should stop......"
                blooky "oh, but that's not fair..... i've asked five questions, and you've only asked four.... do you want to ask another question?"
                menu:
                    "Yeah, just one more!": #(+ FP)
                        blooky "okay.... make it a good one..... or don't...... whatever you want."
                    "No, I'm done, too.": #(+0)
                        blooky "okay..... well......"
                        jump end_blook_date
            if question_num >= 6:
                jump end_blook_date
                
            menu:
                "What do you think of humans?": #(+ DP)
                    blooky "they seem really nice..."
                    #Happy
                    blooky "...and so are you... so..."
                    #Normal
                    blooky "i think monsters might really have... a chance....."
                    blooky "once we get out of here...... maybe."
                    blooky "it's been a long time since the last human fell down here......"
                    blooky "a really long time, it feels like...."
                    #Happy
                    blooky "but they're just as nice as you... so all humans must be, right?"
                    
                    menu: 
                        "I'd like to think so!": #(+DP)
                            #Smile
                            blooky "hehehe...."
                            blooky "me too."
                        "Definitely not.": #(-FP)
                            $ temp = 0
                            jump notnice
                        "Not all of us are nice.": #(+HB)
                            label notnice:
                                blooky "huh?"
                                blooky "what do you mean?"
                                menu:
                                    "Some people are just jerks.": #(-FP)
                                        blooky "oh"
                                        blooky "..........well, i just hope that..."
                                        blooky "you aren’t one of them..."
                                    "Nothing, sorry about that.":
                                        blooky ".....oh..."
                                        blooky "it’s ok..."
                                    "I’m worried that I’m the only that can be trusted.": #(+HB)
                                        blooky "that’s....that’s not true..."
                                        blooky ".....frisk is another human like you and....."
                                        blooky "and they would never hurt anyone.... they said so themselves..."
                                        blooky "........."
                                        blooky "i know.... that.... its hard, ‘cause i’m the same way..."
                                        blooky "if..... if anything..."
                                        blooky "you can always trust me........ know that"
                "Can you eat normal food? Does it phase through you?": #(+ FP)
                    $ asked_ghostfood == True
                    blooky "human food passes through me, yeah"
                    blooky "but ghost food... and monster food...."
                    blooky "that i can actually digest"
                    blooky "....."
                    blooky "........."
                    blooky "have you ever had a ghost sandwich?"
                    blooky "they’re my favorite thing to eat when i’m at home......"
                    blooky "last time i offered a human a ghost sandwich.... ....they had trouble holding it"
                    blooky "i felt bad that they didn’t get to try it......."
                    blooky "so i think it’s the other way around... humans can’t eat ghost food?"
                    blooky "........"
                    blooky "i’m sorry......i got carried away... i talk too much sometimes..."
                    
                    menu:
                        "What do ghost sandwiches taste like?":
                             blooky "well....."
                             blooky "they taste light and fluffy..."
                             blooky "like a ghost"
                             blooky "......."
                             blooky "not that i eat ghosts"
                             blooky "i think that’s called cannibalism"
                        "No need to apologize!": #(+FP)
                            blooky "oh, i’m..."
                            blooky "i’m just so used to apologizing that it kind of just slips..."
                            blooky "i’m sor--"
                            blooky ".........heh........."
                            blooky "..........my bad."
                        "I’m probably the only person who likes your rambling.": #(+HB)
                            blooky "yeah......probably.........."
                            blooky ".....but....... that’s good...... right?"
                            blooky "so long as i’m not.... boring you or anything......."
                            blooky "then i guess it’s ok..."
                
                "How can you be so cute?":#if DP > XXXXX: #(++DP) ONLY ON TL ROUTE
                    #Surprised
                    blooky "i-i......"
                    #Blush
                    blooky "........i don't think i am... ...but..."
                    blooky "i don't know......"
                    blooky "am i really cute...?"
                    blooky "....."
                    blooky "............"
                    blooky "i don't know what to say....."
                    blooky "i guess lying around feeling like trash helps..."
                    
                    menu:
                        "Must be adorable trash then.": #(+HB)
                            blooky "huh?"
                            #Normal
                            blooky "i'm......... i wouldn't say that........."
                            blooky "i don't think so..... at least,but....."
                            #Smile
                            blooky "thanks..... i think..."
                        "You're not trash, you're just cute!": #(+DP)
                            blooky "..........i......"
                            blooky ".....i don't know what to say"
                            blooky "oh..... that sounds... it's pretty... uh....... spiffy."
                        "Maybe!": #(+FP)
                            #Smile
                            blooky "hehehe"
                            #Normal
                            blooky ".....it's the only thing that makes sense."
                
                "What's up with the waterworks?":#if HB > XXXXX: #(++ HB) ONLY ON HB ROUTE
                    # Sad
                    blooky "i-i. ......"
                    blooky "i get emotional sometimes it just.... ....i don’t...."
                    blooky "i don’t know......"
                    blooky "does it bother you?"
                    blooky "......"
                    blooky "......that i cry too much?"
                    blooky "i can’t help it... i’m sorry if it bothers you..."
                    blooky "i guess lying around feeling like trash helps..."
                    
                    menu:
                        "Must be adorable trash, then.": #(+HB)
                            # Blushing
                            blooky "huh?"
                            blooky "im........i wouldn’t say that....."
                            blooky "i don’t think so.....at least, but....."
                            blooky "thanks.......i think..."
                        "You’re not trash, you’re just cute!": #(+FP)
                            # Blushing
                            blooky ".............i...."
                            blooky ".......i don’t know what to say"
                            blooky "oh..... that sounds.... it's pretty..... uh........ spiffy"
                        "Maybe!": #(+FP)
                            #Smiles
                            blooky "hehehe"
                            blooky ".....it’s the only thing that makes sense"
                            
                "What are your hobbies?": #(+HB +FP)
                        
                    blooky "i like to make music"
                    blooky ".....i like to think i’m good at it... i’ve been told it’s pretty good, but..."
                        
                    if listened_music = False:
                        $ hobbies_asked = True
                        
                        blooky "i’m afraid to show it to too many people........"
                        blooky "i don’t want to bother everyone with myself....."
                        blooky "......oh..."
                        #Sad
                        blooky "i made myself sad... i’m sorry"
                        
                        menu: 
                            "Don’t be sad, that’s cool!": #(+FP)
                                #Happy
                                blooky "do you really think so?"
                                blooky ".....well......i enjoy it a lot..."
                                blooky "........i really would like to invite you to hear it sometime"
                                blooky "if.... you think it’s cool now"
                                blooky "wait until you hear it........"
                                #Smile
                                blooky "heheh......"
                            "Oh, I’m sorry.": #(+FP)
                                blooky "its not your fault....."
                                blooky "i always make myself sad........."
                                blooky "its just my thing.....it’s ok"
                            ".......": #(-DP)
                                blooky ".........."
                                blooky "well......"
                                blooky "thanks for...... being patient......"
                                blooky "letting me cry it out........ it always feels good to cry"
                                
                    elif dislikedmusic = True: #(ONLY AVAILABLE AFTER HANGOUT ONE -> DISLIKED MUSIC)
                        blooky "you... um... didn't seem to like it that much when i showed you..."
                        
                        menu:
                            "I'm sorry... it's not that it's not good, it's just not what I ususally listen to.": #(+FP)
                                blooky "oh..... that's okay... i understand....."
                                blooky "you don't have to like it... not everyone does..."
                                blooky "sometimes, i think people just pretend to like it to make me feel better"
                            "Not really, but my opinion doesn't matter. You should do what makes you happy.": #(+DP)
                                blooky "it matters to me..."
                                blooky "but... thanks..... i'll keep that in mind..."
                            "Do you think you could try to make something that I'd like next time?": #(+HB)
                                #Sad
                                blooky "um... maybe..... i could try..."
                                blooky "i'll try to do better next time....."
                                
                    elif likedmusic = True: #(ONLY AVAILABLE AFTER HANGOUT ONE -> LIKED MUSIC)
                        #Blush
                        blooky ".....you, um, seemed to like it, last time....."
                        
                        menu:
                            "Yeah! I had fun.":#(+FP)
                                #Surprise
                                blooky "r-really?"
                                #Smile
                                blooky "well, i'm glad you liked it....."
                            "We should do that again sometime.": #(+DP)
                                blooky "well, it takes a while to make a new song....."
                                blooky "but..... i'd like that....."
                                blooky "we don't even have to listen to my music..... we could listen to other artists, too."
                                #Smile
                                blooky "i think that would be just as fun..."
                
                "Were you ever even alive?": #(+HB)
                    blooky "but... i am alive......"
                    blooky "..."
                    blooky "i’ve always been like this..."
                    blooky "for as long as i can remember......"
                    blooky "which isn’t that far back, really...... i have a bad memory"
                    blooky "thinking about it hurts, though......"
                    blooky "and i don’t know why......."
                    blooky "......."
                    blooky "i'm sorry... i'm rambling again, you must be bored..."
                    blooky "now i feel bad..."
                    
                    menu:
                        "Most would say you're dead, but I like ghosts.": #(+HB)
                            blooky "oh... well....."
                            blooky ".......i'm glad you like ghosts..."
                            blooky "i’ve always been this way...... there’s no changing me......"
                            blooky "even if i wanted to change"
                            blooky ".....thanks for accepting me, though"
                        "Don't feel bad, this is interesting.": #(+FP)
                            blooky "is it?"
                            blooky "i’m sure that..... for most...... my rambling gets annoying"
                            blooky "i’m surprised you aren’t trying to... run or something."
                            blooky "........but..."
                            blooky "i’m glad you’re interested"
                        "I'm sorry, it was rude of me to ask...": #(+0)
                            blooky "n-no it’s okay, really"
                            blooky "i can see why some would wonder......."
                            blooky "i wish i had a better..... answer of..... some sort........"
                            blooky "........."
                            blooky "but i don’t"
                            blooky "i’m glad you’re interested, though"
                
                "Are any of the other monsters as nice as you?":#if DP > XXXXX: #(+DP +FP) #ONLY ON TL ROUTE
                    #Surprised
                    blooky "o-oh..... i mean...... i don't know"
                    #Normal
                    blooky "probably"
                    blooky "........"
                    blooky "that's very nice of you to say..... .....i try not to be a burden or a bother..."
                    #Happy
                    blooky "it makes me relieved, actually"
                    blooky "so..... i'm not boring you? that's good."
                    #Normal
                    blooky ".....but i know a few others who are really kind....."
                    blooky "i think you have nothing to worry about."
                    
                    menu:
                        "So long as they’re nice, I think I’ll be alright here.": #(+FP)
                            blooky "yeah..."
                            blooky "everyone is just great...... in their own way"
                            blooky "i think you’ll like it.......here........ for as long as you stay, of course"
                            blooky "i know..... like frisk..... humans that fall down here...... must be worried"
                            blooky "maybe you want to try going home........"
                            blooky "but maybe... also like frisk... you'll consider staying..... after you meet everyone?"
                        "I wasn’t worried!": #(+DP)
                            blooky "really?"
                            blooky "that's good..."
                            blooky "it means........ maybe you’ll have fun while you’re down here, right?"
                            blooky "i hope so, at least...... .i think you’ll like it here"
                        "That was me flirting, Blooky.": #(+HB)
                            #Surprised
                            blooky "f-flirting?"
                            blooky "oh...... oh i..."
                            #Blush
                            blooky "i don't think........ anyone's ever flirted with me before....."
                            blooky "........ah....... i'm sorry....."
                
                "Why is everyone down here so creepy looking?":#if HB > XXXXX: #(+HB +FP) #ONLY ON HB ROUTE
                    blooky "o-oh..... i mean..... i don't know"
                    blooky "i wouldn’t think everyone was creepy looking"
                    blooky "......."
                    blooky "everyone just looks different...... that's all."
                    blooky "i can understand that not a lot of humans are..... used to seeing people like..... us....."
                    blooky "monsters, and ghosts i mean."
                    blooky "but don’t be afraid..... not everyone is as scary as they look......."
                    blooky "......i know a few who are really kind..."
                    blooky "i think you have nothing to worry about"
                    
                    menu:
                        "So long as they’re nice, I think I’ll be alright here.": #(+FP)
                            blooky "yeah..."
                            blooky "everyone is just great...... in their own way"
                            blooky "i think you’ll like it.......here........ for as long as you stay, of course"
                            blooky "i know..... like frisk..... humans that fall down here...... must be worried"
                            blooky "maybe you want to try going home........"
                            blooky "but maybe... also like frisk... you'll consider staying..... after you meet everyone?"
                        "I wasn’t worried!": #(+HB)
                            blooky "really?"
                            blooky "that's good..."
                            blooky "it means........ maybe you’ll have fun while you’re down here, right?"
                            blooky "i hope so, at least...... .i think you’ll like it here"
                        "Not you, though.": #(+HB)
                            blooky "...huh?"
                            blooky "oh...... um....... i'm glad you think so--"
                            blooky ".....or don’t think so i guess.....?"
                            
                            menu:
                                "That was me flirting, Blooky.": #(+HB)
                                    #Surprised
                                    blooky "f-flirting?"
                                    #Blushing
                                    blooky "oh..... oh i...."
                                    blooky "i don’t think....... anyone's ever flirted with me before......."
                                    blooky "..........ah...... i'm sorry........."
                                "Well anyway, let's keep talking.":
                                    #Normal
                                    blooky "alright....."
                                    blooky "let’s keep talking then"
                
                "How long have you been down here?":#if DP > XXXXX: #(+DP) #ONLY ON TL ROUTE
                    #Normal
                    blooky "for as long as i can remember, really..."
                    blooky "that's all i can say... i don't remember ever being on the surface"
                    blooky "....."
                    blooky "sorry that i'm not much help with your questions..."
                    blooky "i hope i'm not troubling you..."
                    
                    menu:
                        "I was just curious, it's alright.": #(+FP)
                            blooky ".........."
                            blooky "if you're sure....."
                            blooky "......i wish i could remember more.... but i can't."
                            blooky "maybe because it never happened?"
                            blooky "......oh well......"
                        "You're no trouble at all!": #(+DP)
                            blooky "are you sure?"
                            #Sad
                            blooky "i feel like..... i've just been bothering you..."
                            #Normal
                            blooky "but....... if you say so, then....... i'll believe you"
                            blooky ".......i wish i could remember more for you, but....... i can't"
                            blooky "maybe because it never happened?"
                            blooky "......oh well......"
                        "You can't think back further?": #(+0)
                            blooky "......no......"
                            blooky "i wonder why....."
                            blooky "it's like..... my brain wants to just..... save me the trouble, i suppose"
                            blooky "heh......."
                            #Sad
                            blooky "doesn't..... want me to even bother........."
                
                "Did you choose to be a loner?":#if HB > XXXXX: #(+HB) #ONLY ON HB ROUTE
                    blooky "n-no..... not really..."
                    blooky "that’s all i can say..... i just have trouble getting..... comfortable around people"
                    blooky "i can’t help it..... i find myself just..... drifting away from people..."
                    blooky "there’s a few i’m close to, and some that i’m not"
                    blooky "i'm..... difficult to be around, so i can understand why not many want to be around me......."
                    blooky "and some days i don’t blame them because i don’t want to be around people either"
                    blooky "......"
                    blooky "sorry that i’m not much help with your questions......."
                    blooky "i hope i’m not troubling you..."
                    
                    menu:
                        "I was just curious, it’s alright.": #(+HB)
                            blooky "......."
                            blooky "if you're sure......."
                            blooky ".......i wish i could explain myself more..... but i can't."
                            blooky "......oh well......"
                        "You’re no trouble at all!": #(+FP)
                            blooky "are you sure?"
                            blooky "i feel like...... i’ve just been bothering you....."
                            blooky "but...... if you say so, then..... i'll believe you"
                            blooky "......oh well......"
                            blooky "maybe i won't be such a loner with you around....."
                    
                "Weren’t monsters just a myth or some legend?": #(+FP)
                    blooky "i thought humans were a myth, too"
                    blooky "......then i saw frisk..."
                    blooky "though, i never bumped into humans as much as i did other monsters"
                    blooky "probably the same as you not bumping into many monsters when you were on the surface..."
                    blooky "it takes some getting used to, i bet... ...but you’ll manage fine"
                    
                    menu:
                        "I read about them in books and stories, but I never thought they could be real.":
                            blooky "well........."
                            blooky "here..... we are....."
                            #Smile
                            blooky "...........tada"
                            #Contemplative
                            blooky "...........hm....."
                            blooky "don't worry...... you’ll get used to it"
                            #Normal
                            blooky "if it’s just like in the books, then maybe you’ll already..... know a bit about everyone..."
                        "I feel like I fit in already.": #(+HB)
                            #Smile
                            blooky "that's..... that’s good"
                            blooky "i'm glad..."
                            #Normal
                            blooky "it's not... so bad down here when you get used to it, i’m sure..."
                            blooky "everyone’s nice......"
                            blooky "..."
                            blooky "i think"
                        "I don’t think I could ever get used to this...": #(-FP -HB)
                            blooky ".......i'm ........sorry"
                            blooky "i wish i could help...... but......."
                            #Sad
                            blooky "i’m never much....help with anything"
                            blooky "........oh.......um......"
                            #Normal
                            blooky "well........it just....takes time"
                            blooky "and with {color=#00ffff}{b}patience{/b}{/color} and {color=#228b22}{b}kindness{/b}{/color}.....i think you’ll do ok."
                            
                "Are you self conscious about being a shut-in?": #(+HB)
                    blooky "w-well....... a little bit..."
                    blooky "i know i can be awkward sometimes......."
                    blooky "i know i bother people just by being around them......."
                    blooky "is it that noticeable?"
                    
                    menu:
                        "I’m sure everyone knows, but don’t worry about what they think.": #(+HB)
                            blooky "i... i’ll try not to..."
                            blooky "it’s hard...... though..."
                            blooky "i usually don’t worry about what others think because..... i already know..."
                            blooky "......it’s hard to shut everything out sometimes......"
                            blooky "but.... i'll try"
                            #Smile
                            blooky "thank you for dealing with me......"
                            blooky "really....i appreciate it"
                        "Not at all, you blend in well.": #(+HB)
                            blooky "oh......."
                            #Smile
                            blooky "thank you........"
                            blooky "that's just..... what i wanted, too"
                            blooky "i don’t want to be noticed........"
                            blooky "i just want to..... fit in......."
                            blooky "even if that means being invisible"
                        "Yes, you should fix that.": #(-FP -HB)
                            blooky "......i will......"
                            blooky "eventually..."
                            blooky "i....... know i will, someday..."
                            blooky "........i hope"
                            blooky ".............."
                        "Just be yourself, always!": #(+FP)
                            #Smile
                            blooky "heh........... well..."
                            blooky "i tried that already....... but..."
                            #Indifferent/Content
                            blooky "it doesn’t always........ work.........."
                            #Normal
                            blooky ".....i'll keep trying though."
                            blooky "...maybe...... it’ll all work out"
                            
                "One day, will you show me your music?" if hobbies_asked: #(+DP) ONLY AVAILABLE IF YOU DIDN'T COMPLETE HANGOUT 1 ALREADY
                    blooky "......i would....."
                    blooky "but i don't have it with me right now..."
                    blooky "maybe you can come over to my place sometime?"
                    blooky "so..... we can lay around listening together..."
                    blooky "or i could bring it here to the ruins sometime..."
                    #Smile
                    blooky "it would be great"
                    
                    menu:
                        "Sounds like another date then!": #(+DP)
                            blooky "well........"
                            blooky "i wouldn't mind it....."
                            blooky "so long as it isn't too much...... trouble"
                            blooky "it would be nice"
                        "Nod happily": #(+FP)
                            #Smile
                            blooky "..."
                        "It better just be you and me again, too!": #(+HB)
                            #Smile
                            blooky ".....heh"
                            #Normal
                            blooky "i mean, if you want to, then sure."
                            blooky "i don't like big crowds anyway....... so..."
                            #Smile
                            blooky "i think that's a good idea"
                    
            jump blooky_date_questions 
            
        label end_blook_date:
            #python:
            #       HB_threshold = XXXXX
            #       FP_threshold = XXXXX
            #       date_success = False
            #       friendzoned = False
            #
            #       if (HB > HB_threshold) && (FP < FP_threshold):
            #               jump HB_ending
            #       else if (HB < HB_threshold) && (FP > FP_threshold):
            #               jump FP_ending
            #       else:
            #               jump date_failed
            
            ###TEMPORARY- FOR TESTING PURPOSES ONLY ###
            "Jump to..."
            menu:
                "HB":
                    jump HB_ending
                "FP":
                    jump FP_ending
                "Failed Date":
                    jump Failed_ending
            
            jump blooky_ruins
            
        label HB_ending:
            blooky "this was nice... i enjoyed hanging out with you"
            blooky "i’m glad we got to know eachother better"
            blooky "............"
            blooky "i should really get going......"
            blooky "......"
            #Smile
            blooky "this was fun, though"
            blooky "i hope..... that we can hang out again sometime..."
            #Fades away
            blooky "bye..."
            blooky "..."
            # $ date_success = True
            jump blooky_ruins
        
        label FP_ending:
            blooky "this was fun... it really was..."
            blooky "it’s been...... so long since i last got to just relax and talk to someone..."
            blooky "i almost forgot what it was like...... hehe......."
            blooky "........."
            #Smile
            blooky "i'm glad we're friends........"
            #Fades away
            blooky "bye..."
            blooky "..."
            # $ friendzoned = True
            jump blooky_ruins
            
        label Failed_ending:
            blooky "um.....i hope i wasn’t too boring....."
            blooky "i’m sorry if i was..."
            blooky "......."
            blooky "it just felt like........ i thought........."
            blooky ".............."
            blooky "this just isn’t going to work out... i’m not good at these things... i’m sorry"
            blooky "..............well, i guess i'll see you around....."
            #Fades away
            blooky "bye..."
            blooky "..."
            jump blooky_ruins