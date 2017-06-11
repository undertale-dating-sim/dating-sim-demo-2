#when clicking on Flowey
label Flowey_Interaction:
    label Flowey_Regular_Dialogue:
        menu:
            #"Change Standing":
            #    jump Flowey_Change_Standing
            "Ruins":
                call Flowey_Ruins_Regular
            "Flowers":
                call Flowey_When_In_Flowers_Regular
            "Waterfall: Echo Flower Room":
                call Flowey_Waterfall_Echo_Flower_Room
            "Distant Castle View Room":
                call Flowey_Distant_Castle_View_Room_Regular
            "Casual Chats":
                call Flowey_Casual_Chats
            "Leave":
                call flowey_goodbye(owner)
                return
        call show_flowey_sprite(owner)
        jump Flowey_Regular_Dialogue

    #label Flowey_Change_Standing:
    #    menu:
    #        "Hated":
    #            $ flowey_hated = True
    #            $ flowey_disliked = False
    #            $ flowey_neutral = False
    #        "Disliked":
    #            $ flowey_hated = False
    #            $ flowey_disliked = True
    #            $ flowey_neutral = False
    #        "Neutral":
    #            $ flowey_hated = False
    #            $ flowey_disliked = False
    #            $ flowey_neutral = True
    #    jump Flowey_Regular_Dialogue
        
    label Flowey_Ruins_Regular:
        menu:
            "The ruins are nice, aren’t they?":
                show flowey annoyed with Dissolve(.25)
                flowey "I mean, I guess?"
                flowey "If you like these types of places."
                flowey "They’re old, cold, and at the brink of crumbling."
                show flowey sideglance with Dissolve(.25)
                flowey "..."
                flowey "Almost like the caretaker!"
            "The ruins are beautiful.":
                show flowey normal with Dissolve(.25)
                flowey "If you like this sort of stuff, then sure."
                show flowey wink with Dissolve(.25)
                flowey "I guess you like the dark, quiet, dusty old places, huh?"
            "What do you know about the ruins?":
                show flowey annoyed with Dissolve(.25)
                flowey "Well."
                flowey "There are plenty of puzzles and traps lying around just {i}waiting{/i} for you to make the wrong move."
                show flowey sideglance with Dissolve(.25)
                flowey "There's a caretaker, that old goat, trying to make sure that any dumb human who falls down here stays safe from... well..."
                show flowey wink with Dissolve(.25)
                flowey "Let’s just go with {i}accidents{/i}."
                show flowey normal with Dissolve(.25)
                flowey "Frisk is wandering around sometimes... being their usual indecisive self."
                show flowey smug with Dissolve(.25)
                flowey "And that old, earthy smell you’re getting a wiff of?"
                show flowey horror with Dissolve(.25)
                flowey "That’s probably just a bunch of dust from the corpses that flutter off in the breeze."
                show flowey sideglance with Dissolve(.25)
                flowey "..."
                show flowey normal with Dissolve(.25)
                flowey "Yeah, the ruins sure are swell."
            "Why are you in the ruins?":
                show flowey annoyed with Dissolve(.25)
                flowey "Because I feel like it."
                flowey "I can go wherever I please."
                flowey "I’m mostly here in hopes of you doing something interesting but..."
                flowey "So far looks like you’re just like that {i}other{/i} human, huh."
            "What do you like about the ruins?":
                if flowey_hated or flowey_disliked:
                    show flowey normal with Dissolve(.25)
                    flowey "The silence."
                    flowey "And the lack of idiots around."
                    show flowey sideglance with Dissolve(.25)
                    flowey "But looks like I gotta find a new place to hang out, huh?"
                elif flowey_neutral:
                    show flowey normal with Dissolve(.25)
                    flowey "I find myself curious sometimes."
                    flowey "I wonder if another human will fall down, and maybe they’ll {i}actually{/i} die from impact."
                    show flowey sideglance with Dissolve(.25)
                    flowey "..."
                    show flowey normal with Dissolve(.25)
                    flowey "But nope, the storyline doesn’t allow that sort of thing I guess."
                    flowey "..."
                    show flowey wink with Dissolve(.25)
                    flowey "This place also has one of the best sun spots, so I like to work on my tan."
                    flowey "Like all flowers of my stature do."
            "Leave":
                return
                
        call show_flowey_sprite(owner)
        jump Flowey_Ruins_Regular
                
    label Flowey_When_In_Flowers_Regular:
        menu:
            "Why are you hanging out with flowers?":
                show flowey normal with Dissolve(.25)
                flowey "I enjoy surprising people."
                flowey "Seeing reactions to idiots not expecting you is {i}great{/i}."
                show flowey wink with Dissolve(.25)
                flowey "...it’s especially fun when you get to catch monsters doing what they aren’t supposed to."

            "Do you ever wish you were a different kind of flower so you didn’t blend in so much?":
                show flowey annoyed with Dissolve(.25)
                flowey "I was born this way."
                flowey "Don’t ask me to be different just because {i}you{/i} have low self esteem."
                flowey "I may blend in, but that’s only when I want to."
                show flowey wink with Dissolve(.25)
                flowey "Obviously, you know it’s me when I stand out, dont’cha?"
            "Leave":
                return
                
        call show_flowey_sprite(owner)
        jump Flowey_When_In_Flowers_Regular

    label Flowey_Waterfall_Echo_Flower_Room:
        menu:
            "You don’t think it’s too dark or quiet here?":
                show flowey normal with Dissolve(.25)
                flowey "... are you scared?"
                menu:
                    "A little...":
                        if flowey_hated or flowey_disliked:
                            show flowey sideglance with Dissolve(.25)
                            flowey "Aw..."
                            show flowey horror with Dissolve(.25)
                            flowey "Alone, scared, in a dark and quiet place..."
                            show flowey smug with Dissolve(.25)
                            flowey "Sounds like the perfect setting for a murder mystery!"
                            flowey "Games always ease the tension-- So how about this,"
                            show flowey horror with Dissolve(.25)
                            flowey "I kill {i}you{i}, and then we find out if the others can guess who did it!"
                            flowey "Wouldn’t {i}that be F U N ?{/i}"
                        else:
                            show flowey normal with Dissolve(.25)
                            flowey "..."
                            flowey "What are you afraid of, exactly?"
                            show flowey annoyed with Dissolve(.25)
                            flowey "And if you say \"I’m afraid of monsters!\" I’m leaving."
                            flowey "There’s nothing lurking in the dark that you don’t know about--"
                            flowey "..."
                            flowey "Okay maybe there is, whoopsie."
                            show flowey wink with Dissolve(.25)
                            flowey "But if I told you everything so quickly what fun would that be~?"
                    "I’m not!":
                        if flowey_hated or flowey_disliked:
                            show flowey normal with Dissolve(.25)
                            flowey "Well."
                            flowey "..."
                            show flowey horror with Dissolve(.25)
                            flowey "Y O U   S H O U L D   B E  ."
                        else:
                            show flowey annoyed with Dissolve(.25)
                            flowey "Good."
                            flowey "I was worried I was dealing with a baby here."
                            show flowey sideglance with Dissolve(.25)
                            flowey "..."
                            flowey "There’s... no room for cry babies here."
                            flowey "Well, keep moving already! No reason to sit around talking to me!"
            "What are these blue flowers?":
                show flowey normal with Dissolve(.25)
                flowey "They’re called Echo Flowers."
                flowey "Fun for the whole family!"
                show flowey sideglance with Dissolve(.25)
                flowey "They repeat whatever is said to them, and sometimes they even repeat secrets."
                flowey "You’ll find a lot of them underground."
                flowey "..."
                show flowey normal with Dissolve(.25)
                flowey "Anything else you need to bother me with?"

            "Why do you like hanging out in here?":
                if flowey_hated or flowey_disliked:
                    show flowey normal with Dissolve(.25)
                    flowey "Well..."
                    flowey "I mostly enjoy hanging out here because-"
                    show flowey sideglance with Dissolve(.25)
                    flowey "It’s none of your business."
                else:
                    show flowey normal with Dissolve(.25)
                    flowey "Well..."
                    flowey "I can’t help but get a bit curious. Sure most of the secrets... the wishes... they’re the same. I’ve heard them all before."
                    flowey "But on rare occasions with that that {i}other human{/i}, and with you perhaps..."
                    flowey "There’s something different for me to enjoy."
                    flowey "..."
                    flowey "Sometimes we all find even the simplest of things entertaining."
            "Leave":
                return
        call show_flowey_sprite(owner)
        jump Flowey_Waterfall_Echo_Flower_Room
                
    label Flowey_Distant_Castle_View_Room_Regular:
        menu:
            "This is a great view of the castle, isn’t it?":
                if flowey_hated or flowey_disliked:
                    show flowey annoyed with Dissolve(.25)
                    flowey "Not really."
                    flowey "You could be seeing it up close and {i}personal{/i}."
                    flowey "But instead you’re standing here."
                    flowey "So how about getting this show on the road?"
                else:
                    show flowey normal with Dissolve(.25)
                    flowey "...Sure."
                    show flowey excited with Dissolve(.25)
                    flowey "But this view is nothing compared to actually being inside."
                    flowey "Even the courtyard is ginormous."
                    flowey "Hell, even the rooms inside of the place are huge and--"
                    show flowey normal with Dissolve(.25)
                    flowey "...."
                    show flowey annoyed with Dissolve(.25)
                    flowey "Tch."
                    flowey "Yeah... well..."
                    flowey "This view is great too, I guess."
                    menu:
                        "Have you been inside before?":
                            show flowey sad with Dissolve(.25)
                            flowey "..."
                            flowey "No."
                            flowey "...not in this timeline at least."
                            flowey "..."
                            show flowey annoyed with Dissolve(.25)
                            flowey "Shouldn’t you be interviewing actual monsters instead of flowers?"
                        "Say nothing.":
                            jump Flowey_Distant_Castle_View_Room_Regular
            "It’s really dark isn’t it?":
                show flowey normal with Dissolve(.25)
                flowey "Your eyes should have adjusted by now to the underground. I’m surprised you consider {i}this{/i} dark."
                show flowey sideglance with Dissolve(.25)
                flowey "...Or are you just {i}afraid?{/i}"
                show flowey normal with Dissolve(.25)
                flowey "Aw..."
                show flowey wink with Dissolve(.25)
                flowey "...Sucks to suck."
                
            "I didn’t think flowers liked dark places.":
                show flowey normal with Dissolve(.25)
                flowey "Golly!"
                show flowey sideglance with Dissolve(.25)
                flowey "You’re so funny that... my gosh I just forgot to laugh!"
                show flowey normal with Dissolve(.25)
                flowey "I’m {i}so{/i} sorry about that. Try again, and next time I’ll at {i}least{/i} giggle!"

            "Have you ever been to that castle?":
                if flowey_hated or flowey_disliked:
                    show flowey annoyed with Dissolve(.25)
                    flowey "..."
                    flowey "Nope."
                else:
                    show flowey normal with Dissolve(.25)
                    flowey "A few times."
                    flowey "Can’t say I care for it much, though."
                    show flowey annoyed with Dissolve(.25)
                    flowey "The {i}King of all Cowards{/i} lives there... with his huge garden of... {i}me’s{/i}."
                    flowey "And with all the golden flower tea he drinks?"
                    flowey "I’d be in such great danger!"
                    flowey "..."
                    show flowey normal with Dissolve(.25)
                    flowey "I have my own reasons for not visiting that often."
                    show flowey sideglance with Dissolve(.25)
                    flowey "But if you decide to go, how about making sure your {i}heart is kept under lock and key?{/i}"
                    flowey "{i}You never know{/i}..."
                    show flowey horror with Dissolve(.25)
                    flowey "{i}He just might try and take it. Hehehehe~{/i}"
            "Leave":
                return
                
        call show_flowey_sprite(owner)
        jump Flowey_Distant_Castle_View_Room_Regular

    label Flowey_Casual_Chats:
        show flowey normal with Dissolve(.25)
        menu: 
            "How are you?":
                if flowey_hated:
                    show flowey normal with Dissolve(.25)
                    flowey "I could be better."
                    flowey "I could be buried alive and {i}tortured{/i} for the rest of my life."
                    show flowey annoyed with Dissolve(.25)
                    flowey "...and yet here I am instead... having to hear your {i}cliche{/i} conversation starter of \"{i}how are you{/i}\"."
                    flowey "So many other {i}monsters{/i} waiting for a chat,"
                    flowey "But you instead choose to talk to the flower who doesn’t even like talking."
                    flowey "...Well."
                    flowey "Doesn’t care much for talking to braindead idiots like you, at least."
                    flowey "........"
                    flowey ".....Ugh."
                    show flowey angry with Dissolve(.25)
                    flowey "Don’t you have anything {i}better{/i} to do?"                
                elif flowey_disliked:
                    show flowey normal with Dissolve(.25)
                    flowey "Oh, just peachy-keen!"
                    flowey "I’m having the best time of my life, all things considered--"
                    show flowey sideglance with Dissolve(.25)
                    flowey "As in dealing with the likes of you confronting a flower on how they’re {i}feeling{/i}, which is ridiculous in itself, but I digress..."
                    show flowey normal with Dissolve(.25)
                    flowey "........Anyway."
                    flowey "Don’t you have anything {i}better{/i} to do?"
                else:
                    show flowey normal with Dissolve(.25)
                    flowey "....I guess I’m alright."
                    flowey "Not sure what you expect me to say, not much is going on."
                    show flowey annoyed with Dissolve(.25)
                    flowey "Mostly because you’re wasting time trying to chat up a flower instead of someone else."
                    show flowey sideglance with Dissolve(.25)
                    flowey "Now I {i}know{/i} you have something {i}better{/i} to do... don’tcha buddy?"
            
            "I think I need help...":
                flowey "Don't we all."
                flowey "And... with what exactly?"
                menu:
                    "I’m lost.":
                        show flowey normal with Dissolve(.25)
                        flowey "Then you should probably go find yourself, huh?"
                        show flowey sideglance with Dissolve(.25)
                        flowey "What do I look like, an information kiosk?"
                        
                    "I don’t know what to do next.":
                        show flowey normal with Dissolve(.25)
                        flowey "You could drop dead."
                        flowey "That’d be something."
                        show flowey sideglance with Dissolve(.25)
                        flowey "....Or you could try to think about what you might have missed."
                        flowey "Ya know, maybe a mission, or having to find someone?"
                        flowey "Who was the last person you talked to, hm? What did {i}they{/i} want from you?"
                        show flowey normal with Dissolve(.25)
                        flowey "Things like that."

            "What do you do for fun around here?":
                show flowey normal with Dissolve(.25)
                flowey "For fun?"
                show flowey wink with Dissolve(.25)
                flowey "Well, I like long walks on the beach, picking daisies and frolicking through the park!"
                flowey "............"
                show flowey annoyed with Dissolve(.25)
                flowey "Tch."
                flowey "That was a joke, in case you didn't get it."
                show flowey smug with Dissolve(.25)
                flowey "What I {i}really{/i} like to do for fun..."
                flowey "...Is watch morons fall from that big \"hard to miss\" hole in the mountain..."
                show flowey horror with Dissolve(.25)
                flowey "...slam down into a pile of flowers that aren't likely to keep normal people from snapping their tiny necks..." 
                flowey "...and watch them run around aimlessly trying to make a story for themselves!"
                show flowey normal with Dissolve(.25)
                flowey "That, my friend,"
                show flowey sideglance with Dissolve(.25)
                flowey "Is comedy gold."
                show flowey normal with Dissolve(.25)
                flowey "However it’s ineffective if {i}said{/i} moron would rather stand around talking to a flower instead of actually going forward."
                flowey "So on that note."
                flowey "Make it happen, {i}cap’n!{/i}"

            "How would you describe your perfect day?":
                show flowey smug with Dissolve(.25)
                flowey "Not dealing with you would be pretty perfect if I do say so myself."
                menu:
                    "Do you have a favorite color?":
                        show flowey normal with Dissolve(.25)
                        flowey "No."                        
                    "Do you have a favorite drink?":
                        if flowey_hated:
                            show flowey annoyed with Dissolve(.25)
                            flowey "No."                        
                        else:
                            show flowey normal with Dissolve(.25)
                            flowey "Water."
                        menu:
                            "Do you just hate casual conversation?":
                                show flowey annoyed with Dissolve(.25)
                                flowey "Do you just {i}hate{/i} living and enjoy walking into {i}suicidal situations?{/i}"
                                menu:
                                    "Alright moving on...":
                                        show flowey normal with Dissolve(.25)
                                        flowey "Right..."
                                        return
            "What’s it like being a flower?":
                show flowey normal with Dissolve(.25)
                flowey "It’s exactly what you’d expect it to be."
                show flowey sideglance with Dissolve(.25)
                flowey "..."
                show flowey normal with Dissolve(.25)
                flowey "Anything else ya need, {i}pal?{/i}"

            "How’s the weather down there?":
                show flowey annoyed with Dissolve(.25)
                flowey "..."
                show flowey angry with Dissolve(.25)
                flowey "If you were completely useless, I’d rip you open from the inside out."
                flowey "{i}Good thing you’re insured{/i}."

            "What do you think about...":
                jump Flowey_Other_Characters
                
            "Do you believe in fate or destiny?":
                if flowey_hated:
                    show flowey smug with Dissolve(.25)
                    flowey "I believe in burying people alive and hearing them scream."
                elif flowey_disliked:
                    show flowey annoyed with Dissolve(.25)
                    flowey "Is this really a question you should be bothering with right now?"
                    flowey "It’s nice to see you have your priorities in order."
                else:
                    show flowey annoyed with Dissolve(.25)
                    flowey "Neither."
                    flowey "Both are dumb."
            "Leave":
                return
        
        call show_flowey_sprite(owner)
        jump Flowey_Casual_Chats
        
    label Flowey_Other_Characters:
        menu:
            "Toriel":
                if flowey_hated or flowey_disliked:
                    call Flowey_Casual_Hated from _call_Flowey_Casual_Hated
                else:
                    show flowey normal with Dissolve(.25)
                    flowey "She’s got a green thumb, I guess?"
                    flowey "I don’t think much of her, if that matters."
                    show flowey sideglance with Dissolve(.25)
                    flowey "...."
                    show flowey normal with Dissolve(.25)
                    flowey "She waters me sometimes."
                    flowey "The end."                        
            "Frisk":
                if flowey_hated or flowey_disliked:
                    call Flowey_Casual_Hated from _call_Flowey_Casual_Hated_1
                else:
                    show flowey smug with Dissolve(.25)
                    flowey "The one who fell before you..."
                    flowey "And spontaneously decided \"{i}Let’s just stay- why the hell not?{/i}\""
                    show flowey annoyed with Dissolve(.25)
                    flowey "How great."
                    flowey "They did nothing at {i}all{/i} and it is just {i}ridiculous{/i}."
                    flowey "...which is somewhat similar to what you’re doing now so, I guess it must be human nature to waste a person’s time."

            "Napstablook":
                if flowey_hated or flowey_disliked:
                    call Flowey_Casual_Hated from _call_Flowey_Casual_Hated_2
                else:
                    show flowey normal with Dissolve(.25)
                    flowey "...."
                    flowey "What’s there to think about?"
                    flowey "They’re a ghost."
                    flowey "....."
                    flowey "...’nuff said."
            "Mettaton":
                if flowey_hated or flowey_disliked:
                    call Flowey_Casual_Hated from _call_Flowey_Casual_Hated_3
                else:
                    show flowey normal with Dissolve(.25)
                    flowey "I'm not gonna lie."
                    show flowey wink with Dissolve(.25)
                    flowey "Those are some mighty fine legs."
                    show flowey normal with Dissolve(.25)
                    flowey "Remove them, and they could also do some mighty fine damage to that stupid, glittery face of his."
            "Sans":
                if flowey_hated or flowey_disliked:
                    call Flowey_Casual_Hated from _call_Flowey_Casual_Hated_4
                else:
                    show flowey normal with Dissolve(.25)
                    flowey "...."
                    flowey "I refer to him as Smiley Trashbag."
                    show flowey sideglance with Dissolve(.25)
                    flowey "..."
                    show flowey normal with Dissolve(.25)
                    flowey "....Don’t you have {i}anyone better{/i} to talk about?"
            "Papyrus":
                if flowey_hated or flowey_disliked:
                    call Flowey_Casual_Hated from _call_Flowey_Casual_Hated_5
                else:
                    show flowey normal with Dissolve(.25)
                    flowey "...."
                    show flowey sideglance with Dissolve(.25)
                    flowey "Papyrus is a rather {i}special{/i} case."
                    flowey "....He’s pretty much on a {i}need to know basis."
                    show flowey normal with Dissolve(.25)
                    flowey "....And you really don’t {i}need to know{/i}, so let’s move along, shall we?"
            "Undyne":
                if flowey_hated or flowey_disliked:
                    call Flowey_Casual_Hated from _call_Flowey_Casual_Hated_6
                else:
                    show flowey normal with Dissolve(.25)
                    flowey "What’s there to think about?"
                    show flowey sideglance with Dissolve(.25)
                    flowey "She’s the generic {i}storybook heroine{/i}."
                    show flowey normal with Dissolve(.25)
                    flowey "Get to know her better and see for yourself."
            "Alphys":
                if flowey_hated or flowey_disliked:
                    call Flowey_Casual_Hated from _call_Flowey_Casual_Hated_7
                else:
                    show flowey normal with Dissolve(.25)
                    flowey "..."
                    flowey "There’s so many things that can be said about that one."
                    show flowey sideglance with Dissolve(.25)
                    flowey "Are they {i}good things?{/i} Are they {i}bad things?{/i}"
                    show flowey normal with Dissolve(.25)
                    flowey "Well,"
                    flowey "That’s for you to decide later on, isn’t it?"
            "Asgore":
                if flowey_hated or flowey_disliked:
                    call Flowey_Casual_Hated from _call_Flowey_Casual_Hated_8
                else:
                    show flowey normal with Dissolve(.25)
                    flowey "..."
                    flowey "He's a green thumb, like the {i}other one{/i}."
                    show flowey sideglance with Dissolve(.25)
                    flowey "Flowerboy... manchild."
                    flowey "The {i}King of All Monsters{/i} if you will."
                    show flowey normal with Dissolve(.25)
                    flowey "Not much else to that, the end."
            "Nevermind":
                call show_flowey_sprite(owner)
                return
                
        call show_flowey_sprite(owner)
        jump Flowey_Other_Characters
                
    label Flowey_Casual_Hated:
        show flowey annoyed with Dissolve(.25)
        flowey "Well they don’t waste my time as much as {i}you{/i}."
        flowey "So on that note, from a scale of 1 to 10, you’re hell of alot {i}worse{/i} than they are."
        flowey "And yes, choosing a different person for me to critique will give you the exact same answer."
        show flowey normal with Dissolve(.25)
        flowey "So spare me repeating myself until you’re further acquainted with someone who cares about you."
        show flowey sideglance with Dissolve(.25)
        flowey "Which so far..."
        show flowey horror with Dissolve(.25)
        flowey "{i}No one does{/i}."  
        return