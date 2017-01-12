# Flowey Hangout 1.5
# This dialogue does not contribute much to Flowey’s FP or HB points. It is mostly for comedic purposes and showing Flowey’s realization of his place in the dating sim, that he can be "dated" like all other characters.
# If possible, this hangout would not occur in subsequent playthroughs after the first time it occurs.
# The hangout occurs the second time the player encounters Flowey after Day 1
label Flowey_Hangout_1_5_menu:
    menu:
        "Q1":
            call Flowey_Hangout_1_5_start
        "Q2":
            call Flowey_Hangout_1_5_Q2
        "Q3":
            call Flowey_Hangout_1_5_Q3
        "Q4":
            call Flowey_Hangout_1_5_Q4

label Flowey_Hangout_1_5_start:
    show flowey annoyed
    flowey "Oh. It’s you again."
    flowey "Great. This is lovely."
    flowey "..."
    jump Flowey_Hangout_1_5_Q1

label Flowey_Hangout_1_5_Q1:
    #F Q1: Evil
    show flowey evil
    flowey "Turn around and walk away if you know what’s good for you."
    jump Flowey_Hangout_1_5_selection1
label Flowey_Hangout_1_5_selection1:
    menu:
        "No need to tell me twice.":
            jump Flowey_Hangout_1_5_choice1              
            #//Neutral 0
        "Too bad, weed. You’re stuck with me.":
            jump Flowey_Hangout_1_5_Q2        
            #// Decrease -FP
        "I was just wondering how your day has been.":
            jump Flowey_Hangout_1_5_Q2    
            #// Increase +FB
        "Why be mean to the one person trying to talk to you?": 
            jump Flowey_Hangout_1_5_choice2 #ior Flowey_Hangout_1_5_choice4?
            #// Increase +HB

label Flowey_Hangout_1_5_choice1:
    #/// If >(No need to tell me twice.)<
    show flowey smug
    flowey "Hey, look. It has a brain."
    show flowey Normal
    flowey "Good choice!"
    show flowey wink
    flowey "Now use that newfound brain of yours to start walking."
    #-Player exits encounter-
    jump Flowey_Hangout_1_5_menu

label Flowey_Hangout_1_5_choice2:
#/// If >"Why be mean to the one person trying to talk to you?":
        
    show flowey smug
    flowey "Because I don’t  N E E D  anyone."
    flowey "Because I don’t need anyone around. Especially someone like you."
    show flowey annoyed
    flowey "You’re more of an annoying gnat than a conversationalist."
    show flowey slightlyannoyed
    flowey "Quit bothering me and go away."
    jump Flowey_Hangout_1_5_selection2
label Flowey_Hangout_1_5_selection2:
    menu:
        "Fine.":
            jump Flowey_Hangout_1_5_choice3
             #// Neutral  0
        "You’ll be alone forever if you keep acting like that.":
            jump Flowey_Hangout_1_5_choice4
            #// Increase +HB
        "Everyone needs someone.":
            jump Flowey_Hangout_1_5_choice5
        #// Increase +FP
label Flowey_Hangout_1_5_choice3:
    #/// If >"Why be mean to the one person trying to talk to you?":
       #// If >"Fine.":
       
    show flowey annoyed
    flowey "Well."
    show flowey angry
    flowey "If you're not going to leave, then I will."
    show flowey smug
    flowey "Feel free to stand around talking to yourself, though."
    show flowey laughing
    flowey "Idiot."
    #-Flowey exits encounter-
    jump Flowey_Hangout_1_5_menu
label Flowey_Hangout_1_5_choice4:
    #/// If >"Why be mean to the one person trying to talk to you?":
       #// If >"You’ll be alone forever if you keep acting like that.":
       
    flowey "…"
    show flowey sad
    flowey "…………………"
    flowey "Well."
    show flowey slightly annoyed
    flowey "I don’t care."
    #-Flowey exits encounter-
    jump Flowey_Hangout_1_5_menu
label Flowey_Hangout_1_5_choice5:
    #/// If >"Why be mean to the one person trying to talk to you?":
       #// If >"Everyone needs someone.":
       
    show flowey annoyed
    flowey "In case you didn’t notice, idiot, I’m not exactly like everyone else here."
    flowey " …"
    show flowey slightly annoyed
    flowey "I don’t need anyone."
    show flowey sad
    flowey "And I don’t want anyone, either."
    show flowey annoyed
    flowey "So go befriend Frisk or something..."
    #-Flowey exits encounter-
    jump Flowey_Hangout_1_5_menu
label Flowey_Hangout_1_5_Q2:
#/// If >(Too bad, weed. You’re stuck with me.)< OR #/// If >(I was just wondering how your day has been.)<
    show flowey angry
    flowey "Why do you keep talking to me?!"  
    flowey "Aren't you playing this game to date Sans or something?!"
    show flowey smug
    flowey "Tch. You look like the type that would hunt through internet blogs just to collect pictures of some imaginary OTP." 
    show flowey laughs
    show flowey surprised
    flowey "…."
    show flowey slightlyannoyed
    flowey "…………."
    show flowey narrowseyes
    flowey "Oh my god, you are, aren’t you."
    show flowey annoyed
    flowey "Well, either way!"
    show flowey angry
    flowey "I’m definitely not a part of this dumb game! Chit-chatting with me will get you nowhere, so--"
    flowey "What are you hanging around me for?!"
    jump Flowey_Hangout_1_5_selection3
