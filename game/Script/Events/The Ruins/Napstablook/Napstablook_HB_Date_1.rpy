# Note: End of date HB, FP, and DP values still need to be added. Currently ending is chosen via player-select menu.

label napstablook_hb_date:
    #Event Name: "Blooky's Date"
    #Event Trigger: Reaching waterfall. Must have enough HB points to trigger.
    
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
        asked_tiredunder = False
        asked_ghostfood = False
        asked_waterworks = False
        asked_hobbies = False
        asked_alive = False
        asked_creepy = False
        asked_loner = False
        asked_legend = False
        asked_shutin = False
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
    
    show napstablook surprised at napstabob with dissolve
    napstablook "really?"
    napstablook "hangout........with me? that'd be nice..."
    show napstablook smile with dissolve
    napstablook "sure.....if it's not too much of a bother..."
    napstablook "..... ...well i know a place nearby we can go..."
    napstablook "follow me...."
    
    scene black
    
    napstablook "..."
    
    scene background ruins_first_entrance
    show napstablook smile at napstabob with dissolve
    
    napstablook "oh good"
    napstablook "it's empty"
    
    menu:
        "\"Just the two of us, then.\"":
            $world.get_monster('Napstablook').update_DP(2)
            show napstablook smile with dissolve
            napstablook "yeah..."
            napstablook "just you and me..."
            show napstablook normal with dissolve
            napstablook "i hope that's okay.... ...i come to the ruins to usually be alone so..."
            napstablook "usually my music is good company"
            
            show napstablook smallsmile with dissolve
            
            napstablook ".... ....but so are you"
        "\"Is that okay?\"": #+1 Kindness
            $world.get_monster('Napstablook').update_FP(2)
            napstablook "i think so yeah..."
            napstablook "i usually like being alone with my music..."
            napstablook "i don't mind it at all..."
        
        "\"Are people avoiding you?\"":
            $world.get_monster('Napstablook').update_HB(2)
            show napstablook sad with dissolve
            napstablook "i don't know......"
            napstablook "i really wouldn't be surprised if they did....."
            napstablook "i can understand that i'm a downer"
            napstablook "i learned to accept it......"
            
            menu:
                "Well I don't think you're a downer.": #+1 Patience
                    $world.get_monster('Napstablook').update_HB(1)
                    show napstablook smile with dissolve
                    napstablook "oh.... good..."
                    napstablook "im glad.... ... at least there's still you"
                "Quietly smile.": 
                    $ bump = 0
    jump date_start
                    
label date_start:
    
    show napstablook normal with dissolve
    napstablook "so"
    napstablook "how do we start this?"
    
    show napstablook shyblush with dissolve
    
    napstablook "to be honest... ...it's been awhile since i last got to hang out with someone....."
    napstablook "....."
    napstablook "..........."
    napstablook "maybe we could... ask each other questions? that's how people get to know each other.... right?"
    
    menu:
        "\"The cliche approach. How original.\"":
            $world.get_monster('Napstablook').update_HB(2)
            napstablook "oh...thanks... it's no big deal...."
        "\"I guess, if that's what you want to do...\"":
            $world.get_monster('Napstablook').update_FP(1)
            show napstablook normal with dissolve
            napstablook "oh..... um........ okay...."
    napstablook "well... i guess...... we can take turns..... or something..."
    jump napstablook_date_questions
    
    label napstablook_date_questions:
        show napstablook normal with dissolve
        if question_num >= 5:
            jump end_napstablook_hb_date_1
            
        python:
            napstablook_asking = True
            while napstablook_asking is True:
                    
                randnum = renpy.random.randint(1, 10)
                if randnum in prev_qs:
                    continue
                else:
                    prev_qs.append(randnum)
                    napstablook_asking = False
                    question_num += 1
                    
        #$ randnum = 1
        #"%(randnum)d" 
        #"%(question_num)i"
        
        if (randnum is 1) and (asked_1 is False):
            $ asked_1 = True
            call hb1_blook_q1
        if (randnum is 2) and (asked_2 is False):
            $ asked_2 = True
            call hb1_blook_q2                    
        if (randnum is 3) and (asked_3 is False):
            $ asked_3 = True
            call hb1_blook_q3
        if (randnum is 4) and (asked_4 is False):
            $ asked_4 = True
            call hb1_blook_q4            
        if (randnum is 5) and (asked_5 is False):
            $ asked_5 = True
            call hb1_blook_q5
        if (randnum is 6) and (asked_6 is False):
            $ asked_6 = False
            call hb1_blook_q6
        if (randnum is 7) and (asked_7 is False):
            $ asked_7 = True
            call hb1_blook_q7
        if (randnum is 8) and (asked_8 is False):
            $ asked_8 = True
            call hb1_blook_q8
        if (randnum is 9) and (asked_9 is False):
            $ asked_9 = True
            call hb1_blook_q9
        if (randnum is 10) and (asked_10 is False):
            $ asked_10 = True
            call hb1_blook_q10

