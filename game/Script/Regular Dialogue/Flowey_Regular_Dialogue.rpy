$ flowey_hated = True
$ flowey_disliked = False
$ flowey_neutral = False
label Flowey_Regular_Dialogue:
    menu:
        "Change Standing":
            jump Flowey_Change_Standing
        "Ruins":
            call Flowey_Ruins_Regular from _call_Flowey_Ruins_Regular
        "Flowers":
            call Flowey_When_In_Flowers_Regular from _call_Flowey_When_In_Flowers_Regular
        "Waterfall: Echo Flower Room":
            call Flowey_Waterfall_Echo_Flower_Room from _call_Flowey_Waterfall_Echo_Flower_Room
        "Distant Castle View Room":
            call Flowey_Distant_Castle_View_Room_Regular from _call_Flowey_Distant_Castle_View_Room_Regular
        "Casual Chats":
            call Flowey_Casual_Chats from _call_Flowey_Casual_Chats

label Flowey_Change_Standing:
    menu:
        "Hated":
            $ flowey_hated = True
            $ flowey_disliked = False
            $ flowey_neutral = False
        "Disliked":
            $ flowey_hated = False
            $ flowey_disliked = True
            $ flowey_neutral = False
        "Neutral":
            $ flowey_hated = False
            $ flowey_disliked = False
            $ flowey_neutral = True
    jump Flowey_Regular_Dialogue
label Flowey_Ruins_Regular:
    menu:
        "The ruins are nice, aren’t they?":
            flowey "I mean, I guess?"
            flowey "If you like these types of places."
            flowey "They’re old, cold, and at the brink of crumbling down to extinction."
            flowey "..."
            flowey "Almost like the caretaker!"
        "The ruins are beautiful.":
            flowey "If you like this sort of stuff, then sure."
            flowey "I guess you like the dark, quiet, dusty old places, huh?"
        "What do you know about the ruins?":
            flowey "Well."
            flowey "There are plenty of puzzles and traps lying around just waiting for you to make the wrong step."
            flowey "Toriel is the caretaker, trying to make sure that any dumb human who falls down here stays safe from... well..."
            flowey "Let’s just go with accidents."
            flowey "Frisk is wandering around sometimes... being their usual indecisive self."
            flowey "And that old, earthy smell you’re getting a wiff of?"
            flowey "That’s probably just a bunch of dust from the corpses that flutter off in the breeze."
            flowey "..."
            flowey "Yeah, the ruins sure are swell."
        "Why are you in the ruins?":
            flowey "Because I feel like it."
            flowey "I can go wherever I please."
            flowey "I’m mostly here in hopes of you doing something interesting but..."
            flowey "So far looks like you’re just another Frisk, huh."
        "What do you like about the ruins?":
            if flowey_hated or flowey_disliked:
                flowey "The silence."
                flowey "And the lack of idiots around."
                flowey "But looks like I gotta find a new place to hang out, huh?"
            elif flowey_neutral:
                flowey "I find myself curious sometimes."
                flowey "I wonder if another human will fall down, and maybe they’ll actually die from impact."
                flowey "..."
                flowey "But nope, the storyline doesn’t allow that sort of thing I guess."
                flowey "..."
                flowey "This place also has one of the best sun spots, so I like to work on my tan."
                flowey "Like all flowers of my stature do."
        "Leave":
            jump Flowey_Regular_Dialogue
    jump Flowey_Ruins_Regular
label Flowey_When_In_Flowers_Regular:
    menu:
        "Why are you hanging out with flowers?":
            flowey "I enjoy surprising people."
            flowey "Seeing reactions to idiots not expecting you is great."
            flowey "...it’s especially fun when you get to catch monsters doing what they aren’t supposed to."

        "Do you ever wish you were a different kind of flower so you didn’t blend in so much?":
            flowey "I was born this way."
            flowey "Don’t ask me to be different just because you have low self esteem."
            flowey "I may blend in, but that’s only when I want to."
            flowey "Obviously, you know it’s me when I stand out, dont’cha?"
        "Leave":
            jump Flowey_Regular_Dialogue
    jump Flowey_When_In_Flowers_Regular

