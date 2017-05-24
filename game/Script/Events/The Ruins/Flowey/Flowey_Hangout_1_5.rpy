label Flowey_Hangout_1_5:
    # The hangout occurs the second time the player encounters Flowey after Day 1.
    # If possible, this hangout would not occur in subsequent playthroughs after the first time it occurs.
    
    scene background floweyroomplaceholder
    
    show flowey annoyed
    flowey "Oh. It's you again."
    flowey "Great. This is lovely."
    flowey "..."
    show flowey horror
    flowey "Turn around and walk away if you know what's good for you."
    
    menu:
        "No need to tell me twice.":
            show flowey smug
            flowey "Hey, look. It has a brain."
            show flowey normal
            flowey "Good choice!"
            show flowey wink
            flowey "Now use that newfound brain of yours to start walking."
        "Too bad, weed. You're stuck with me.":
            $world.get_monster('Flowey').update_FP(-4)
            call Flowey_Hangout_Path1            
        "I was just wondering how your day has been.":
            $world.get_monster('Flowey').update_FP(2)
            call Flowey_Hangout_Path1
        "Why be mean to the one person trying to talk to you?":
            $world.get_monster('Flowey').update_HB(3)
            call Flowey_Hangout_Path2
    return
    
    
    label Flowey_Hangout_Path1:
        show flowey angry
        flowey "Why do you keep talking to me?!"  
        flowey "Aren't you playing this game to date {i}Sans{/i} or something?!"
        show flowey smug
        flowey "Tch. You look like the type that would hunt through internet blogs just to collect pictures of some imaginary {i}OTP{/i}." 
        show flowey laugh
        flowey "ehehehe..."
        show flowey surprised
        flowey "..."
        show flowey annoyed
        flowey "........."
        show flowey sideglance
        flowey "Oh my god, you are, aren't you."
        show flowey annoyed
        flowey "Well, either way!"
        show flowey angry
        flowey "I'm definitely not a part of this dumb game! Chit-chatting with me will get you nowhere, so--"
        flowey "What are you hanging around me for?!?"

        menu:
            "...":
                $world.get_monster('Flowey').update_FP(0)
            "...":
                $world.get_monster('Flowey').update_FP(0)
            "...":
                $world.get_monster('Flowey').update_FP(0)
                 
        show flowey suspicious
        flowey "..."
        flowey "........."
        show flowey surprised
        flowey "...oh."
        show flowey angry
        flowey "You have got to be joking. I can't be some option like the rest of these morons!"
        flowey "......"
        show flowey surprised
        flowey "There's just no way."
        
        menu:
            "Looks like you're not as special as you think.": #-3 FP
                $world.get_monster('Flowey').update_FP(-3)
            "Well, this is our second hangout...":
                $world.get_monster('Flowey').update_FP(0)
                
        show flowey angry
        flowey "Look, bucko. I'm gonna make this crystal clear."
        flowey "So listen closely, as best as you can, idiot."
        show flowey annoyed
        flowey "I feel nothing at all.  Seriously, I don't."
        flowey "I literally have no soul."
        flowey "And trying to go down this path... will only end in flames..."
        show flowey horror
        flowey "...Specifically for {i}you{/i}."
        
        menu:
            "Cool it. I just want to be friends.":
                $world.get_monster('Flowey').update_FP(4)
                show flowey surprised
                flowey "..."
                flowey " ...I don't..."
                show flowey angry
                flowey "I don't want friends!"
                flowey "I don't need them, either!"
                show flowey blush
                flowey "Geeze!"
                show flowey annoyed
                flowey "I'm outta here!"
            "Bet those flames won't be nearly as hot as you are.": #DP???
                $world.get_monster('Flowey').update_FP(1)
                show flowey surprised
                flowey "......"
                flowey "..............."
                flowey "Oh."
                flowey "My."
                flowey "God."
                show flowey annoyed
                flowey "If you're a part of the \"Flowey Fan Club\" I'm going to seriously get pissed."
                flowey "That stupid group's supposed to be secret!"
                flowey "That dumb bag of bones wasn't supposed to run around {i}inviting{/i} people!"
                show flowey angry
                flowey "It's {i}literally{/i} just Papyrus! That idiot!"
                flowey "And there's no way you could have met him yet, so how did you--"
                show flowey surprised
                flowey "..."
                flowey "Wait."
                show flowey smug
                flowey "...Tch."
                flowey "Oh, I get it... You're just a {i}real freak{/i}, huh?"
                flowey "Well."
                show flowey laugh
                flowey "I'm definitely not that type of available, sicko."
                show flowey normal
                flowey "And I sure as hell never will be."
                flowey "So, if you got a {i}thing{/i} for {i}plants{/i}, then I suggest exploring the flowers around Toriel's house."
                flowey "......"
                show flowey sideglance
                flowey "Now..."
                flowey "I'm gonna go. I feel a little..."
                show flowey normal
                flowey "...uncomfortable."
            "We'll see.": #+2 HB
                $world.get_monster('Flowey').update_HB(2)
                show flowey surprised
                flowey "..."
                show flowey annoyed
                flowey "No, we won't."
                show flowey horror
                flowey "Don't even think about it, P A L."
                flowey "Now get lost."
            "You think I care about you? How cute.":
                $world.get_monster('Flowey').update_FP(-4)
                show flowey surprised
                flowey "...What?"
                show flowey sideglance
                flowey "No, of course not. That'd be stupid." 
                show flowey normal
                flowey "Now leave me alone."
                show flowey horror
                flowey "We wouldn't want an  a c c i d e n t  to happen, now, would we?"
        return
    
    label Flowey_Hangout_Path2:
        show flowey smug
        flowey "Because I don't need anyone around. {i}Especially{/i} someone like {i}you{/i}"
        show flowey annoyed
        flowey "You're more of an annoying gnat than a conversationalist."
        show flowey sideglance
        flowey "Quit bothering me and go away."
        
        menu:
            "Fine.":
                show flowey annoyed
                flowey "Well."
                show flowey angry
                flowey "If you're not going to leave, then I will."
                show flowey smug
                flowey "Feel free to stand around talking to yourself, though."
                show flowey laughing
                flowey "Idiot."
            "You'll be alone forever if you keep acting like that.":
                $world.get_monster('Flowey').update_HB(3)
                flowey "..."
                show flowey sad
                flowey ".........."
                flowey "Well."
                show flowey sideglance
                flowey "I don't care."
            "Everyone needs someone.":
                $world.get_monster('Flowey').update_FP(2)
                show flowey annoyed
                flowey "In case you didn't notice, idiot, I'm not exactly like everyone else here."
                flowey "..."
                show flowey sideglance
                flowey "I don't {i}need{/i} anyone."
                show flowey backside
                flowey "And I don't {i}want{/i} anyone, either."
                flowey "So go befriend Frisk or something..."
        return