###############################     NAPSTABLOOK FILLER      ################################

    label hb_ask_napstablook:
        show napstablook normal with dissolve
        if question_num is 1:
            napstablook "okay.... um..... i think it's your turn to.... ask a question. if you want to, i mean..."
        if question_num is 2:
            napstablook "um.... it's your turn... again....."
        if question_num is 3:
            napstablook "i'm sorry..... is this boring? maybe this question thing was a bad idea....."
            menu:
                "\"I'm having fun! Let's keep going!\"":
                    $ world.get_monster('Napstablook').update_FP(2)
                    show napstablook smile with dissolve
                    "really? okay, it's your turn then..."
                "\"Not the best idea, but let's keep going anyway.\"":
                    $world.get_monster('Napstablook').update_HB(2)
                    napstablook "oh... sorry..... i'm not the best at coming up with ideas......"
                    napstablook "let's keep going, then, if you're having fun...... it's your turn, then....."
                "\"Yeah, I'm bored. Let's stop.\"":
                    $ world.get_monster('Napstablook').update_FP(-1)
                    $ world.get_monster('Napstablook').update_HB(-1)
                    show napstablook sad with dissolve
                    napstablook "oh, okay..... if you really want............"
                    jump end_napstablook_hb_date_1
        if question_num is 4:
            napstablook "okay, you go... i think i like it better when it's your turn to ask the questions..... it's less pressure......"
        if question_num is 5:
            napstablook "i think i'm out of questions.... i can't think of any more...."
            napstablook "sorry, i guess we should stop......"
            napstablook "oh, but that's not fair..... i've asked five questions, and you've only asked four.... do you want to ask another question?"
            menu:
                "\"Yeah, just one more!\"":
                    napstablook "okay.... whatever you want is fine... ask away..."
                "\"No, I'm done, too.\"":
                    napstablook "okay..... well......"
                    jump end_napstablook_hb_date_1
            
