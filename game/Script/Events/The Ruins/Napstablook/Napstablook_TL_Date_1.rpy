label napstablook_tl_date:
    #Event Name: "napstablook's TL Date"
    #Event Trigger: Entering the section of the Ruins where blooky is initially found in Undertale.
    
    ####### TEMP TESTING VALUES!!!! #######
    $ isdancer = False
    $ napstablook_friendship_hangout1_complete = False
    
    python:
        question_num = 0
        prev_qs = [0]
        
        likesart = False
        likesreading = False
        likesguns = False
        likescooking = False
        likesexercise = False
        
        asked_thinkhumans = False
        asked_ghostfood = False
        asked_socute = False
        asked_hobbies = False
        asked_alive = False
        asked_nicemonsters = False
        asked_howlong = False
        asked_monsterlegend = False
        asked_shutin = False
        asked_showmusic= False
        
        didnothing = False
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
        asked_11 = False
        hobbies_asked = False
    
    show napstablook surprised at napstabob with Dissolve(.25)
    napstablook "really?"
    napstablook "hangout........with me? that'd be nice..."
    show napstablook normal with Dissolve(.25)
    napstablook "sure.....if it's not too much of a bother..."
    napstablook "..... ...well i know a place nearby we can go..."
    napstablook "follow me...."
    
    scene black
    
    napstablook "..."
    
    scene background ruins_first_entrance
    show napstablook normal with Dissolve(.25)
    napstablook "oh good"
    napstablook "it's empty"
    
    menu:
        "\"Just the two of us, then.\"":
            $world.get_monster('Napstablook').update_DP(3)
            show napstablook normal with Dissolve(.25)
            napstablook "yeah..."
            napstablook "just you and me..."
            napstablook "i hope that's okay.... ...i generally come to the ruins to be alone so..."
            napstablook "usually my music is good company"
            
            show napstablook smallsmile  with Dissolve(.25)
            
            napstablook ".... ....but so are you"
        "\"Is that good?\"":
            $world.get_monster('Napstablook').update_FP(2)
            show napstablook sad  with Dissolve(.25)
            napstablook "i think so yeah..."
            napstablook "i usually like being alone with my music..."
            napstablook "i don't mind it at all..."
        
        "\"Are people avoiding you?\"":
            $world.get_monster('Napstablook').update_HB(1)
            show napstablook sad  with Dissolve(.25)
            napstablook "i don't know......"
            napstablook "i really wouldn't be surprised if they did....."
            napstablook "i can understand that i'm a downer"
            napstablook "i learned to accept it......"
            menu:
                "\"Well I don't think you're a downer.\"":
                    $world.get_monster('Napstablook').update_HB(1)
                    show napstablook smile  with Dissolve(.25)
                    napstablook "oh.... good..."
                    napstablook "i'm glad.... ... at least there's still you"
                "Quietly smile.": #+1 Patience ?    
                    show napstablook normal  with Dissolve(.25)
    jump tl_date_start
                
    label tl_date_start:
        
        show napstablook normal  with Dissolve(.25)
        napstablook "so"
        napstablook "how do we start this?"
        
        show napstablook shyblush  with Dissolve(.25)
        
        napstablook "to be honest... ...it's been awhile since i last got to hang out with someone....."
        napstablook "....."
        napstablook "maybe we could... ask each other questions? that's how people get to know each other.... right?"
        
        menu:
            "\"Yeah, that sounds like fun!\"":
                $world.get_monster('Napstablook').update_DP(2)
                show napstablook smallsmile  with Dissolve(.25)
                napstablook "o-okay... i'm glad you think so..."
            "\"I guess, if that's what you want to do...\"":
                $world.get_monster('Napstablook').update_FP(1)
                show napstablook normal  with Dissolve(.25)
                napstablook "oh..... um........ okay...."
                
        napstablook "i  guess i'll start...... we can take turns....."
        jump tl_napstablook_date_questions
    
    label tl_napstablook_date_questions:
        show napstablook normal  with Dissolve(.25)
        if question_num >= 5:
            jump end_napstablook_tl_date_1
            
        python:
            napstablook_asking = True
            while napstablook_asking is True:
                    
                randnum = renpy.random.randint(1, 11)
                if randnum in prev_qs:
                    continue
                else:
                    prev_qs.append(randnum)
                    napstablook_asking = False
                    question_num += 1
                    
        #$ randnum = 1
        "%(randnum)d" 
        "%(question_num)i"
        
        if (randnum is 1) and (asked_1 is False):
            $ asked_1 = True
            call tl1_blook_q1
        if (randnum is 2) and (asked_2 is False):
            $ asked_2 = True
            call tl1_blook_q2                    
        if (randnum is 3) and (asked_3 is False):
            $ asked_3 = True
            call tl1_blook_q3
        if (randnum is 4) and (asked_4 is False):
            $ asked_4 = True
            call tl1_blook_q4            
        if (randnum is 5) and (asked_5 is False):
            $ asked_5 = True
            call tl1_blook_q5
        if (randnum is 6) and (asked_6 is False):
            $ asked_6 = False
            call tl1_blook_q6
        if (randnum is 7) and (asked_7 is False):
            $ asked_7 = True
            call tl1_blook_q6
        if (randnum is 8) and (asked_8 is False):
            $ asked_8 = True
            call tl1_blook_q8
        if (randnum is 9) and (asked_9 is False):
            $ asked_9 = True
            call tl1_blook_q9
        if (randnum is 10) and (asked_10 is False):
            $ asked_10 = True
            call tl1_blook_q10
            
###############################     NAPSTABLOOK FILLER      ################################

    label tl_ask_napstablook:
        show napstablook normal  with Dissolve(.25)
        if question_num is 1:
            napstablook "okay.... um..... i think it's your turn to.... ask a question. if you want to, i mean..."
        elif question_num is 2:
            napstablook "um.... it's your turn... again....."
        elif question_num is 3:
            napstablook "i'm sorry..... is this boring? maybe this question thing was a bad idea....."
            menu:
                "\"I'm having fun! Let's keep going!\"":
                    $ world.get_monster('Napstablook').update_FP(2)
                    show napstablook smile  with Dissolve(.25)
                    "really? okay, it's your turn then..."
                "\"It's never boring hanging out with you.\"":
                    $ world.get_monster('Napstablook').update_DP(2)
                    show napstablook shyblush  with Dissolve(.25)
                    napstablook "o-oh..... ha..... that's nice of you to say......"
                    napstablook "let's keep going, then, if you're having fun...... it's your turn, then....."
                "\"Yeah, I'm bored. Let's stop.\"":
                    $ world.get_monster('Napstablook').update_DP(-1)
                    napstablook "oh, okay.... that's alright, at least we learned a little about each other...."
                    jump end_napstablook_tl_date_1
        elif question_num is 4:
            napstablook "okay, you go... i think i like it better when it's your turn to ask the questions..... it's less pressure......"
        elif question_num is 5:
            napstablook "i think i'm out of questions.... i can't think of any more...."
            napstablook "sorry, i guess we should stop......"
            napstablook "oh, but that's not fair..... i've asked five questions, and you've only asked four.... do you want to ask another question?"
            menu:
                "\"Yeah, just one more!\"":
                    $ world.get_monster('Napstablook').update_FP(1)
                    napstablook "okay.... make it a good one..... or don't...... whatever you want."
                "\"No, I'm done, too.\"":
                    napstablook "okay..... well......"
                    jump end_napstablook_tl_date_1