label Flowey_Waterfall_Echo_Flower_Room:    

    menu:
        "You don’t think it’s too dark or quiet here?":
            flowey "... are you scared?"
            menu:
                "A little...":
                    if flowey_hated or flowey_disliked:
                        flowey "Aw..."
                        flowey "Alone, scared, in a dark and quiet place..."
                        flowey "Sounds like the perfect setting for a murder mystery!"
                        flowey "Games always ease the tension-- So how about this,"
                        flowey "I kill you, and then we find out if the others can guess who did it!"
                        flowey "Wouldn’t that be F U N ?"
                    else:
                        flowey "..."
                        flowey "What are you afraid of, exactly?"
                        flowey "And if you say ‘I’m afraid of monsters!’ I’m leaving."
                        flowey "There’s nothing lurking in the dark that you don’t know about--"
                        flowey "..."
                        flowey "Okay maybe there is, whoopsie."
                        flowey "But if I told you everything so quickly what fun would that be~?"
                "I’m not!":
                    if flowey_hated or flowey_disliked:
                        flowey "Well."
                        flowey "..."
                        flowey "Y O U   S H O U L D   B E  ."
                    else:
                        flowey "Good."
                        flowey "I was worried I was dealing with a baby here."
                        flowey "..."
                        flowey "There’s... no room for cry babies here."
                        flowey "Well, keep moving already! No reason to sit around talking to me!"
        "What are these blue flowers?":
            flowey "They’re called Echo Flowers."
            flowey "Fun for the whole family!"
            flowey "They repeat whatever is said to them, and sometimes they even repeat secrets."
            flowey "You’ll find a lot of them underground."
            flowey "..."
            flowey "Anything else you need to bother me with?"

        "Why do you like hanging out in here?":
            if flowey_hated or flowey_disliked:
                flowey "Well..."
                flowey "I mostly enjoy hanging out here because-"
                flowey "It’s none of your business."
            else:
                flowey "Well..."
                flowey "I can’t help but get a bit curious. Sure most of the secrets being told, the wishes being given, they’re all the same... I’ve heard them before."
                flowey "But on rare occasions, like with Frisk, and with you perhaps..."
                flowey "There’s something different for me to enjoy."
                flowey "..."
                flowey "Sometimes we all find even the simplest of things entertaining."
        "Leave":
            jump Flowey_Regular_Dialogue
    jump Flowey_Waterfall_Echo_Flower_Room
label Flowey_Distant_Castle_View_Room_Regular:
    menu:
        "This is a great view of the castle, isn’t it?":
            if flowey_hated or flowey_disliked:
                flowey "Not really."
                flowey "You could be seeing it up close and personal."
                flowey "But instead you’re standing here."
                flowey "So how about getting this show on the road?"
            else:
                flowey "...Sure."
                flowey "But this view is nothing compared to actually being inside."
                flowey "Even the courtyard is ginormous."
                flowey "The rooms inside of the place are huge and--"
                flowey "...."
                flowey "Tch."
                flowey "Yeah... well..."
                flowey "This view is great too, I guess."
                menu:
                    "Have you been inside before?":
                        flowey "..."
                        flowey "No."
                        flowey "...not in this timeline at least."
                        flowey "..."
                        flowey "Shouldn’t you be interviewing actual monsters instead of flowers?"
                    "You sound like you’ve been inside of the castle once.":
                        flowey "..."
                        flowey "No."
                        flowey "...not in this timeline at least."
                        flowey "..."
                        flowey "Shouldn’t you be interviewing actual monsters instead of flowers?"
                    "Say nothing.":
                        jump Flowey_Distant_Castle_View_Room_Regular
        "It’s really dark isn’t it?":
            flowey "Your eyes should have adjusted by now to the underground. I’m surprised you consider this dark."
            flowey "...Are you just afraid?"
            flowey "Aw..."
            flowey "...Sucks to suck."
        "I didn’t think flowers liked dark places.":
            flowey "Golly!"
            flowey "You’re so funny that... my gosh I just forgot to laugh!"
            flowey "I’m so sorry about that, maybe try again and next time I’ll giggle for sure!"

        "Have you ever been to that castle?":
            if flowey_hated or flowey_disliked:
                flowey "..."
                flowey "Nope."
            else:
                flowey "A few times."
                flowey "Can’t say I care for it much, though."
                flowey "Asgore lives there... with his huge garden of... me’s."
                flowey "And all the golden flower tea he drinks?"
                flowey "I’d be in such great danger!"
                flowey "..."
                flowey "I have my own reasons for not visiting that often."
                flowey "But if you decide to gore, how about making sure your heart is kept under lock and key?"
                flowey "You never know..."
                flowey "He just might try and take it. Hehehehe~"
        "Leave":
            jump Flowey_Regular_Dialogue
    jump Flowey_Distant_Castle_View_Room_Regular