###############################     PLAYER QUESTIONS      ################################

        menu:
            "\"Aren't you tired of being down here?\"" if asked_tiredunder == False:
                $ asked_tiredunder = True
                $world.get_monster('Napstablook').update_HB(1)
                napstablook "well......"
                napstablook "not really...? i guess that it can be boring after awhile...... ...seeing the same thing every day......"
                napstablook "but its more bearable with people you care about"
                call napstablook_hb_date_tiredofunder
            "\"Can you eat normal food? Does it phase through you?\"" if asked_ghostfood == False:
                $ asked_ghostfood = True
                $world.get_monster('Napstablook').update_FP(1)
                napstablook "human food passes through me, yeah"
                napstablook "but ghost food... and monster food...."
                napstablook "that i can actually digest"
                call napstablook_hb_date_ghostsandwich                
            "\"What's up with the waterworks?\"" if asked_waterworks == False:
                $ asked_waterworks = True
                show napstablook sad with dissolve
                call napstablook_hb_date_waterworks                            
            "\"What are your hobbies?\"" if asked_hobbies == False:
                $ asked_hobbies = True
                napstablook "i like to make music"
                call napstablook_hb_date_hobbies
            "\"Were you ever even alive?\"" if asked_alive == False:
                $ asked_alive = True
                $world.get_monster('Napstablook').update_HB(2)
                napstablook "but... i am alive......"
                napstablook "..."
                call napstablook_hb_date_alive   
            "\"Why is everyone down here so creepy looking?\"" if asked_creepy == False:
                $ asked_creepy = True
                $ world.get_monster('Napstablook').update_HB(1)
                $ world.get_monster('Napstablook').update_FP(-2)
                napstablook "o-oh..... i mean..... i don't know"
                napstablook "i wouldn't think everyone was creepy looking"
                call napstablook_hb_date_creepy                
            "\"Did you choose to be a loner?\"" if asked_loner == False:
                $ asked_loner = True
                $ world.get_monster('Napstablook').update_HB(2)
                napstablook "n-no..... not really..."
                napstablook "that's all i can say..... i just have trouble getting..... comfortable around people"
                call napstablook_hb_date_loner
            "\"Weren't monsters just a myth or some legend?\"" if asked_legend == False:
                $ asked_legend = True
                $world.get_monster('Napstablook').update_FP(2)
                call napstablook_hb_date_monsterlegend
            "\"Are you self conscious about being a shut-in?\"" if asked_shutin == False:
                $ asked_shutin = True
                $world.get_monster('Napstablook').update_HB(2)
                call napstablook_hb_date_shutin
                
        jump napstablook_date_questions 
        
        label napstablook_hb_date_tiredofunder:
            menu:
                "\"I'd like to think so!\"":
                    $world.get_monster('Napstablook').update_FP(3)
                    show napstablook smile with dissolve
                    napstablook "hehehe......"
                    napstablook "me too"
                    return
                "\"Not all people are nice.\"":
                    $world.get_monster('Napstablook').update_HB(1)
                "\"Definitely not.\"":
                    $world.get_monster('Napstablook').update_FP(-2)
                    
            napstablook "huh?"
            napstablook "what do you mean?"
            
            menu:
                "\"Some people are just jerks.\"":
                    $world.get_monster('Napstablook').update_FP(-2)
                    napstablook "oh"
                    napstablook "......well, i just hope that..."
                    napstablook "you aren't one of them..."
                "\"Nothing, sorry about that.\"":
                    napstablook "...oh..."
                    napstablook "it's ok..."
                "\"I'm worried that I'm the only one that can be trusted.\"":
                    $world.get_monster('Napstablook').update_HB(2)
                    napstablook "that's... that's not true..."
                    napstablook ".....frisk is another human like you and..."
                    napstablook "and they would never hurt anyone...... they said so themselves..."
                    napstablook "......."
                    napstablook "i know..... that... its hard, 'cause i'm the same way..."
                    napstablook "if..... if anything..."
                    napstablook "you can always trust me...... know that"
            return
            
        label napstablook_hb_date_ghostsandwich:
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
                    $world.get_monster('Napstablook').update_FP(2)
                    napstablook "oh, i'm..."
                    napstablook "i'm just so used to apologizing that it kind of just slips..."
                    napstablook "i'm sor--"
                    napstablook ".........heh........."
                    napstablook "..........my bad."
                "\"I'm probably the only person who likes your rambling.\"":
                    $world.get_monster('Napstablook').update_HB(2)
                    napstablook "yeah......probably.........."
                    napstablook ".....but....... that's good...... right?"
                    napstablook "so long as i'm not.... boring you or anything......."
                    napstablook "then i guess it's ok..."
            return
        
        label napstablook_hb_date_waterworks:
            napstablook "i-i. ......"
            napstablook "i get emotional sometimes it just.... ....i don't...."
            napstablook "i don't know......"
            napstablook "does it bother you?"
            napstablook "......"
            napstablook "......that i cry too much?"
            napstablook "i can't help it... i'm sorry if it bothers you..."
            napstablook "i guess lying around feeling like trash helps..."
            
            menu:
                "\"Must be adorable trash, then.\"":
                    $world.get_monster('Napstablook').update_HB(2)
                    show napstablook shyblush with dissolve
                    napstablook "huh?"
                    napstablook "im........i wouldn't say that....."
                    napstablook "i don't think so.....at least, but....."
                    napstablook "thanks.......i think..."
                "\"You're not trash, you're just cute!\"":
                    $world.get_monster('Napstablook').update_FP(3)
                    show napstablook shyblush with dissolve
                    napstablook ".............i...."
                    napstablook ".......i don't know what to say"
                    napstablook "oh..... that sounds.... it's pretty..... uh........ spiffy"
                "\"Maybe!\"":
                    $world.get_monster('Napstablook').update_FP(-1)
                    show napstablook smile with dissolve
                    napstablook "hehehe"
                    napstablook ".....it's the only thing that makes sense"
            return
        
        label napstablook_hb_date_hobbies:
            napstablook ".....i like to think i'm good at it... i've been told it's pretty good, but..."
            napstablook "i'm afraid to show it to too many people........"
            napstablook "i don't want to bother everyone with myself....."
            napstablook "......oh..."
            show napstablook sad with dissolve
            napstablook "i made myself sad... i'm sorry"
            
            menu: 
                "\"Don't be sad, that's cool!\"":
                    $world.get_monster('Napstablook').update_FP(2)
                    show napstablook normal with dissolve
                    napstablook "do you really think so?"
                    napstablook ".....well......i enjoy it a lot..."
                    napstablook "........i really would like to invite you to hear it sometime"
                    napstablook "if.... you think it's cool now"
                    napstablook "wait until you hear it........"
                    show napstablook smile with dissolve
                    napstablook "heheh......"
                "\"Oh, I'm sorry.\"":
                    $world.get_monster('Napstablook').update_FP(1)
                    napstablook "its not your fault....."
                    napstablook "i always make myself sad........."
                    napstablook "its just my thing.....it's ok"
                "Say nothing.":
                    napstablook ".........."
                    napstablook "well......"
                    napstablook "thanks for...... being patient......"
                    napstablook "letting me cry it out........ it always feels good to cry"
            return
        
        label napstablook_hb_date_alive:
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
                    $world.get_monster('Napstablook').update_HB(2)
                    napstablook "oh... well....."
                    napstablook ".......i'm glad you like ghosts..."
                    napstablook "i've always been this way...... there's no changing me......"
                    napstablook "even if i wanted to change"
                    napstablook ".....thanks for accepting me, though"
                "\"Don't feel bad, this is interesting.\"":
                    $world.get_monster('Napstablook').update_FP(2)
                    napstablook "is it?"
                    napstablook "i'm sure that..... for most...... my rambling gets annoying"
                    napstablook "i'm surprised you aren't trying to... run or something."
                    napstablook "........but..."
                    napstablook "i'm glad you're interested"
                "\"I'm sorry, it was rude of me to ask...\"":
                    napstablook "n-no it's okay, really"
                    napstablook "i can see why some would wonder......."
                    napstablook "i wish i had a better..... answer of..... some sort........"
                    napstablook "........."
                    napstablook "but i don't"
                    napstablook "i'm glad you're interested, though"
            return
            
        label napstablook_hb_date_creepy:
            napstablook "......."
            napstablook "everyone just looks different...... that's all."
            napstablook "i can understand that not a lot of humans are..... used to seeing people like..... us....."
            napstablook "monsters, and ghosts i mean."
            napstablook "but don't be afraid..... not everyone is as scary as they look......."
            napstablook "......i know a few who are really kind..."
            napstablook "i think you have nothing to worry about"
            
            menu:
                "\"So long as they're nice, I think I'll be alright here.\"":
                    $world.get_monster('Napstablook').update_FP(2)
                    napstablook "yeah..."
                    napstablook "everyone is just great...... in their own way"
                    napstablook "i think you'll like it.......here........ for as long as you stay, of course"
                    napstablook "i know..... like frisk..... humans that fall down here...... must be worried"
                    napstablook "maybe you want to try going home........"
                    napstablook "but maybe... also like frisk... you'll consider staying..... after you meet everyone?"
                "\"I wasn't worried!\"":
                    $world.get_monster('Napstablook').update_HB(1)
                    napstablook "really?"
                    napstablook "that's good..."
                    napstablook "it means........ maybe you'll have fun while you're down here, right?"
                    napstablook "i hope so, at least...... .i think you'll like it here"
                "\"Not you, though.\"":
                    $world.get_monster('Napstablook').update_HB(3)
                    napstablook "...huh?"
                    napstablook "oh...... um....... i'm glad you think so--"
                    napstablook ".....or don't think so i guess.....?"
                    
                    menu:
                        "\"That was me flirting, Blooky.\"":
                            $ world.get_monster('Napstablook').update_HB(1)
                            show napstablook surprised with dissolve
                            napstablook "f-flirting?"
                            show napstablook shyblush with dissolve
                            napstablook "oh..... oh i...."
                            napstablook "i don't think....... anyone's ever flirted with me before......."
                            napstablook "..........ah...... i'm sorry........."
                        "\"Well anyway, let's keep talking.\"":
                            show napstablook normal with dissolve
                            napstablook "alright....."
                            napstablook "let's keep talking then"
            return
        
        label napstablook_hb_date_loner:
            napstablook "i can't help it..... i find myself just..... drifting away from people..."
            napstablook "there's a few i'm close to, and some that i'm not"
            napstablook "i'm..... difficult to be around, so i can understand why not many want to be around me......."
            napstablook "and some days i don't blame them because i don't want to be around people either"
            napstablook "......"
            napstablook "sorry that i'm not much help with your questions......."
            napstablook "i hope i'm not troubling you..."
            
            menu:
                "\"I was just curious, it's alright.\"":
                    $ world.get_monster('Napstablook').update_HB(2)
                    napstablook "......."
                    napstablook "if you're sure......."
                    napstablook ".......i wish i could explain myself more..... but i can't."
                    napstablook "......oh well......"
                "\"You're no trouble at all!\"":
                    $ world.get_monster('Napstablook').update_FP(2)
                    napstablook "are you sure?"
                    napstablook "i feel like...... i've just been bothering you....."
                    napstablook "but...... if you say so, then..... i'll believe you"
                    napstablook "......oh well......"
                    napstablook "maybe i won't be such a loner with you around....."
            return
        
        label napstablook_hb_date_monsterlegend:
            napstablook "i thought humans were a myth, too"
            napstablook "......then i saw frisk..."
            napstablook "though, i never bumped into humans as much as i did other monsters"
            napstablook "probably the same as you not bumping into many monsters when you were on the surface..."
            napstablook "it takes some getting used to, i bet... ...but you'll manage fine"
            menu:
                "\"I read about them in books and stories, but I never thought they could be real.\"":
                    napstablook "well........."
                    napstablook "here..... we are....."
                    show napstablook smile with dissolve
                    napstablook "...........tada"
                    show napstablook sad with dissolve
                    napstablook "...........hm....."
                    napstablook "don't worry...... you'll get used to it"
                    show napstablook normal with dissolve
                    napstablook "if it's just like in the books, then maybe you'll already..... know a bit about everyone..."
                "\"I feel like I fit in already.\"":
                    $ world.get_monster('Napstablook').update_FP(1)
                    $ world.get_monster('Napstablook').update_HB(1)
                    show napstablook smile with dissolve
                    napstablook "that's..... that's good"
                    napstablook "i'm glad..."
                    show napstablook normal with dissolve
                    napstablook "it's not... so bad down here when you get used to it, i'm sure..."
                    napstablook "everyone's nice......"
                    napstablook "..."
                    napstablook "i think"
                "\"I don't think I could ever get used to this...\"":
                    $ world.get_monster('Napstablook').update_FP(-1)
                    $ world.get_monster('Napstablook').update_HB(-1)
                    napstablook ".......i'm ........sorry"
                    napstablook "i wish i could help...... but......."
                    show napstablook sad with dissolve
                    napstablook "i'm never much....help with anything"
                    napstablook "........oh.......um......"
                    show napstablook normal with dissolve
                    napstablook "well........it just....takes time"
                    napstablook "and with {color=#00ffff}{b}patience{/b}{/color} and {color=#228b22}{b}kindness{/b}{/color}.....i think you'll do ok."
            return
            
        label napstablook_hb_date_shutin:
            napstablook "w-well....... a little bit..."
            napstablook "i know i can be awkward sometimes......."
            napstablook "i know i bother people just by being around them......."
            napstablook "is it that noticeable?"
            menu:
                "\"I'm sure everyone knows, but don't worry about what they think.\"":
                    $ world.get_monster('Napstablook').update_HB(2)
                    napstablook "i... i'll try not to..."
                    napstablook "it's hard...... though..."
                    napstablook "i usually don't worry about what others think because..... i already know..."
                    napstablook "......it's hard to shut everything out sometimes......"
                    napstablook "but.... i'll try"
                    show napstablook smile with dissolve
                    napstablook "thank you for dealing with me......"
                    napstablook "really....i appreciate it"
                "\"Not at all, you blend in well.\"":
                    $ world.get_monster('Napstablook').update_HB(2)
                    napstablook "oh......."
                    show napstablook smile with dissolve
                    napstablook "thank you........"
                    napstablook "that's just..... what i wanted, too"
                    napstablook "i don't want to be noticed........"
                    napstablook "i just want to..... fit in......."
                    napstablook "even if that means being invisible"
                "\"Yes, you should fix that.\"":
                    $ world.get_monster('Napstablook').update_FP(-2)
                    $ world.get_monster('Napstablook').update_HB(-2)
                    napstablook "......i will......"
                    napstablook "eventually..."
                    napstablook "i....... know i will, someday..."
                    napstablook "........i hope"
                    napstablook ".............."
                "\"Just be yourself, always!\"":
                    $ world.get_monster('Napstablook').update_FP(2)
                    show napstablook smile with dissolve
                    napstablook "heh........... well..."
                    napstablook "i tried that already....... but..."
                    show napstablook normal with dissolve
                    napstablook "it doesn't always........ work.........."
                    show napstablook normal with dissolve
                    napstablook ".....i'll keep trying though."
                    napstablook "...maybe...... it'll all work out"
            return