###############################     PLAYER QUESTIONS      ################################

        menu:
            "\"What do you think of humans?\"" if (asked_thinkhumans == False):
                $ asked_thinkhumans = True
                $ world.get_monster('Napstablook').update_DP(2)
                call napstablook_tl_date_thinkhumans
            "\"Can you eat normal food? Does it phase through you?\"" if (asked_ghostfood == False):
                $ asked_ghostfood = True
                $ world.get_monster('Napstablook').update_FP(2)
                call napstablook_tl_date_ghostsandwich
            "\"How can you be so cute?\"" if (asked_socute == False):
                $ asked_socute = True
                $ world.get_monster('Napstablook').update_DP(4)
                call napstablook_tl_date_socute                        
            "\"What are your hobbies?\"" if (asked_hobbies == False):
                $ asked_hobbies = True
                $ world.get_monster('Napstablook').update_DP(1)
                $ world.get_monster('Napstablook').update_FP(1)
                call napstablook_tl_date_hobbies
            "\"Were you ever even alive?\"" if (asked_alive == False):
                $ asked_alive = True
                $ world.get_monster('Napstablook').update_HB(2)
                call napstablook_tl_date_alive
            "\"Are any of the other monsters as nice as you?\"" if (asked_nicemonsters == False):
                $ asked_nicemonsters = True
                $ world.get_monster('Napstablook').update_DP(1)
                $ world.get_monster('Napstablook').update_FP(1)
                call napstablook_tl_date_nicemonsters
            "\"How long have you been down here?\"" if (asked_howlong == False): #+ DP
                $ asked_howlong = True
                call napstablook_tl_date_howlong
            "\"Weren't monsters just a myth or some legend?\"" if (asked_monsterlegend == False):
                $ asked_monsterlegend = True
                $ world.get_monster('Napstablook').update_FP(2)
                call napstablook_tl_date_monsterlegend
            "\"Are you self conscious about being a shut-in?\"" if (hobbies_asked == False and napstablook_friendship_hangout1_complete and asked_shutin == False):
                $ asked_shutin = True
                $ world.get_monster('Napstablook').update_HB(3)
                call napstablook_tl_date_shutin
            "\"One day, will you show me your music?\"" if (napstablook_friendship_hangout1_complete == False and asked_showmusic == False):
                $ asked_showmusic = True
                $ world.get_monster('Napstablook').update_DP(2)
                call napstablook_tl_date_showmusic
                                
        jump tl_napstablook_date_questions 

        label napstablook_tl_date_thinkhumans:
            show napstablook normal  with Dissolve(.25)
            napstablook "they seem really nice..."
            show napstablook smallsmile  with Dissolve(.25)
            napstablook "...and so are you... so..."
            show napstablook normal  with Dissolve(.25)
            napstablook "i think monsters might really have... a chance....."
            napstablook "once we get out of here...... maybe."
            napstablook "it's been a long time since the last human fell down here......"
            napstablook "a really long time, it feels like...."
            show napstablook smile  with Dissolve(.25)
            napstablook "but they're just as nice as you... so all humans must be, right?"
            menu: 
                "\"I'd like to think so!\"":
                    $ world.get_monster('Napstablook').update_DP(2)
                    show napstablook smile  with Dissolve(.25)
                    napstablook "hehehe...."
                    napstablook "me too."
                "\"Definitely not.\"":
                    $ world.get_monster('Napstablook').update_FP(-2)
                    jump .tl_notnice
                "\"Not all of us are nice.\"":
                    $ world.get_monster('Napstablook').update_HB(2)
                    label .tl_notnice:
                        show napstablook normal  with Dissolve(.25)
                        napstablook "huh?"
                        napstablook "what do you mean?"
                        menu:
                            "Some people are just jerks.":
                                $ world.get_monster('Napstablook').update_FP(-2)
                                napstablook "oh"
                                napstablook "..........well, i just hope that..."
                                napstablook "you aren't one of them..."
                            "Nothing, sorry about that.":
                                napstablook ".....oh..."
                                napstablook "it's ok..."
                            "I'm worried that I'm the only that can be trusted.":
                                $ world.get_monster('Napstablook').update_HB(1)
                                napstablook "that's....that's not true..."
                                napstablook ".....frisk is another human like you and....."
                                napstablook "and they would never hurt anyone.... they said so themselves..."
                                napstablook "........."
                                napstablook "i know.... that.... its hard, ‘cause i'm the same way..."
                                napstablook "if..... if anything..."
                                napstablook "you can always trust me........ know that"
                                show napstablook smallsmile  with Dissolve(.25)
            return
            
        label napstablook_tl_date_ghostsandwich: 
            show napstablook normal  with Dissolve(.25)
            napstablook "human food passes through me, yeah"
            napstablook "but ghost food... and monster food...."
            napstablook "that i can actually digest"
            napstablook "....."
            napstablook "........."
            napstablook "have you ever had a ghost sandwich?"
            napstablook "they're my favorite thing to eat when i'm at home......"
            napstablook "last time i offered a human a ghost sandwich.... ....they had trouble holding it"
            napstablook "i felt bad that they didn't get to try it......."
            napstablook "so i think it's the other way around... humans can't eat ghost food?"
            napstablook "........"
            napstablook "i'm sorry......i got carried away... i talk too much sometimes..."
            
            menu:
                "\"What do ghost sandwiches taste like?\"":
                     napstablook "well....."
                     napstablook "they taste light and fluffy..."
                     napstablook "like a ghost"
                     napstablook "......."
                     napstablook "not that i eat ghosts"
                     napstablook "i think that's called cannibalism"
                "\"No need to apologize!\"":
                    $ world.get_monster('Napstablook').update_FP(1)
                    $ world.get_monster('Napstablook').update_DP(1)
                    napstablook "oh, i'm..."
                    napstablook "i'm just so used to apologizing that it kind of just slips..."
                    napstablook "i'm sor--"
                    napstablook ".........heh........."
                    napstablook "..........my bad."
                "\"I'm probably the only person who likes your rambling.\"":
                    $ world.get_monster('Napstablook').update_HB(2)
                    napstablook "yeah......probably.........."
                    napstablook ".....but....... that's good...... right?"
                    napstablook "so long as i'm not.... boring you or anything......."
                    napstablook "then i guess it's ok..."
            return

        label napstablook_tl_date_socute:
            show napstablook surprised  with Dissolve(.25)
            napstablook "i-i......"
            show napstablook shyblush  with Dissolve(.25)
            napstablook "........i don't think i am... ...but..."
            napstablook "i don't know......"
            napstablook "am i really cute...?"
            napstablook "....."
            napstablook "............"
            napstablook "i don't know what to say....."
            napstablook "i guess lying around feeling like trash helps..."
            
            menu:
                "\"Must be adorable trash then.\"":
                    $ world.get_monster('Napstablook').update_HB(2)
                    napstablook "huh?"
                    show napstablook normal  with Dissolve(.25)
                    napstablook "i'm......... i wouldn't say that........."
                    napstablook "i don't think so..... at least,but....."
                    show napstablook smile  with Dissolve(.25)
                    napstablook "thanks..... i think..."
                "\"You're not trash, you're just cute!\"":
                    $ world.get_monster('Napstablook').update_DP(3)
                    napstablook "..........i......"
                    napstablook ".....i don't know what to say"
                    napstablook "oh..... that sounds... it's pretty... uh....... spiffy."
                "\"Maybe!\"":
                    $ world.get_monster('Napstablook').update_FP(1)
                    show napstablook smile  with Dissolve(.25)
                    napstablook "hehehe"
                    show napstablook normal  with Dissolve(.25)
                    napstablook ".....it's the only thing that makes sense."
            return
            
        label napstablook_tl_date_hobbies:
            show napstablook normal  with Dissolve(.25)
            napstablook "i like to make music"
            napstablook ".....i like to think i'm good at it... i've been told it's pretty good, but..."
                
            if listened_music == False:
                $ hobbies_asked = True
                
                napstablook "i'm afraid to show it to too many people........"
                napstablook "i don't want to bother everyone with myself....."
                napstablook "......oh..."
                show napstablook sad  with Dissolve(.25)
                napstablook "i made myself sad... i'm sorry"
                
                menu: 
                    "\"Don't be sad, that's cool!\"":
                        $ world.get_monster('Napstablook').update_DP(3)
                        show napstablook smile  with Dissolve(.25)
                        napstablook "do you really think so?"
                        napstablook ".....well......i enjoy it a lot..."
                        napstablook "........i really would like to invite you to hear it sometime"
                        napstablook "if.... you think it's cool now"
                        napstablook "wait until you hear it........"
                        show napstablook smile  with Dissolve(.25)
                        napstablook "heheh......"
                    "\"Oh, I'm sorry.\"":
                        $ world.get_monster('Napstablook').update_FP(2)
                        napstablook "its not your fault....."
                        napstablook "i always make myself sad........."
                        napstablook "its just my thing.....it's ok"
                    ".......":
                        $ world.get_monster('Napstablook').update_DP(-2)
                        napstablook ".........."
                        napstablook "well......"
                        napstablook "thanks for...... being patient......"
                        napstablook "letting me cry it out........ it always feels good to cry"
                        
            elif dislikedmusic = True: #(ONLY AVAILABLE AFTER HANGOUT ONE -> DISLIKED MUSIC)
                napstablook "you... um... didn't seem to like it that much when i showed you..."
                
                menu:
                    "\"I'm sorry... it's not that it's not good, it's just not what I ususally listen to.\"":
                        $ world.get_monster('Napstablook').update_FP(1)
                        napstablook "oh..... that's okay... i understand....."
                        napstablook "you don't have to like it... not everyone does..."
                        napstablook "sometimes, i think people just pretend to like it to make me feel better"
                    "\"My opinion doesn't matter. You should do what makes you happy.\"":
                        $ world.get_monster('Napstablook').update_DP(1)
                        napstablook "it matters to me..."
                        napstablook "but... thanks..... i'll keep that in mind..."
                    "\"Do you think you could try to make something that I'd like next time?\"":
                        $ world.get_monster('Napstablook').update_HB(2)
                        show napstablook sad  with Dissolve(.25)
                        napstablook "um... maybe..... i could try..."
                        napstablook "i'll try to do better next time....."
                        
            elif likedmusic = True: #(ONLY AVAILABLE AFTER HANGOUT ONE -> LIKED MUSIC)
                show napstablook shyblush  with Dissolve(.25)
                napstablook ".....you, um, seemed to like it, last time....."
                
                menu:
                    "\"Yeah! I had fun.\"":
                        $ world.get_monster('Napstablook').update_FP(2)
                        show napstablook surprised  with Dissolve(.25)
                        napstablook "r-really?"
                        show napstablook smile  with Dissolve(.25)
                        napstablook "well, i'm glad you liked it....."
                    "\"We should do that again sometime.\"":
                        $ world.get_monster('Napstablook').update_DP(2)
                        napstablook "well, it takes a while to make a new song....."
                        napstablook "but..... i'd like that....."
                        napstablook "we don't even have to listen to my music..... we could listen to other artists, too."
                        show napstablook smile  with Dissolve(.25)
                        napstablook "i think that would be just as fun..."
            return

        label napstablook_tl_date_alive:
            show napstablook normal  with Dissolve(.25)
            napstablook "but... i am alive......"
            napstablook "..."
            napstablook "i've always been like this..."
            napstablook "for as long as i can remember......"
            napstablook "which isn't that far back, really...... i have a bad memory"
            napstablook "thinking about it hurts, though......"
            napstablook "and i don't know why......."
            napstablook "......."
            napstablook "i'm sorry... i'm rambling again, you must be bored..."
            napstablook "now i feel bad..."
            
            menu:
                "\"Most would say you're dead, but I like ghosts.\"":
                    $ world.get_monster('Napstablook').update_HB(2)
                    napstablook "oh... well....."
                    napstablook ".......i'm glad you like ghosts..."
                    napstablook "i've always been this way...... there's no changing me......"
                    napstablook "even if i wanted to change"
                    napstablook ".....thanks for accepting me, though"
                "\"Don't feel bad, this is interesting.\"":
                    $ world.get_monster('Napstablook').update_FP(2)
                    napstablook "is it?"
                    napstablook "i'm sure that..... for most...... my rambling gets annoying"
                    napstablook "i'm surprised you aren't trying to... run or something."
                    napstablook "........but..."
                    napstablook "i'm glad you're interested"
                "\"I'm sorry, it was rude of me to ask...\"":
                    $ world.get_monster('Napstablook').update_DP(1)
                    napstablook "n-no it's okay, really"
                    napstablook "i can see why some would wonder......."
                    napstablook "i wish i had a better..... answer of..... some sort........"
                    napstablook "........."
                    napstablook "but i don't"
                    napstablook "i'm glad you're interested, though"
            return

        label napstablook_tl_date_nicemonsters:
            show napstablook surprised  with Dissolve(.25)
            napstablook "o-oh..... i mean...... i don't know"
            show napstablook normal  with Dissolve(.25)
            napstablook "probably"
            napstablook "........"
            napstablook "that's very nice of you to say..... .....i try not to be a burden or a bother..."
            show napstablook smile  with Dissolve(.25)
            napstablook "it makes me relieved, actually"
            napstablook "so..... i'm not boring you? that's good."
            show napstablook normal  with Dissolve(.25)
            napstablook ".....but i know a few others who are really kind....."
            napstablook "i think you have nothing to worry about."
            
            menu:
                "\"So long as they're nice, I think I'll be alright here.\"":
                    $ world.get_monster('Napstablook').update_FP(2)
                    napstablook "yeah..."
                    napstablook "everyone is just great...... in their own way"
                    napstablook "i think you'll like it.......here........ for as long as you stay, of course"
                    napstablook "i know..... like frisk..... humans that fall down here...... must be worried"
                    napstablook "maybe you want to try going home........"
                    napstablook "but maybe... also like frisk... you'll consider staying..... after you meet everyone?"
                "\"I wasn't worried!\"":
                    $ world.get_monster('Napstablook').update_DP(2)
                    napstablook "really?"
                    napstablook "that's good..."
                    napstablook "it means........ maybe you'll have fun while you're down here, right?"
                    napstablook "i hope so, at least...... .i think you'll like it here"
                "\"That was me flirting, Blooky.\"":
                    $ world.get_monster('Napstablook').update_HB(1)
                    show napstablook surprised  with Dissolve(.25)
                    napstablook "f-flirting?"
                    napstablook "oh...... oh i..."
                    show napstablook shyblush  with Dissolve(.25)
                    napstablook "i don't think........ anyone's ever flirted with me before....."
                    napstablook "........ah....... i'm sorry....."
            return

        label napstablook_tl_date_howlong:
            show napstablook normal  with Dissolve(.25)
            napstablook "for as long as i can remember, really..."
            napstablook "that's all i can say... i don't remember ever being on the surface"
            napstablook "....."
            napstablook "sorry that i'm not much help with your questions..."
            napstablook "i hope i'm not troubling you..."
            
            menu:
                "\"I was just curious, it's alright.\"":
                    $ world.get_monster('Napstablook').update_FP(1)
                    napstablook ".........."
                    napstablook "if you're sure....."
                    napstablook "......i wish i could remember more.... but i can't."
                    napstablook "maybe because it never happened?"
                    napstablook "......oh well......"
                "\"You're no trouble at all!\"":
                    $ world.get_monster('Napstablook').update_DP(1)
                    napstablook "are you sure?"
                    show napstablook sad  with Dissolve(.25)
                    napstablook "i feel like..... i've just been bothering you..."
                    show napstablook normal  with Dissolve(.25)
                    napstablook "but....... if you say so, then....... i'll believe you"
                    napstablook ".......i wish i could remember more for you, but....... i can't"
                    napstablook "maybe because it never happened?"
                    napstablook "......oh well......"
                "\"You can't think back further?\"":
                    napstablook "......no......"
                    napstablook "i wonder why....."
                    napstablook "it's like..... my brain wants to just..... save me the trouble, i suppose"
                    napstablook "heh......."
                    show napstablook sad  with Dissolve(.25)
                    napstablook "doesn't..... want me to even bother........."
            return

        label napstablook_tl_date_monsterlegend:
            show napstablook normal  with Dissolve(.25)
            napstablook "i thought humans were a myth, too"
            napstablook "......then i saw frisk..."
            napstablook "though, i never bumped into humans as much as i did other monsters"
            napstablook "probably the same as you not bumping into many monsters when you were on the surface..."
            napstablook "it takes some getting used to, i bet... ...but you'll manage fine"
            
            menu:
                "\"I read about them in books and stories, but I never thought they could be real.\"":
                    napstablook "well........."
                    napstablook "here..... we are....."
                    show napstablook smile  with Dissolve(.25)
                    napstablook "...........tada"
                    show napstablook sad  with Dissolve(.25)
                    napstablook "...........hm....."
                    napstablook "don't worry...... you'll get used to it"
                    show napstablook normal  with Dissolve(.25)
                    napstablook "if it's just like in the books, then maybe you'll already..... know a bit about everyone..."
                "\"I feel like I fit in already.\"":
                    $ world.get_monster('Napstablook').update_FP(1)
                    $ world.get_monster('Napstablook').update_DP(1)
                    show napstablook smile  with Dissolve(.25)
                    napstablook "that's..... that's good"
                    napstablook "i'm glad..."
                    show napstablook normal  with Dissolve(.25)
                    napstablook "it's not... so bad down here when you get used to it, i'm sure..."
                    napstablook "everyone's nice......"
                    napstablook "..."
                    napstablook "i think"
                "\"I don't think I could ever get used to this...\"":
                    $ world.get_monster('Napstablook').update_FP(-1)
                    $ world.get_monster('Napstablook').update_DP(-1)
                    napstablook ".......i'm ........sorry"
                    napstablook "i wish i could help...... but......."
                    show napstablook sad  with Dissolve(.25)
                    napstablook "i'm never much....help with anything"
                    napstablook "........oh.......um......"
                    show napstablook normal  with Dissolve(.25)
                    napstablook "well........it just....takes time"
                    napstablook "and with {color=#00ffff}{b}patience{/b}{/color} and {color=#228b22}{b}kindness{/b}{/color}.....i think you'll do ok."
            return

        label napstablook_tl_date_shutin:
            show napstablook normal  with Dissolve(.25)
            napstablook "w-well....... a little bit..."
            napstablook "i know i can be awkward sometimes......."
            napstablook "i know i bother people just by being around them......."
            napstablook "is it that noticeable?"
            
            menu:
                "\"I'm sure everyone knows, but don't worry about what they think.\"":
                    $ world.get_monster('Napstablook').update_HB(1)
                    napstablook "i... i'll try not to..."
                    napstablook "it's hard...... though..."
                    napstablook "i usually don't worry about what others think because..... i already know..."
                    napstablook "......it's hard to shut everything out sometimes......"
                    napstablook "but.... i'll try"
                    show napstablook smile  with Dissolve(.25)
                    napstablook "thank you for dealing with me......"
                    napstablook "really....i appreciate it"
                "\"Not at all, you blend in well.\"":
                    $ world.get_monster('Napstablook').update_HB(1)
                    napstablook "oh......."
                    show napstablook smile  with Dissolve(.25)
                    napstablook "thank you........"
                    napstablook "that's just..... what i wanted, too"
                    napstablook "i don't want to be noticed........"
                    napstablook "i just want to..... fit in......."
                    napstablook "even if that means being invisible"
                "\"Yes, you should fix that.\"":
                    $ world.get_monster('Napstablook').update_DP(-1)
                    $ world.get_monster('Napstablook').update_FP(-1)
                    napstablook "......i will......"
                    napstablook "eventually..."
                    napstablook "i....... know i will, someday..."
                    napstablook "........i hope"
                    napstablook ".............."
                "\"Just be yourself, always!\"":
                    $ world.get_monster('Napstablook').update_FP(3)
                    show napstablook smile  with Dissolve(.25)
                    napstablook "heh........... well..."
                    napstablook "i tried that already....... but..."
                    show napstablook normal  with Dissolve(.25)
                    napstablook "it doesn't always........ work.........."
                    napstablook ".....i'll keep trying though."
                    napstablook "...maybe...... it'll all work out"
            return

        label napstablook_tl_date_showmusic:
            show napstablook normal  with Dissolve(.25)
            napstablook "......i would....."
            napstablook "but i don't have it with me right now..."
            napstablook "maybe you can come over to my place sometime?"
            napstablook "so..... we can lay around listening together..."
            napstablook "or i could bring it here to the ruins sometime..."
            show napstablook smile  with Dissolve(.25)
            napstablook "it would be great"
            
            menu:
                "\"Sounds like another date then!\"":
                    $ world.get_monster('Napstablook').update_DP(3)
                    napstablook "well........"
                    napstablook "i wouldn't mind it....."
                    napstablook "so long as it isn't too much...... trouble"
                    napstablook "it would be nice"
                "Nod happily":
                    $ world.get_monster('Napstablook').update_FP(2)
                    show napstablook smile  with Dissolve(.25)
                    napstablook "..."
                "\"It better just be you and me again, too!\"":
                    $ world.get_monster('Napstablook').update_HB(2)
                    show napstablook smile  with Dissolve(.25)
                    napstablook ".....heh"
                    show napstablook normal  with Dissolve(.25)
                    napstablook "i mean, if you want to, then sure."
                    napstablook "i don't like big crowds anyway....... so..."
                    show napstablook smile  with Dissolve(.25)
                    napstablook "i think that's a good idea"
            return

