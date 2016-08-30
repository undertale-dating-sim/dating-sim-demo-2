#Whimsun Random Encounter for the Ruins
label whimsun_re_start:
    scene
    "You come upon a group of Loox and Migosp bullying a Whimsun."
    menu:
        "They look like they deserve it.":
            $ player.modify_cruelty(5)
            "The monsters turn to sneer at you, then go back to bullying the Whimsun."
            "You walk away."
            return
            

        "Take Whimun's arm and run away.":
            $ player.modify_cowardice(4)
            "You quickly snatch the Whimsun away from the bullies and the two of you rush to another room."
            "For some reason, Whimsun doesn't look any happier."
            call whimsun_ruins_run
            

        "Hey- stop hurting them!":
            $ player.modify_bravery(3)
            call whimsun_ruins_facebullies
            
    return

label whimsun_ruins_facebullies:
    "They stop bullying the Whimsun, but now they're looking at you."

    'One of them says, "Oh yeah? And what are you gonna do about it?'

    menu:
        "I'm going to tell your mothers.":
            $ player.modify_integrity(4)
            "The group of Loox and Migosp look horrified and retreat."
            "Some of them apologize to the Whimsun and make them promise not to tell anyone's mom."
            menu:
                "Help the Whimsun home.":
                    $ player.modify_kindness(5)
                    "You walk Whimsun to their house and say goodbye."
                    "They half-heartedly thank you and you hear the lock on their door click."
                    return
                "Leave them there.":
                    $ player.modify_apathy(5)
                    "You've done your job. So you walk away."
                    return


        "I'll make you stop.":
            $ player.modify_bravery(5)
            "The monsters look scared and flee."
            "Whimsun is shaking."

            menu:
                "It's okay now, they are gone.":
                    $ player.modify_kindness(3)
                    "Whimsun bursts into tears and runs away."
                    return
                "Do you want me to walk you home?":
                    $ player.modify_kindness(3)
                    "Whimsun bursts into tears and runs away."
                    return

                "Leave them and walk away":
                    $ player.modify_apathy(5)
                    "You've done your job, so you walk away."
                    return
        "Stare at them disapprovingly":
            "The group of Loox and Migosp look unnerved."
            'One of the brave ones say,"Y-yeah? You just gonna stand there?"'

            menu:
                "Continue to stare at the disapprovingly":
                    $ player.modify_patience(5)
                    "They begin fidgeting.  You seem to be making them feel bad."
                    menu:
                        "Channel the mother. Keep staring.":
                            $ player.modify_patience(5)
                        "What do you have to say for yourselves?":
                            "The Loox and Migosp start to stammer out excuses, but soon fall silent.  They decide to retreat with what dignity they have left."
                            menu:
                                "Help Whimsun home":
                                    $ player.modify_kindness(5)
                                    "You walk Whimsun to their house and say goodbye. They half-heartedly thank you and you hear the lock on their door click."
                                    return
                                "Leave them there":
                                    $ player.modify_apathy(5)
                                    "You've done your job. So you walk away."
                                    return
                        "You know, in my experience, people like you get arrested.":
                            $ player.modify_justice(4)
                            "The monsters quickly run away. Whimsun is left trembling on the ground."
                            menu:
                                "It's okay now, they are gone.":
                                    $ player.modify_kindness(3)
                                    "Whimsun bursts into tears and runs away."
                                    return
                                "Do you want me to walk you home?":
                                    $ player.modify_kindness(3)
                                    "Whimsun bursts into tears and runs away."
                                    return
                                "Leave them and walk away":
                                    $ player.modify_apathy(5)
                                    "You have done your job. So you walk away."
                                    return
                "Leave. Now.":
                    "They leave in terror."
                    "Whimsun still looks scared."
                    menu:
                        "It's okay now, they are gone.":
                            $ player.modify_kindness(3)
                            "Whimsun bursts into tears and runs away."
                            return
                        "Do you want me to walk you home?":
                            $ player.modify_kindness(3)
                            "Whimsun bursts into tears and runs away."
                            return
                        "Leave them and walk away":
                            $ player.modify_apathy(5)
                            "You have done your job. So you walk away."
                            return

                "Calmly pick up Whimsun and walk away":
                    $ player.modify_kindness(4)
                    "You carry Whimsun out of danger.  They stammer out the directions to their house."
                    "They half-heartedly thank you and you hear the lock on their door click."
                    return



label whimsun_ruins_run:
    menu:
        "Why were they bullying you?":
            "Whimsun doens't answer.  They just curl up and look ashamed."
            menu:
                "Wow, okay. I guess I understand why they were picking on you now.":
                    $ player.modify_cruelty(5)
                    "Whimsun curls up more. There's no use trying to talk to them now."
                    "You walk away."
                    return
                "I'm sorry for asking.":
                    "They look a little relieved, but otherwise not much better."
                    menu:
                        "Help Whimsun home.":
                            $ player.modify_kindness(5)
                            "You walk Whimsun to their house and say goodbye."
                            "They half-heartedly thank you and you hear the lock on their door click."
                            return
                        "Leave them there":
                            $ player.modify_apathy(5)
                            "You've done your job. So you walk away."
                            return
                "Escape from the awkward situation.":
                    $ player.modify_cowardice(3)
                    "You leave Whimsun curled up on the ground and leave."
                    return


        "Console them":
            $ player.modify_kindness(3)
            "They don't seem very consoled."

            menu:
                "Try consoling again":
                    $ player.modify_perseverance(4)
                    "You think they just need more consoling, so you try again."
                    "You realize that they somehow escaped when you weren't looking."
                    return

                "Change the subject":
                    $ player.modify_cowardice(3)
                    "You ask about the weather."
                    "Whimsun looks confused."
                    "You realize that there is no weather."

                    menu:
                        "Continue conversation about the weather.":
                            $ player.modify_perseverance(5)
                            "You mention that the ceiling looks lovely today."
                            whimsun "...sure."
                            "Whimsun's escape was successful."
                            return

                        "Offer to walk them home.":
                            $ player.modify_kindness(5)
                            "You walk Whimsun to their house and say goodbye."
                            "They half-heartedly thank you and you hear the lock on their door click."
                            return

                        "Run away from this situation.":
                            $ player.modify_cowardice(3)
                            "You flee. You don't want to face your shame."
                            return

                "Offer to walk them home":
                    $ player.modify_kindness(5)

        "I helped you. Why aren't you happy?":
            "Whimsun bursts into tears. They don't seem ot know the answer either."
            menu:
                "Sorry I didn't mean to be rude":
                    $ player.modify_surrender(4)
                    "They cry harder and run away."
                    return

                "Why do you keep on crying?":
                    $ player.modify_impulsiveness(2)
                    "They cry harder and run away."
                    return

                "Pat them on the back":
                    "You reach to gently put your hand on their back, but they see your hand, scream, and run away."
                    return