#####################################     NAPSTABLOOK QUESTIONS     ######################################

    label hb1_blook_q1:
        napstablook "um......."
        napstablook "if you don't...... mind me asking......."
        napstablook "how did.... you end up down here...?"
        napstablook "i know you fell but..... how did you..... manage to fall into.... such a big hole?"
        napstablook "how did you wind up down here?"
        
        menu:
            "\"I mean, it was a {i}really big hole.{/i}\"":
                $ world.get_monster('Napstablook').update_HB(2)
                napstablook "well....... i can understand that......."
                napstablook "i didn't mean to sound...... offensive or......."
                napstablook "to come off in such a way...... sorry...."
                napstablook "i was just wondering........"
                napstablook "because........... well........"
                napstablook "i've heard some people don't actually...... fall down here for good reasons...."
                napstablook "....but...."
                napstablook "..........."
                show napstablook sad with dissolve
                napstablook "i'm sorry..... maybe this is a touchy subject........."
            "\"I wasn't really paying attention too much where I was going.\"":
                $ world.get_monster('Napstablook').update_FP(2)
                napstablook "i get it... sometimes i'm not paying too much attention either..."
                napstablook "though...i never run into anything or fall really..."
                napstablook "since you know….i'm a ghost..."
                napstablook "........"
                show napstablook sad with dissolve
                napstablook "i...hope you didn't hurt yourself too much..."
                napstablook "...when you fell down here"
                show napstablook normal with dissolve
                napstablook "just...be careful, okay?"
            "...": #(+0 FP DP)
                napstablook "it's ok...."
                napstablook "......you don't have to answer"
                napstablook "..........."
                show napstablook sad with dissolve
                napstablook "i'm sorry..... maybe this is a touchy subject........."
            "\"I'm not really comfortable... answering.\"": #(+FP)
                show napstablook sad with dissolve
                napstablook "oh......"
                napstablook "i understand... it's ok it's....."
                napstablook "it was wrong of me to ask........ i understand, i'm sorry"
                show napstablook normal with dissolve
                napstablook "but..... for whatever reason it might be......."
                show napstablook smile with dissolve
                napstablook "i'm.....glad you're here"
        return

    label hb1_blook_q2:
        napstablook "i really find this place.... well......"
        show napstablook smallsmile with dissolve
        napstablook "peaceful"
        napstablook "...... what do you think about this part of the ruins?"
        
        menu:
            "\"It's not the best place for a first date...\"":
                $ world.get_monster('Napstablook').update_HB(2)
                show napstablook surprised with dissolve
                napstablook "oh..... date.......?"
                show napstablook normal with dissolve
                napstablook "i just... figured maybe this would be better than....... .....a busy place...."
                napstablook "i don't really like crowded places and this is the most quiet...... um....."
                napstablook ".....sorry, maybe i should have asked you where you wanted to go"
                
                menu:
                    "\"Maybe next time I'll tell you where to go, it'll be fine.\"":
                        $ world.get_monster('Napstablook').update_HB(3)
                        show napstablook surprised with dissolve
                        napstablook "n-next time.....?"
                        napstablook "......."
                        show napstablook shyblush with dissolve
                        napstablook "i....... okay..... i'd like that......."
                    "\"Yeah you should've.\"":
                        $ world.get_monster('Napstablook').update_FP(-1)
                        $ world.get_monster('Napstablook').update_HB(-1)
                        show napstablook sad with dissolve
                        napstablook "i-i'm sorry......"
                        napstablook "....... really.... really sorry........."
                        napstablook "um......"
                        napstablook "lets just... keep going......."                            
                    "\"No, this is fine, don't worry!\"":
                        $ world.get_monster('Napstablook').update_FP(2)
                        show napstablook normal with dissolve
                        napstablook "oh..... are you sure?"
                        napstablook "well....... thanks..... "
                        show napstablook smile with dissolve
                        napstablook "......i'm glad you like this place...."
                        napstablook "even if it's only a little bit"
            "\"It's kind of eerily quiet.\"":
                $ world.get_monster('Napstablook').update_FP(1)
                napstablook ".....is it?"
                napstablook "i like it quiet sometimes....."
                napstablook "don't be worried… we're here together, so....."
                napstablook "maybe it won't be as scary as you think....."
            "\"I don't really like it here.\"":
                $ world.get_monster('Napstablook').update_HB(-1)
                show napstablook sad with dissolve
                napstablook "o-oh.........."
                napstablook "...sorry, i guess i should've picked more carefully..."
                napstablook "........"
                napstablook "sorry..."
            "\"I couldn't really care less about this place.\"":
                $ world.get_monster('Napstablook').update_HB(3)
                show napstablook sad with dissolve
                napstablook "oh"
                napstablook "........you don't like it?"
                
                menu:
                    "\"I like you, but not this place.\"":
                        $ world.get_monster('Napstablook').update_HB(1)
                        show napstablook shyblush with dissolve
                        napstablook "o-oh..... really?"
                        napstablook "well........"
                        show napstablook smile with dissolve
                        napstablook "i guess that means... so long as we're together... we'll be alright"
                    "\"Well maybe a little bit.\"":
                        $ world.get_monster('Napstablook').update_FP(1)
                        show napstablook smile with dissolve
                        napstablook "oh, good....."
                        show napstablook normal with dissolve
                        napstablook "i was worried that..... I chose a bad spot..."
                        show napstablook smile with dissolve
                        napstablook "i'm glad you like it though..."
                        napstablook "even just a little"
                    "\"Nah.\"":
                        $ world.get_monster('Napstablook').update_FP(-1)
                        show napstablook sad with dissolve
                        napstablook "oh..... i'm sorry....."
                        napstablook "maybe....... next time i'll try to find someplace else.........."
                        napstablook ".....i'm sorry....."
        return
        
    label hb1_blook_q3:
        napstablook "i know you haven't been underground that long, but..."
        napstablook ".....i hope you're enjoying yourself"
        napstablook "........"
        show napstablook sad with dissolve
        napstablook "“i hope i'm not boring you too much either........ i'm sorry........"
        
        menu:
            "\"This could be worse, but at least you're trying.\"":
                $ world.get_monster('Napstablook').update_HB(2)
                napstablook "yeah...sorry... i wanted to pick something you'd like..."
                napstablook "sorry...if i'm getting on your nerves..."
                napstablook "..."
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
                        napstablook "so long as you're okay....."
                    "\"I'll get over it.\"":
                        napstablook "ah........... alright..."
                        napstablook "if you're sure......."
                        napstablook "hm........."
            "\"It gets pretty dull around here, I won't lie.\"":
                $ world.get_monster('Napstablook').update_FP(-2)
                napstablook "you think so?"
                napstablook "i'm sorry....... i wish i was better at entertaining people......."
                napstablook "i don't go out much..... and i'm usually alone so......"
                napstablook "this is all new to me...... too......"
                show napstablook sad with dissolve
                napstablook "i'm sorry......."
        return
        
    label hb1_blook_q4:
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
                    show napstablook smile with dissolve
                    napstablook "yeah?"
                    napstablook ".....my cousin is a robot....."
                    napstablook "and if you like robots....... then you two will get along really well....."
                    napstablook "that...... makes me happy."
            "\"Depends on the robot...\"":
                napstablook "well....."
                napstablook "the kind that cook...dance..... sing......."
                napstablook "star in their own movies and shows"
                napstablook "......the kind that can do anything i guess?"
                napstablook "do you like those kind of robots?"
                
                menu:
                    "\"Oh, definitely!\"":
                        $ world.get_monster('Napstablook').update_FP(2)
                        show napstablook smile with dissolve
                        napstablook "yeah?"
                        napstablook ".....my cousin is a robot....."
                        napstablook "and if you like robots....... then you two will get along really well....."
                        napstablook "that...... makes me happy."
                    "\"They're alright, I guess.\"":
                        $ world.get_monster('Napstablook').update_HB(1)
                        napstablook "......."
                        napstablook "i'm sorry if the conversation is boring......."
                        napstablook "we can talk about something else......."
                    "\"Not really.\"":
                        napstablook ".....oh......"
                        napstablook "well..... ok..."
                        
                        menu:
                            "\"I hope that didn't come out wrong!\"":
                                $ world.get_monster('Napstablook').update_FP(1)
                                napstablook "no... no it's ok..."
                                napstablook "i just..... wish you'd give robots a chance....."
                                napstablook "......but oh well..."
                            "\"But I do like ghosts.\"":
                                $ world.get_monster('Napstablook').update_HB(1)
                                napstablook "a-ah....."
                                show napstablook shyblush with dissolve
                                napstablook "well........"
                                napstablook "that's good........ i think"
                            "Shrug.":
                                napstablook "........."
        return
        
    label hb1_blook_q5:
        napstablook "well....... i only really ever come here to relax..."
        napstablook "sometimes, i'm just not in the mood to talk or do anything"
        napstablook "........not all the time..."
        napstablook "but most of the time"
        napstablook "..."
        napstablook "do....... you ever feel like escaping sometimes?"
        
        menu:
            "\"Yeah, for the most part.\"":
                $ world.get_monster('Napstablook').update_HB(1)
                napstablook "really? i can relate....."
                napstablook "that...... makes me relieved."
                napstablook "i always thought i was the only one"
                show napstablook smile with dissolve
                napstablook ".........this is nice"
            "\"Not really, no.\"":
                $ world.get_monster('Napstablook').update_FP(1)
                napstablook "..........must be nice"
                napstablook "to not have to worry about....... running away....."
                napstablook "........."
            "\"Only from people with an emotional crisis.\"":
                $ world.get_monster('Napstablook').update_FP(-3)
                napstablook "........"
                napstablook "......oh"
                show napstablook sad with dissolve
                napstablook "i'm sorry i....... i didn't realize......."
                show napstablook normal with dissolve
                
                menu:
                    "\"That's not what I meant, I'm sorry...\"":
                        $ world.get_monster('Napstablook').update_FP(1)
                        napstablook "oh.....?"
                        napstablook "it's ok....."
                        show napstablook shyblush
                        napstablook "i was just worried that..... i was annoying you....."
                        napstablook "i wouldn't be surprised..... but it's fine......"
                    "\"It's okay, I'll be around to cheer you up.\"":
                        $ world.get_monster('Napstablook').update_HB(2)
                        napstablook "...really?"
                        napstablook "oh..... good."
                        show napstablook shyblush
                        napstablook "i know that i..... get sad a lot..... it can make people uncomfortable and upset....."
                        napstablook "maybe with you around i can cheer up more"
                    "\"Don't worry about it.\"":
                        napstablook ".........."
                        napstablook "alright....... i won't..."
        return

    label hb1_blook_q6:
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
            "\"Yes, I guess.\"":
                $ world.get_monster('Napstablook').update_HB(1)
                napstablook "you..... don't sound very happy about that..."
                napstablook "but i guess any chance you could get was a good one..... right?"
                napstablook "that must feel nice though..... to meet new people..."
            "\"A few places.\"":
                $ world.get_monster('Napstablook').update_FP(2)
                napstablook ".....well, even a few places is better than no place, right?"
                napstablook "that's good......"
            "\"I don't socialize much.\"":
                napstablook "oh..... really?"
                napstablook "well..... i don't either... if that makes it any better..."
                
                menu:
                    "\"I'd rather just talk to you.\"":
                        $ world.get_monster('Napstablook').update_HB(2)
                        show napstablook shyblush with dissolve
                        napstablook "that's........."
                        napstablook "......."
                        show napstablook smile with dissolve
                        napstablook "you're really nice....."
                    "\"That's why we get along so well.\"":
                        $ world.get_monster('Napstablook').update_HB(2)
                        napstablook "yeah?"
                        napstablook "we do..... don't we....."
                        napstablook "hehe....."
                    "\"I just don't see a point in it.\"":
                        $ world.get_monster('Napstablook').update_FP(-2)
                        napstablook "i understand..."
                        napstablook "i'm the same way sometimes, but......"
                        napstablook "some days it's really nice to go to a friend..... or just..... let go....."
                        napstablook ".....well for me at least"
        return
        
    label hb1_blook_q7:
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
                    $ world.get_monster('Napstablook').update_FP(-2)
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
                            show napstablook sad with dissolve
                            napstablook "i'm so sorry....... i'm sorry............"
                            napstablook "........ah........  i'm really bad at this..... forgive me......."
                                
                            menu:
                                "\"It's okay, I'll forgive you this time.\"":
                                    $ world.get_monster('Napstablook').update_HB(2)
                                    show napstablook smile with dissolve
                                    napstablook "oh... thank you..."
                                "\"Oh, no, it's okay. Sorry I overreacted.\"":
                                    $ world.get_monster('Napstablook').update_FP(2)
                                    napstablook "really... are you sure?"
                                    show napstablook smile with dissolve
                                    napstablook "...thank you..."
                    show napstablook normal with dissolve
                "\"Yes, I do sometimes.\"":
                    $ world.get_monster('Napstablook').update_FP(2)
                    napstablook "maybe..... then....."
                    napstablook "we could feel like trash together?"
                    napstablook "sometime?"
                "\"Not really.\"":
                    $ world.get_monster('Napstablook').update_FP(2)
                    napstablook "oh....."
                    napstablook "well..... maybe you should try it sometime..."
                    napstablook "it's not so bad..... it's kinda relaxing....."
                "\"Only trash should feel like trash.\"":
                    $ world.get_monster('Napstablook').update_HB(2)
                    napstablook "i... well......"
                    napstablook "i am trash..."
                    
                    menu:
                        "\"Then I guess you're cute and classy trash.\"":
                            $ world.get_monster('Napstablook').update_HB(3)
                            napstablook "heheheh........."
                            show napstablook shyblush with dissolve
                            napstablook ".....do you really think i'm classy?"
                            napstablook "........maybe some other time..... i can show you my....."
                            show napstablook smile with dissolve
                            napstablook "{i}dapperblook{/i}"
                        "\"No you aren't!\"":
                            $ world.get_monster('Napstablook').update_FP(2)
                            show napstablook sad with dissolve
                            napstablook "i just..... feel like it sometimes......."
                            napstablook "but..... i know i shouldn't talk that way around people......."
                            napstablook "i'm sorry..."
        return

    label hb1_blook_q8:
        napstablook "......."
        napstablook "did i mention that i own a snail farm?"
        napstablook "probably but my memory isn't great....."
        napstablook "it's been in the blook family for generations"
        napstablook "there's racing and show snails for everyone to see......."
        napstablook "there aren't many of us left... just me....... so i'm taking care of it..."
        napstablook "do you like snails?"
        
        menu:
            "\"Yes.\"":
                napstablook "oh, cool..."
                napstablook "maybe you can stop by the farm sometime..."
                napstablook "i think you'll like it"
            "\"I don't ‘dislike' them?\"":
                $ world.get_monster('Napstablook').update_FP(2)
                napstablook "well..... that's good..."
                napstablook "maybe you can stop by the farm sometime..."
                napstablook "you might like it..."
            "\"Ew, no!\"":
                $ world.get_monster('Napstablook').update_FP(-2)
                napstablook "........oh"
                napstablook "well....... that's ok..."
                napstablook "we can always go somewhere else...... so..... i'm not worried about that..."
        return
        
    label hb1_blook_q9:
        napstablook "what type of music do you like listening to?"
        napstablook "if it's okay to ask....... you probably haven't heard anything in awhile since you fell..."
        napstablook "but....... did you like anything when you used to be on the surface?"
    
        label .music_q:
            menu:
                "Pop":
                    napstablook "pop?"
                    napstablook "isn't that a drink...?"
                    napstablook "well....... i guess that would sound cool..."
                    napstablook "i think i like pop, too"
                "Hip Hop and R&B":
                    napstablook "hip..... hop.....?"
                    napstablook "i don't think i've heard of that before..."
                    napstablook "it must be hip"
                    napstablook "does it get humans to hop?"
                "Trap and Trance":
                    napstablook "trap?"
                    napstablook "there are a lot of old puzzles and tests through the ruins..."
                    napstablook "i'm sure if you get a few wrong, you'll find plenty of traps..."
                    napstablook "........."
                    napstablook "though i don't think they sound all that great, to be honest"
                "Dance and Techno":
                    napstablook "dance and techno... huh..."
                    napstablook "technology types of things sound like something the royal scientist would know about..."
                    napstablook "and i can't dance..."
                    napstablook "at least........ not well..."
                "Classical and Instrumental":
                    napstablook "i don't know what classical is... but..."
                    napstablook "instrumental i do."
                    napstablook "i think..... i like instrumental, too..."
                    napstablook "i don't have a lot of instruments, though....."
                    napstablook "......."
                    napstablook ".......sometimes, i hear someone playing a trombone..."
                "Kpop and Jpop":
                    napstablook "what do the k and j stand for?"
                    napstablook "is it different from the regular pop?"
                    napstablook "........"
                    napstablook "sounds unique..."
                "Oldies music":
                    napstablook "oldies?"
                    napstablook "old music?"
                    napstablook "........"
                    napstablook "i do have a few records in my room..."
                    napstablook "...maybe you'll like to hear them sometime..."
                "Jazz and Swing.":
                    napstablook "i've heard of jazz and swing before..."
                    napstablook "i can't say i listen to it all the time...... but it's nice every now and then"
                    napstablook "we have similar tastes"
                    napstablook "......."
                    show napstablook smile with dissolve
                    napstablook "that's cool"
                "\"I don't like music.\"" if dislikedmusic is False:
                    $ world.get_monster('Napstablook').update_FP(-1)
                    napstablook "really?"
                    napstablook "well......"
                    napstablook "what do you like?"
                    
                    menu:
                        "\"I messed up, I actually do like music.\"":
                            $ world.get_monster('Napstablook').update_FP(1)
                            $ dislikedmusic = True
                            napstablook "oh, that's ok."
                            napstablook "so... what kind of music do you like?"
                            jump .music_q
                        "\"Well, it's not music.\"":
                            show napstablook sad with dissolve
                            napstablook "........"
                            napstablook "well..... that's ok"
                            napstablook "..................."
                            napstablook "i guess....."
                        "\"You.\"":
                            $ world.get_monster('Napstablook').update_HB(2)
                            show napstablook shyblush with dissolve
                            napstablook ".....o-oh.....?"
                            napstablook "well..... well....."
                            napstablook "i like you too..."
                            napstablook "......"
                            show napstablook smile with dissolve
                            napstablook "...but i also like music."
        return
        
    label hb1_blook_q10:
        napstablook "um....."
        show napstablook sad with dissolve
        napstablook "sorry..... i'm not very talkative"
        napstablook "it's hard to get to know people... or talk to people..... or purposefully approach people......."
        napstablook "you know?"
        show napstablook normal with dissolve
        
        menu:
            "\"Yeah, I understand how you feel.\"":
                $ world.get_monster('Napstablook').update_FP(2)
                napstablook "yeah"
                napstablook "it feels..... like it takes up a lot of energy"
                napstablook ".....i get tired easily and i start to feel..... small....."
                napstablook "it's easier to just avoid it altogether"
            "\"Don't worry, you never have to feel that way with me.\"":
                $ world.get_monster('Napstablook').update_HB(1)
                napstablook "oh........ well, that's nice........"
                napstablook "i'm glad......"
                napstablook ".....you make me feel very..... relaxed"
                show napstablook smile with dissolve
                napstablook "it's really..... nice"
            "\"Um... no? I don't know.\"":
                $ world.get_monster('Napstablook').update_FP(-2)
                napstablook "oh..... well....."
                napstablook "that's fine..... i guess"
                napstablook "we don't have to have everything in common to be friends"
        return

