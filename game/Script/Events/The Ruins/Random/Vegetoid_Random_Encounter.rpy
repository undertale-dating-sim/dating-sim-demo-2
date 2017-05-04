label vegetoid_ruins_re_start:
    
    "Oh hello!"
    show vegetoid normal  at Position(xpos = 0.5,xanchor = 'center', yanchor = 'center')  with moveinbottom
    "* A wild Vegetoid has appeared!"
    show vegetoid normal at Position(xpos = 0.5,ypos=.5, xanchor = 'center', yanchor = 'center') with moveinbottom
    "* ....."
    "* They seem to be asking for assistance in the pursuit of higher education."

    menu:
        "Alright, how can I help you?":
            show vegetoid happy at center with dissolve
            vegetoid "I want to live my dream of being an accountant, but I need help with math."
            menu:
                "Never mind, accountants suck.":
                    show vegetoid normal at center with dissolve
                    vegetoid "Yeah, well so do you."
                    menu:
                        "Excuse you, I am a delight.":
                            vegetoid "I disagree. Now leave me alone, I need to make my mouther proud."
                            hide vegetoid with dissolve
                            return
                        "I'm just telling the truth.":
                            vegetoid "....I know."
                            hide vegetoid with moveoutbottom
                            "Vegetoid runs away crying"
                            return
                        "Leave them, they don't deserve your presence.":
                            hide vegetoid with dissolve
                            "You leave the Vegetoid to figure out math by themself."
                            return

                "Alright, do you know how to calculate income or social security tax?":
                    show vegetoid normal at center with dissolve
                    vegetoid "I said I needed help with math, not taxes."
                    menu:
                        "Taxes are math.":
                            vegetoid "No, taxes are taxes and math is math."
                            menu:
                                "Do you want my help or not?":
                                    vegetoid "Well it's not like you are being much help in the first place."
                                    menu:
                                        "Hey, stop being so rude.":
                                            hide vegetoid with moveoutbottom
                                            vegetoid "Alright then, I guess I'll just leave."
                                            return
                                        "Maybe you should help yourself before you expect others to help you.":
                                            vegetoid "...I know.  I just wanted to make my parents proud of me for once."
                                            hide vegetoid with moveoutbottom
                                            "Vegetoid runs away crying."
                                            return
                                        "Leave them. They clearly don't recognize genius.":
                                            hide vegetoid with moveoutbottom
                                            "You leave the vegetoid to figure out math by themself."
                                            return
                                "Can you tell me what part of math you need help with?":
                                    vegetoid "You know, math. Like counting and stuff."
                                    menu:
                                        "I think you should try to pursue careers that don't involve math.":
                                            vegetoid "No, I want to be an accountant."
                                            hide vegetoid with moveoutbottom
                                            vegetoid "You are not the boss of me. I'm going to find someone that will actually be useful."
                                            return
                                        "Sorry, I don't know how to count either.":
                                            hide vegetoid with moveoutbottom
                                            vegetoid "Figures, you don’t seem the type. I’ll try to find someone else then."
                                            return
                                        "Leave them. You don't want to deal with this.":
                                            hide vegetoid with moveoutbottom
                                            "You leave the vegetoid to figure out math by themself."
                                            return

                                "Leave. This is pointless.":
                                    hide vegetoid with moveoutbottom
                                    "You leave the vegetoid to figure out math by themself."
                                    return
                        "Um. Okay. Do you know how to add?":
                            show vegetoid happy at center with dissolve
                            vegetoid "You know, math. Like counting and stuff."
                            menu:
                                "I think you should try to pursue careers that don't involve math.":
                                    show vegetoid normal at center with dissolve
                                    vegetoid "No, I want to be an accountant."
                                    hide vegetoid with moveoutbottom
                                    vegetoid "You are not the boss of me. I'm going to find someone that will actually be useful."
                                    return
                                "Sorry, I don't know how to count either.":
                                    hide vegetoid with moveoutbottom
                                    vegetoid "Figures, you don’t seem the type. I’ll try to find someone else then."
                                    return
                                "Leave them. You don't want to deal with this.":
                                    hide vegetoid with moveoutbottom
                                    "You leave the vegetoid to figure out math by themself."
                                    return
                        "Do you know what an accountant is?":
                            show vegetoid happy at center with dissolve
                            vegetoid "Yeah, they do, like, math and stuff."
                            menu:
                                "No, they do interpretive dancing.":
                                    show vegetoid normal at center with dissolve
                                    vegetoid "Wait really? I can't get my parents to be proud of me with interpretive dancing."
                                    hide vegetoid with moveoutbottom
                                    return

                                "You know what, I suggest you try searching Google for answers.":
                                    show vegetoid normal at center with dissolve
                                    vegetoid "You're right. It's not as if you're helping me, anyway."

                                    return

                                "Leave them. This is pointless.":
                                    show vegetoid normal at center with dissolve
                                    "You leave the vegetoid to figure out math by themself."
                                    return

                "I suggest you go for an easier job, like a writer for a dating sim or something.":
                    vegetoid "I don't think you appreciate the amount of effort those people go through for these things."
                    menu:
                        "Alright then, be a coder. That can't be too hard.":
                            vegetoid "I don't know if that is any better. Why don't you try to be more helpful?"
                        
                            menu:
                                "Hey, stop being so rude.":
                                    vegetoid "Alright then, I guess I'll just leave."
                                    hide vegetoid with moveoutbottom
                                    return
                                "Maybe you should help yourself before you expect others to help you.":
                                    vegetoid "...I know.  I just wanted to make my parents proud of me for once."
                                    hide vegetoid with moveoutright
                                    "Vegetoid runs away crying."
                                    return
                                "Leave them. They clearly don't recognize genius.":
                                    hide vegetoid with moveoutbottom
                                    "You leave the vegetoid to figure out math by themself."
                                    return

                        "What about an artist?":
                            vegetoid "No thanks, I want my parents to be proud of me. Try being more helpful."
                            menu:
                                "Hey, stop being so rude.":
                                    vegetoid "Alright then, I guess I'll just leave."
                                    hide vegetoid with moveoutbottom
                                    return
                                "Maybe you should help yourself before you expect others to help you.":
                                    vegetoid "...I know.  I just wanted to make my parents proud of me for once."
                                    hide vegetoid with moveoutright
                                    "Vegetoid runs away crying."
                                    return
                                "Leave them. They clearly don't recognize genius.":
                                    hide vegetoid with moveoutbottom
                                    "You leave the vegetoid to figure out math by themself."
                                    return
                        "Give up. Live on the streets.":
                            vegetoid "You're not being very helpful."
                            menu:
                                "Hey, stop being so rude.":
                                    vegetoid "Alright then, I guess I'll just leave."
                                    hide vegetoid with moveoutbottom
                                    return
                                "Maybe you should help yourself before you expect others to help you.":
                                    vegetoid "...I know.  I just wanted to make my parents proud of me for once."
                                    hide vegetoid with moveoutright
                                    "Vegetoid runs away crying."
                                    return
                                "Leave them. They clearly don't recognize genius.":
                                    hide vegetoid with moveoutright
                                    "You leave the vegetoid to figure out math by themself."
                                    return

        "College isn't worth it.":
            vegetoid "Well, unlike you, I plan to be successful in life."
            menu:
                "You will never be a successful accountant.":
                    vegetoid "...You sound just like my parents."
                    hide vegetoid with moveoutright
                    "Vegetoid runs away crying."
                    return
                "I know, I'm a failure.":
                    vegetoid "At least some of use are self aware. Now if you don't mind, I'm going to go and become a hard-working member of society!"
                    hide vegetoid with moveoutbottom
                    "Vegetoid has left."
                    return
                "Hey, at least I'm not a vegetable.":
                    vegetoid "Oh yeah? At least I'm not an unhelpful jerk."
                    menu:
                        "Hey, don't be rude.":
                            vegetoid "Alright then, I guess I'll just leave."
                            hide vegetoid with moveoutbottom
                            "Vegetoid has left."
                            return

                        "Maybe you should help yourself before you expect others to help you.":
                            vegetoid "...I know. I just wanted to make my parents proud of me for once."
                            hide vegetoid with moveoutright
                            "Vegetoid runs away crying."
                            return
                        "Leave them. They clearly don't recognize genius.":
                            hide vegetoid with moveoutbottom
                            "You leave the vegetoid by themself."
                            return

        "I think you might be a plant.":
            vegetoid "Wow, really, smart guy?"
            menu:
                "Plants can’t pursue higher education.":
                    vegetoid "I get to decide what plants do, not you."
                    menu:
                        "It’s just common sense.":
                            vegetoid "'Common Sense' is doing something productive instead of playing a video game."
                            menu:
                                "I have no idea what you are talking about.":
                                    vegetoid "Right, of course you don't. Talk to me when you have a better answer."
                                    hide vegetoid with moveoutbottom
                                    return
                                "Don't you dare go meta on me.":
                                    vegetoid "I have no idea what you are talking about. Goodbye."
                                    hide vegetoid with moveoutbottom
                                    return

                        "Leave them. Plants can’t talk.":
                            hide vegetoid with moveoutbottom
                            "You leave the vegetoid all by themself."
                            return
                "Was that sarcasm?":
                    vegetoid "What, no, of course not. I would never."
                    menu:
                        "I'm starting to think that you might be lying.":
                            vegetoid "How dare you accuse me of such things. You don't deserve to talk to me."
                            hide vegetoid with moveoutbottom
                            return
                        "Alright, if you say so.":
                            vegetoid "..."
                            vegetoid "Good talk."
                            hide vegetoid with moveoutbottom
                            return
                "‍‍So... you are a plant?":
                    show vegetoid normal at center with dissolve
                    vegetoid "No, I'm the absolute god of hyperdeath. What do you think I am?"
                    menu:
                        "Okay, I get it. You are a plant. Geez.":
                            vegetoid "Are you sure? How do you know I’m not the absolute god of hyperdeath, huh? It’s not as if you can recognize a plant on sight."
                            menu:
                                "Hey, stop being so rude.":
                                    vegetoid "Alright then, I guess I'll just leave."
                                    hide vegetoid with moveoutbottom
                                    "* Vegetoid has left."
                                    return
                                "* Leave the overly sarcastic plant.":
                                    hide vegetoid with moveoutbottom
                                    "* You leave the vegetoid all by themself."
                                    return

                        "I don't know but you remind me of a carrot.":
                            show vegetoid happy at center with dissolve
                            vegetoid "That is because I'm part of a Complete and Balanced Breakfast™."
                            menu:
                                "So does that mean I can eat you?":
                                    vegetoid "Please stay away from me."
                                    hide vegetoid with moveoutbottom
                                    "* Vegetoid runs away in fear."
                                    return
                                "* Run away. This carrot is intimidating.":
                                    hide vegetoid with moveoutbottom
                                    "* You flee from the vegetoid."
                                    return

                        "You look like my grandmother.":
                            show vegetoid normal at center with dissolve
                            vegetoid "...How?"
                            menu:
                                "You know, because you're all wrinkly and stuff.":
                                    vegetoid "If you’re going to be like that then I’m leaving."
                                    hide vegetoid with moveoutbottom
                                    "* Vegetoid has left."
                                    return

                                "I think it is just your personality.":
                                    vegetoid "???"
                                    hide vegetoid with moveoutbottom
                                    "* Vegetoid has left."
                                    return
                                "* Leave before you have to explain yourself":
                                    "* You leave the vegetoid all by themself."
                                    hide vegetoid with moveoutbottom
                                    return