####################################     NAPSTABLOOK QUESTIONS     ##################################

    label tl1_blook_q1:
        show napstablook normal  with Dissolve(.25)
        napstablook "so… what did you enjoy doing... ...in your free time?"
        napstablook "back when you were up on the surface?"
        
        menu:
            "\"I enjoyed creating art.\"":
                $ world.get_monster('Napstablook').update_DP(1)
                show napstablook smallsmile  with Dissolve(.25)
                napstablook "oh really?"
                napstablook "that's nice... i like to make art too"
            "\"I enjoyed reading.\"":
                $ world.get_monster('Napstablook').update_DP(1)
                napstablook "reading is nice..."
                napstablook "...i don't read much..."
                napstablook "but i heard it's really relaxing....."
                napstablook "that's a good hobby."
            "\"I went to the gun range often.\"":
                $ world.get_monster('Napstablook').update_FP(1)
                napstablook "the gun range.... i don't think i've ever been..."
                napstablook "but then again.... ...."
                napstablook "i don't think i've ever used a gun...."
                napstablook "it's too dangerous...."
                napstablook "but you're very brave."
            "\"I loved to dance\"":
                $ world.get_monster('Napstablook').update_DP(1)
                if isdancer is False:
                    show napstablook normal  with Dissolve(.25)
                    napstablook "dancing? wow..."
                    napstablook "that sounds like fun......."
                    napstablook "sometimes, i dance to the music i play at home."
                    show napstablook smallsmile  with Dissolve(.25)
                    napstablook "i bet you're a great dancer."
                if isdancer is True:
                    show napstablook smallsmile  with Dissolve(.25)
                    napstablook "ha, i should've guessed...."
                    napstablook "i like your dancing... it's funny....."
                    napstablook "but, um... not in a bad way...."
            "\"I enjoyed cooking and baking.\"":
                $ world.get_monster('Napstablook').update_DP(1)
                show napstablook smallsmile  with Dissolve(.25)
                napstablook "oh wow"
                napstablook "that's really cool....."
                napstablook "one of my friends likes to cook..."
                napstablook "...and my cousin has his own cooking show on tv..."
                napstablook "i think you'd really like them."
            "\"I liked to exercise.\"":
                $ world.get_monster('Napstablook').update_DP(1)
                show napstablook normal  with Dissolve(.25)
                napstablook "exercise?"
                napstablook "like flexing?"
                napstablook "...aaron likes to walk around flexing at people..."
                napstablook "if you bumb into him, maybe you two can compete..."
                napstablook "...."
                napstablook "it takes a lot of walking to get around the underground... so...."
                napstablook "i think you'll get plenty of exercise down here"
            "\"I didn't do much.\"" if apathy == False:
                $ world.get_monster('Napstablook').update_FP(1)
                show napstablook normal  with Dissolve(.25)
                napstablook "really?"
                show napstablook sad  with Dissolve(.25)
                napstablook "that... sounds sad...."
                show napstablook normal  with Dissolve(.25)
                napstablook "did you never find anything you fit into?"
                napstablook "nothing at all?"
                menu:
                    "Well, actually, maybe there is something.":
                        napstablook "what did you like to do, then?"
                        $ apathy = True
                        jump napstablook_tl_date1_hobbies
                    "Nope.":
                        $ world.get_monster('Napstablook').update_DP(-2)
                        napstablook "wow..."
                        napstablook "the surface must be really boring if even someone like you couldn't find anything to do...."
                        napstablook "maybe it's a good thing... you know...."
                        napstablook "that you're down here after all."
        return

    label tl1_blook_q2:
         menu:
            "\"It's a beautiful place.\"":
                $ world.get_monster('Napstablook').update_DP(3)
                show napstablook normal  with Dissolve(.25)
                napstablook "yeah.... i think so too..."
                napstablook "i like to wander around sometimes......"
                napstablook "but usually i end up here...."
                napstablook "it's really serene."
            "\"It's kind of eerily quiet.\"":
                $ world.get_monster('Napstablook').update_FP(2)
                napstablook ".....is it?"
                napstablook "i like it quiet sometimes....."
                napstablook "don't be worried… we're here together, so....."
                napstablook "maybe it won't be as scary as you think....."
            "\"I don't care where we are, so long as I'm here with you.\"":
                $ world.get_monster('Napstablook').update_DP(4)
                show napstablook sad  with Dissolve(.25)
                napstablook "o-oh.........."
                napstablook "............"
                napstablook "...."
                show napstablook shyblush  with Dissolve(.25)
                napstablook "i don't know what to say."
            "\"I couldn't really care less about this place.\"":
                $ world.get_monster('Napstablook').update_HB(2)
                show napstablook sad  with Dissolve(.25)
                napstablook "oh"
                napstablook "........you don't like it?"
                
                menu:
                    "\"I like you, but not this place.\"":
                        $ world.get_monster('Napstablook').update_HB(1)
                        show napstablook shyblush  with Dissolve(.25)
                        napstablook "o-oh..... really?"
                        napstablook "well........"
                        show napstablook smile  with Dissolve(.25)
                        napstablook "i guess that means... so long as we're together... we'll be alright"
                    "\"Well maybe a little bit.\"":
                        $ world.get_monster('Napstablook').update_FP(2)
                        show napstablook smile  with Dissolve(.25)
                        napstablook "oh, good....."
                        show napstablook normal  with Dissolve(.25)
                        napstablook "i was worried that..... I chose a bad spot..."
                        show napstablook smile  with Dissolve(.25)
                        napstablook "i'm glad you like it though..."
                        napstablook "even just a little"
                    "\"Nah.\"":
                        $ world.get_monster('Napstablook').update_FP(-1)
                        show napstablook sad  with Dissolve(.25)
                        napstablook "oh..... i'm sorry....."
                        napstablook "maybe....... next time i'll try to find someplace else.........."
                        napstablook ".....i'm sorry....."
         return

    label tl1_blook_q3:
        napstablook "i know you haven't been underground that long, but..."
        napstablook ".....i hope you're enjoying yourself"
        napstablook "........"
        show napstablook sad  with Dissolve(.25)
        napstablook "“i hope i'm not boring you too much either........ i'm sorry........"
        
        menu:
            "\"It's nice down here, and you're not boring at all!\"":
                $ world.get_monster('Napstablook').update_DP(2)
                napstablook "really?"
                napstablook "oh... that's good..."
                napstablook "i'm sure i get on people's nerves eventually..."
                napstablook "this is a good start..."
            "\"I'm just a little tired, but I'm having fun.\"":
                $ world.get_monster('Napstablook').update_FP(1)
                napstablook ".......oh..... do you need to rest?"
                napstablook "i'm happy you're having fun..... but......"
                napstablook "if you're tired you should really get some rest......."
                napstablook "i don't want to be....... taking up your time"
                
                menu:
                    "\"You're not.\"":
                        $ world.get_monster('Napstablook').update_FP(2)
                        napstablook "are you sure?"
                        napstablook "well..... ok then....."
                    "\"I'll get over it.\"":
                        napstablook "ah........... alright..."
                        napstablook "if you're sure......."
                napstablook "so long as you're okay....."
                
            "\"It gets pretty dull around here, I won't lie.\"":
                $ world.get_monster('Napstablook').update_FP(-2)
                napstablook "you think so?"
                napstablook "i'm sorry....... i wish i was better at entertaining people......."
                napstablook "this is all new to me...... too......"
                show napstablook sad  with Dissolve(.25)
                napstablook "i'm sorry......."
        return
        
    label tl1_blook_q4:
        napstablook "actually......"
        napstablook "i think you'd get along with my cousin......"
        napstablook "for some reason..... you two seem alike......"
        napstablook "........"
        napstablook "what do you think of robots?"
        
        menu:
            "\"Robots are cool.\"":
                $ world.get_monster('Napstablook').update_FP(3)
                $temp = 0
                jump .robot_q
            "\"They're pretty neat, I guess.\"":
                $ world.get_monster('Napstablook').update_HB(2)
                label .robot_q:
                    show napstablook smile  with Dissolve(.25)
                    napstablook "yeah?"
                    napstablook ".....my cousin is a robot....."
                    napstablook "and if you like robots....... then you two will get along really well....."
                    napstablook "that...... makes me happy."
            "\"Depends on the robot...\"":
                $ world.get_monster('Napstablook').update_FP(-1)
                napstablook "well....."
                napstablook "the kind that cook...dance..... sing......."
                napstablook "star in their own movies and shows"
                napstablook "......the kind that can do anything i guess?"
                napstablook "do you like those kind of robots?"
                
                menu:
                    "\"Oh, definitely!\"":
                        $ world.get_monster('Napstablook').update_DP(2)
                        show napstablook smile  with Dissolve(.25)
                        napstablook "yeah?"
                        napstablook ".....my cousin is a robot....."
                        napstablook "and if you like robots....... then you two will get along really well....."
                        napstablook "that...... makes me happy."
                    "\"They're alright, I guess.\"":
                        napstablook "......."
                        napstablook "i'm sorry if the conversation is boring......."
                        napstablook "we can talk about something else......."
                    "\"Not really.\"":
                        $ world.get_monster('Napstablook').update_FP(-3)
                        napstablook ".....oh......"
                        napstablook "well..... ok..."
                        
                        menu:
                            "\"I hope that didn't come out wrong!\"":
                                $ world.get_monster('Napstablook').update_FP(2)
                                napstablook "no... no it's ok..."
                                napstablook "i just..... wish you'd give robots a chance....."
                                napstablook "......but oh well..."
                            "\"But I do like ghosts.\"":
                                $ world.get_monster('Napstablook').update_HB(3)
                                napstablook "a-ah....."
                                show napstablook shyblush  with Dissolve(.25)
                                napstablook "well........"
                                napstablook "that's good........ i think"
                            "Shrug.":
                                napstablook "........."
        return

    label tl1_blook_q5:
        napstablook "well....... i only really ever come here to relax..."
        napstablook "sometimes, i'm just not in the mood to talk or do anything"
        napstablook "........not all the time..."
        napstablook "but most of the time"
        napstablook "..."
        napstablook "do....... you ever feel like escaping sometimes?"
        
        menu:
            "\"All the time.\"":
                $ world.get_monster('Napstablook').update_DP(1)
                napstablook "really? i can relate....."
                napstablook "that...... makes me relieved."
                napstablook "i always thought i was the only one"
                show napstablook smile  with Dissolve(.25)
                napstablook ".........this is nice"
            "\"Not really, no.\"":
                $ world.get_monster('Napstablook').update_FP(1)
                napstablook "..........must be nice"
                napstablook "to not have to worry about....... running away....."
                napstablook "........."
            "\"Only from people with an emotional crisis.\"":
                $ world.get_monster('Napstablook').update_FP(-2)
                napstablook "........"
                napstablook "......oh"
                show napstablook sad  with Dissolve(.25)
                napstablook "i'm sorry i....... i didn't realize......."
                show napstablook normal  with Dissolve(.25)
                
                menu:
                    "\"That's not what I meant, I'm sorry...\"":
                        $ world.get_monster('Napstablook').update_FP(1)
                        napstablook "oh.....?"
                        napstablook "it's ok....."
                        show napstablook shyblush  with Dissolve(.25)
                        napstablook "i was just worried that..... i was annoying you....."
                        napstablook "i wouldn't be surprised..... but it's fine......"
                    "\"It's okay, I'll be around to cheer you up.\"":
                        $ world.get_monster('Napstablook').update_HB(2)
                        napstablook "...really?"
                        napstablook "oh..... good."
                        show napstablook shyblush  with Dissolve(.25)
                        napstablook "i know that i..... get sad a lot..... it can make people uncomfortable and upset....."
                        napstablook "maybe with you around i can cheer up more"
                    "\"Don't worry about it.\"":
                        napstablook ".........."
                        napstablook "alright....... i won't..."
        return

    label tl1_blook_q6:
        napstablook "i wouldn't call myself a hermit but"
        napstablook "i like to be alone a lot..."
        napstablook "....."
        napstablook "if i want company i usually just go to work on the family snail farm..."
        napstablook "or sometimes i even turn on the tv to watch something"
        napstablook "it's nice to go out now and again, though"
        napstablook "..."
        napstablook "while you were on the surface,"
        napstablook "were there places you wanted to go to meet new people?"
        
        menu:
            "\"All the time!\"":
                $ world.get_monster('Napstablook').update_DP(4)
                napstablook "that's cool."
                napstablook "i think whenever i do feel like hanging out and meeting people..."
                napstablook "i usually find myself.... wandering in waterfall...."
                napstablook "or going to the MTT hotel and cafe...."
                napstablook "that place is really popular though...."
                napstablook "so i don't stay for too long."
            "\"Yes.\"":
                $ world.get_monster('Napstablook').update_DP(1)
                napstablook "you..... don't sound very happy about that..."
                napstablook "but i guess any chance you could get was a good one..... right?"
                napstablook "that must feel nice though..... to meet new people..."
            "\"A few places.\"":
                $ world.get_monster('Napstablook').update_FP(1)
                napstablook ".....well, even a few places is better than no place, right?"
                napstablook "that's good......"
            "\"I don't socialize much.\"":
                $ world.get_monster('Napstablook').update_FP(1)
                napstablook "oh..... really?"
                napstablook "well..... i don't either... if that makes it any better..."
                
                menu:
                    "\"I'd rather just talk to you.\"":
                        $ world.get_monster('Napstablook').update_HB(2)
                        show napstablook shyblush  with Dissolve(.25)
                        napstablook "that's........."
                        napstablook "......."
                        show napstablook smile  with Dissolve(.25)
                        napstablook "you're really nice....."
                    "\"That's why we get along so well.\"":
                        $ world.get_monster('Napstablook').update_FP(1)
                        napstablook "yeah?"
                        napstablook "we do..... don't we....."
                        napstablook "hehe....."
                    "\"I just don't see a point in it.\"":
                        $ world.get_monster('Napstablook').update_FP(-1)
                        napstablook "i understand..."
                        napstablook "i'm the same way sometimes, but......"
                        napstablook "some days it's really nice to go to a friend..... or just..... let go....."
                        napstablook ".....well for me at least"
        return
        
    label tl1_blook_q7:
        napstablook "i actually come here to cry sometimes..."
        napstablook ".....not a lot, but enough i guess to not want others to see what i'm doing"
        napstablook ".....and i like to lay down in my house and feel like trash..."
        napstablook "i could stay home where no one can see me, but....."
        napstablook "some days i wind up here anyway..."
        napstablook "......."
        napstablook ".....do you ever feel like trash?"
        
        label .trash_q:
            menu:
                "\"Excuse me?!\"" if feelliketrash is False:
                    $ world.get_monster('Napstablook').update_DP(-3)
                    napstablook "huh?"
                    napstablook "n-no..... not..... bad..... but-"
                    napstablook "i don't know how to....... explain myself..."
                    napstablook "just laying around....... not caring what happens?"
                    napstablook "just..... laying around... like trash........"
                    napstablook "......."
                    
                    menu:
                        "\"Oh... well, in that case...\"":
                            $ feelliketrash = True
                            jump .trash_q
                        "\"I am NOT trash!\"":
                            $ world.get_monster('Napstablook').update_HB(2)
                            napstablook "i-i didn't mean for it to sound like....."
                            napstablook "that's not......."
                            show napstablook sad  with Dissolve(.25)
                            napstablook "i'm so sorry....... i'm sorry............"
                            napstablook "........ah........  i'm really bad at this..... forgive me......."
                "\"Yes, I do sometimes.\"":
                    $ world.get_monster('Napstablook').update_DP(2)
                    napstablook "maybe..... then....."
                    napstablook "we could feel like trash together?"
                    napstablook "sometime?"
                "\"Not really.\"":
                    $ world.get_monster('Napstablook').update_FP(2)
                    napstablook "oh....."
                    napstablook "well..... maybe you should try it sometime..."
                    napstablook "it's not so bad..... it's kinda relaxing....."
                "\"Only trash should feel like trash.\"":
                    $ world.get_monster('Napstablook').update_HB(3)
                    napstablook "i... well......"
                    napstablook "i am trash..."
                    
                    menu:
                        "\"Then I guess you're cute and classy trash.\"":
                            $ world.get_monster('Napstablook').update_HB(1)
                            show napstablook shyblush  with Dissolve(.25)
                            napstablook "heheheh........."
                            napstablook ".....do you really think i'm classy?"
                            napstablook "........maybe some other time..... i can show you my....."
                            show napstablook smallsmile  with Dissolve(.25)
                            napstablook "{i}dapperblook{/i}"
                        "\"No you aren't!\"":
                            $ world.get_monster('Napstablook').update_FP(2)
                            show napstablook sad  with Dissolve(.25)
                            napstablook "i just..... feel like it sometimes......."
                            napstablook "but..... i know i shouldn't talk that way around people......."
                            napstablook "i'm sorry..."
        return

    label tl1_blook_q8:
        napstablook "......."
        napstablook "did i mention that i own a snail farm?"
        napstablook "probably but my memory isn't great....."
        napstablook "it's been in the blook family for generations"
        napstablook "there's racing and show snails for everyone to see......."
        napstablook "there aren't many of us left... just me....... so i'm taking care of it..."
        napstablook "do you like snails?"
        
        menu:
            "\"Yes!\"":
                $ world.get_monster('Napstablook').update_DP(2)
                napstablook "oh, cool..."
                napstablook "maybe you can stop by the farm sometime..."
                napstablook "i think you'll like it"
            "\"I don't ‘dislike' them?\"":
                $ world.get_monster('Napstablook').update_FP(2)
                napstablook "well..... that's good..."
                napstablook "maybe you can stop by the farm sometime..."
                napstablook "you might like it..."
            "\"Ew, no!\"":
                $ world.get_monster('Napstablook').update_DP(-2)
                napstablook "........oh"
                napstablook "well....... that's ok..."
                napstablook "we can always go somewhere else...... so..... i'm not worried about that..."
        return

    label tl1_blook_q9:
        napstablook "what type of music do you like listening to?"
        napstablook "if it's okay to ask....... you probably haven't heard anything in awhile since you fell..."
        napstablook "but....... did you like anything when you used to be on the surface?"
    
        label .music_q:
            menu:
                "Pop":
                    $ world.get_monster('Napstablook').update_DP(2)
                    napstablook "pop?"
                    napstablook "isn't that a drink...?"
                    napstablook "well....... i guess that would sound cool..."
                    napstablook "i think i like pop, too"
                "Hip Hop and R&B":
                    $ world.get_monster('Napstablook').update_DP(2)
                    napstablook "hip..... hop.....?"
                    napstablook "i don't think i've heard of that before..."
                    napstablook "it must be hip"
                    napstablook "does it get humans to hop?"
                "Trap and Trance":
                    $ world.get_monster('Napstablook').update_DP(2)
                    napstablook "trap?"
                    napstablook "there are a lot of old puzzles and tests through the ruins..."
                    napstablook "i'm sure if you get a few wrong, you'll find plenty of traps..."
                    napstablook "........."
                    napstablook "though i don't think they sound all that great, to be honest"
                "Dance and Techno":
                    $ world.get_monster('Napstablook').update_DP(2)
                    napstablook "dance and techno... huh..."
                    napstablook "technology types of things sound like something the royal scientist would know about..."
                    napstablook "and i can't dance..."
                    napstablook "at least........ not well..."
                "Classical and Instrumental":
                    $ world.get_monster('Napstablook').update_DP(2)
                    napstablook "i don't know what classical is... but..."
                    napstablook "instrumental i do."
                    napstablook "i think..... i like instrumental, too..."
                    napstablook "i don't have a lot of instruments, though....."
                    napstablook "......."
                    napstablook ".......sometimes, i hear someone playing a trombone..."
                "Kpop and Jpop":
                    $ world.get_monster('Napstablook').update_DP(2)
                    napstablook "what do the k and j stand for?"
                    napstablook "is it different from the regular pop?"
                    napstablook "........"
                    napstablook "sounds unique..."
                "Oldies music":
                    $ world.get_monster('Napstablook').update_DP(2)
                    napstablook "oldies?"
                    napstablook "old music?"
                    napstablook "........"
                    napstablook "i do have a few records in my room..."
                    napstablook "...maybe you'll like to hear them sometime..."
                "Jazz and Swing.":
                    $ world.get_monster('Napstablook').update_DP(2)
                    napstablook "i've heard of jazz and swing before..."
                    napstablook "i can't say i listen to it all the time...... but it's nice every now and then"
                    napstablook "we have similar tastes"
                    napstablook "......."
                    show napstablook smile  with Dissolve(.25)
                    napstablook "that's cool"
                "\"I don't like music.\"" if dislikedmusic is False:
                    $ world.get_monster('Napstablook').update_FP(-1)
                    napstablook "really?"
                    napstablook "well......"
                    napstablook "what do you like?"
                    
                    menu:
                        "\"I messed up, I actually do like music.\"":
                            $ world.get_monster('Napstablook').update_FP(2)
                            $ dislikedmusic = True
                            napstablook "oh, that's ok."
                            napstablook "so... what kind of music do you like?"
                            jump .music_q
                        "\"Well, it's not music.\"":
                            $ world.get_monster('Napstablook').update_DP(2)
                            show napstablook sad  with Dissolve(.25)
                            napstablook "........"
                            napstablook "well..... that's ok"
                            napstablook "..................."
                            napstablook "i guess....."
                "\"You.\"":
                    $ world.get_monster('Napstablook').update_HB(2)
                    show napstablook shyblush  with Dissolve(.25)
                    napstablook ".....o-oh.....?"
                    napstablook "well..... well....."
                    napstablook "i like you too..."
                    napstablook "......"
                    show napstablook smallsmile  with Dissolve(.25)
                    napstablook "...but i also like music."
        return

    label tl1_blook_q10:
        napstablook "um....."
        show napstablook sad  with Dissolve(.25)
        napstablook "sorry..... i'm not very talkative"
        napstablook "it's hard to get to know people... or talk to people..... or purposefully approach people......."
        napstablook "you know?"
        show napstablook normal  with Dissolve(.25)
        
        menu:
            "\"Yeah, I understand how you feel.\"":
                $ world.get_monster('Napstablook').update_FP(2)
                napstablook "yeah"
                napstablook "it feels..... like it takes up a lot of energy"
                napstablook ".....i get tired easily and i start to feel..... small....."
                napstablook "it's easier to just avoid it altogether"
            "\"Don't worry, you never have to feel that way with me.\"":
                $ world.get_monster('Napstablook').update_HB(3)
                napstablook "oh........ well, that's nice........"
                napstablook "i'm glad......"
                napstablook ".....you make me feel very..... relaxed"
                show napstablook smile  with Dissolve(.25)
                napstablook "it's really..... nice"
            "\"Um... no? I don't know.\"":
                $ world.get_monster('Napstablook').update_DP(-2)
                napstablook "oh..... well....."
                napstablook "that's fine..... i guess"
                napstablook "we don't have to have everything in common to be friends"
        return
        
    label tl1_blook_q11:
        napstablook "hey... i've been wondering...."
        napstablook "back up there...."
        napstablook "did you have... many friends...?"
        napstablook "i always thought humans were friendly... despite the fact that they locked us here...."
        
        menu:
            "\"I can't say I had many friends. I used to spend my days alone.\"":
                $ world.get_monster('Napstablook').update_DP(1)
                napstablook "oh..."
                napstablook "i know the feeling.... i don't have many friends either..."
                show napstablook smallsmile  with Dissolve(.25)
                napstablook "...though it's better to have a few good friends than to have many bad ones..."
                napstablook "but that might just be me..."
            "\"I was pretty popular up there; people must be looking for me even now.\"":
                $ world.get_monster('Napstablook').update_FP(1)
                napstablook "i....never got to know how it feels to be popular..."
                napstablook "the only popular person i know is my cousin.... he's amazing..."
                show napstablook smallsmile  with Dissolve(.25)
                napstablook "i guess you're amazing too.... that's...nice..."
            "\"I had tons of friends. What do you take me for, a loser?\"":
                $ world.get_monster('Napstablook').update_HB(2)
                show napstablook surprised  with Dissolve(.25)
                napstablook "no...sorry.... i didn't mean to upset you..."
                show napstablook sad  with Dissolve(.25)
                napstablook "i don't have many friends and i thought that..."
                napstablook "..."
                napstablook "....nevermind... sorry..."
            "\"No, I didn't have any. I didn't bother interacting with people too often.\"":
                $ world.get_monster('Napstablook').update_DP(2)
                napstablook "oh...."
                napstablook "watching them....seems more interesting than participating..."
                napstablook "but not always..."
                napstablook "..."
                show napstablook smallsmile  with Dissolve(.25)
                napstablook "...i enjoy being out here with you, though..."
        return
        