###############################     DATE ENDINGS      ################################

label end_napstablook_hb_date_1:
    python:
        HB_threshold = 22
        FP_threshold = 10
        date_success = False
        friendzoned = False
        HB = owner.HB
        FP = owner.FP
    
    if HB > HB_threshold:
        call napstablook_hb_date1_HB_ending
    elif ((HB < HB_threshold) and (FP > FP_threshold)):
        call napstablook_hb_date1_FP_ending
    else:
        call napstablook_hb_date1_Failed_ending
    return
    
#    ###TEMPORARY- FOR TESTING PURPOSES ONLY ###
#    "Jump to..."
#    menu:
#        "HB":
#            jump napstablook_hb_date1_HB_ending
#        "FP":
#            jump napstablook_hb_date1_FP_ending
#       "Failed Date":
#            jump napstablook_hb_date1_Failed_ending
#   
#    return
       
    label napstablook_hb_date1_HB_ending:
        napstablook "this was nice... i enjoyed hanging out with you"
        napstablook "i'm glad we got to know eachother better"
        napstablook "............"
        napstablook "i should really get going......"
        napstablook "......"
        show napstablook smile with dissolve
        napstablook "this was fun, though"
        napstablook "i hope..... that we can hang out again sometime..."
        #Fades away
        napstablook "bye..."
        napstablook "..."
        # $ date_success = True
        return
    
    label napstablook_hb_date1_FP_ending:
        napstablook "this was fun... it really was..."
        napstablook "it's been...... so long since i last got to just relax and talk to someone..."
        napstablook "i almost forgot what it was like...... hehe......."
        napstablook "........."
        show napstablook smile with dissolve
        napstablook "i'm glad we're friends........"
        #Fades away
        napstablook "bye..."
        napstablook "..."
        # $ friendzoned = True
        return
        
    label napstablook_hb_date1_Failed_ending:
        napstablook "um.....i hope i wasn't too boring....."
        napstablook "i'm sorry if i was..."
        napstablook "......."
        napstablook "it just felt like........ i thought........."
        napstablook ".............."
        napstablook "this just isn't going to work out... i'm not good at these things... i'm sorry"
        napstablook "..............well, i guess i'll see you around....."
        #Fades away
        napstablook "bye..."
        napstablook "..."
        return
        