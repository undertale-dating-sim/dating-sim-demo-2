label dummy_ruins_random_event_start:    

    show dummy normal

    $ player.variables['dummy_approached'] = False 
    "*  You approach the Dummy, ready to have a light-hearted conversation."
    dummy "..."

label dummy_ruins_event_menu:
    menu:
        dummy "..."
        "Talk":
            $ player.variables['dummy_approached'] = True
            menu:
                "Chat":
                    dummy "..."
                    menu:
                        dummy "..."

                        "You're looking bright as day.":
                            "* ...is it even daytime out, though?"
                            dummy "..."
                            "* Even though it didn’t really react, you feel as if it took the compliment well."
                            jump dummy_ruins_event_menu

                        "The weather's beatiful today.":
                            "* ...there was an attempt."
                            dummy "..."
                            "* The Dummy seems to note your attempt and appreciates it nonetheless."
                            jump dummy_ruins_event_menu

                "Flirt":
                    dummy "..."
                    menu:
                        dummy "..."

                        "So, aside from being cute, what else do you do?":
                            dummy "..."
                            "* ...did your finger guns actually make it blush?"
                            jump dummy_ruins_event_menu

                        "Show off?":
                            "* You try to impress the Dummy by showing some dance moves."
                            dummy "..."
                            "* It’s hard to tell if they worked or not."
                            "* ...hold on, is the Dummy blushing?"
                            jump dummy_ruins_event_menu

                "Pick on":
                    "* You pick on the dummy."
                    dummy "..."
                    "..."
                    "* It doesn’t seem to react in any way…"
                    "* But it still feels like you got your point across."
                    jump dummy_ruins_event_menu

                    
                "Back":
                    jump dummy_ruins_event_menu

        "Ask":
            $ player.variables['dummy_approached'] = True
            dummy "..."
            
            menu:
                dummy "..."
                "What brought you to the underground?":
                    dummy "..."
                    "* It doesn’t exactly give any sort of response."
                    "* However, if it could, you’re sure it would say something along the lines of:"
                    '*  "Just like everyone else down here."'
                    jump dummy_ruins_event_menu

                "How are you today?":
                    dummy "..."
                    "* ..."
                    "* You can only assume that the Dummy is doing fine."
                    jump dummy_ruins_event_menu
                    
        "Leave":
            if(player.variables['dummy_approached'] == False):
                "* You approached the dummy with good intentions..."
                "* ...but quickly realized that standing around attempting conversation with an inanimate object was a bad idea."
                "Time to go."
                dummy "..."
                hide dummy
                return
            else:
                "* You figured that was enough talking to an inanimate object."
                "Time to go."
                dummy "..."
                hide dummy
                return