label Flowey_Hangout_1_5_selection3:
    menu:
        "…":
            jump Flowey_Hangout_1_5_choice6

               #//Neutral 0
        "…":
            jump Flowey_Hangout_1_5_choice6
               #//Neutral 0
        "…":
            jump Flowey_Hangout_1_5_choice6
               #//Neutral 0
label Flowey_Hangout_1_5_choice6:
        #/// If >(…)<
    show flowey Suspicious
    flowey "…"
    flowey "……………."
    show flowey surprised
    flowey "…..oh."
    jump Flowey_Hangout_1_5_Q3
label Flowey_Hangout_1_5_Q3:
    #F Q3: Angry
    show flowey angry
    flowey "You have got to be joking. I can’t be some option like the rest of these morons!"
    flowey "……"
    show flowey surprised
    flowey "There’s just no way."
    jump Flowey_Hangout_1_5_selection4
label Flowey_Hangout_1_5_selection4:
    menu:
        "Looks like you’re not as special as you think.":
            jump Flowey_Hangout_1_5_choice7
               #//Increase +HB
        "Well, this is our second hangout...":
            jump Flowey_Hangout_1_5_choice7
                   #//Neutral 0
label Flowey_Hangout_1_5_choice7:
    #/// If >(Looks like you’re not as special as you think.)< OR #/// If >(Well, this is our second hangout...)<
    show flowey Angry
    flowey "Look, bucko. I’m gonna make this crystal clear."
    flowey "So listen closely, as best as you can, idiot."
    show flowey annoyed
    flowey "I feel nothing at all.  Seriously, I don’t."
    flowey "I literally have no soul."
    flowey "And trying to go down this path... will only end in flames…"
    jump Flowey_Hangout_1_5_Q4
label Flowey_Hangout_1_5_Q4:
   # F Q4: Evil
    show flowey evil
    flowey "…Specifically for you."
    jump Flowey_Hangout_1_5_selection5
label Flowey_Hangout_1_5_selection5:
    menu:
        "Cool it. I just want to be friends.":
            jump Flowey_Hangout_1_5_choice8
                           #//Increase +FP
        "Bet those flames won’t be nearly as hot as you are.":
            jump Flowey_Hangout_1_5_choice11
               #//Increase +FP
        "We’ll see.":
            jump Flowey_Hangout_1_5_choice9
                                       #//Neutral 0
        "You think I care about you? How cute.":
            jump Flowey_Hangout_1_5_choice10
                       #//Increase +HB
label Flowey_Hangout_1_5_choice8:
    #/// If >(Cool it. I just want to be friends.)<
    show flowey surprised
    flowey "…"
    flowey " ...I don’t…"
    show flowey angry
    flowey "I don’t want friends!"
    flowey "I don’t need them, either!"
    show flowey bashful
    flowey "Geeze!"
    show flowey annoyed
    flowey "I’m outta here!"
    #-Flowey exits encounter-
    jump Flowey_Hangout_1_5_menu
label Flowey_Hangout_1_5_choice9:
    #/// If >(We’ll see.)<
    show flowey surprised
    flowey "…"
    show flowey annoyed
    flowey "No, we won’t."
    show flowey Evil
    flowey "Don’t even think about it, P A L."
    flowey "Now get lost."
    #-Flowey exits encounter-
    jump Flowey_Hangout_1_5_menu
label Flowey_Hangout_1_5_choice10:
    #/// If >(You think I care about you? How cute.)<
    show flowey surprised
    flowey "...What?"
    show flowey Suspicious side glace
    flowey "No, of course not. That’d be stupid." 
    show flowey normal
    flowey "Now leave me alone."
    show flowey Evil
    flowey "We wouldn’t want an   a c c i d e n t   to happen, now, would we?"
    #-Player exits encounter-
    jump Flowey_Hangout_1_5_menu

label Flowey_Hangout_1_5_choice11:
    #/// If >(Bet those flames won’t be nearly as hot as you are.)<
    show flowey surprised
    flowey "…………..."
    flowey "Oh."
    flowey "My."
    flowey "God."
    show flowey annoyed
    flowey "If you’re a part of the \"Flowey Fan Club\" I’m going to seriously get pissed."
    flowey "That stupid group’s supposed to be secret!"
    flowey "That dumb bag of bones wasn’t supposed to run around inviting people!"
    show flowey angry
    flowey "It’s literally just Papyrus! That idiot!"
    flowey "And there’s no way you could have met him yet, so how did you--"
    show flowey surprised
    flowey "…"
    flowey "Wait."
    show flowey smug
    flowey "...Tch."
    flowey "Oh, I get it… You’re just a real freak, huh?"
    flowey "Well."
    show flowey laughs
    flowey "I’m definitely not that type of available, sicko."
    show flowey normal
    flowey "And I sure as hell never will be."
    flowey "So, if you got a thing for plants, then I suggest exploring the flowers around Toriel’s house."
    flowey "…….."
    show flowey Suspicioussideglance
    flowey "Now…"
    flowey "I’m gonna go. I feel a little…"
    show flowey normal
    flowey "uncomfortable."
    #-Flowey exits encounter-
    jump Flowey_Hangout_1_5_menu