######################################     DATE ENDINGS     ###########################################


label end_napstablook_tl_date_1:
    python:
        DP_threshold = 10
        FP_threshold = 10
        date_success = False
        friendzoned = False
        DP = owner.DP
        FP = owner.FP
    
    if (DP >= DP_threshold):
        call napstablook_tl_date1_DP_ending
    elif ((DP < DP_threshold) and (FP > FP_threshold)):
        call napstablook_tl_date1_FP_ending
    else:
        call napstablook_tl_date1_Failed_ending
    return
    
    ###TEMPORARY- FOR TESTING PURPOSES ONLY ###
#        "Jump to..."
#        menu:
#            "DP":
#                call napstablook_tl_date1_DP_ending
#            "FP":
#                call napstablook_tl_date1_FP_ending
#            "Failed Date":
#                call napstablook_tl_date1_Failed_ending
#        
#        return
    
    label napstablook_tl_date1_DP_ending:
        show napstablook smallsmile  with Dissolve(.25)
        napstablook "wow.... ...i'm actually glad we got to hang out..."
        show napstablook normal  with Dissolve(.25)
        napstablook "it was nice, i never realized.... how much fun it would be to..... well..."
        show napstablook smallsmile  with Dissolve(.25)
        napstablook "meet someone new."
        napstablook "........."
        show napstablook normal  with Dissolve(.25)
        napstablook "i should really get going...."
        napstablook "this was fun, though."
        napstablook "i hope.... that we can hang out again sometime..."
        napstablook "here's my phone number....if you want to....hang out again, then just......"
        napstablook "call.... i guess..."
        #player gets napstablook's phone number
        hide napstablook
        napstablook "bye..."
        napstablook "..."
        $ date_success = True
        return
    
    label napstablook_tl_date1_FP_ending:
        napstablook "this was fun... it really was..."
        napstablook "it's been...... so long since i last got to just relax and talk to someone..."
        show napstablook smallsmile  with Dissolve(.25)
        napstablook "i almost forgot what it was like...... hehe......."
        napstablook "........."
        napstablook "i'm glad we're friends........"
        napstablook "here's my phone number....if you want to....hang out again, then just......"
        napstablook "call.... i guess..."
        #player gets napstablook's phone number
        hide napstablook
        napstablook "bye..."
        napstablook "..."
        $ friendzoned = True
        return
        
    label napstablook_tl_date1_Failed_ending:
        napstablook "um.....i hope i wasn't too boring....."
        napstablook "i'm sorry if i was..."
        napstablook "......."
        napstablook "it just felt like........ i thought........."
        napstablook ".............."
        napstablook "this just isn't going to work out... i'm not good at these things... i'm sorry"
        napstablook "..............well, i guess i'll see you around....."
        hide napstablook
        napstablook "bye..."
        napstablook "..."
        return