label Flowey_Casual_Chats:
    menu: 
        "How are you?":
            if flowey_hated:
                flowey "I could be better."
                flowey "I could be buried alive and tortured for the rest of my life."
                flowey "...and yet here I am instead... having to hear your cliche conversation starters of ‘how are you’."
                flowey "So many other monsters waiting for a chat,"
                flowey "But you instead choose to talk to the flower who doesn’t even like talking."
                flowey "...Well."
                flowey "At least doesn’t care much for talking to braindead idiots like yourself."
                flowey "........"
                flowey ".....ugh."
                flowey "Don’t you have anything better to do?"                
            elif flowey_disliked:
                flowey "Oh, just peachy-keen!"
                flowey "I’m having the best time of my life, all things considered--"
                flowey "As in dealing with the likes of you confronting a flower on how they’re feeling which is ridiculous in itself BUT I digress..."
                flowey "........anyway."
                flowey "Don’t you have anything better to do?"
            else:
                flowey "....I guess I’m alright."
                flowey "Not sure what you expect me to say, not much is going on."
                flowey "Mostly because you’re wasting time trying to chat up a flower instead of someone else."
                flowey "Now I know you have something better to do... don’tcha buddy?"
        "I think I need help...":
            flowey "And... with what exactly?"
            menu:
                "I’m lost.":
                    flowey "Then you should probably go find yourself then, huh."
                    flowey "What do I look like? An information kiosk?"                    
                "I don’t know what to do next.":
                    flowey "You could drop dead."
                    flowey "That’d be something."
                    flowey "....or you could try to think about what you’re missing."
                    flowey "Ya know, maybe a mission, or having to find someone?"
                    flowey "Things like that."


        "What do you do for fun around here?":
            flowey "For fun?"
            flowey "Well, I like long walks on the beach, picking daisies and frolicking through the park!"
            flowey "............"
            flowey "Tch."
            flowey "In case you didn’t get that, it was a joke."
            flowey "What I really like to do for fun..."
            flowey "...is watch morons fall from that big ‘hard to miss’ hole in the mountain,"
            flowey "slam down into a pile of flowers that are less than likely to keep normal people from snapping their tiny necks," 
            flowey "and watch them run around aimlessly trying to make a story for themselves!"
            flowey "That, my friend"
            flowey "Is comedy gold."
            flowey "However it’s uneffective if said moron would rather stand around talking to a flower instead of actually going forward."
            flowey "So on that note."
            flowey "Make it happen, cap’n!"

        "How would you describe your perfect day?":
            flowey "Not dealing with you would be pretty perfect if I do say so myself."
            menu:
                "Do you have a favorite color?":
                    flowey "No."                        
                "Do you have a favorite drink?":
                    if flowey_hated:
                        flowey "No."                        
                    else:
                        flowey "Water."
                    menu:
                        "Do you just hate casual conversation?":
                            flowey "Do you just hate living and enjoy walking into suicidal situations?"
                            menu:
                                "Alright moving on...":
                                    flowey "Right..."
                                    jump Flowey_Regular_Dialogue
        "What’s it like being a flower?":
            flowey "It’s exactly what you’d expect it to be."
            flowey "..."
            flowey "Anything else ya need, pal?"

        "How’s the weather down there?":
            flowey "..."
            flowey "If you were completely useless, I’d rip you open from the inside out."
            flowey "Good thing you’re insured."

        "What do you think about...":
            jump Flowey_Other_Characters
            
        "Do you believe in fate or destiny?":
            if flowey_hated:
                flowey "I believe in burying people alive and hearing them scream."
            elif flowey_disliked:
                flowey "Is this really a question you should be bothering with now?"
                flowey "It’s nice to see you have your priorities straightened out."
            else:
                flowey "Neither."
                flowey "Both are dumb."
        "Leave":
            jump Flowey_Regular_Dialogue
    jump Flowey_Casual_Chats
    label Flowey_Other_Characters:
        menu:
            "Toriel":
                if flowey_hated or flowey_disliked:
                    call Flowey_Casual_Hated from _call_Flowey_Casual_Hated
                else:
                    flowey "She’s got a green thumb I guess?"
                    flowey "I don’t think much of her, if that matters."
                    flowey "...."
                    flowey "She waters me sometimes."
                    flowey "The end."                        
            "Frisk":
                if flowey_hated or flowey_disliked:
                    call Flowey_Casual_Hated from _call_Flowey_Casual_Hated_1
                else:
                    flowey "The one who fell before you..."
                    flowey "And spontaneously decided \"Let’s just stay why the hell not?\""
                    flowey "How great."
                    flowey "They did nothing at all and it is just ridiculous."
                    flowey "...which is somewhat similar to what you’re doing now so, I guess it must be a general human trait to waste a person’s time."

            "Napstablook":
                if flowey_hated or flowey_disliked:
                    call Flowey_Casual_Hated from _call_Flowey_Casual_Hated_2
                else:
                    flowey "...."
                    flowey "What’s there to think about?"
                    flowey "They’re a ghost."
                    flowey "....."
                    flowey "...’nuff said."
            "Mettaton":
                if flowey_hated or flowey_disliked:
                    call Flowey_Casual_Hated from _call_Flowey_Casual_Hated_3
                else:
                    flowey "I will not tell a lie."
                    flowey "Those are some mighty fine legs."
                    flowey "If only they could be used to beat the rest of himself with."
            "Sans":
                if flowey_hated or flowey_disliked:
                    call Flowey_Casual_Hated from _call_Flowey_Casual_Hated_4
                else:
                    flowey "...."
                    flowey "I refer to him as Smiley Trashbag."
                    flowey "..."
                    flowey "....Don’t you have anyone better to talk about?"
            "Papyrus":
                if flowey_hated or flowey_disliked:
                    call Flowey_Casual_Hated from _call_Flowey_Casual_Hated_5
                else:
                    flowey "...."
                    flowey "Papyrus is a rather special case."
                    flowey "....He’s pretty much on a need to know basis."
                    flowey "....which you really don’t need to know my opinion on him so let’s move along, shall we?"
            "Undyne":
                if flowey_hated or flowey_disliked:
                    call Flowey_Casual_Hated from _call_Flowey_Casual_Hated_6
                else:
                    flowey "What’s there to think about?"
                    flowey "She’s the generic hero in most stories."
                    flowey "Get to know her better and see for yourself."
            "Alphys":
                if flowey_hated or flowey_disliked:
                    call Flowey_Casual_Hated from _call_Flowey_Casual_Hated_7
                else:
                    flowey "..."
                    flowey "There’s so many things that can be said about that one."
                    flowey "Are they good things? Are they bad things?"
                    flowey "Well,"
                    flowey "that’s for you to decide later on, isn’t it?"
            "Asgore":
                if flowey_hated or flowey_disliked:
                    call Flowey_Casual_Hated from _call_Flowey_Casual_Hated_8
                else:
                    flowey "..."
                    flowey "Also a green thumb,"
                    flowey "Flowerboy... manchild."
                    flowey "The King of All Monsters if you will."
                    flowey "Not much else to that, the end."
            "Nevermind":
                jump Flowey_Casual_Chats
        jump Flowey_Other_Characters
    label Flowey_Casual_Hated:
        flowey "Well they don’t waste my time as much as you."
        flowey "So on that note, from a scale of 1 to 10, you’re hell of alot worse than they are."
        flowey "And yes, choosing a different person for me to critique will give you the exact same answer."
        flowey "So spare me repeating myself until you’re further acquainted with someone who cares about you."
        flowey "Which so far..."
        flowey "No one does."  
        jump Flowey_Casual_Chats




